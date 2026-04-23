---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Testing & quality assurance

Reusable, **project-agnostic** blueprint for **testing** — the discipline of verifying that software behaves correctly, meets requirements, and is fit for purpose. Grounded in the [ISTQB](https://www.istqb.org/) body of knowledge, adapted for teams already using [`blueprints/sdlc/`](../../../sdlc/README.md) and [`blueprints/pdlc/`](../../../pdlc/README.md).

Testing answers **"is the software correct, reliable, and fit for purpose?"** — a question that spans SDLC verification (phases D–E), PDLC validation (P5 outcome measurement), and continuous delivery pipelines.

| Document | Purpose |
|----------|---------|
| [**APPROACHES.md**](APPROACHES.md) | ISTQB-aligned vocabulary (test levels, test types, test design techniques); modern test pyramid; strategies (shift-left, TDD, BDD, contract testing, visual testing, AI-augmented testing); SDLC phase mapping; ISTQB certification landscape |
| [**AUTOMATION-LANDSCAPE.md**](AUTOMATION-LANDSCAPE.md) | Test automation framework taxonomy (web/E2E, mobile, API/contract, BDD runners, AI-augmented); per-framework profiles; selection decision matrix; cloud infrastructure and device farms |
| [**PLAYWRIGHT-INFRASTRUCTURE.md**](PLAYWRIGHT-INFRASTRUCTURE.md) | Playwright templates, bootstrap scripts, workspace runner, and optional agents recipe — submodule path `blueprints/sdlc/templates/playwright/` |
| [**TESTING-SDLC-PDLC-BRIDGE.md**](TESTING-SDLC-PDLC-BRIDGE.md) | How testing maps across SDLC phases A–F and PDLC phases P1–P6 — role mapping, artifact flow, calibration, anti-patterns |

**Forge defect workflow (markdown repos):** [`sdlc/templates/forge/forge-defect-triage-rca-test-impact.prompt.md`](../../../sdlc/templates/forge/forge-defect-triage-rca-test-impact.prompt.md) — triage, **RCA**, ISTQB-oriented **confirmation/regression** design, `docs/defects/**`, **TRACEABILITY**; pair with **`versona-testing`**.

## Relationship to other packages

| Package | How Testing relates |
|---------|---------------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | Testing activities map to SDLC phases D–E (Build, Verify). The SDLC quality-gate spine ([`SDLC.md`](../../../sdlc/SDLC.md) §7) defines *that* testing is required; this package defines *what kinds* of testing exist and *which tools* are available. Methodology packages keep their testing aspects (V-Model verification pairing, DevOps test pyramid, XP TDD, BDD behavioral contracts). |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | PDLC P5 (Grow) uses testing outcomes as inputs to solution evaluation — did the delivered software meet the validated needs? Acceptance testing validates against outcome criteria from P3. |
| [`blueprints/disciplines/product/ba/`](../../product/ba/README.md) | BA acceptance criteria define *what* to test. Requirements traceability links requirements to test cases. |
| [`blueprints/disciplines/engineering/devops/`](../devops/README.md) | DevOps CI/CD pipelines automate test execution. The test pyramid informs pipeline stage design. |

## Scope

This package covers **testing as a discipline** — not just unit testing or CI configuration. It includes:

- **Test levels** — unit, integration, system, acceptance
- **Test types** — functional, non-functional (performance, security, usability), regression, smoke
- **Test design techniques** — equivalence partitioning, boundary value analysis, decision tables, state transition, exploratory
- **Test strategies** — shift-left, TDD, BDD, contract testing, visual testing, AI-augmented
- **Test automation** — framework taxonomy, selection guidance, cloud infrastructure
- **ISTQB alignment** — standard vocabulary and certification landscape

The package is **descriptive, not prescriptive**: use the test levels, types, and strategies that fit your project's risk profile and team context.

## Related SDLC content

Testing aspects are also threaded through SDLC methodology packages:

| SDLC doc | Testing aspect |
|----------|----------------|
| [`SDLC.md`](../../../sdlc/SDLC.md) §7 | CI/CD, quality gates, test plans — the lifecycle spine |
| [`templates/TEST-PLAN.template.md`](../../../sdlc/templates/TEST-PLAN.template.md) | Copy-paste template for scope-level test plans |
| [`methodologies/v-model/`](../../../sdlc/methodologies/v-model/README.md) | Verification-and-validation pairing; RTM; test-level gates |
| [`methodologies/devops/`](../../../sdlc/methodologies/devops/README.md) | CI/CD pipeline; automated test pyramid in Verify phase |
| [`methodologies/xp.md`](../../../sdlc/methodologies/xp.md) | TDD, continuous integration, pair programming |
| [`methodologies/bdd.md`](../../../sdlc/methodologies/bdd.md) | Behavior-driven development; Given-When-Then; living specs |
| [`methodologies/agentic-sdlc.md`](../../../sdlc/methodologies/agentic-sdlc.md) | AI agent roles in testing (generation, self-healing, drift) |

---

*Keep project-specific test plans in `docs/testing/`, not in this file.*
