---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Customer health scoring and risk detection

## Overview

**Customer health scoring** turns scattered signals — usage, support, sentiment, billing, and outcomes — into a **prioritized view of risk and opportunity**. It supports proactive customer management: who needs attention now, with what playbook, and whether interventions work. This guide covers components, methods, tiers, and implementation — without prescribing a single vendor or model.

---

## Health score components

| Component | Typical signals |
|-----------|-----------------|
| **Product engagement** | DAU / WAU / MAU, depth (breadth of features, key events), recency and frequency, seat utilization |
| **Support health** | Ticket volume and trend, severity / priority mix, reopen rate, CSAT / CES after resolution |
| **Relationship health** | NPS or pulse surveys, executive sponsor engagement, QBR attendance, stakeholder coverage |
| **Financial health** | Payment status, expansion vs. contraction signals, contract timeline and renewal window |
| **Outcome achievement** | Success plan milestones, implementation checklist completion, stated goal progress |

Weight components by **what predicts your outcomes** (retention, expansion, advocacy) — not by what is easiest to measure.

---

## Health score architecture

```blueprint-diagram
key: swimlane
alt: Health score architecture
title: Health score signal architecture
summary: How component signals compose a governed composite score while calibration loops keep tiers actionable for CSMs.
node: Health score architecture
detail: Frames how signal lanes compose the prioritized risk and opportunity view.
more: Engagement, support, relationship, financial, and outcome components from the table above feed weighted sub-scores before tier routing.
node: Lane A
detail: Primary path from raw signals through scoring to prioritized account action.
more: Pipelines collect product, support, billing, and outcome metrics with consistent account IDs before weights produce a composite score.
node: handoff
detail: Passes tiered scores and alerts into CSM and automated playbooks.
more: Green, yellow, and red bands trigger different automated actions and outreach depth per the risk tier framework below.
node: shared outcome
detail: A reviewable prioritized view of account risk and opportunity.
more: CSMs and managers use the composite to decide Monday-morning attention without analytics theater.
node: Lane B
detail: Parallel lane for score calibration and governed course correction.
more: CSM judgment, false-positive review, and quarterly weight iteration keep the model aligned with churn and expansion outcomes.
node: inspect / adapt
detail: Reviews tier accuracy against outcomes and adjusts weights or thresholds.
more: Correlate component metrics with churn or downgrade; recalibrate when thresholds fire too often or miss saves.
node: feedback
detail: Returns intervention results and tier movement to refine the score model.
more: Track whether tier changes and plays correlate with improved usage, renewal, or save rate per the closure guidance on this page.
fallback_ascii: |
  Health score architecture

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
```

---

## Scoring methodology comparison

| Method | Pros | Cons | Data requirements |
|--------|------|------|-------------------|
| **Weighted average** | Transparent; easy to explain to CSMs and leadership | May miss nonlinear interactions | Clean metrics per component; calibration against outcomes |
| **Machine learning** | Can capture complex patterns | “Black box” risk; governance harder | Historical churn/expand labels; feature store discipline |
| **Rule-based** | Fast to ship; aligns to known failure modes | Brittle if product/market shifts | Documented business rules; regular review |
| **Hybrid** | Rules for known risks + model for edge cases | More operational complexity | Both rule definitions and labeled outcomes |

Start simple where culture and data maturity are low; add sophistication when **actions** and **measurement** keep pace.

---

## Weight calibration

1. **Hypothesize** drivers from churn interviews, support themes, and product analytics.
2. **Correlate** component metrics with **churn**, **downgrade**, or **negative expansion** (and with positive outcomes you want to reinforce).
3. **Iterate** weights quarterly or when major product changes alter behavior.
4. **Validate** with CSMs: false positives erode trust; false negatives miss saves.

Document **lineage**: which fields feed which sub-score, refresh cadence, and known gaps.

---

## Risk tier framework

| Tier | Score range (example) | Characteristics | Automated actions | CSM actions | Escalation |
|------|------------------------|-----------------|-------------------|-------------|------------|
| **Healthy (green)** | Upper band | Strong usage, low support distress, positive or neutral sentiment | Positive triggers (expansion cues, advocacy asks) | Proactive QBRs; growth plays | As needed for strategic accounts |
| **At-risk (yellow)** | Middle band | Mixed signals; usage dip or support spike | Alerts to owner; suggested playbooks | Outreach, success plan refresh, training | Manager visibility on aged yellow |
| **Critical (red)** | Lower band | Severe usage collapse, exec churn, payment risk, or explicit risk statements | High-priority routing; exec notification rules | Rescue plan, exec sponsor, commercial levers per policy | VP / cross-functional war room where warranted |

Thresholds should be **calibrated** to your base rates — a “red” that fires on 40% of accounts is not operational.

---

## Risk detection through intervention and learning

```blueprint-diagram
key: linear
alt: Risk detection through intervention and learning
title: Risk detection intervention loop
summary: Detect tier shifts, intervene with matched playbooks, and learn whether actions improve usage and renewal outcomes.
node: Start
detail: Leading signals from the composite health score cross tier thresholds.
more: Product engagement dips, support spikes, and relationship gaps trigger yellow or red bands before renewal crisis.
node: Core steps (see walkthrough below)
detail: Route alerts to tier-matched playbooks and governed CSM outreach.
more: Automated routing, suggested playbooks, and escalation rules from the risk tier framework guide intervention depth by band.
node: Outcome
detail: Record whether usage, renewal, or save rate improved after plays.
more: Lagging signals such as cancellation requests validate model tuning and post-mortem learning.
node: Note: tier changes
detail: Track tier movement as evidence that interventions changed account trajectory.
more: Correlating tier changes with plays closes the loop on score calibration and playbook effectiveness.
fallback_ascii: |
  Risk detection through intervention and learning

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: tier changes
```

Close the loop: track whether **tier changes** and **plays** correlate with improved usage, renewal, or save rate.

---

## Leading vs. lagging indicators

| Type | Examples | Use |
|------|----------|-----|
| **Leading** | Login frequency drop, key feature abandonment, support escalation pattern, champion departure, stalled onboarding milestones | Early warning; trigger playbooks before renewal crisis |
| **Lagging** | Cancellation request, payment failure, signed non-renewal, contract expiry without engagement | Confirms outcome; feeds model training and post-mortems |

Health scores should emphasize **leading** signals for actionability; lagging signals validate and tune the model.

---

## Health score by business model

| Model | Emphasis |
|-------|----------|
| **SaaS (seat / usage)** | Product depth, seat activation, admin health |
| **Marketplace** | Supply and demand balance, liquidity, quality / dispute signals |
| **API platform** | Call volume, error rates, latency SLO adherence, key integration health |
| **Enterprise** | Stakeholder map coverage, security / procurement milestones, executive engagement |

One global score rarely fits; consider **sub-scores** by motion (e.g. product vs. relationship) with a composite for prioritization.

---

## Implementation roadmap

| Phase | Focus |
|-------|--------|
| **Phase 1 — Manual scoring** | Spreadsheet or CRM fields; CSM judgment + weekly review; document definitions |
| **Phase 2 — Automated data collection** | Pipeline from product, support, billing; consistent account IDs; data quality checks |
| **Phase 3 — Predictive model** | Labeled outcomes; validate lift over rules; governance and explainability policy |
| **Phase 4 — Prescriptive actions** | Recommended next best action; experiment framework for plays |

Skipping **Phase 2** quality usually wastes model effort.

---

## Technology stack

| Layer | Examples |
|-------|----------|
| **CS platforms** | Gainsight, ChurnZero, Totango, Vitally — health scores, plays, dashboards |
| **Custom** | Warehouse + dbt + reverse ETL or in-app flags; full control, higher build cost |
| **Integration** | Event pipelines, CRM as system of record for account, ticketing sync |
| **Dashboards** | Executive rollup, CSM workbench, manager queue — different detail density |

Design dashboards for **decisions**, not vanity: “what do I do Monday morning?”

---

## Anti-patterns

| Anti-pattern | Effect |
|--------------|--------|
| **Too many components** | Noise; unstable scores; CSM distrust |
| **Equal weighting** | Ignores true drivers of churn |
| **No action triggers** | Score is analytics theater |
| **No benchmarks** | Cannot tell normal seasonality from crisis |
| **Gaming the score** | Incentives drive theater metrics instead of customer outcomes |

---

## External references

- **Gainsight** — Customer Success resources and health score playbooks.
- **Customer Success** (Mehta et al.) — Foundational framing for CS operations and metrics.
- **ChurnZero** — Blog and materials on engagement scoring and plays.
- **TSIA** — Frameworks for service and success economics and maturity.

---

*Keep project-specific customer success documentation in `docs/product/customer-success/` and support playbooks in `docs/operations/`, not in this file.*
