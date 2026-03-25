---
name: run-product-versona-challenge
description: >-
  Run a Forge Product family Versona challenge (or Sampling demo) using blueprint
  rules and output shape. Use when the user wants structured product/BA/UX/marketing/CS
  challenge or triage before deeper work.
---

# Run Product Versona challenge (Forge)

## When to use

- User asks for **product challenge**, **multi-lens review**, **assumption / risk pass**, or **which Versona to invoke**.
- Work touches **vision, roadmap, requirements, GTM, or success** — not low-level code craft alone.

## Steps

1. **Confirm context** — Which artifact or Spark is in scope? Which files are open?
2. **Pick rule** — Full pass: **Product family** (`versona-family-product` if installed) or **Sampling** (`versona-sampling` + tasklets) for a shallow demo. Single discipline: `versona-product-management`, `versona-ba`, etc.
3. **Globs** — If rules never attach, suggest tuning per [`blueprints/sdlc/methodologies/forge/versona/RECOMMENDED-GLOBS.md`](../../../../methodologies/forge/versona/RECOMMENDED-GLOBS.md) (copy path for the consuming repo’s `blueprints/` submodule).
4. **Output** — Follow [`VERSONA-CONTRACT.md`](../../../../methodologies/forge/versona/VERSONA-CONTRACT.md): work item, phase, intensity, concerns table, evidence requests, recommendation.
5. **Routing** — If unsure which disciplines apply, run or emulate [`forge-versona.mdc`](../../cursor-rules/forge-versona.mdc) routing first.

## Install reference

- Versona templates: `blueprints/sdlc/methodologies/forge/versona/` — `versona-generic.mdc.template` at root; everything else under `catalog/` (`discipline/<domain>/`, `discipline/<domain>/family/` for aggregators, `routing/`, `meta/`, `workflow/`). See `versona/catalog/TEMPLATE-INDEX.md`.
- Tasklets + Sampling: `bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh`
- Align rules with `forge.config.yaml`: `bash blueprints/sdlc/methodologies/forge/setup/check-forge-cursor-alignment.sh`

## Adoption

Copy this folder to the project’s **`.cursor/skills/run-product-versona-challenge/`** (or merge into your skills library) so the agent can discover it when relevant.
