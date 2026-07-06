---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Frontend performance (blueprint)

**Purpose:** Deep, **project-agnostic** guidance for web performance optimization. Covers measurement, analysis, and optimization strategies tied to Core Web Vitals and user experience.

**Audience:** Teams adopting [`blueprints/disciplines/engineering/frontend/`](../README.md); project-specific performance budgets and reports stay in **`docs/development/frontend/performance/`**.

Performance is **user experience**: latency, stability, and loading behavior shape trust, task completion, and accessibility. These blueprints separate **how to think** about metrics and optimization from **where this repo records** concrete budgets and regressions.

```blueprint-diagram
key: linear
alt: Process flow
title: Frontend performance workflow
summary: How teams move from framing performance as user experience to governed measurement, optimization, and traceable outcomes.
node: Start
detail: Frame performance as latency, stability, and loading behavior that shapes trust.
more: Anchor work in project-agnostic fundamentals from FRONTEND.md before chasing local optimizations.
node: Core steps (see walkthrough below)
detail: Measure Core Web Vitals, diagnose bottlenecks, and apply targeted optimizations.
more: Deep guides cover web-vitals.md for LCP, INP, CLS, budgets, and RUM; optimization-strategies.md for bundles, images, caching, and rendering.
node: Outcome
detail: Ship reviewable improvements with budgets and evidence kept outside this blueprint.
more: Record project-specific budgets in docs/development and optimization decisions in docs/adr for traceable governance.
fallback_ascii: |
  Process flow

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: Core knowledge:
```

**Core knowledge:** [`FRONTEND.md`](../FRONTEND.md) — web performance fundamentals, rendering strategies.

**Bridge:** [`FE-SDLC-PDLC-BRIDGE.md`](../FE-SDLC-PDLC-BRIDGE.md) — where performance work fits in the lifecycle.

## Deep guides

| Guide | Focus |
|-------|-------|
| [**Core Web Vitals and metrics**](web-vitals.md) | LCP, INP, CLS, related lab metrics, optimization tables, tooling, budgets, framework notes |
| [**Optimization strategies**](optimization-strategies.md) | Loading, rendering, images, JS, caching layers, CSS/fonts, network, monitoring, anti-patterns |

## Topic map (overview)

| Topic | Focus | See |
|-------|-------|-----|
| **Core Web Vitals** | LCP, INP, CLS — measurement, diagnosis, optimization strategies | [Web Vitals](web-vitals.md) |
| **Bundle optimization** | Code splitting, tree shaking, dynamic imports, dependency audit, compression | [Optimization strategies](optimization-strategies.md) |
| **Image and media** | Format selection (WebP, AVIF), responsive images, lazy loading, CDN transforms | [Optimization strategies](optimization-strategies.md) |
| **Font optimization** | `font-display` strategies, subsetting, preloading, self-hosting vs CDN | [Optimization strategies](optimization-strategies.md) |
| **Caching strategies** | Cache-Control, CDN configuration, service worker caching, stale-while-revalidate | [Optimization strategies](optimization-strategies.md) |
| **Rendering performance** | Main-thread optimization, virtual scrolling, Web Workers, `requestIdleCallback` | [Optimization strategies](optimization-strategies.md) |
| **Performance budgets** | Setting, enforcing, and evolving budgets; Lighthouse CI integration | [Web Vitals](web-vitals.md) |
| **Real User Monitoring (RUM)** | Collecting field data; correlating performance with business metrics | [Web Vitals](web-vitals.md) |

---

*Keep project-specific performance budgets in `docs/development/` and optimization decisions in `docs/adr/`, not in this file.*
