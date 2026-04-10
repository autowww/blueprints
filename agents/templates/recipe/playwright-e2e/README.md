---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Template recipe: `playwright-e2e`

**Purpose:** Run **`@playwright/test`** inside a **Linux container** that already has **Chromium OS dependencies**, matching the pattern in [`blueprints/disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md`](../../../../disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md).

**Aligned with:** [`STRUCTURE.md`](../../STRUCTURE.md) L4–L5 — frozen template; mutable copy under **`agents/recipes/playwright-e2e/`** in the consuming repo.

## Non-goals

- Does not replace **local** `npx playwright test` on developer machines.  
- Does not install your app’s **npm** dependencies into the blueprint image — the recipe runs **`npm ci`** in the mounted tree.

## Adoption

1. Copy this folder to **`agents/recipes/playwright-e2e/`** at the consuming repository root (or scaffold with [`new-agent-recipe.sh`](../../scripts/new-agent-recipe.sh) and merge).  
2. Build the Playwright image:  
   `docker compose -f blueprints/agents/docker/compose.yaml build agent-playwright`  
3. Mount the repo at **`/work`** and set **`PLAYWRIGHT_PACKAGE_DIR`** to the directory that contains `package.json` with your Playwright scripts (e.g. `desktop`).

## Environment

| Variable | Required | Default | Meaning |
|----------|----------|---------|---------|
| `PLAYWRIGHT_REPO_ROOT` | No | Auto (`git` or path relative to recipe) | Repo root inside container — use **`/work`** when mounting the checkout |
| `PLAYWRIGHT_PACKAGE_DIR` | No | `.` | Subdirectory under repo root with `package.json` |
| `PLAYWRIGHT_NPM_SCRIPT` | No | `test:e2e` | npm script to run after `npx playwright install` |
| `PLAYWRIGHT_INSTALL_FLAGS` | No | — | Extra flags for `npx playwright install` (e.g. `--with-deps` if needed beyond the image) |

## Usage

**Host** (after copying the recipe to `agents/recipes/playwright-e2e/`):

```bash
export PLAYWRIGHT_PACKAGE_DIR=desktop
./agents/recipes/playwright-e2e/run.sh
```

**Docker** (example):

```bash
docker compose -f blueprints/agents/docker/compose.yaml run --rm \
  -v "$PWD:/work" \
  -e PLAYWRIGHT_REPO_ROOT=/work \
  -e PLAYWRIGHT_PACKAGE_DIR=desktop \
  agent-playwright \
  bash /work/agents/recipes/playwright-e2e/run.sh
```

**Electron on Linux** often needs a display; in CI use **`xvfb-run`** (see [`github-actions-snippet.md`](../../../../sdlc/templates/playwright/github-actions-snippet.md)). Inside Docker you may add **`xvfb`** to a derived image or run `xvfb-run` in the command.

**Stack:** [`Dockerfile.playwright`](../../docker/Dockerfile.playwright) — Node + `playwright install-deps chromium`.
