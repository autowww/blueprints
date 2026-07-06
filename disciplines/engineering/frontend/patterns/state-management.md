---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# State management patterns

**Purpose:** Project-agnostic map of **where state lives**, how to choose local vs shared vs server state, and how common libraries and patterns fit together.

**Audience:** Teams aligning with [`FRONTEND.md`](../FRONTEND.md) and [`patterns/README.md`](README.md).

---

## Overview

State management is often the hardest problem in UI development because it couples **correctness** (single source of truth), **performance** (who rerenders when), and **ergonomics** (how easy it is to change behavior). The goal is not one global store—it is **the smallest correct scope** for each piece of data, with clear update paths.

---

## State categories

| Category | Ownership | Lifecycle | Typical home |
|----------|-----------|-----------|--------------|
| **Local / component** | Component instance | Mount → unmount | `useState`, refs, Svelte `$state` |
| **Shared / application** | App or feature module | Session / app lifetime | Context, Pinia, Zustand, Redux |
| **Server / remote** | Backend + client cache | TTL, invalidation, background refresh | TanStack Query, SWR, Apollo |
| **URL / navigation** | Browser + router | Survives refresh; shareable | Route params, query strings |
| **Form** | Form subtree | Until submit or reset | Controlled fields, form libraries |
| **Derived / computed** | Derived from source state | Recomputed on dependency change | Selectors, `useMemo`, computed refs |

**Ownership rule of thumb:** if only one subtree needs it, keep it there; if the server is the authority, treat the client as a cache with a defined invalidation story.

```blueprint-diagram
key: decision
alt: State categories
title: State scope checkpoint
summary: Decide whether each piece of state belongs in the smallest correct ownership category before continuing design.
node: State categories
detail: Map the data to local, shared, server, URL, form, or derived buckets.
more: The category table above defines ownership, lifecycle, and typical home for each kind.
node: Current state
detail: Inventory where the value lives today and who reads or writes it.
more: Trace subscriptions, cache keys, and prop drilling to spot overlap or hidden globals.
node: Checkpoint / gate
detail: Ask whether this scope is the smallest that stays correct.
more: Apply the ownership rule: one subtree only, server authority, or shareable navigation state.
node: refine or escalate
detail: Narrow scope, lift to shared store, or move authority to the server.
more: Revisit the category table and anti-patterns when local, global, and server copies disagree.
node: Continue flow
detail: Proceed with a traceable update path and clear invalidation rules.
more: Document who rerenders when this state changes and how updates propagate through the tree.
fallback_ascii: |
  State categories

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

---

## Flux / Redux-style cycle

Unidirectional data flow: actions describe *what happened*; the store holds *state*; views read and dispatch.

```blueprint-diagram
key: linear
alt: Flux / Redux-style cycle
title: Flux unidirectional cycle
summary: Actions describe events; reducers update store state; views render and dispatch the next action.
node: Flux / Redux-style cycle
detail: Frame every update as a one-way loop from view through store back to view.
node: Start
detail: User interaction or an async result becomes a typed action.
node: Core steps (see walkthrough below)
detail: Reducer applies the action; the store holds the single source of truth.
more: Selectors derive view data; middleware can handle side effects without mutating state in place.
node: Outcome
detail: Subscribed views rerender from the updated store slice.
more: Predictable updates support time-travel debugging and team-wide conventions when slice patterns are standardized.
fallback_ascii: |
  Flux / Redux-style cycle

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: When this shines:
```

**When this shines:** predictable updates, time-travel debugging, large teams needing conventions. **Cost:** ceremony unless you standardize selectors and slice patterns.

---

## Library comparison matrix

| Library | Paradigm | Boilerplate | Devtools | Learning curve | Bundle (rough) |
|---------|----------|-------------|----------|----------------|----------------|
| **Redux** | Explicit actions + reducers | High | Excellent | Medium | Small core + ecosystem |
| **MobX** | Observable / reactive | Low | Good | Medium | Moderate |
| **Zustand** | Minimal store + selectors | Very low | Add-on | Low | Small |
| **Recoil** | Atoms + selectors (React) | Medium | Good | Medium | Moderate |
| **Jotai** | Atomic bottom-up (React) | Low | Add-on | Low–medium | Small |
| **Pinia** | Stores (Vue) | Low | Good (Vue) | Low | Small |
| **NgRx** | Redux-like (Angular) | High | Excellent | Steeper | Larger |
| **Svelte stores** | Writable/readable/derived | Low | Browser | Low | Tiny (framework) |

*Bundle sizes vary by version and tree-shaking—treat as relative guidance.*

---

## Server state management

| Concern | Practice |
|---------|----------|
| **Cache invalidation** | Invalidate by key, tag, or mutation success; prefer stale-while-revalidate for reads. |
| **Optimistic updates** | Update UI immediately; roll back on error; reconcile with server truth. |
| **Background refetch** | Refetch on focus, reconnect, or interval for data that goes stale. |
| **Deduplication** | Same key in flight should share one request. |

| Library | Strength |
|---------|----------|
| **TanStack Query** | Normalized patterns, mutations, devtools |
| **SWR** | Simple API, Vercel ecosystem |
| **Apollo Client** | GraphQL cache, normalized entities |

```blueprint-diagram
key: sequence
alt: Server state management
title: Server state request flow
summary: A trigger fetches or mutates remote authority, then hands a reconciled cache outcome to the UI.
node: Server state management
detail: Treat the backend as source of truth with a governed client cache layer.
node: Actor / trigger
detail: Mount, focus, mutation, or invalidation tag starts the cycle.
more: The same cache key in flight deduplicates to one shared request.
node: System step
detail: Query library fetches, caches, and applies stale-while-revalidate policy.
more: Supports optimistic updates with rollback on error and background refetch on reconnect or interval.
node: Outcome / handoff
detail: UI reads cached data while reconciliation tracks server truth.
more: Invalidate by key, tag, or mutation success; avoid duplicating server truth in a second ad hoc store.
fallback_ascii: |
  Server state management

  Actor / trigger
      |
      v
  System step
      |
      v
  Outcome / handoff
```

---

## State machines and statecharts

Finite states reduce impossible UI combinations (e.g. loading + error + success at once). **XState** and similar libraries model **states**, **events**, and **guards** explicitly—ideal for wizards, checkout, and async workflows with retries.

```blueprint-diagram
key: state
alt: State machines and statecharts
title: Explicit state machine flow
summary: Model phases as finite states and events so impossible UI combinations cannot render together.
node: State machines and statecharts
detail: Replace implicit boolean flags with states, events, and guarded transitions.
node: Start
detail: Enter the initial state defined for the workflow.
more: Suited to wizards, checkout, and upload flows with mutually exclusive phases.
node: Core steps (see walkthrough below)
detail: Events trigger guarded transitions between named states.
more: Libraries like XState encode retries, backoff, and parallel regions for autosave or collaboration.
node: Outcome
detail: Terminal state reflects success, failure, or a reviewable handoff.
more: Prevents loading, error, and success flags from all being true at once.
fallback_ascii: |
  State machines and statecharts

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

| Signal to use a machine | Example |
|-------------------------|---------|
| Mutually exclusive phases | Upload: selecting → uploading → done |
| Retries and backoff | Payment submission |
| Parallel regions | Editor with autosave + collaboration |

---

## Form state

| Style | Description | Trade-off |
|-------|-------------|-----------|
| **Controlled** | Value from state; every keystroke updates | Predictable; more rerenders if not batched |
| **Uncontrolled** | DOM holds value; read on submit | Less React/Vue churn; harder cross-field rules |

| Library | Ecosystem | Notes |
|---------|-----------|-------|
| **React Hook Form** | React | Uncontrolled-friendly; low rerenders |
| **Formik** | React | Controlled; familiar API |
| **VeeValidate** | Vue | Schema + composition integration |
| **Angular Reactive Forms** | Angular | Strong typing with typed forms |

---

## URL as state

| Pattern | Use when |
|---------|----------|
| **Route params** | Identity of resource (`/users/:id`) |
| **Query params** | Filters, sort, pagination, shareable views |
| **Deep linking** | Restore full UI from URL; document which keys are stable |

**Caveat:** sensitive data does not belong in query strings; prefer server session or secure storage patterns per product requirements.

---

## Anti-patterns

| Anti-pattern | Problem | Prefer |
|--------------|---------|--------|
| **Global state for everything** | Coupling; hard testing; unnecessary subscriptions | Colocate; server cache for remote data |
| **Global store to avoid drilling** | Hides data flow; same as above | Lift, composition, or narrow context |
| **Stale closures** | Handlers see old state in async/effects | Correct dependency arrays; functional updates |
| **Unnecessary rerenders** | Wide subscriptions, unstable object identities | Selectors, memoization, split stores |
| **Duplicated server truth** | Two caches disagree | Single query layer; derive view state |

---

## External references

- [TkDodo — Practical React Query](https://tkdodo.eu/blog/practical-react-query) — server state, caching, and mental model.
- [XState documentation](https://stately.ai/docs) — state machines and statecharts.
- [Redux Style Guide](https://redux.js.org/style-guide/) — patterns and priorities for Redux-style apps.

---

*Keep project-specific performance budgets in `docs/development/` and optimization decisions in `docs/adr/`, not in this file.*
