---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Spiral ceremonies → ceremony foundation

**Purpose:** Map **Spiral Model** quadrant events and anchor-point milestones to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical Spiral narrative:** [`https://forgesdlc.com/methodologies-spiral.html`](https://forgesdlc.com/methodologies-spiral.html) · [Wikipedia — Spiral model](https://en.wikipedia.org/wiki/Spiral_model)

**Note:** The Spiral Model's ceremonies revolve around **quadrant transitions** and **milestone gates**. Below maps typical practices; actual cadence depends on spiral scope and risk profile.

---

## Practices / meetings × intent types

| Common practice | Foundation intents (primary → secondary) | Notes |
|-----------------|------------------------------------------|--------|
| **Spiral planning** (Q1) | **C1 Align** → **C2 Commit** | Define objectives, alternatives, constraints; commit to risk-analysis approach. |
| **Risk review** (Q2) | **C6 Assure** → **C1 Align** | Systematic risk identification and resolution; may redirect objectives. |
| **Development sync** (Q3) | **C3 Sync** | Coordination during build; approach may be Agile, phased, or prototype-driven. |
| **Prototype demo** | **C4 Inspect** → **C6 Assure** | Demonstrate risk-reduction evidence; validate feasibility. |
| **Anchor-point review** (Q4) | **C4 Inspect** → **C1 Align** | Stakeholder commitment gate; evaluate results and plan next spiral. |
| **Retrospective** | **C5 Improve** | Compare predicted vs actual risk outcomes; improve estimation and process. |

**C6** in the Spiral Model is primarily **risk-driven**: assurance comes from systematic risk analysis (Q2) and evidence-based reviews (Q4), not from a separate quality phase.

---

## Tracking

**Risk register** is the primary tracking artifact beyond the standard spine. Each spiral should document: risks identified, resolution strategy chosen, outcome achieved. Git shows engineering progress; **risk decisions** need explicit documentation in `docs/` or the project risk register.

---

## Suggestions (Spiral-specific)

| Practice | Suggestions |
|----------|-------------|
| **Spiral planning** | Scale planning effort to the spiral: early concept spirals need hours, not days. Focus on **what risks to address**, not detailed task breakdowns. |
| **Risk review** | Prioritize ruthlessly: address the **top 3–5 risks** per spiral. Use prototypes for technical risks, market research for business risks. |
| **Prototype demo** | Make prototypes **visibly disposable** — label them, timebox them, and plan their retirement. Production-quality prototypes defeat the purpose. |
| **Anchor-point review** | Present **evidence**, not opinions. Show what risks were resolved, what remains, and what the next spiral will address. |
| **Retrospective** | Track **risk prediction accuracy** across spirals. Teams that consistently underestimate risk need to adjust their analysis approach. |

Crosswalk to other methodologies: [`methodology-bridge.md`](methodology-bridge.md).
