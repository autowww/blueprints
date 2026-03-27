#!/usr/bin/env bash
# Thin wrapper — prefer sync-forge-cursor-rules.sh diff.
#
# Compare installed .cursor/rules Versona/Forge files to current blueprint sources (SHA256).
# Exit 1 if any expected file is missing or differs — use sync … sync --force after review.
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec "$SCRIPT_DIR/sync-forge-cursor-rules.sh" diff "$@"
