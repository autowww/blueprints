# Testing & test plans

**Purpose:** Scope-level **test plans** (who tests what, which levels, exit criteria) complement per-story acceptance criteria and the traceability matrix under `docs/requirements/traceability/`.

## When to add a test plan

- Milestone or release with several stories and manual/QA involvement
- Regulatory or high-risk areas (auth, data handling)
- Before a major release — pair with [`docs/release/README.md`](../release/README.md)

For small changes, a **test plan section inside the story spec** is enough.

## Template

Copy [`blueprints/sdlc/templates/TEST-PLAN.template.md`](../../blueprints/sdlc/templates/TEST-PLAN.template.md) to this folder (e.g. `TEST-PLAN-M1.md`) and fill in.

## Automation

<!-- Document CI test steps here; link to [`docs/development/CI-CD.md`](../development/CI-CD.md). -->

## SDLC

Process detail: [`blueprints/sdlc/SDLC.md`](../../blueprints/sdlc/SDLC.md) §7 (CI/CD, quality gates, test plans).
