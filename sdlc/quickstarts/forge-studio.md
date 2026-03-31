# Forge Studio quickstart

**Time to complete:** about 15–30 minutes (after Git and Python 3 are available)

**You’ll have:** a local **[forge-lenses](https://github.com/autowww/forge-lenses)** checkout, the Python server running, and **Forge Studio** (Lenses Studio) at **`/studio/`** in the browser — optional **Electron** shell for development.

**Forge Studio** is the product name for **Lenses Studio** (React SPA + shared Python APIs). **Classic** Lenses remains the server-rendered UI at `/`; Studio is the Electron-first surface for new UI. See the upstream [ADR 001](https://github.com/autowww/forge-lenses/blob/main/docs/adr-001-lenses-studio-shell.md).

**Handbook (static, read-only):** [blueprints.forgesdlc.com/lenses](https://blueprints.forgesdlc.com/lenses/index.html) — same ecosystem as Blueprints; the app itself is not hosted there.

## Prerequisites

- **Git**, **Python 3**, **pip** (venv recommended).
- For **Studio UI assets** in production mode: **Node.js** (LTS) to run `npm run build` under `lenses-enterprise/` when `/studio/` needs a fresh bundle (see upstream README).
- For **Electron:** Node.js; the shell does not bundle Python (it expects `python3` on `PATH`).

## 1. Get the repository

**Standalone clone** (typical — sibling to your product repos):

```bash
git clone https://github.com/autowww/forge-lenses.git
cd forge-lenses
```

**Git submodule** (from a parent folder that contains your workspace):

```bash
git submodule add https://github.com/autowww/forge-lenses.git forge-lenses
git submodule update --init --recursive
cd forge-lenses
```

Then run `./scripts/setup.sh` for nested submodules (blueprints, kitchensink) as described in the [forge-lenses README](https://github.com/autowww/forge-lenses/blob/main/README.md).

## 2. Install and build docs (optional)

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python3 generator/build-lenses-docs.py
```

Omit the generator step if you only need the dashboard without `/docs/` content.

## 3. Run the server

```bash
./scripts/run-lenses.sh
```

Or: `.venv/bin/python3 -m lenses` from the repo root with the same venv activated.

**Verify:** [http://127.0.0.1:8080/](http://127.0.0.1:8080/) loads (classic UI). JSON: [http://127.0.0.1:8080/api/workspace-state](http://127.0.0.1:8080/api/workspace-state).

## 4. Open Forge Studio (`/studio/`)

If the Studio bundle is missing or stale, build it from **`lenses-enterprise/`** (upstream: `npm install && npm run build` — output goes to `lenses/static/studio/`). Then open:

**[http://127.0.0.1:8080/studio/](http://127.0.0.1:8080/studio/)**

For day-to-day UI work, the upstream repo documents **`npm run watch`** while the server runs.

## 5. Optional: Electron (dev-oriented)

From **`desktop/`**: `npm install`, then `LENSES_STUDIO_UI=1 npm start` so the window opens `/studio/`. Full notes (workspace picker, sandbox, Ubuntu launchers): [forge-lenses README — Desktop app](https://github.com/autowww/forge-lenses/blob/main/README.md#desktop-app-electron-phase-1-dev-only).

## 6. Workspace root (multi-repo)

To scan sibling repositories, set **`LENSES_WORKSPACE_ROOT`** to the parent directory that contains your clones, or use **`lenses-desktop.json`** / the folder picker as documented upstream.

## Pin a known-good revision

Use **annotated tags** and submodule pointers (or `git checkout <tag>` in a standalone clone). Maintainers may publish **GitHub Releases** with notes. Details: [**Releases and versioning**](https://github.com/autowww/forge-lenses/blob/main/README.md#releases-and-versioning) in the forge-lenses README.

## Go deeper

- **First hour with Blueprints** (submodule, `sdlc/`, Forge, Cursor): [First hour in your repo](first-hour.md)
- **ICP adoption paths:** [Adopting Blueprints](../../docs/ADOPTION.md)
- **Upstream** clone/setup: [github.com/autowww/forge-lenses](https://github.com/autowww/forge-lenses)
