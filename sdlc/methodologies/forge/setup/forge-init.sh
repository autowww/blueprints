#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FORGE_ROOT="$(cd "${SCRIPT_DIR}/../../.." && pwd)"
REPO_ROOT="$(pwd)"
INTERACTIVE=0
REINIT=0

usage() {
  cat <<'EOF'
Usage: forge-init.sh [--interactive] [--reinit]

  --interactive  Prompt for scale/tier + branching model and write defaults.
  --reinit       Allow refreshing existing forge config/policy files.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --interactive)
      INTERACTIVE=1
      ;;
    --reinit)
      REINIT=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

echo "=== Forge SDLC workspace initialization ==="
echo "Repository root: ${REPO_ROOT}"
echo ""

if [[ ! -d "blueprints/sdlc" ]]; then
  echo "Error: blueprints/sdlc/ not found. Run from the repository root with blueprints/ submodule."
  exit 1
fi

create_dir() {
  if [[ ! -d "$1" ]]; then
    mkdir -p "$1"
    echo "  Created: $1/"
  else
    echo "  Exists:  $1/"
  fi
}

copy_template() {
  local src="$1"
  local dest="$2"
  if [[ ! -f "$dest" ]]; then
    if [[ -f "$src" ]]; then
      cp "$src" "$dest"
      echo "  Created: $dest"
    else
      echo "  Warning: template not found: $src"
    fi
  else
    echo "  Exists:  $dest"
  fi
}

copy_or_refresh_template() {
  local src="$1"
  local dest="$2"
  if [[ ! -f "$dest" ]]; then
    copy_template "$src" "$dest"
    return
  fi
  if [[ "$REINIT" != "1" ]]; then
    echo "  Exists:  $dest"
    return
  fi
  if [[ "$INTERACTIVE" == "1" ]]; then
    local reply=""
    read -r -p "  Refresh ${dest} from template? [y/N]: " reply
    if [[ ! "$reply" =~ ^[Yy]$ ]]; then
      echo "  Kept:    $dest"
      return
    fi
  fi
  cp "$src" "$dest"
  echo "  Refreshed: $dest"
}

prompt_with_default() {
  local prompt="$1"
  local default="$2"
  local out=""
  read -r -p "$prompt [$default]: " out
  if [[ -z "$out" ]]; then
    printf '%s' "$default"
  else
    printf '%s' "$out"
  fi
}

apply_interactive_defaults() {
  local forge_cfg="forge/forge.config.yaml"
  local branch_cfg="forge/branching.yml"
  [[ -f "$forge_cfg" ]] || return
  [[ -f "$branch_cfg" ]] || return

  local default_scale
  default_scale="$(python3 - <<'PY'
import re
from pathlib import Path
t=Path("forge/forge.config.yaml").read_text(encoding="utf-8", errors="replace")
m=re.search(r'^\s*scale:\s*([A-Za-z0-9_-]+)\s*$', t, flags=re.M)
print(m.group(1) if m else "solo")
PY
)"
  local default_stage
  default_stage="$(python3 - <<'PY'
import re
from pathlib import Path
t=Path("forge/forge.config.yaml").read_text(encoding="utf-8", errors="replace")
m=re.search(r'^\s*stage:\s*([A-Za-z0-9_-]+)\s*$', t, flags=re.M)
print(m.group(1) if m else "mvp")
PY
)"
  local default_cicd
  default_cicd="$(python3 - <<'PY'
import re
from pathlib import Path
t=Path("forge/branching.yml").read_text(encoding="utf-8", errors="replace")
m=re.search(r'^\s*cicd_maturity:\s*([A-Za-z0-9_-]+)\s*$', t, flags=re.M)
print(m.group(1) if m else "none")
PY
)"
  local default_topology
  default_topology="$(python3 - <<'PY'
import re
from pathlib import Path
t=Path("forge/branching.yml").read_text(encoding="utf-8", errors="replace")
m=re.search(r'^\s*topology:\s*([A-Za-z0-9_-]+)\s*$', t, flags=re.M)
print(m.group(1) if m else "single")
PY
)"
  local default_model
  default_model="$(python3 - <<'PY'
import re
from pathlib import Path
t=Path("forge/branching.yml").read_text(encoding="utf-8", errors="replace")
m=re.search(r'^\s*model:\s*([A-Za-z0-9_-]+)\s*$', t, flags=re.M)
print(m.group(1) if m else "team_tier")
PY
)"

  echo ""
  echo "Interactive setup (press Enter for current/default value):"
  local scale
  local stage
  local cicd
  local topology
  local model
  local approvals
  scale="$(prompt_with_default "  Team scale (solo|small|team|multi-team)" "$default_scale")"
  stage="$(prompt_with_default "  Product stage (poc|mvp|growth|mature)" "$default_stage")"
  cicd="$(prompt_with_default "  CI/CD maturity (none|basic|standard|advanced)" "$default_cicd")"
  topology="$(prompt_with_default "  Repo topology (single|monorepo|polyrepo|submodule)" "$default_topology")"
  model="$(prompt_with_default "  Branch model (team_tier|forge_lanes)" "$default_model")"
  approvals="$(prompt_with_default "  Required PR approvals" "1")"

  python3 - "$scale" "$stage" "$cicd" "$topology" "$model" "$approvals" <<'PY'
import re
import sys
from pathlib import Path

scale, stage, cicd, topology, model, approvals = sys.argv[1:]
forge_cfg = Path("forge/forge.config.yaml")
branch_cfg = Path("forge/branching.yml")

def repl_line(text: str, key_pat: str, value: str) -> str:
    m = re.search(key_pat, text, flags=re.M)
    if not m:
        return text
    return text[:m.start()] + value + text[m.end():]

f = forge_cfg.read_text(encoding="utf-8", errors="replace")
f = repl_line(f, r'^\s*stage:\s*[A-Za-z0-9_-]+\s*$', f"  stage: {stage}")
f = repl_line(f, r'^\s*scale:\s*[A-Za-z0-9_-]+\s*$', f"  scale: {scale}")
forge_cfg.write_text(f, encoding="utf-8")

b = branch_cfg.read_text(encoding="utf-8", errors="replace")
b = repl_line(b, r'^\s*model:\s*[A-Za-z0-9_-]+\s*$', f"model: {model}")
b = repl_line(b, r'^\s*scale:\s*[A-Za-z0-9_-]+\s*$', f"  scale: {scale}")
b = repl_line(b, r'^\s*topology:\s*[A-Za-z0-9_-]+\s*$', f"  topology: {topology}")
b = repl_line(b, r'^\s*cicd_maturity:\s*[A-Za-z0-9_-]+\s*$', f"  cicd_maturity: {cicd}")
b = repl_line(b, r'^\s*required_approvals:\s*[0-9]+\s*$', f"  required_approvals: {approvals}")
b = repl_line(b, r'^\s*enabled:\s*(true|false)\s*$', f"  enabled: {'true' if model == 'forge_lanes' else 'false'}")
b = repl_line(b, r'^\s*use_forge_lanes:\s*(true|false)\s*$', f"use_forge_lanes: {'true' if model == 'forge_lanes' else 'false'}")
b = repl_line(b, r'^\s*product_parent_enabled:\s*(true|false)\s*$', "  product_parent_enabled: false")
b = repl_line(b, r'^\s*require_green_checks:\s*(true|false)\s*$', f"  require_green_checks: {'true' if cicd in ('standard','advanced') else 'false'}")
branch_cfg.write_text(b, encoding="utf-8")
PY

  echo "  Updated: ${forge_cfg}"
  echo "  Updated: ${branch_cfg}"
}

echo "Creating Forge workspace directories..."
create_dir "forge"
create_dir "forge/journal"
create_dir "forge/releases"
create_dir "forge/charge-archive"
create_dir "forge/evidence"
create_dir "ember-logs"
create_dir "forge-logs"
create_dir "forge-logs/versona-track"

TEMPLATE_DIR="${SCRIPT_DIR}"
DAILY_DIR="${SCRIPT_DIR}/../daily"

echo ""
echo "Copying seed files..."
copy_or_refresh_template "${TEMPLATE_DIR}/forge.config.template.yaml" "forge/forge.config.yaml"
copy_or_refresh_template "${TEMPLATE_DIR}/branching.template.yaml" "forge/branching.yml"

if [[ "$INTERACTIVE" == "1" ]]; then
  apply_interactive_defaults
fi

echo ""
echo "Creating .gitkeep files for empty directories..."
for dir in forge/journal forge/releases forge/charge-archive forge/evidence ember-logs forge-logs forge-logs/versona-track; do
  if [[ ! "$(ls -A "$dir" 2>/dev/null)" ]]; then
    touch "${dir}/.gitkeep"
  fi
done

CURSOR_DIR=".cursor/rules"
echo ""
echo "Cursor rules..."
if [[ ! -d "$CURSOR_DIR" ]]; then
  mkdir -p "$CURSOR_DIR"
  echo "  Created: ${CURSOR_DIR}/"
fi
echo "  Install Cursor rules (recommended bundle):"
echo "    bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended"
echo "  YAML-only (no preset): bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync"
echo "  Compare / status: bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh diff --preset recommended"
echo "    bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh status --preset recommended"
echo "  Manual copy still allowed — see CURSOR-RULES-QUICKSTART.md and CURSOR-RULES-ALIGNMENT.md"
echo "  Optional adoption manifest (Skills/tasklets/recipes pointers): add --write-adoption-manifest to sync (see CURSOR-RULES-ALIGNMENT.md)"
echo "  Tasklets (cognition .mdc): bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh"
echo "  (Recommended preset already installs versona-sampling.mdc; tasklets add forge-tasklet-*.mdc.)"
echo "  Optional — semver + CHANGELOG post-commit hook (manifest .forge/version-release.json):"
echo "    bash blueprints/sdlc/methodologies/forge/setup/install-version-release-hook.sh"
echo "    Policy: blueprints/sdlc/methodologies/forge/setup/VERSIONING-AND-RELEASES.md"

echo ""
echo "=== Forge workspace initialized ==="
echo ""
echo "Next steps:"
echo "  1. Edit forge/forge.config.yaml and forge/branching.yml to match your team"
echo "  2. bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended"
echo "  3. bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check"
echo "  3b. (Optional) bash blueprints/sdlc/methodologies/forge/setup/install-version-release-hook.sh"
echo "  4. Run your first Refinement: turn Ore into Ingots"
echo "  5. Run your first Planning: decompose Ingots into Sparks"
echo "  6. Start your first Charge: ./blueprints/sdlc/methodologies/forge/scripts/forge-charge.sh new"
echo ""
echo "See: blueprints/sdlc/methodologies/forge/setup/QUESTIONNAIRE.md"
echo "Branch policy template: blueprints/sdlc/methodologies/forge/setup/branching.template.yaml"
echo "Artifact layout (specs, ADRs, sessions, evidence): blueprints/sdlc/methodologies/forge/versona/ARTIFACT-CONTRACTS.md"
echo "Process-first migration + verification: blueprints/sdlc/methodologies/forge/setup/VERSONA-PROCESS-MODEL-MIGRATION.md"
echo "  … and blueprints/sdlc/methodologies/forge/setup/VERSONA-VERIFICATION.md"
