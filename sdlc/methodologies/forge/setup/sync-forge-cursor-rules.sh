#!/usr/bin/env bash
# Single entry for Forge Cursor rules: sync (install), diff, status, check.
#
# Recommended one-liner after submodule update or on a new machine:
#   bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended
#
# Usage: run from consuming repo root. Subcommands forward args to versona_cursor_rules.py.
# See: CURSOR-RULES-QUICKSTART.md, CURSOR-RULES-ALIGNMENT.md
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${SCRIPT_DIR}/versona_cursor_rules.py"

if [[ $# -lt 1 ]] || [[ "${1:-}" == -* ]]; then
  echo "Usage: sync-forge-cursor-rules.sh {sync|diff|status|check} [args...]" >&2
  echo "  sync   — copy templates into .cursor/rules (same as install)" >&2
  echo "  diff   — SHA256 compare installed .mdc vs blueprints" >&2
  echo "  status — per-file missing / drift / ok" >&2
  echo "  check  — forge.config.yaml expected Versona files exist" >&2
  echo "Example: bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended" >&2
  exit 1
fi

sub="$1"
shift

case "$sub" in
  sync)
    exec python3 "$PY" install "$@"
    ;;
  diff|status|check)
    exec python3 "$PY" "$sub" "$@"
    ;;
  *)
    echo "Unknown subcommand: $sub (use sync, diff, status, or check)" >&2
    exit 1
    ;;
esac
