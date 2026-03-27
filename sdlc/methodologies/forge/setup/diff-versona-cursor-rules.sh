#!/usr/bin/env bash
# Compare installed .cursor/rules Versona/Forge files to current blueprint sources (SHA256).
# Exit 1 if any expected file is missing or differs — use install script with --force after review.
#
# Usage:
#   bash blueprints/sdlc/methodologies/forge/setup/diff-versona-cursor-rules.sh
#   bash .../diff-versona-cursor-rules.sh --with-all-routing --with-standard-forge-rules
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${SCRIPT_DIR}/versona_cursor_rules.py"

exec python3 "$PY" diff "$@"
