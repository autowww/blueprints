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
alt: Diagram
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
alt: Diagram
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
