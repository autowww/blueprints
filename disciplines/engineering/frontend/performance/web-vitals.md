# Core Web Vitals and performance metrics

**Purpose:** Project-agnostic reference for **Core Web Vitals** (CWV), related lab metrics, optimization levers, measurement tooling, and framework hooks—framed as product quality, not optional tuning.

**Audience:** Teams aligning with [`FRONTEND.md`](../FRONTEND.md) and [`performance/README.md`](README.md).

---

## Overview

**Performance is a feature:** slow or janky interfaces lose trust, conversions, and accessibility. Google's Core Web Vitals distill field-measurable signals that correlate with user experience; they are a common baseline for goals, budgets, and regression checks—not the only metrics that matter.

---

## Core Web Vitals

| Metric | What it measures | Good | Needs improvement | Poor | User impact |
|--------|------------------|------|-------------------|------|-------------|
| **LCP** (Largest Contentful Paint) | When the largest visible content element paints | ≤ 2.5s | 2.5s – 4.0s | > 4.0s | Perceived load completion; frustration if delayed |
| **INP** (Interaction to Next Paint) | Latency until next visual update after interaction | ≤ 200ms | 200ms – 500ms | > 500ms | Responsiveness; feels “stuck” when high |
| **CLS** (Cumulative Layout Shift) | Visual stability (unexpected layout movement) | ≤ 0.1 | 0.1 – 0.25 | > 0.25 | Mis-clicks; disorientation; readability |

*Thresholds align with [web.dev/vitals](https://web.dev/articles/vitals) guidance; they evolve—verify current docs.*

**INP and FID:** INP superseded First Input Delay (FID) as a Core Web Vital—INP captures worst-case interaction latency across the page lifetime, not only the first input.

```blueprint-diagram
key: timeline
alt: Diagram
```

---

## Additional performance metrics

| Metric | Definition | Relationship to CWV |
|--------|------------|---------------------|
| **FCP** | First Contentful Paint | Earlier milestone; not a CWV but correlates with perceived speed |
| **TTFB** | Time to First Byte | Server/network; upper bound on LCP if HTML is slow |
| **TBT** | Total Blocking Time (lab) | Main-thread busy time; relates to INP risk |
| **Speed Index** | Visual completeness over time (lab) | Holistic perceived load; complements LCP |
| **TTI** | Time to Interactive (legacy lab) | Less emphasized vs INP; still useful for heavy JS apps |

---

## Field data vs lab data

| Source | What you get | Best for |
|--------|--------------|----------|
| **Field (RUM, CrUX)** | Real devices, networks, caches | Truth about users; percentile distributions |
| **Lab (Lighthouse, WPT)** | Repeatable environment | Regressions, before/after comparisons |

Always triage disagreements: a fast lab run can hide slow field INP if interactions differ from the scripted audit.

---

## LCP optimization strategies

| Lever | Tactics |
|-------|---------|
| **Images** | Modern formats (WebP/AVIF), responsive sizing, `fetchpriority` for hero, avoid oversized decode |
| **Lazy loading** | Defer below-fold images; do not lazy-load LCP candidate |
| **Preload** | `rel=preload` for critical LCP image/font when safe |
| **Fonts** | `font-display: swap` or `optional`; subset; preload only critical faces |
| **Critical CSS** | Inline or prioritize above-the-fold CSS; reduce render-blocking |
| **SSR / SSG** | Deliver meaningful HTML early so LCP can paint without waiting for all JS |
| **CDN** | Edge caching and HTTP/2/3 for faster first byte and assets |

---

## INP optimization strategies

| Lever | Tactics |
|-------|---------|
| **Long tasks** | Split work; yield (`scheduler.postTask`, chunking) |
| **Main thread** | Reduce JS parse/execute; defer non-critical work |
| **Web Workers** | Offload heavy compute from interaction path |
| **Events** | Debounce/throttle where appropriate; avoid synchronous layout thrash |
| **Lists** | Virtualize large lists; avoid huge DOM updates per keystroke |

---

## CLS optimization strategies

| Lever | Tactics |
|-------|---------|
| **Dimensions** | `width`/`height` or aspect-ratio on images and embeds |
| **Fonts** | Reserve space; `size-adjust` / metric overrides where supported |
| **Placeholders** | Skeletons matching final layout |
| **Animation** | Prefer `transform`/`opacity`; avoid animating layout properties |

---

## Measurement tools

| Tool | Type | Strengths |
|------|------|------------|
| **Lighthouse** | Lab (CI/local) | Actionable audits; scores |
| **PageSpeed Insights** | Lab + field (CrUX) | URL-level field data when available |
| **Chrome DevTools Performance** | Lab | Main thread, long tasks, rendering |
| **WebPageTest** | Lab | Filmstrip, connection profiles, repeat view |
| **CrUX** | Field | Real-user aggregates; origin/URL |
| **RUM** | Field | Custom attribution, segments, business correlation |
| **Synthetic** | Lab | Scripted, repeatable baselines |

---

## Performance budgets

| Aspect | Guidance |
|--------|----------|
| **Set** | Align budgets with CWV thresholds and business constraints (JS weight, LCP proxy). |
| **Measure** | Track lab (Lighthouse CI) and field (RUM) where possible. |
| **CI** | Fail or warn on regressions; tie to main branch and releases. |

```blueprint-diagram
key: linear
alt: Diagram
```

---

## Framework-specific performance

| Stack | Levers |
|-------|--------|
| **React** | `React.memo`, `useMemo`/`useCallback` where profiling justifies, `lazy` + `Suspense` |
| **Vue** | Async components, `defineAsyncComponent`, `keep-alive` for tab-like UIs |
| **Next.js / Nuxt** | SSR/SSG/ISR, image components, route-level splitting, streaming |

---

## External references

- [web.dev — Web Vitals](https://web.dev/articles/vitals) — definitions and thresholds.
- [Chrome DevTools — Performance](https://developer.chrome.com/docs/devtools/performance) — profiling workflows.
- *Web Performance in Action* — Jeremy Wagner; practical measurement and optimization (book).

---

*Keep project-specific performance budgets in `docs/development/` and optimization decisions in `docs/adr/`, not in this file.*
