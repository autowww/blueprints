# Forge Studio quickstart — maintainer and operator notes

This companion page supports [Forge Studio quickstart](../sdlc/quickstarts/forge-studio.md). It covers **building Studio assets**, **feature flags**, **Electron dev**, and **architecture references** for contributors — not the minimum path to open `/studio/`.

## Architecture reference

**Forge Studio** is the product name for **Lenses Studio** (React SPA + shared Python APIs). **Classic** Lenses remains the server-rendered UI at `/`; Studio is the Electron-first surface for new UI. Upstream decision record: [ADR 001: Lenses Studio shell](https://github.com/autowww/forge-lenses/blob/main/docs/adr-001-lenses-studio-shell.md).

## Build and watch (Studio bundle)

- For **Studio UI assets** in production mode: **Node.js** (LTS) to run `npm run build` under `lenses-enterprise/` when `/studio/` needs a fresh bundle — output goes to `lenses/static/studio/`. See the [forge-lenses README](https://github.com/autowww/forge-lenses/blob/main/README.md).
- For day-to-day UI work, the upstream repo documents **`npm run watch`** while the server runs.

## Optional: local docs build

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python3 generator/build-lenses-docs.py
```

Omit the generator step if you only need the dashboard without `/docs/` content.

## Blueprints Wizard (operator detail)

- **Feature flags:** server **`LENSES_EXPERIMENTAL_BLUEPRINTS_WIZARD`**, Studio build **`VITE_EXPERIMENTAL_BLUEPRINTS_WIZARD`** — see [forge-lenses README — Blueprints Wizard](https://github.com/autowww/forge-lenses/blob/main/README.md).
- **Operator / maintainer usage:** [wizard-usage.md](https://github.com/autowww/forge-lenses/blob/main/docs/blueprints/wizard-usage.md) in the forge-lenses repo.

## Electron (desktop shell)

From **`desktop/`**: `npm install`, then `LENSES_STUDIO_UI=1 npm start` so the window opens `/studio/`. Full notes: [forge-lenses README — Desktop app](https://github.com/autowww/forge-lenses/blob/main/README.md#desktop-app-electron-phase-1-dev-only).

## Workspace root and releases

- **Multi-repo:** set **`LENSES_WORKSPACE_ROOT`** or use **`lenses-desktop.json`** / the folder picker as documented upstream.
- **Pin a revision:** use annotated tags and submodule pointers, or [Releases and versioning](https://github.com/autowww/forge-lenses/blob/main/README.md#releases-and-versioning) in the forge-lenses README.
