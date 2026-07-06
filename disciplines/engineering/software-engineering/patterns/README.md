---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Design patterns — index

**Pattern thinking** means naming recurring **forces** (change, scale, integration) and matching proven structures — without using the catalog as a mandatory checklist. Prefer simple modules until **duplication proves the force**.

**Cross-reference:** Parent summaries for GoF and enterprise patterns: [`../SOFTWARE-ENGINEERING.md`](../SOFTWARE-ENGINEERING.md) § **3. Design patterns**.

---

## Pattern categories (overview)

```blueprint-diagram
key: swimlane
alt: Pattern categories (overview)
title: Pattern category lanes
summary: Two parallel tracks for matching named forces to proven structures without treating the catalog as mandatory.
node: Pattern categories (overview)
detail: Frames how pattern families coordinate on this index page.
more: Pattern thinking names recurring forces first; guides below route creational, structural, behavioral, and integration concerns.
node: Lane A
detail: The forward path from force identification toward a shared design outcome.
node: handoff
detail: Passes a resolved pattern concern to the next selection step.
more: Each handoff should cite the force—change, scale, or integration—that triggered escalation from simpler modules.
node: shared outcome
detail: The bounded structure both lanes converge on after pattern selection.
node: Lane B
detail: The inspect-and-adapt path for revising pattern choice as forces clarify.
node: inspect / adapt
detail: Reviews applied patterns against duplication and integration pressures.
more: Escalate per the selection table when adapters absorb domain rules or sagas dominate cross-service work.
node: feedback
detail: Returns selection lessons to refine the next pattern pass.
node: Note: single-process
detail: Scopes in-process collaboration patterns to one runtime boundary.
more: GoF patterns address single-process collaboration; enterprise integration patterns apply when messaging crosses service boundaries.
fallback_ascii: |
  Pattern categories (overview)

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback

  Note: single-process
```

GoF addresses **single-process** collaboration; EIP addresses **cross-service** messaging and evolution.

---

## Selection guidance

| Situation | Start here | Escalate when |
|-----------|------------|----------------|
| Variable object creation | [GoF creational](gof-patterns.md#creational-patterns) | Many product families need registries |
| Compose or wrap types | [GoF structural](gof-patterns.md#structural-patterns) | Adapters absorb domain rules |
| Vary algorithms or notifications | [GoF behavioral](gof-patterns.md#behavioral-patterns) | Cross-service sagas dominate |
| Decouple services / absorb bursts | [Enterprise integration](enterprise-integration.md) | Ordering, idempotency, schema contracts |
| Shared-memory parallelism | **Concurrency patterns** *(planned)* | Locks/races drive the design |

---

## Guides

| Guide | Focus | See |
|-------|--------|-----|
| [**GoF design patterns**](gof-patterns.md) | 23 patterns, selection flowchart, modern relevance | |
| [**Enterprise integration**](enterprise-integration.md) | Channels, routing, transformation, sagas, platforms | |
| **Concurrency patterns** *(planned)* | Active object, monitor, fork-join, pipeline | [SOFTWARE-ENGINEERING.md §3](../SOFTWARE-ENGINEERING.md#3-design-patterns) |

---

*Keep project-specific engineering standards in `docs/development/` and architecture decisions in `docs/adr/`, not in this file.*
