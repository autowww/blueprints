# Project setup profile (consuming repository)

Use this checklist when the **blueprints** package is available as **`blueprints/` at the repository root** (typically a git submodule). Copy this file to your project root as `SETUP.md` if you want a local checklist, or follow it from the submodule path.

| Field | Value |
|-------|--------|
| **Profile version** | 1.0 |
| **Last reviewed** | 2025-03-24 |
| **Blueprints submodule** | Record `git rev-parse HEAD` inside `blueprints/` after `git submodule update` |

Canonical layout and conventions: [`DOCUMENTATION-STRUCTURE.md`](DOCUMENTATION-STRUCTURE.md).

## Path assumptions

- **`blueprints/`** must sit at the **repository root** next to `forge/`, `sdlc/`, `docs/`, etc. Scripts such as [`methodologies/forge/setup/forge-init.sh`](methodologies/forge/setup/forge-init.sh) and [`methodologies/forge/tasklets/install-tasklets.sh`](methodologies/forge/tasklets/install-tasklets.sh) use paths like `blueprints/sdlc/...` from the current working directory (repo root).
- If your org cannot use that layout, you need **wrapper scripts** or forks that adjust paths — the stock blueprints tooling does **not** support a configurable `BLUEPRINTS_ROOT`.

## Recommended order

1. **Submodule** — Ensure `blueprints/` is present; `git submodule update --init` so `blueprints/sdlc` exists.
2. **Documentation tree (as needed)** — Create `docs/` per [`DOCUMENTATION-STRUCTURE.md`](DOCUMENTATION-STRUCTURE.md).
3. **Project `sdlc/` workspace** — From repo root:  
   `./blueprints/sdlc/scripts/init-sdlc-workspace.sh "Project Name"`  
   See [`SDLc-WORKSPACE.md`](SDLc-WORKSPACE.md), [`scripts/README.md`](scripts/README.md).
4. **Forge workspace** — `./blueprints/sdlc/methodologies/forge/setup/forge-init.sh`  
   Creates `forge/`, `ember-logs/`, seeds `forge/forge.config.yaml`.
5. **Configure Forge in YAML** — Edit `forge/forge.config.yaml`; questionnaire: [`methodologies/forge/setup/QUESTIONNAIRE.md`](methodologies/forge/setup/QUESTIONNAIRE.md).
6. **Cursor — install rules** — From repo root, run [`methodologies/forge/setup/install-versona-cursor-rules.sh`](methodologies/forge/setup/install-versona-cursor-rules.sh) (uses `forge.config.yaml`; add `--with-standard-forge-rules` for `forge-daily`, `forge-planning`, `forge-versona`, `forge-setup`, `forge-product-manager`). Or copy manually — see [`methodologies/forge/setup/CURSOR-RULES-ALIGNMENT.md`](methodologies/forge/setup/CURSOR-RULES-ALIGNMENT.md).
7. **Cursor — optional extras** — Flags on the same script: `--with-project-setup`, `--with-roadmap-gate`, `--with-all-routing`, family aggregators, etc. After `git submodule update` on `blueprints/`, re-run install; use [`diff-versona-cursor-rules.sh`](methodologies/forge/setup/diff-versona-cursor-rules.sh) to see drift before `--force`.
8. **Cursor — tasklets + Sampling (optional)** — `bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh`
9. **Optional Skills** — Copy from [`templates/forge/cursor-skills/`](templates/forge/cursor-skills/) into `.cursor/skills/`.
10. **Validate alignment** — `bash blueprints/sdlc/methodologies/forge/setup/check-forge-cursor-alignment.sh` (Python 3 + PyYAML; uses [`versona_cursor_rules.py`](methodologies/forge/setup/versona_cursor_rules.py) `check` — same map as the install script).
11. **Operational start** — Forge scripts: [`methodologies/forge/scripts/README.md`](methodologies/forge/scripts/README.md); workspace overview: [`templates/forge/README.template.md`](templates/forge/README.template.md).
12. **Optional product-led path** — [`methodologies/forge/product-manager/README.md`](methodologies/forge/product-manager/README.md), [`methodologies/forge/product-manager/product-bootstrap-flow.md`](methodologies/forge/product-manager/product-bootstrap-flow.md).

## Cursor: Project Setup Versona

- **Template:** [`methodologies/forge/versona/catalog/workflow/versona-project-setup.mdc.template`](methodologies/forge/versona/catalog/workflow/versona-project-setup.mdc.template) → `.cursor/rules/versona-project-setup.mdc`
- **Trigger:** **`setup`** or `@versona-project-setup` — checklist and gap analysis (pair with **`@forge-setup`** from [`methodologies/forge/setup/forge-setup.mdc.template`](methodologies/forge/setup/forge-setup.mdc.template) for the questionnaire).

## See also

- [`methodologies/forge/setup/README.md`](methodologies/forge/setup/README.md) — adoption entry point  
- [`methodologies/forge/versona/README.md`](methodologies/forge/versona/README.md) — Versona catalog
