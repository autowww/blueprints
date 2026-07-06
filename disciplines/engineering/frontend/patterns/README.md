---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Frontend patterns (blueprint)

**Purpose:** Deep, **project-agnostic** guides for frontend component, state management, and data-fetching patterns. Each pattern describes its intent, implementation, trade-offs, and testing strategy.

**Audience:** Teams adopting [`blueprints/disciplines/engineering/frontend/`](../README.md); project-specific component documentation stays in **Storybook** and **`docs/development/frontend/`**.

UI pattern thinking means naming recurring structures—composition, state ownership, data flow—so teams can reuse solutions deliberately instead of reinventing ad hoc trees and stores. Start from the **component boundary**, then decide **where state lives**, then **how data crosses the network**; routing and forms sit on top of those choices.

```blueprint-diagram
key: linear
alt: Process flow
title: Frontend patterns adoption path
summary: How teams move from shared frontend vocabulary through deep pattern guides to deliberate, reviewable component and state choices.
node: Process flow
detail: Conceptual map for navigating this patterns index.
more: Orients readers before they commit to a specific pattern guide or project-specific component documentation.
node: Start
detail: Align on component boundaries, state ownership, and data flow from FRONTEND.md.
more: Name recurring structures—composition, state ownership, data flow—so teams reuse solutions deliberately instead of reinventing ad hoc trees and stores.
node: Core steps (see walkthrough below)
detail: Open the deep guides for component architecture and state management.
more: The tables below map pattern categories—components, state, fetching, routing, forms, errors, i18n—to the right linked guide.
node: Outcome
detail: Deliberate pattern choices with project specifics left to Storybook and docs/development/.
more: Teams adopt patterns with traceable rationale; performance budgets and ADRs stay in project repositories per this page's footer.
node: Note: Core knowledge:
detail: FRONTEND.md supplies foundational component, rendering, state, and CSS vocabulary.
more: Read FRONTEND.md before deep dives; FE-SDLC-PDLC-BRIDGE.md shows how patterns apply across the lifecycle.
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

**Core knowledge:** [`FRONTEND.md`](../FRONTEND.md) — component architecture, rendering, state management, CSS.

**Bridge:** [`FE-SDLC-PDLC-BRIDGE.md`](../FE-SDLC-PDLC-BRIDGE.md) — how frontend patterns apply across the lifecycle.

## Deep guides

| Guide | Focus |
|-------|-------|
| [**Component architecture**](component-architecture.md) | Taxonomy, composition APIs, state ownership, design systems, testing, framework comparison |
| [**State management**](state-management.md) | Categories, decision tree, Flux/Redux, library matrix, server cache, machines, forms, URL state |

## Pattern categories (overview)

| Pattern category | Focus | See |
|-----------------|-------|-----|
| **Component patterns** | Compound components, render delegation, controlled vs uncontrolled, polymorphic components, error boundaries | [Component architecture](component-architecture.md) |
| **State management patterns** | State colocation, derived state, optimistic updates, state machines for complex flows | [State management](state-management.md) |
| **Data fetching patterns** | Cache-and-network, stale-while-revalidate, infinite scroll, polling, real-time subscriptions | [State management](state-management.md) |
| **Routing patterns** | File-based routing, nested layouts, route-level code splitting, prefetching, auth guards | [Component architecture](component-architecture.md) |
| **Form patterns** | Multi-step forms, field-level validation, server-side validation integration, autosave | [State management](state-management.md) |
| **Error handling patterns** | Error boundaries, toast notifications, retry UI, graceful degradation, offline fallbacks | [Component architecture](component-architecture.md) |
| **Internationalization patterns** | ICU message format, locale-aware formatting, RTL layout, translation workflow integration | [FRONTEND.md](../FRONTEND.md) |

---

*Keep project-specific performance budgets in `docs/development/` and optimization decisions in `docs/adr/`, not in this file.*
