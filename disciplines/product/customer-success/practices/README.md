---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Customer Success — practice guides (index)

These **project-agnostic** guides support **proactive customer management**: instrumenting journeys, scoring risk before renewal crises, and running retention and win-back with clear metrics. They extend the conceptual body of knowledge in [**CUSTOMER-SUCCESS.md**](../CUSTOMER-SUCCESS.md) (principles, lifecycle, PDLC/SDLC). Use them for topic depth; keep implementation specifics in project docs (footer).

---

## Where practices sit in the customer lifecycle

```blueprint-diagram
key: swimlane
alt: Where practices sit in the customer lifecycle
title: Customer success practice lanes
summary: How proactive practice guides advance customers toward outcomes while inspect-and-adapt loops keep retention governed and traceable.
node: Where practices sit in the customer lifecycle
detail: Frames how the practice guides map across the customer lifecycle on this index.
more: Onboarding, health scoring, and churn prevention extend CUSTOMER-SUCCESS.md; expansion and advocacy remain in the parent body of knowledge.
node: Lane A
detail: Primary work stream from first value through sustained customer outcomes.
more: Carries onboarding design, activation milestones, and handoffs from sales or marketing into measurable success plans.
node: handoff
detail: Passes governed context between lifecycle stages and practice guides.
more: Sales-to-CS transitions, milestone completion, and renewal prep each produce artifacts the next practice consumes without losing account history.
node: shared outcome
detail: Observable customer value both lifecycles and teams align on.
more: Time-to-value, activation, health tier, and retention metrics land in project docs under docs/product/customer-success/ per this page's footer guidance.
node: Lane B
detail: Parallel stream for risk inspection and governed course correction.
more: Health scoring, support signals, and feedback programs feed interventions before renewal crises or preventable churn.
node: inspect / adapt
detail: Reviews journey signals and adjusts coverage or playbooks.
more: Tiered thresholds, alert routing, and false-positive governance from the health-scoring guide inform when CSM or digital plays change.
node: feedback
detail: Returns measured results and customer voice to upstream practices.
more: VoC synthesis, churn-prevention experiments, and exit insights reopen onboarding assumptions or health-model weights with reviewable evidence.
node: Note: Onboarding
detail: First practice anchor where proactive customer management begins.
more: Onboarding design sets time-to-value, persona journeys, and activation metrics that downstream scoring and retention plays inherit; see onboarding-design.md.
fallback_ascii: |
  Where practices sit in the customer lifecycle

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback

  Note: Onboarding
```

Deep dives: [**Onboarding**](onboarding-design.md), [**Health scoring**](health-scoring.md), [**Churn prevention**](churn-prevention.md). **Expansion and advocacy** remain in [**CUSTOMER-SUCCESS.md**](../CUSTOMER-SUCCESS.md).

---

## Practice guide index

| Practice guide | Focus |
|----------------|--------|
| [**Onboarding design**](onboarding-design.md) | Time-to-value, guided setup and progressive disclosure, persona-based journeys, milestone definition, in-product vs. human-led onboarding, completion and activation metrics, handoff from sales/marketing. |
| [**Health scoring**](health-scoring.md) | Signal selection (product usage, support, billing, sentiment), model design (rules vs. ML), tiering and thresholds, data contracts with engineering/analytics, alert routing, governance and false-positive management. |
| [**Support operations setup**](../CUSTOMER-SUCCESS.md#4-support-operations) | Tiered support (L1/L2/L3), channel mix, SLA policy and measurement, ticket taxonomy, escalation paths, shift and capacity planning, knowledge base IA, deflection strategy, tooling integrations. |
| [**Feedback program design**](../CUSTOMER-SUCCESS.md#6-feedback-loops) | NPS / CSAT / CES program architecture, sampling and timing, survey fatigue controls, linking responses to accounts and journeys, VoC synthesis, routing insights to roadmap and closing the loop with respondents. |
| [**Churn prevention**](churn-prevention.md) | Risk signals by segment, tiered interventions (digital, CSM, executive), save offers and commercial levers, win-back and exit interviews, involuntary churn (dunning, payments), experiment design for retention initiatives. |

For lifecycle mapping across SDLC/PDLC, see [**CS-SDLC-PDLC-BRIDGE.md**](../CS-SDLC-PDLC-BRIDGE.md).

---

*Keep project-specific customer success documentation in `docs/product/customer-success/` and support playbooks in `docs/operations/`, not in this file.*
