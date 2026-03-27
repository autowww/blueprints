#!/usr/bin/env bash
# Thin wrapper — prefer sync-forge-cursor-rules.sh check.
#
# Compare forge/forge.config.yaml versona.* flags to .cursor/rules/ versona-*.mdc presence.
# Usage: run from repository root. Requires Python 3 + PyYAML.
# Logic lives in versona_cursor_rules.py.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${1:-.}"

exec "$SCRIPT_DIR/sync-forge-cursor-rules.sh" check "$ROOT"
