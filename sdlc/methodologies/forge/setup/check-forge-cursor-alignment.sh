#!/usr/bin/env bash
# Compare forge/forge.config.yaml versona.* flags to .cursor/rules/ versona-*.mdc presence.
# Usage: run from repository root. Requires Python 3 + PyYAML.
# Logic lives in versona_cursor_rules.py (single source of truth with install-versona-cursor-rules.sh).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${1:-.}"

exec python3 "${SCRIPT_DIR}/versona_cursor_rules.py" check "$ROOT"
