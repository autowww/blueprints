#!/usr/bin/env bash
# Thin wrapper — prefer sync-forge-cursor-rules.sh sync (see CURSOR-RULES-QUICKSTART.md).
#
# Install Forge Versona Cursor rules from blueprints templates into REPO_ROOT/.cursor/rules/
# driven by forge/forge.config.yaml (same expectations as check-forge-cursor-alignment.sh).
#
# Usage (from consuming repo root):
#   bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh
#   bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh --preset recommended --force
#
# See: CURSOR-RULES-ALIGNMENT.md
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec "$SCRIPT_DIR/sync-forge-cursor-rules.sh" sync "$@"
