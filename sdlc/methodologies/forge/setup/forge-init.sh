#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FORGE_ROOT="$(cd "${SCRIPT_DIR}/../../.." && pwd)"
REPO_ROOT="$(pwd)"

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

echo "Creating Forge workspace directories..."
create_dir "forge"
create_dir "forge/journal"
create_dir "forge/releases"
create_dir "forge/charge-archive"
create_dir "ember-logs"

TEMPLATE_DIR="${SCRIPT_DIR}"
DAILY_DIR="${SCRIPT_DIR}/../daily"

echo ""
echo "Copying seed files..."
copy_template "${TEMPLATE_DIR}/forge.config.template.yaml" "forge/forge.config.yaml"

echo ""
echo "Creating .gitkeep files for empty directories..."
for dir in forge/journal forge/releases forge/charge-archive ember-logs; do
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
echo "  Install Versonas from forge.config.yaml (and optional extras):"
echo "    bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh"
echo "    bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh --with-standard-forge-rules"
echo "  Compare templates vs installed: bash blueprints/sdlc/methodologies/forge/setup/diff-versona-cursor-rules.sh"
echo "  Manual copy still allowed — see CURSOR-RULES-ALIGNMENT.md"
echo "  Example tasklets + Sampling Versona: bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh"

echo ""
echo "=== Forge workspace initialized ==="
echo ""
echo "Next steps:"
echo "  1. Edit forge/forge.config.yaml to match your team"
echo "  2. bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh [--with-standard-forge-rules]"
echo "  3. bash blueprints/sdlc/methodologies/forge/setup/check-forge-cursor-alignment.sh"
echo "  4. Run your first Refinement: turn Ore into Ingots"
echo "  5. Run your first Planning: decompose Ingots into Sparks"
echo "  6. Start your first Charge: ./blueprints/sdlc/methodologies/forge/scripts/forge-charge.sh new"
echo ""
echo "See: blueprints/sdlc/methodologies/forge/setup/QUESTIONNAIRE.md"
