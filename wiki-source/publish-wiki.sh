#!/usr/bin/env bash
# Deprecated: use sync-wiki.sh (full markdown mirror).
set -euo pipefail
exec "$(dirname "$0")/sync-wiki.sh"
