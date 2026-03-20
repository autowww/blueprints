#!/usr/bin/env bash
# Scaffold agents/recipes/<name>/ from templates/recipe/*.template.*
# Usage (from repository root — directory containing blueprints/agents/ and agents/):
#   ./blueprints/agents/scripts/new-agent-recipe.sh <kebab-case-name>
#   ./blueprints/agents/scripts/new-agent-recipe.sh my-recipe --purpose "Lint all Markdown links"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLUEPRINT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TEMPLATE_DIR="$BLUEPRINT_ROOT/templates/recipe"

REPO_ROOT="$(pwd)"
if [[ -n "${REPO_ROOT_OVERRIDE:-}" ]]; then
  REPO_ROOT="$REPO_ROOT_OVERRIDE"
fi

usage() {
  echo "Usage: $0 <kebab-case-name> [--purpose \"one line description\"]" >&2
  echo "  Run from repository root (must contain blueprints/agents/ and agents/)." >&2
  exit 1
}

[[ $# -ge 1 ]] || usage
NAME="$1"
shift
PURPOSE="TODO: describe what this recipe does."
while [[ $# -gt 0 ]]; do
  case "$1" in
    --purpose)
      [[ $# -ge 2 ]] || { echo "error: --purpose requires a value" >&2; exit 1; }
      PURPOSE="$2"
      shift 2
      ;;
    -h|--help) usage ;;
    *) echo "error: unknown argument: $1" >&2; exit 1 ;;
  esac
done

if [[ ! -d "$REPO_ROOT/blueprints/agents" ]]; then
  echo "error: blueprints/agents not found in $REPO_ROOT — run this script from the repository root" >&2
  exit 1
fi
if [[ ! -d "$REPO_ROOT/agents" ]]; then
  echo "error: agents/ not found — run: ./blueprints/agents/scripts/init-agents-workspace.sh" >&2
  exit 1
fi

if [[ ! "$NAME" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "error: recipe name must be kebab-case (e.g. ui-e2e, docs-lint)" >&2
  exit 1
fi

DEST="$REPO_ROOT/agents/recipes/$NAME"
if [[ -e "$DEST" ]]; then
  echo "error: already exists: $DEST" >&2
  exit 1
fi

if [[ ! -f "$TEMPLATE_DIR/README.template.md" || ! -f "$TEMPLATE_DIR/run.sh.template" ]]; then
  echo "error: missing templates in $TEMPLATE_DIR" >&2
  exit 1
fi

mkdir -p "$DEST"

export NAME PURPOSE
export README_TEMPLATE="$TEMPLATE_DIR/README.template.md"
export RUN_TEMPLATE="$TEMPLATE_DIR/run.sh.template"
export README_OUT="$DEST/README.md"
export RUN_OUT="$DEST/run.sh"

python3 << 'PY'
import os
from pathlib import Path

name = os.environ["NAME"]
purpose = os.environ["PURPOSE"]
readme_t = Path(os.environ["README_TEMPLATE"]).read_text(encoding="utf-8")
run_t = Path(os.environ["RUN_TEMPLATE"]).read_text(encoding="utf-8")
readme_t = readme_t.replace("{{RECIPE_NAME}}", name).replace("{{ONE_LINE_PURPOSE}}", purpose)
run_t = run_t.replace("{{RECIPE_NAME}}", name)
Path(os.environ["README_OUT"]).write_text(readme_t, encoding="utf-8")
Path(os.environ["RUN_OUT"]).write_text(run_t, encoding="utf-8")
PY

chmod +x "$DEST/run.sh"

echo "Created: $DEST"
echo "Next: edit README.md and run.sh; follow blueprints/agents/ORCHESTRATION.md"
