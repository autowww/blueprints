# Scripts (`blueprints/sdlc/scripts/`)

Small helpers for **consuming repos** (not required to *use* the SDLC process text). Run from the **repository root** (where `blueprints/sdlc/` lives).

## `init-sdlc-workspace.sh`

Creates or refreshes a project **`sdlc/`** folder from [`../templates/sdlc/`](../templates/sdlc): copies `TRACKING-*.md` and renders `README.md` from `README.template.md` with the project name.

**Requires:** `bash`, **`python3`** (for safe `{{PROJECT_NAME}}` substitution).

**Usage:**

```bash
# Default target directory: ./sdlc
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "My Product Name"

# Custom target (e.g. scratch compare folder)
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "My Product Name" sdlc.new

# Overwrite existing README.md in target (TRACKING files are always copied)
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "My Product Name" sdlc --force
```

**Human-oriented steps** (manual copy, no script): see [`../SDLc-WORKSPACE.md`](../SDLc-WORKSPACE.md).

---

## `init-playwright-e2e.sh`

Copies Playwright **templates** from [`../templates/playwright/`](../templates/playwright/) into the consuming repo: `playwright.config.ts` at the repository root and example specs under `e2e/`.

**Requires:** `bash`.

**Usage:**

```bash
./blueprints/sdlc/scripts/init-playwright-e2e.sh
./blueprints/sdlc/scripts/init-playwright-e2e.sh --force
```

Then install tooling in the **same package** that will run tests: `npm install -D @playwright/test` and `npx playwright install`. See [`../../disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md`](../../disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md) (from consuming repo root: `blueprints/disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md`).

---

## `playwright-workspace-run.sh`

Runs an npm script (default `test:e2e`) in **multiple** sibling directories under a shared **workspace root** — useful when several repos live side by side (e.g. `~/Code/forge-lenses/desktop`).

**Requires:** `bash`, `node`, `npm`, targets must define the chosen npm script.

**Usage:**

```bash
export WORKSPACE_ROOT="$HOME/Code"
./forge-lenses/blueprints/sdlc/scripts/playwright-workspace-run.sh forge-lenses/desktop
```

Or:

```bash
export WORKSPACE_ROOT="$HOME/Code"
export PLAYWRIGHT_WORKSPACE_TARGETS="forge-lenses/desktop other/ui"
./any-consumer/blueprints/sdlc/scripts/playwright-workspace-run.sh
```

**Environment:** `PLAYWRIGHT_WORKSPACE_NPM_SCRIPT` (default `test:e2e`), `PLAYWRIGHT_INSTALL_FLAGS` (e.g. `--with-deps` on Linux).

---

*Part of [`blueprints/sdlc/README.md`](../README.md).*
