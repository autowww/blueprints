---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Growth engineering — index

**Growth engineering** is the practice of improving acquisition, activation, retention, revenue, and referral through **systematic experimentation**, **sound instrumentation**, and **honest metrics** — not one-off hacks. It overlaps with marketing operations and product analytics but emphasizes **closed-loop tests** with pre-registered success criteria and **guardrails** (support load, refunds, trust). Blueprint material here is **framework-level**; operational runbooks, experiment tickets, and dashboards belong in `docs/product/marketing/` or platform docs.

**Relationship to channels:** Acquisition levers (SEO, paid, social) live under [`../channels/`](../channels/README.md); this folder focuses on **funnel mechanics**, prioritization, and experimentation discipline once traffic exists or loops are designed.

```blueprint-diagram
key: linear
alt: Process flow
title: Growth engineering loop
summary: How teams move from framed intent through bounded experiments to measurable funnel outcomes with guardrails.
node: Start
detail: Frame the growth opportunity and pre-register success criteria.
more: Anchor the work in a funnel stage lever and define guardrails for support load, refunds, and trust before tests run.
node: Core steps (see walkthrough below)
detail: Run instrumented experiments using the guides and walkthroughs linked below.
more: Apply funnel mechanics, prioritization, and experiment hygiene from funnel-optimization.md; project runbooks live in docs/product/marketing/.
node: Outcome
detail: Deliver a measurable lift or a documented learn with traceable evidence.
more: Compare results against pre-registered criteria and guardrails so wins stay honest and repeatable across the AARRR funnel.
fallback_ascii: |
  Process flow

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## Guides

| Guide | Focus |
|-------|--------|
| [**Funnel optimization**](funnel-optimization.md) | AARRR framing, stage levers, growth process, testing culture, guardrails |

## Planned / stub topics

| Topic | Focus | See |
|-------|--------|-----|
| **A/B testing infrastructure** | Randomization units, sample size and power, sequential testing, SRM checks, feature flags, holdouts, and ethical guardrails | [Funnel optimization](funnel-optimization.md) |
| **Referral programs** | Loop design, K-factor limitations, incentive economics, invite UX, tracking implementation, fraud and abuse — *(planned)* | [Funnel optimization](funnel-optimization.md) |
| **Retention engineering** | Cohort curves, churn drivers, habit formation, lifecycle messaging coordination, win-back experiments — *(planned)* | [Churn prevention](../../customer-success/practices/churn-prevention.md) |
| **Activation optimization** | Time-to-value, aha-moment definition, onboarding experiments, empty states, checklist and progressive disclosure | [Onboarding design](../../customer-success/practices/onboarding-design.md) |

When a topic is still *(planned)*, use [`funnel-optimization.md`](funnel-optimization.md) for the overlapping AARRR framing and experiment hygiene until a dedicated guide lands.

**Core marketing map:** See [`../MARKETING.md`](../MARKETING.md) for how growth fits channels, positioning, and analytics.

**Suggested reading order**

1. [`../MARKETING.md`](../MARKETING.md) — principles and funnel vocabulary  
2. [`funnel-optimization.md`](funnel-optimization.md) — stage metrics, loops, and experiment rigor  
3. [`../channels/README.md`](../channels/README.md) — where acquisition tactics are indexed  

---

*Keep project-specific marketing plans in `docs/product/marketing/` and GTM documents in `docs/product/`, not in this file.*
