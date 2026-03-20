#!/usr/bin/env bash
# Initialize project sdlc/ from blueprints/sdlc/templates/sdlc
# Usage (from repo root):
#   ./blueprints/sdlc/scripts/init-sdlc-workspace.sh "Project Name"
#   ./blueprints/sdlc/scripts/init-sdlc-workspace.sh "Project Name" sdlc.new
#   ./blueprints/sdlc/scripts/init-sdlc-workspace.sh "Project Name" sdlc --force

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLUEPRINT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TEMPLATE_DIR="$BLUEPRINT_ROOT/templates/sdlc"

PROJECT_NAME="${1:?Usage: $0 \"Project Name\" [target_dir] [--force]}"
shift || true

TARGET="sdlc"
FORCE=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --force) FORCE=1; shift ;;
    *) TARGET="$1"; shift ;;
  esac
done

if [[ ! -d "$TEMPLATE_DIR" ]]; then
  echo "error: missing $TEMPLATE_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET"

for f in TRACKING-FOUNDATION.md TRACKING-METHODOLOGIES.md TRACKING-CHALLENGES.md; do
  cp "$TEMPLATE_DIR/$f" "$TARGET/$f"
done

README="$TARGET/README.md"
if [[ -f "$README" && "$FORCE" -eq 0 ]]; then
  echo "error: $README already exists (use --force to overwrite README only)" >&2
  exit 1
fi

export PROJECT_NAME
export TEMPLATE_DIR
export README_OUT="$README"
python3 -c '
from pathlib import Path
import os
name = os.environ["PROJECT_NAME"]
src = Path(os.environ["TEMPLATE_DIR"]) / "README.template.md"
dst = Path(os.environ["README_OUT"])
dst.write_text(src.read_text(encoding="utf-8").replace("{{PROJECT_NAME}}", name), encoding="utf-8")
' || {
  echo "error: python3 failed; install Python 3 or create README.md manually" >&2
  exit 1
}

echo "Initialized $TARGET/ with README.md and TRACKING-*.md (from $TEMPLATE_DIR)"
