---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

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
| [**forge/retro-record.template.md**](forge/retro-record.template.md) | Retro Record — themes, experiments, evidence pointers, triage toward directives ([`../methodologies/forge/ceremonies-prescriptive.md`](../methodologies/forge/ceremonies-prescriptive.md) § “From retro to directives”). |
| [**forge/directive-change-proposal.template.md**](forge/directive-change-proposal.template.md) | Directive Change Proposal (DCP) — bridge before merging `sdlc/` or technical directive updates. |
| [**forge/project-sdlc-directive.template.md**](forge/project-sdlc-directive.template.md) | Project SDLC directive seed (methodology / process). |
| [**forge/technical-directive.template.md**](forge/technical-directive.template.md) | Technical directive seed (implementation standards); pair with ADR when architecture forks. |
| [**forge/versona-session.template.md**](forge/versona-session.template.md) | Versona session folder seed (`SESSION.md` + manifest fields) — see [`../methodologies/forge/versona/VERSONA-FRAMEWORK.md`](../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §7. |
| [**forge/discipline-spike-open.template.md**](forge/discipline-spike-open.template.md) | Exploration spike open checklist (hypothesis, anchors, no-roadmap branch) — [`../methodologies/forge/versona/DISCIPLINE-SPIKE.md`](../methodologies/forge/versona/DISCIPLINE-SPIKE.md). |
| [**forge/discipline-spike-close.template.md**](forge/discipline-spike-close.template.md) | Exploration spike close record (`outputs/SPIKE-CLOSE.md`), Ember Log + git prompts. |
| [**forge/session.manifest.yaml.template**](forge/session.manifest.yaml.template) | Optional YAML twin of session manifest. |
| [**forge/versona-process.template.md**](forge/versona-process.template.md) | Repeatable multi-step Versona / human process doc (diagram-as-code placeholders). |
| [**forge/estimation/ESTIMATION-RULES.template.md**](forge/estimation/ESTIMATION-RULES.template.md) | Copy to `forge/estimation/ESTIMATION-RULES.md` — Fibonacci, t-shirt, token bands, roll-up, defect multipliers (markdown-canonical). |
| [**requirements/ESTIMATES.template.md**](requirements/ESTIMATES.template.md) | Copy to `docs/requirements/ESTIMATES.md` — estimates ledger tables. |
| [**forge/forge-estimation-bootstrap.prompt.md**](forge/forge-estimation-bootstrap.prompt.md) | AI prompt to bootstrap estimation method + `versona-estimation` install. |
| [**forge/forge-defect-triage-rca-test-impact.prompt.md**](forge/forge-defect-triage-rca-test-impact.prompt.md) | AI prompt: defect triage, **RCA**, ISTQB **test impact**, `docs/defects/**`, **TRACEABILITY**. |
| **forge/cursor-rules/markdown-canonical/** | **Markdown-only** guardrails (`markdown-artifact-policy`, `canonicalization-policy`, classifier, decomposer, spark planner, import, estimation, defects, Versona routing) + **`AGENTS.template.md`** — copy into consuming repo `.cursor/rules/` and root `AGENTS.md`. |
| **forge/cursor-rules/** | Ready-to-use Cursor rules: `forge-daily.mdc`, `forge-planning.mdc`, `forge-setup.mdc`, `forge-versona.mdc`, `forge-product-manager.mdc`. Optional Layer-0 baseline: copy `../methodologies/forge/versona/versona-generic.mdc.template` from blueprints (see `versona/catalog/ANCESTRY.md`, `versona/catalog/TEMPLATE-INDEX.md`). |
| **forge/cursor-skills/** | Optional Cursor **Skills** to copy into `.cursor/skills/` (e.g. `run-product-versona-session`, `run-engineering-ai-code-review`). |
| **—** | Cursor rules: [`../methodologies/forge/setup/sync-forge-cursor-rules.sh`](../methodologies/forge/setup/sync-forge-cursor-rules.sh) (`sync` / `diff` / `status` / `check`) — quick ref [`../methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md`](../methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md) |

## Spec-driven (SDD) — ceremony & process I/O

| Path | Use |
|------|-----|
| [**sdd/README.md**](sdd/README.md) | Blank specs for **inputs/outputs/preconditions** (agents, product, engineering). |
| [**sdd/CEREMONY-INTENT.template.md**](sdd/CEREMONY-INTENT.template.md) | Map **C1–C6** or team rituals to SDD tables. |
| [**sdd/PROCESS-SLOT.template.md**](sdd/PROCESS-SLOT.template.md) | Gates, release slices, toolchain steps. |

Normative schema and worked examples: [`../methodologies/spec-driven/`](../methodologies/spec-driven/README.md) · handbook HTML: generated under `blueprints/website/` by `generator/build-handbook.py` (e.g. `sdlc--methodologies-spec-driven-sdd-io-schema.html`).
