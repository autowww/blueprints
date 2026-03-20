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

## Spec-driven (SDD) — ceremony & process I/O

| Path | Use |
|------|-----|
| [**sdd/README.md**](sdd/README.md) | Blank specs for **inputs/outputs/preconditions** (agents, product, engineering). |
| [**sdd/CEREMONY-INTENT.template.md**](sdd/CEREMONY-INTENT.template.md) | Map **C1–C6** or team rituals to SDD tables. |
| [**sdd/PROCESS-SLOT.template.md**](sdd/PROCESS-SLOT.template.md) | Gates, release slices, toolchain steps. |

Normative schema and worked examples: [`../methodologies/spec-driven/`](../methodologies/spec-driven/README.md) · handbook [`../docs/spec-driven-sdd-schema.html`](../docs/spec-driven-sdd-schema.html).
