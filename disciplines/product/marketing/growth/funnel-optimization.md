---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Growth Engineering & Funnel Optimization

**Overview:** Growth engineering treats the funnel as a **system** — stages, conversion rates, guardrails, and feedback loops — improved through **prioritized experiments** rather than one-off campaigns. The goal is repeatable learning: each change should be falsifiable, measured against pre-registered metrics, and safe for users and the brand.

## AARRR (“pirate metrics”) framework

| Stage | Definition | Key metrics (examples) | Example KPIs | Typical ownership |
|-------|------------|------------------------|--------------|-----------------|
| **Acquisition** | Users arrive via channels | CAC, installs, signups, traffic by source | Blended CAC, paid vs organic mix, channel LTV | Marketing, Growth |
| **Activation** | Users reach first meaningful value | Time-to-value, activation rate, onboarding completion | % completing “aha” event in session 1 | Product, Growth |
| **Retention** | Users return or stay subscribed | D1/D7/D30, churn, cohort curves | Net revenue retention (NRR), WAU/MAU | Product, CS, Growth |
| **Revenue** | Monetization and expansion | ARPU, expansion, trial-to-paid | LTV, paywall conversion, upgrade rate | Product, Finance, Growth |
| **Referral** | Users bring others | K-factor (use carefully), invite rate, NPS → referral | Viral coefficient by cohort, referral % of signups | Growth, Product |

## AARRR funnel with conversion rates

```blueprint-diagram
key: linear
alt: Diagram
```

## Growth process cycle

```blueprint-diagram
key: linear
alt: Diagram
```

- **ICE / RICE:** Score ideas on Impact, Confidence, Ease (ICE) or add Reach for RICE — use consistently so the backlog is comparable week to week.
- **Learning:** Document **hypothesis, design, result, decision** — even null results reduce duplicate work.

## Funnel instrumentation and guardrails

| Layer | Examples |
|-------|----------|
| **Stage definitions** | Mutually exclusive rules (e.g. “activated” = completed event X within Y hours of signup) |
| **Event quality** | Schema versioning, deduplication, identity stitching for logged-in vs anonymous |
| **Guardrail metrics** | Refund rate, chargebacks, support tickets per thousand users, spam signups — must not regress while optimizing conversion |
| **Qualitative triangulation** | Session replay (privacy-safe), interviews, and support themes to explain *why* a metric moved |

Without guardrails, teams often “win” experiments that damage trust, compliance, or operational load — then pay the cost in the next quarter.

## Acquisition optimization

| Lever | Notes |
|-------|--------|
| **Channel diversification** | Reduce single-channel dependency; compare cohort quality, not just CPA |
| **CAC optimization** | Improve creative, landing, and activation together — cheap clicks that do not activate raise blended CAC |
| **Organic vs paid mix** | Paid for learning velocity; organic for durability — align budget to PMF stage |
| **Virality (k-factor)** | Treat K as a sketch; model invites per active user, saturation, and incentive distortion |

## Activation optimization

| Lever | Notes |
|-------|--------|
| **Time-to-value** | Remove steps between signup and the first successful outcome |
| **“Aha moment”** | Infer from retention correlates (events that split retained vs churned cohorts) — validate with experiments |
| **Onboarding** | Checklists, templates, guided setup, and smart defaults |
| **Progressive disclosure** | Surface depth after the first win — avoid walls of configuration up front |

## Activation sequence (conceptual)

```blueprint-diagram
key: sequence
alt: Diagram
```

## Retention optimization

| Topic | Practice |
|-------|----------|
| **Cohort analysis** | Group by signup week or campaign; compare curves, not single snapshots |
| **Retention curves** | Flattening curves suggest PMF in a segment; steep drops flag onboarding or value gaps |
| **Engagement loops** | Notifications, in-product triggers, and content that tie to recurring jobs |
| **Re-engagement** | Push, email, and in-app win-back — respect frequency caps and consent |
| **Habit (Hook model)** | Trigger → action → variable reward → investment — ensure the “investment” stores future value (data, content, workflow) |

## Revenue optimization

| Lever | Notes |
|-------|--------|
| **Pricing experiments** | Grandfather fairly; test packaging and presentation before destructive list-price wars |
| **Upgrade triggers** | Usage thresholds, feature gates, and success moments (not arbitrary paywalls) |
| **Expansion** | Seats, usage tiers, add-ons — align sales and PLG motions |
| **LTV / CAC** | Targets depend on payback period and capital efficiency; define guardrails (support load, refunds) |
| **Paywall UX** | Clarity of value, trial design, and payment friction materially affect conversion |

## Referral optimization

| Element | Guidance |
|---------|----------|
| **Loop design** | Make inviting part of a natural workflow (collaboration, sharing output) |
| **Incentives** | Two-sided rewards reduce friction; watch fraud and low-quality referrals |
| **Tracking** | De-duplicate invites; attribute assisted vs direct referral paths |
| **NPS** | Promoters are a pool for referrals — pair surveys with concrete invite CTAs |

## A/B testing infrastructure

| Topic | Guidance |
|-------|----------|
| **Experiment design** | Hypothesis, primary metric, guardrails, minimum detectable effect |
| **Sample size / power** | Pre-calculate before launch; avoid peeking without sequential rules |
| **Statistical significance** | Frequentist p-values or Bayesian probability — pick one approach per program |
| **Sequential testing** | Safe interim reads when volume is high |
| **Multi-armed bandits** | Good for short-lived optimization (headlines, creatives) with clear reward |
| **Feature flags** | Tie exposure to user/account IDs; support kill switches and gradual rollouts |
| **SRM checks** | Sample ratio mismatch invalidates many results — monitor allocation drift |

## Experimentation culture

| Pillar | Behaviors |
|--------|-----------|
| **Velocity** | Small batches, clear WIP limits on running experiments |
| **Learning backlog** | Ideas ranked; “done” includes write-up |
| **Team shape** | PM + engineer + designer + analyst (or shared analyst pool) for full-stack tests |
| **Ethics** | No dark patterns; informed consent where required; vulnerable users protected |

## Anti-patterns

| Anti-pattern | Consequence |
|--------------|-------------|
| **Premature growth** | Scaling before PMF burns capital and damages reputation |
| **Vanity metrics** | Optimizing signups without activation or revenue |
| **No statistical rigor** | False wins and thrashing roadmap |
| **Growth hacking without ethics** | Regulatory risk, churn, and brand erosion |

## External references

- Sean Ellis & Morgan Brown, *Hacking Growth* — growth process and case patterns
- [Reforge](https://www.reforge.com/) — Growth Series and advanced retention / monetization material (paid programs)
- Alistair Croll & Benjamin Yoskovitz, *Lean Analytics* — metrics, stages, and focus for startups

**Index:** [`growth/README.md`](README.md) · **Marketing map:** [`../MARKETING.md`](../MARKETING.md)

---

*Keep project-specific marketing plans in `docs/product/marketing/` and GTM documents in `docs/product/`, not in this file.*
