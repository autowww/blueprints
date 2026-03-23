# Forge ceremonies → ceremony foundation

**Purpose:** Map **Forge ceremonies** to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical Forge narrative:** [`https://forgesdlc.com/methodology-overview.html`](https://forgesdlc.com/methodology-overview.html) · [Prescriptive ceremonies](../forge/ceremonies-prescriptive.md)

---

## Ceremonies × intent types

| Forge ceremony | Foundation intents (primary → secondary) | Notes |
|----------------|------------------------------------------|-------|
| **Refinement** (Ore → Ingot) | **C1 Align** → **C2 Commit** | Shape Ore into Ingots; Bellows challenge at decision points; Ember Log captures trade-offs. |
| **Planning** (Ingot → Sparks) | **C2 Commit** → **C1 Align** | Decompose Ingots into Sparks with phase prefixes; scope the iteration; sequence by risk reduction. |
| **Daily sync** (Charge) | **C3 Sync** | Confirm today's Charge; surface blockers; declare hat; Banking decisions. 15-minute timebox. |
| **Review** (evidence assessment) | **C4 Inspect** → **C1 Align** | Demonstrate increment; assess evidence; Bellows challenge; determine Assay Gate readiness. |
| **Assay Gate** (release readiness) | **C6 Assure** | Evidence-based release decision; per-work-type evidence requirements. Separate from Review. |
| **Retro** (learning) | **C5 Improve** | Metrics review, Ember Log review, Bellows effectiveness, improvement experiments; learning feeds new Ore. |

**Ore intake** is **continuous** — not a scheduled ceremony. It feeds the Refinement pipeline.

---

## What git-based tracking approximates vs what ceremonies need

| Ceremony | Git / commits approximate | You still need (human / AI) |
|----------|---------------------------|------------------------------|
| Refinement | Linked work units, spec changes | **Bellows challenge**, stakeholder input, Ember Log |
| Planning | Work decomposition in issues/tasks | **Capacity**, sequencing, **phase assignment** |
| Daily sync | Activity per contributor | **Charge declaration**, verbal blockers, hat declaration |
| Review | Merged work, test results | **Stakeholder feedback**, evidence assessment |
| Assay Gate | CI quality gates, test reports | **Evidence package review**, release decision |
| Retro | Throughput themes (weak) | **Decision review**, Bellows tuning, improvement experiments |

---

## Suggestions (Forge-specific)

| Ceremony | Suggestions |
|----------|-------------|
| **Refinement** | Time-box Bellows invocation; do not challenge every Ore item. Focus on high-value, high-risk items. Write Ember Log entries during refinement, not after. |
| **Planning** | Verify every Spark has a phase prefix. Intentionally undercommit — leave margin in the Charge for interruption and learning. |
| **Daily sync** | Declare your hat for the day. Keep to 15 minutes; defer problem-solving to follow-up huddles. |
| **Review** | Show working software; Bellows challenges should surface new concerns, not repeat known issues. Feed backlog changes visibly. |
| **Assay Gate** | Keep it strict and short. If evidence is missing, the answer is "not yet" — adjust scope, not standards. |
| **Retro** | Review the Ember Log for decision patterns. Assess which Bellows disciplines added value and which created noise. |

For **cross-methodology** blend tips (e.g. Forge + Kanban flow), see [`methodology-bridge.md`](methodology-bridge.md).

For **lean tenets** (keeping Forge lightweight), see [`https://forgesdlc.com/methodology-overview.html` § Lean tenets](https://forgesdlc.com/methodology-overview.html#lean-tenets-keeping-forge-lightweight).

---

## Agentic note

Human **accountability** for Ore acceptance, Spark quality, release decisions, and Ember Log integrity stays with the team. Bellows agents assist challenge; they do not own delivery. See [`../agentic-sdlc.md`](../agentic-sdlc.md).
