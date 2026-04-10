#!/usr/bin/env bash
# Frozen template — copy to agents/recipes/playwright-e2e/ and customize.
# Runs npm ci, playwright install, and test:e2e in PLAYWRIGHT_PACKAGE_DIR under the repo root.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PKG="${PLAYWRIGHT_PACKAGE_DIR:-.}"
NPM_SCRIPT="${PLAYWRIGHT_NPM_SCRIPT:-test:e2e}"

if [[ -n "${PLAYWRIGHT_REPO_ROOT:-}" ]]; then
  ROOT="$PLAYWRIGHT_REPO_ROOT"
else
  if git -C "$SCRIPT_DIR" rev-parse --show-toplevel >/dev/null 2>&1; then
    ROOT="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"
  else
    # Copied to agents/recipes/<name>/ → repo root is three levels up
    ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
  fi
fi

TARGET="$ROOT/$PKG"
if [[ ! -f "$TARGET/package.json" ]]; then
  echo "playwright-e2e: no package.json at $TARGET (set PLAYWRIGHT_REPO_ROOT / PLAYWRIGHT_PACKAGE_DIR)" >&2
  exit 1
fi

cd "$TARGET"
if [[ -f package-lock.json ]]; then
  npm ci
else
  npm install
fi
# shellcheck disable=SC2086
npx playwright install ${PLAYWRIGHT_INSTALL_FLAGS:-}
npm run "$NPM_SCRIPT"
