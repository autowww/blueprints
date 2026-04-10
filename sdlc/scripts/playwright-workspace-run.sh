#!/usr/bin/env bash
# Run Playwright (npm script) in multiple sibling Node packages from a workspace root directory.
#
# Usage:
#   export WORKSPACE_ROOT="$HOME/Code"
#   ./blueprints/sdlc/scripts/playwright-workspace-run.sh forge-lenses/desktop my-app/ui
#
# Or set PLAYWRIGHT_WORKSPACE_TARGETS to space-separated paths (relative to WORKSPACE_ROOT).
#
# Requires: each target directory contains package.json with script PLAYWRIGHT_WORKSPACE_NPM_SCRIPT
# (default: test:e2e).

set -euo pipefail

WORKSPACE_ROOT="${WORKSPACE_ROOT:-}"
NPM_SCRIPT="${PLAYWRIGHT_WORKSPACE_NPM_SCRIPT:-test:e2e}"

usage() {
  echo "Usage: WORKSPACE_ROOT=/path/to/parent $0 <rel/path> [rel/path ...]"
  echo "   or: WORKSPACE_ROOT=/path PLAYWRIGHT_WORKSPACE_TARGETS='a/b c/d' $0"
  echo ""
  echo "Environment:"
  echo "  WORKSPACE_ROOT          Parent of sibling repos (default: current directory)"
  echo "  PLAYWRIGHT_WORKSPACE_NPM_SCRIPT  npm script name (default: test:e2e)"
  echo "  PLAYWRIGHT_INSTALL_FLAGS         Extra args for: npx playwright install \$FLAGS"
  exit 1
}

if [[ $# -ge 1 && ( "$1" == "-h" || "$1" == "--help" ) ]]; then
  usage
fi

if [[ -z "$WORKSPACE_ROOT" ]]; then
  WORKSPACE_ROOT="$(pwd)"
fi

WORKSPACE_ROOT="$(cd "$WORKSPACE_ROOT" && pwd)"

paths=()
if [[ -n "${PLAYWRIGHT_WORKSPACE_TARGETS:-}" ]]; then
  # shellcheck disable=SC2206
  paths=($PLAYWRIGHT_WORKSPACE_TARGETS)
fi
if [[ $# -gt 0 ]]; then
  paths=("$@")
fi

if [[ ${#paths[@]} -eq 0 ]]; then
  echo "error: no targets — pass relative paths or set PLAYWRIGHT_WORKSPACE_TARGETS" >&2
  usage
fi

failed=0
for rel in "${paths[@]}"; do
  dir="$WORKSPACE_ROOT/$rel"
  if [[ ! -d "$dir" ]]; then
    echo "error: not a directory: $dir" >&2
    failed=1
    continue
  fi
  if [[ ! -f "$dir/package.json" ]]; then
    echo "error: no package.json in $dir — skip" >&2
    failed=1
    continue
  fi
  echo "=== playwright-workspace-run: $rel ==="
  (
    cd "$dir"
    if ! PW_WS_NPM_SCRIPT="$NPM_SCRIPT" node -e "const p=require('./package.json'); const s=process.env.PW_WS_NPM_SCRIPT; process.exit(p.scripts && p.scripts[s] ? 0 : 1)"; then
      echo "error: no npm script '$NPM_SCRIPT' in $dir" >&2
      exit 1
    fi
    if [[ -f package-lock.json ]]; then
      npm ci
    else
      npm install
    fi
    # shellcheck disable=SC2086
    npx playwright install ${PLAYWRIGHT_INSTALL_FLAGS:-}
    npm run "$NPM_SCRIPT"
  ) || failed=1
done

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi
