# Frontend Engineering ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **Frontend / Web Engineering** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **Frontend** — "Is the web experience **fast, accessible, and maintainable**?"

Frontend engineering translates design intent into interactive web experiences, directly impacting user-facing quality metrics that drive PDLC outcomes.

**Canonical sources:** [`FRONTEND.md`](FRONTEND.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md).

---

## Comparison table

| Dimension | Frontend Engineering | SDLC | PDLC |
|-----------|---------------------|------|------|
| **Core question** | Is the web experience fast, accessible, and maintainable? | How do we build this correctly? | Should we build this; does it create the right outcomes? |
| **Scope** | Component architecture, rendering, state management, CSS, performance, design system implementation, build tooling, a11y, i18n | Requirements → design → implementation → verification → release (**A**–**F**) | Problem discovery → strategy → launch → growth → sunset (**P1**–**P6**) |
| **Primary owner** | Frontend / UI engineers | Delivery team | Product manager / product trio |
| **Success metric** | Core Web Vitals, Lighthouse score, a11y conformance, component coverage, bundle size | Velocity, defect escape rate, CI/CD pass rate | Adoption, retention, revenue, NPS |
| **Key artifacts** | Component library, Storybook, design tokens (code), bundle analysis, performance budgets | Specs, code, tests, release notes | Research, strategy, metrics |
| **Risk focus** | Performance, accessibility, cross-browser compat, state complexity, bundle bloat | Technical correctness | Market and outcome risk |

---

## Frontend across the lifecycle

| Phase | Frontend role | Key activities | Outputs |
|-------|--------------|----------------|---------|
| **P1–P2** | **Prototype builder** | Build interactive prototypes for concept testing (code prototypes when Figma fidelity is insufficient) | Clickable prototypes, feasibility notes |
| **P3** | **Technical advisor** | Advise on rendering strategy (CSR/SSR/SSG), performance budgets, a11y conformance target, i18n scope | Tech recommendations, performance budget |
| **A Discover** | **Frontend architect** | Evaluate framework, rendering approach, design system strategy; spike on unknowns | Framework ADR, rendering strategy doc |
| **B Specify** | **Component specifier** | Map wireframes to component tree; define component APIs; identify design system gaps | Component breakdown, props contracts, new token requests |
| **C Design** | **Component builder** | Implement design system components; set up Storybook; integrate design tokens; build page layouts | Component library, Storybook stories, CSS architecture |
| **D Build** | **Feature implementer** | Build features using component library; integrate with APIs; implement state management, routing, i18n | Feature code, integration tests, a11y annotations |
| **E Verify** | **Quality engineer** | Performance testing (Lighthouse CI), visual regression, a11y audit (axe), cross-browser testing, E2E | Lighthouse reports, visual regression results, a11y audit, E2E results |
| **F Release** | **Release engineer** | Build optimization, CDN deployment, cache invalidation, feature flag wiring | Production bundle, deployment verification |
| **P4 Launch** | **Performance monitor** | Real User Monitoring setup, Core Web Vitals tracking, error monitoring | RUM dashboards, performance baselines |
| **P5 Grow** | **Performance optimizer** | A/B test frontend variants, optimize critical paths, reduce bundle, improve LCP/INP | Performance improvements, experiment results |
| **P6 Sunset** | **Migration engineer** | Redirect routes, archive components, remove feature flags | Redirect configuration, archived Storybook |

---

## Artifact flow

### Inputs to Frontend

| Source | Frontend usage |
|--------|---------------|
| Wireframes and interaction specs (UX, **B**) | Component tree, interaction behavior, responsive breakpoints |
| Design tokens (UX Design, **C**) | CSS custom properties, theme configuration |
| API contracts (Architecture, **B/C**) | Data fetching types, error handling, loading states |
| Performance budgets (**P3**, Architecture) | Bundle size limits, LCP/INP targets |
| Accessibility requirements (UX, **B**) | WCAG conformance level, ARIA patterns, keyboard nav requirements |

### Frontend outputs

| Frontend artifact | Consumer |
|-------------------|----------|
| Component library + Storybook (**C/D**) | Other frontend engineers, designers, QA |
| Production bundle (**F**) | CDN, deployment pipeline |
| Lighthouse CI results (**E**) | Quality gates, performance dashboards |
| Visual regression baselines (**E**) | CI/CD pipeline, design review |
| RUM data (**P4/P5**) | Product analytics, performance optimization |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Bundle bloat** | Importing entire libraries for single functions; no code splitting; growing bundle unchecked | Bundle analysis in CI; performance budgets; dynamic imports; dependency audit |
| **CSS at war** | Conflicting specificity, `!important` everywhere, inconsistent naming | Choose one CSS strategy and enforce it; design tokens as single source of truth |
| **Component soup** | Hundreds of one-off components with no shared patterns | Design system with clear component API guidelines; composition over duplication |
| **Test pyramid inversion** | All E2E, no unit/component tests; slow CI, flaky results | Component tests for logic, visual regression for appearance, E2E for critical paths only |
| **Accessibility afterthought** | Semantic HTML ignored; ARIA applied incorrectly as a fix | Accessibility in Definition of Done; automated checks (axe) in CI; manual audit per release |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`FRONTEND.md`](FRONTEND.md) | Component architecture, rendering, performance, CSS, state management, build tooling |
| [`patterns/README.md`](patterns/README.md) | Component, state management, and data-fetching patterns |
| [`performance/README.md`](performance/README.md) | Core Web Vitals, bundle optimization, caching |
| [`UX-DESIGN.md`](../../product/ux-design/UX-DESIGN.md) | Design systems, visual design, interaction design — what frontend implements |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6 |
| [`ARCH-SDLC-PDLC-BRIDGE.md`](../software-architecture/ARCH-SDLC-PDLC-BRIDGE.md) | Architecture decisions that shape frontend (SPA vs MPA, BFF, micro-frontends) |
