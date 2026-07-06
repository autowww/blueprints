---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Programming paradigms — index

**Paradigm literacy** helps teams choose structure before frameworks: whether work is naturally **object-shaped**, **function-shaped**, or **stream-shaped**. Paradigms combine in production; the goal is deliberate composition, not purity contests.

**Cross-references:** [`../SOFTWARE-ENGINEERING.md`](../SOFTWARE-ENGINEERING.md) § **1. Programming paradigms** maps strengths; § **4. Principles** (SOLID, composition) supports OO-heavy designs.

---

## Paradigm relationships (mental model)

```blueprint-diagram
key: linear
alt: Paradigm relationships (mental model)
title: Paradigm relationships mental model
summary: How teams choose object-, function-, or stream-shaped structure before frameworks, then compose paradigms deliberately in production.
node: Start
detail: Begin with whether the problem is object-, function-, or stream-shaped.
more: Paradigm literacy precedes framework choice; the index below maps strengths to problem domains.
node: Core steps (see walkthrough below)
detail: Read the OOP, Functional, and Reactive guides linked below.
more: Each guide covers encapsulation, purity, or async composition; arrows suggest teaching lineage, not hard dependencies between paradigms.
node: Outcome
detail: Apply deliberate multi-paradigm layering rather than pursuing purity.
more: Production systems often combine FP cores, OO boundaries, and reactive IO at integration edges.
fallback_ascii: |
  Paradigm relationships (mental model)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: FP cores
```

Teams often layer **FP cores**, **OO boundaries**, and **reactive IO**; arrows suggest common teaching lineage, not hard dependencies.

---

## Which paradigm for which problem domain?

| Problem domain | Favor | Why |
|----------------|-------|-----|
| Rich business rules with invariants | **OOP** (+ DDD tactics) | Identity, lifecycle, collaboration |
| Deterministic transforms / batch analytics | **FP** | Local reasoning; parallel maps |
| Real-time UI, sockets, market data | **Reactive** | Async composition; cancellation |
| Scripts, firmware, tight kernels | **Procedural** | Low ceremony; explicit control flow |
| Long-lived distributed services | **Multi-paradigm** | Split domain core from integration edges |

---

## Guides

| Guide | Focus | See |
|-------|--------|-----|
| [**OOP**](oop.md) | Encapsulation, polymorphism, composition vs inheritance, language notes, anti-patterns | |
| [**Functional**](functional.md) | Purity, ADTs, FP/OOP matrix, practical functors/monads, ecosystems | |
| [**Reactive**](reactive.md) | Observables, operators, backpressure, Manifesto pillars, frameworks | |
| **Procedural** *(planned)* | Procedures, scripts, CLIs, embedded-style sequencing | [SOFTWARE-ENGINEERING.md §1](../SOFTWARE-ENGINEERING.md#1-programming-paradigms) |
| **Multi-paradigm** *(planned)* | Layering styles and team conventions | [SOFTWARE-ENGINEERING.md §1](../SOFTWARE-ENGINEERING.md#1-programming-paradigms) |

---

*Keep project-specific engineering standards in `docs/development/` and architecture decisions in `docs/adr/`, not in this file.*
