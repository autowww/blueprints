#!/usr/bin/env bash
# Install Forge Versona Cursor rules from blueprints templates into REPO_ROOT/.cursor/rules/
# driven by forge/forge.config.yaml (same expectations as check-forge-cursor-alignment.sh).
#
# Usage (from consuming repo root):
#   bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh
#   bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh --dry-run
#   bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh --force
#   bash .../install-versona-cursor-rules.sh --with-all-routing --with-standard-forge-rules
#
# See: CURSOR-RULES-ALIGNMENT.md
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${SCRIPT_DIR}/versona_cursor_rules.py"

exec python3 "$PY" install "$@"
