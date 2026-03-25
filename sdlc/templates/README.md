# Templates

Copy into `docs/` (or your doc root) and customize. **Not** part of the process itself—shortcuts for new projects.

## Project `sdlc/` workspace

Canonical files for a **mutable** `sdlc/` folder at repo root (see [`../SDLc-WORKSPACE.md`](../SDLc-WORKSPACE.md) and [`../scripts/README.md`](../scripts/README.md)).

| Path | Use |
|------|-----|
| [**sdlc/README.template.md**](sdlc/README.template.md) | Render to `sdlc/README.md` with `{{PROJECT_NAME}}` replaced (script does this). |
| [**sdlc/TRACKING-FOUNDATION.md**](sdlc/TRACKING-FOUNDATION.md) | Copy into `sdlc/` — engineering tracking foundation. |
| [**sdlc/TRACKING-METHODOLOGIES.md**](sdlc/TRACKING-METHODOLOGIES.md) | Copy into `sdlc/` — methodology lenses. |
| [**sdlc/TRACKING-CHALLENGES.md**](sdlc/TRACKING-CHALLENGES.md) | Copy into `sdlc/` — limits and caveats. |

## Docs (`docs/`)

| File | Use |
|------|-----|
| [**ROADMAP.template.md**](ROADMAP.template.md) | Optional milestone/epic table; pair with a WBS or backlog elsewhere. |
| [**TEST-PLAN.template.md**](TEST-PLAN.template.md) | Optional scope-level test plan (levels, environments, traceability, exit criteria). |

## Forge SDLC workspace

Seed files for a **mutable** `forge/` workspace and `ember-logs/` at repo root. See [`../methodologies/forge/setup/README.md`](../methodologies/forge/setup/README.md) for adoption guide.

| Path | Use |
|------|-----|
| [**forge/README.template.md**](forge/README.template.md) | Forge workspace README with directory structure and script references. |
| [**forge/forge.config.template.yaml**](forge/forge.config.template.yaml) | Project Forge configuration (team, Versonas, Assay Gate, paths). |
| [**forge/charge.template.md**](forge/charge.template.md) | Daily Charge seed file. |
| [**forge/ember-log-entry.template.md**](forge/ember-log-entry.template.md) | Ember Log daily file seed. |
| [**forge/journal-entry.template.md**](forge/journal-entry.template.md) | Day journal seed. |
| [**forge/assay-gate.template.md**](forge/assay-gate.template.md) | Assay Gate evidence checklist. |
| [**forge/versona-session.template.md**](forge/versona-session.template.md) | Versona session folder seed (`SESSION.md` + manifest fields) — see [`../methodologies/forge/versona/VERSONA-FRAMEWORK.md`](../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §7. |
| [**forge/session.manifest.yaml.template**](forge/session.manifest.yaml.template) | Optional YAML twin of session manifest. |
| [**forge/versona-process.template.md**](forge/versona-process.template.md) | Repeatable multi-step Versona / human process doc (mermaid placeholders). |
| **forge/cursor-rules/** | Ready-to-use Cursor rules: `forge-daily.mdc`, `forge-planning.mdc`, `forge-setup.mdc`, `forge-versona.mdc`, `forge-product-manager.mdc`. Optional Layer-0 baseline: copy `../methodologies/forge/versona/versona-generic.mdc.template` from blueprints (see `versona/catalog/ANCESTRY.md`, `versona/catalog/TEMPLATE-INDEX.md`). |
| **forge/cursor-skills/** | Optional Cursor **Skills** to copy into `.cursor/skills/` (e.g. `run-product-versona-challenge`). |
| **—** | Align `forge.config.yaml` with `.cursor/rules/`: [`../methodologies/forge/setup/check-forge-cursor-alignment.sh`](../methodologies/forge/setup/check-forge-cursor-alignment.sh) |

## Spec-driven (SDD) — ceremony & process I/O

| Path | Use |
|------|-----|
| [**sdd/README.md**](sdd/README.md) | Blank specs for **inputs/outputs/preconditions** (agents, product, engineering). |
| [**sdd/CEREMONY-INTENT.template.md**](sdd/CEREMONY-INTENT.template.md) | Map **C1–C6** or team rituals to SDD tables. |
| [**sdd/PROCESS-SLOT.template.md**](sdd/PROCESS-SLOT.template.md) | Gates, release slices, toolchain steps. |

Normative schema and worked examples: [`../methodologies/spec-driven/`](../methodologies/spec-driven/README.md) · handbook HTML: generated under `blueprints/website/` by `generator/build-handbook.py` (e.g. `sdlc--methodologies-spec-driven-sdd-io-schema.html`).
