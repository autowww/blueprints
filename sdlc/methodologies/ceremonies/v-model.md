---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# V-Model ceremonies → ceremony foundation

**Purpose:** Map **V-Model** design reviews and test gates to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical V-Model narrative:** [`https://forgesdlc.com/methodologies-v-model.html`](https://forgesdlc.com/methodologies-v-model.html) · [Wikipedia — V-model](https://en.wikipedia.org/wiki/V-model_(software_development))

**Note:** The V-Model's ceremonies center on **left-side reviews** (design gates) and **right-side reviews** (test gates). Below maps typical practices.

---

## Practices / meetings × intent types

| Common practice | Foundation intents (primary → secondary) | Notes |
|-----------------|------------------------------------------|--------|
| **Requirements review** | **C1 Align** → **C2 Commit** | Baseline requirements; agree acceptance approach. Top of the V. |
| **Design review** (system + detailed) | **C2 Commit** → **C4 Inspect** | Approve design; confirm testability and traceability. |
| **Test plan review** | **C2 Commit** → **C6 Assure** | Approve test strategy, traceability matrix, environment plan per V-level. |
| **Development sync** | **C3 Sync** | Coordination during implementation phase (bottom of V). |
| **Test readiness review (TRR)** | **C6 Assure** → **C4 Inspect** | Gate: is the build and environment ready for testing at this V-level? |
| **Test result review** | **C4 Inspect** | Evaluate test outcomes; decide pass/fail/conditional at each V-level. |
| **Acceptance review** | **C4 Inspect** → **C1 Align** | Formal acceptance at top-right of V; deployment authorization. |

**C5 (Improve)** in the V-Model is typically a **post-project** activity (lessons learned, process audit). Better teams add **mid-cycle** retrospectives during long development phases.

---

## Tracking

**Requirements traceability matrix (RTM)** is the primary tracking artifact. It links requirements → design elements → test cases → test results across all V-levels. Maintain in `docs/requirements/traceability/` or your ALM tool.

---

## Suggestions (V-Model-specific)

| Practice | Suggestions |
|----------|-------------|
| **Requirements review** | Verify **testability** of each requirement. Vague requirements produce vague tests. |
| **Design review** | Check traceability: does each design element map to a requirement? Does the corresponding test plan exist? |
| **Test plan review** | Flag **untested requirements** explicitly. 100% coverage is the target; waivers must be documented. |
| **TRR** | Do not proceed if the test environment does not match production configuration (where applicable). |
| **Test result review** | Classify failures by V-level: a unit test failure is different from a system test failure in root cause and fix. |
| **Acceptance** | Base acceptance on **evidence** (traceability, test results, compliance), not on opinions or partial demos. |

Crosswalk to other methodologies: [`methodology-bridge.md`](methodology-bridge.md).
