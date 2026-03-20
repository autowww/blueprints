#!/usr/bin/env bash
# Initialize project agents/ from blueprints/agents/templates/project-agents
# Usage (from repository root):
#   ./blueprints/agents/scripts/init-agents-workspace.sh
#   ./blueprints/agents/scripts/init-agents-workspace.sh my-agents-dir
#   ./blueprints/agents/scripts/init-agents-workspace.sh --force

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLUEPRINT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TEMPLATE_DIR="$BLUEPRINT_ROOT/templates/project-agents"

TARGET="agents"
FORCE=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --force) FORCE=1; shift ;;
    -h|--help)
      echo "Usage: $0 [target_dir] [--force]"
      echo "  Creates target_dir (default: agents) from templates/project-agents."
      exit 0
      ;;
    *) TARGET="$1"; shift ;;
  esac
done

if [[ ! -d "$TEMPLATE_DIR" ]]; then
  echo "error: missing template directory $TEMPLATE_DIR" >&2
  exit 1
fi

if [[ -f "$TARGET/README.md" && "$FORCE" -eq 0 ]]; then
  echo "error: $TARGET/README.md already exists (use --force to overwrite)" >&2
  exit 1
fi

mkdir -p "$TARGET"
cp -a "$TEMPLATE_DIR/." "$TARGET/"
mkdir -p "$TARGET/recipes" "$TARGET/workspaces"

echo "Initialized $TARGET/ from $TEMPLATE_DIR (recipes/, workspaces/ ensured)."
