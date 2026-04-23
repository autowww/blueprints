---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Frontend / web engineering body of knowledge

This document maps the core concerns of **frontend / web engineering** — component architecture, rendering, performance, state management, design system implementation, and build tooling — to the blueprint ecosystem.

**How frontend engineering relates to PDLC and SDLC:** Frontend is a **platform-specific discipline** that executes within SDLC phases and directly impacts PDLC user-facing outcomes. See [`FE-SDLC-PDLC-BRIDGE.md`](FE-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Patterns:** Component, state, and data-fetching patterns are in [`patterns/`](patterns/README.md).

**Performance:** Core Web Vitals and optimization guidance is in [`performance/`](performance/README.md).

---

## 1. Component architecture

### Composition patterns

| Pattern | Description | When to use |
|---------|-------------|-------------|
| **Container / presentational** | Separate data-fetching logic from rendering | Clear data-fetch boundary; simple UI |
| **Compound components** | Related components share implicit state (e.g. `<Tabs>` + `<Tab>` + `<TabPanel>`) | Complex widgets with coordinated children |
| **Render props / slots** | Parent provides rendering logic to child | Highly customizable shared components |
| **Higher-order components** | Function wrapping a component to inject behavior | Cross-cutting concerns (auth, analytics, error boundary) |
| **Hooks / composables** | Reusable stateful logic extracted into functions | Shared behavior without structural coupling |
| **Server components** | Components rendered on the server, zero client JS | Static or data-fetching-heavy UI; reduce bundle |

### Component API design

| Guideline | Rationale |
|-----------|-----------|
| Props should be minimal and well-typed | Reduces cognitive load; catches misuse at compile time |
| Prefer composition over configuration | `children`/slots scale better than prop explosion |
| Expose ref/forwardRef for imperative needs | Integration with form libraries, focus management |
| Document variants, states, and accessibility | Enables correct usage by other developers |

---

## 2. Rendering strategies

| Strategy | Rendering location | HTML delivery | JS hydration | Best fit |
|----------|-------------------|---------------|--------------|----------|
| **CSR** (Client-Side Rendering) | Browser | Empty shell | Full hydration | Authenticated dashboards, highly interactive apps |
| **SSR** (Server-Side Rendering) | Server per request | Complete HTML | Full hydration | SEO-critical, dynamic content, personalized pages |
| **SSG** (Static Site Generation) | Build time | Pre-built HTML | Optional hydration | Marketing pages, docs, blogs |
| **ISR** (Incremental Static Regeneration) | Build time + on-demand | Cached HTML, revalidated on schedule | Optional hydration | E-commerce catalogs, content with moderate update frequency |
| **Streaming SSR** | Server, streamed | Progressive HTML chunks | Progressive hydration | Large pages; show content before all data resolves |
| **RSC** (React Server Components) | Server | Server-rendered components | Selective hydration | Mixed static/interactive pages; zero-JS for static parts |

### Choosing a strategy

| Factor | CSR | SSR | SSG |
|--------|-----|-----|-----|
| First Contentful Paint | Slow (JS must load) | Fast (HTML from server) | Fastest (pre-built) |
| SEO | Poor without prerendering | Good | Excellent |
| Server cost | Low (static hosting) | Higher (per-request render) | Low (CDN) |
| Data freshness | Real-time | Per-request | Build-time or revalidation |
| Complexity | Lower | Higher (server infra) | Lower (build pipeline) |

---

## 3. State management

| State type | Scope | Management approach | Examples |
|------------|-------|---------------------|----------|
| **Local / component** | Single component | `useState`, `ref`, component state | Form input values, toggle states, ephemeral UI |
| **Shared / global** | Multiple components | Context, Zustand, Redux, Pinia, signals | Theme, user session, feature flags |
| **Server state** | Remote data | TanStack Query, SWR, Apollo, RTK Query | API responses with caching, revalidation, optimistic updates |
| **URL state** | Browser URL | Router params, query strings, `URLSearchParams` | Filters, pagination, search terms, deep links |
| **Form state** | Form lifecycle | React Hook Form, Formik, Zod, Valibot | Validation, dirty tracking, submission state |
| **Machine state** | Complex transitions | XState, Robot | Multi-step flows, async processes with defined states |

### Principles

| Principle | Description |
|-----------|-------------|
| **Colocate state** | Keep state as close to where it is used as possible |
| **Derive don't store** | Compute values from source state rather than syncing duplicates |
| **Single source of truth** | Each piece of data has one canonical location |
| **Immutability** | Treat state as immutable; create new references on updates for predictable rendering |

---

## 4. Web performance

### Core Web Vitals

| Metric | Measures | Good threshold | Optimization levers |
|--------|----------|----------------|---------------------|
| **LCP** (Largest Contentful Paint) | Loading performance | < 2.5 s | Optimize critical path, preload hero image, SSR/SSG, CDN |
| **INP** (Interaction to Next Paint) | Responsiveness | < 200 ms | Reduce main-thread work, debounce, `requestIdleCallback`, web workers |
| **CLS** (Cumulative Layout Shift) | Visual stability | < 0.1 | Explicit dimensions on images/embeds, font-display swap, avoid dynamic injection above fold |

### Bundle optimization

| Technique | Impact |
|-----------|--------|
| **Code splitting** | Load only the code needed for the current route/view |
| **Tree shaking** | Eliminate dead code; requires ES modules |
| **Dynamic imports** | Lazy-load below-fold components, modals, heavy libraries |
| **Compression** | Brotli (preferred) or gzip for text assets |
| **Image optimization** | Modern formats (WebP, AVIF), responsive `srcset`, lazy loading, CDN transforms |
| **Font optimization** | `font-display: swap`, subsetting, self-hosting, preloading critical fonts |
| **Dependency audit** | Replace heavy libraries with lighter alternatives; monitor bundle with `bundleanalyzer` |

---

## 5. CSS architecture

| Approach | Description | Trade-off |
|----------|-------------|-----------|
| **BEM** (Block Element Modifier) | Naming convention for class-based CSS | Predictable; verbose; no scope enforcement |
| **CSS Modules** | File-scoped CSS with auto-generated class names | Scoping by default; requires build tooling |
| **CSS-in-JS** (styled-components, Emotion) | CSS authored in JavaScript; runtime or compile-time | Colocated styles; runtime cost (unless compiled); JS-only |
| **Utility-first** (Tailwind) | Composable utility classes; design system as config | Fast iteration; large HTML; learning curve; compile-time purge |
| **Vanilla CSS** (with custom properties and layers) | Modern CSS features — nesting, `@layer`, container queries, custom properties | Zero dependencies; browser-native; requires modern browser support |

### Design tokens in CSS

| Layer | Implementation |
|-------|----------------|
| **Tokens** | CSS custom properties (`:root { --color-primary: …; }`) or JSON tokens exported from design tool |
| **Semantic aliases** | `--color-action-primary`, `--space-md` — meaning-based names referencing raw tokens |
| **Component styles** | Reference semantic tokens; never use raw values directly |
| **Theming** | Override custom properties at a parent selector or media query level (dark mode, brand variants) |

---

## 6. Design system implementation

| Concern | Practice |
|---------|----------|
| **Component library** | Build atomic → molecule → organism hierarchy; publish as versioned package |
| **Storybook / docs** | Interactive documentation with controls, accessibility addon, visual regression |
| **Design tokens pipeline** | Figma → Tokens Studio → Style Dictionary → CSS/JS/iOS/Android tokens |
| **Visual regression testing** | Chromatic, Percy, or Playwright screenshot comparison against baselines |
| **Versioning** | Semantic versioning; changelog; migration guides for breaking changes |
| **Contribution model** | Federated — product teams propose; system team reviews and publishes |

---

## 7. Build tooling

| Tool category | Purpose | Examples |
|---------------|---------|----------|
| **Bundler** | Module resolution, code splitting, optimization | Vite, webpack, Turbopack, Rollup, esbuild |
| **Transpiler** | Modern JS/TS to target browsers | TypeScript compiler, SWC, Babel |
| **Linter / formatter** | Code quality and consistency | ESLint, Biome, Prettier, Stylelint |
| **Test runner** | Unit, component, integration testing | Vitest, Jest, Playwright, Cypress |
| **Monorepo tooling** | Multi-package orchestration | Turborepo, Nx, pnpm workspaces |

---

## 8. Progressive Web Apps

| Capability | Technology | When to use |
|------------|-----------|-------------|
| **Offline support** | Service worker + Cache API | Content-heavy apps, productivity tools, field conditions |
| **Installability** | Web App Manifest | Consumer-facing apps wanting app-like experience |
| **Push notifications** | Push API + service worker | Re-engagement for news, messaging, alerts |
| **Background sync** | Background Sync API | Queuing actions while offline (forms, messages) |
| **File handling** | File Handling API | Productivity tools that open files from OS |

---

## 9. Competencies

| Competency | Description |
|------------|-------------|
| **HTML / CSS mastery** | Semantic markup, layout systems (flexbox, grid), responsive design, accessibility |
| **JavaScript / TypeScript depth** | Async patterns, event loop, module systems, type safety, performance profiling |
| **Framework expertise** | Deep knowledge of at least one major framework (React, Vue, Angular, Svelte) and its ecosystem |
| **Performance engineering** | Profiling, Core Web Vitals optimization, bundle analysis, runtime performance |
| **Accessibility** | WCAG implementation, ARIA patterns, keyboard navigation, assistive technology testing |
| **Testing** | Component testing, E2E testing, visual regression, accessibility testing |
| **Build systems** | Bundler configuration, CI/CD for frontend, artifact management, CDN deployment |
| **Design system thinking** | Building and consuming reusable components; design-dev collaboration |

---

## 10. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| web.dev | https://web.dev/ | Google's web platform best practices and performance guidance |
| MDN Web Docs | https://developer.mozilla.org/ | Authoritative web API and HTML/CSS/JS documentation |
| Patterns.dev | https://www.patterns.dev/ | Modern web app design and rendering patterns |
| Can I Use | https://caniuse.com/ | Browser compatibility data for web features |
| WHATWG HTML Living Standard | https://html.spec.whatwg.org/ | The HTML specification |
| Web Almanac | https://almanac.httparchive.org/ | Annual state-of-the-web report with data-driven insights |
| Component Gallery | https://component.gallery/ | Design system component patterns and naming conventions |

---

*Keep project-specific frontend configuration in `docs/development/frontend/`, component documentation in Storybook, and architecture decisions in `docs/adr/`, not in this file.*
