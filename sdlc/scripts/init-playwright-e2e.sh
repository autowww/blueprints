#!/usr/bin/env bash
# Copy Playwright templates from blueprints/sdlc/templates/playwright into the consuming repo.
# Usage (from repository root — parent of blueprints/):
#   ./blueprints/sdlc/scripts/init-playwright-e2e.sh
#   ./blueprints/sdlc/scripts/init-playwright-e2e.sh --force

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SDL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TEMPLATE_DIR="$SDL_ROOT/templates/playwright"
# Run from the consuming repository root (parent of blueprints/), same as init-sdlc-workspace.sh.
REPO_ROOT="$(pwd)"
if [[ ! -d "$REPO_ROOT/blueprints/sdlc" ]]; then
  echo "error: run from repository root — expected ./blueprints/sdlc (got cwd: $REPO_ROOT)" >&2
  exit 1
fi

FORCE=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --force) FORCE=1; shift ;;
    -h|--help)
      echo "Usage: $0 [--force]"
      echo "  Run from repo root (directory that contains blueprints/). Copies e2e examples and playwright.config.ts."
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

if [[ ! -d "$TEMPLATE_DIR" ]]; then
  echo "error: missing template directory $TEMPLATE_DIR" >&2
  exit 1
fi

CFG_DST="$REPO_ROOT/playwright.config.ts"
if [[ -f "$CFG_DST" && "$FORCE" -eq 0 ]]; then
  echo "error: $CFG_DST already exists (use --force to overwrite)" >&2
  exit 1
fi

mkdir -p "$REPO_ROOT/e2e"

cp "$TEMPLATE_DIR/playwright.config.ts.template" "$CFG_DST"
for src in "$TEMPLATE_DIR/e2e/"*.template; do
  [[ -f "$src" ]] || continue
  base="$(basename "$src" .template)"
  dst="$REPO_ROOT/e2e/$base"
  if [[ -f "$dst" && "$FORCE" -eq 0 ]]; then
    echo "skip existing $dst (use --force to overwrite)"
  else
    cp "$src" "$dst"
    echo "wrote $dst"
  fi
done

echo "wrote $CFG_DST"
echo ""
echo "Next steps:"
echo "  1. npm install -D @playwright/test"
echo "  2. npx playwright install   # add --with-deps on Linux CI"
echo "  3. Add '\"test:e2e\": \"playwright test\"' to package.json (in the same package as these tests)."
echo "  4. Remove example-web.spec.ts or example-electron.spec.ts if not needed; edit paths and env."
echo "See: blueprints/disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md"
