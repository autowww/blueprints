---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Frontend / Web Engineering

Reusable, **project-agnostic** blueprint for **Frontend Engineering** — the discipline of building fast, accessible, maintainable user interfaces for the web platform.

Frontend Engineering answers **"how do we build fast, accessible, maintainable user interfaces for the web?"** — a platform-specific discipline that spans SDLC phases C (Design) through F (Release) and enables PDLC outcomes through user-facing experience quality.

| Document | Purpose |
|----------|---------|
| [**FRONTEND.md**](FRONTEND.md) | Component architecture, rendering strategies, web performance, CSS architecture, design system implementation, state management, build tooling, competencies |
| [**FE-SDLC-PDLC-BRIDGE.md**](FE-SDLC-PDLC-BRIDGE.md) | How Frontend Engineering maps across SDLC phases A–F and PDLC phases P1–P6 — emphasis on Design, Build, and Verify |
| [**patterns/**](patterns/README.md) | Deep guides: component patterns, state management, data fetching, routing, error handling, internationalization |
| [**performance/**](performance/README.md) | Core Web Vitals, bundle optimization, lazy loading, caching strategies, rendering performance |

## Relationship to other packages

| Package | How Frontend Engineering relates |
|---------|----------------------------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | Frontend work executes within SDLC phases C–F. Build tooling, CI/CD, and quality gates apply to frontend artifacts (bundles, assets, Storybook). |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | Frontend quality directly impacts user-facing metrics — Core Web Vitals affect SEO and conversion (P4/P5). Prototype fidelity in P2 depends on frontend capability. |
| [`blueprints/disciplines/product/ux-design/`](../../product/ux-design/README.md) | UX Design defines what to build (wireframes, interaction specs, design tokens); Frontend Engineering implements it. Design systems bridge the two disciplines — shared components, tokens, and Storybook. |
| [`blueprints/disciplines/engineering/software-architecture/`](../software-architecture/README.md) | Architecture decisions (SPA vs MPA, micro-frontends, BFF, API design) directly shape frontend implementation. Frontend is a consumer of API contracts defined at the architecture level. |
| [`blueprints/disciplines/engineering/testing/`](../testing/README.md) | Frontend testing includes unit tests, component tests, integration tests, visual regression, E2E, and accessibility testing — a specific instantiation of the test pyramid. |
| [`blueprints/disciplines/security/`](../../security/README.md) | Frontend is the primary XSS/CSRF attack surface. Content Security Policy, input sanitization, and secure cookie handling are frontend security concerns. |
| [`blueprints/disciplines/engineering/devops/`](../devops/README.md) | Frontend build pipelines, CDN deployment, caching strategies, and performance monitoring integrate with DevOps practices. |

## Scope

This package covers **Frontend / Web Engineering as a discipline** — not just framework tutorials. It includes:

- **Component architecture** — composition patterns, props vs state, controlled vs uncontrolled, compound components, render delegation
- **Rendering strategies** — CSR, SSR, SSG, ISR, React Server Components, streaming, hydration
- **State management** — local vs global state, server state, URL state, state machines, reactive patterns
- **Web performance** — Core Web Vitals (LCP, INP, CLS), bundle analysis, code splitting, lazy loading, image optimization
- **CSS architecture** — BEM, CSS Modules, CSS-in-JS, utility-first (Tailwind), container queries, custom properties
- **Design system implementation** — component libraries, design tokens in code, Storybook, theming, visual regression
- **Build tooling** — bundlers (Vite, webpack, Turbopack), transpilation, tree shaking, module federation
- **Progressive Web Apps** — service workers, offline capability, installability, push notifications
- **Accessibility implementation** — semantic HTML, ARIA, keyboard navigation, focus management, screen reader testing
- **Internationalization** — i18n frameworks, RTL support, locale-aware formatting, translation workflows
- **Browser APIs** — Web Storage, IndexedDB, Web Workers, Intersection Observer, Web Components

Reference bodies of knowledge: web.dev (Google), MDN Web Docs, W3C specifications, WHATWG, Patterns.dev.

---

*Keep project-specific frontend configuration in `docs/development/frontend/` and architecture decisions in `docs/adr/`, not in this file.*
