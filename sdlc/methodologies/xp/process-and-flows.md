---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# XP — major processes & flow maps

## 1. Iteration loop

```blueprint-diagram
key: linear
alt: Iteration loop
title: XP iteration rhythm
summary: How XP teams plan, build, demonstrate, and replan within short bounded iterations.
node: Iteration loop
detail: Frames one XP iteration as a repeatable delivery and learning cycle.
more: Short iterations keep customer feedback close and limit risk from large batch sizes.
node: Start
detail: The team opens the iteration with a bounded story batch from the backlog.
node: Core steps (see walkthrough below)
detail: Pairing, TDD, CI, acceptance, demo, and retrospective execute the planned work.
more: Section 6 maps plan, build, acceptance, customer demo, and retrospective into one inspect-adapt loop.
node: Outcome
detail: Delivered stories and retrospective learnings feed the next planning cycle.
more: Replanning incorporates what the team and customer learned before the next iteration begins.
fallback_ascii: |
  Iteration loop

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 2. TDD micro-loop (within story)

```blueprint-diagram
key: linear
alt: TDD micro-loop (within story)
title: TDD story micro-loop
summary: How red-green-refactor cycles within a story keep design test-guided and CI-backed.
node: TDD micro-loop (within story)
detail: Frames test-driven development as the default rhythm inside story work.
node: Start
detail: A failing test expresses the next behavior the story requires.
node: Core steps (see walkthrough below)
detail: Red, green, and refactor repeat until the story's tests pass.
more: Red adds a failing test; green adds minimal code; refactor improves design while tests stay green.
node: Outcome
detail: Story work completes with passing tests and a design CI can re-verify.
more: CI catches regressions across stories so refactors stay safe between iterations.
fallback_ascii: |
  TDD micro-loop (within story)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 3. Story lifecycle

```blueprint-diagram
key: linear
alt: Story lifecycle
title: XP story acceptance lifecycle
summary: How agreed acceptance tests define done before implementation and customer acceptance closes the story.
node: Story lifecycle
detail: Frames a story from agreed acceptance through customer-visible completion.
node: Start
detail: Customer and team agree acceptance tests that define visible done.
node: Core steps (see walkthrough below)
detail: Implementation with unit tests and green CI satisfies the agreed criteria.
more: Unit tests guard internal behavior; acceptance tests remain the customer-visible definition of done.
node: Outcome
detail: Customer acceptance confirms the story meets the agreed criteria.
more: Accepted stories release incrementally; rejected work returns to implementation with clarified criteria.
fallback_ascii: |
  Story lifecycle

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 4. Planning game (priorities vs estimates)

```blueprint-diagram
key: decision
alt: Planning game (priorities vs estimates)
title: Planning game scope fit
summary: How customer value ordering and team estimates converge on a bounded iteration pull.
node: Planning game (priorities vs estimates)
detail: Separates what the customer values most from what the team can deliver.
node: Current state
detail: The customer orders stories by value while the team supplies estimates.
more: Each story carries a value ranking and a team estimate before iteration scope is chosen.
node: Checkpoint / gate
detail: The team checks whether top-value stories fit the iteration capacity.
more: Stories are pulled in value order until cumulative estimate meets team capacity.
node: refine or escalate
detail: Oversized top-value work triggers split, deferral, or explicit scope negotiation.
more: Teams avoid silent scope creep by negotiating splits or deferrals when capacity cannot fit priority.
node: Continue flow
detail: Agreed stories enter the iteration as a bounded, value-ordered batch.
fallback_ascii: |
  Planning game (priorities vs estimates)

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

## 5. Phases A–F (XP locus)

| Phase | Typical XP locus |
|-------|------------------|
| A Shape | Stories with customer; release themes |
| B Plan | Iteration planning; tasks |
| C Build | Pairing, TDD, CI |
| D Verify | Acceptance tests; collective ownership |
| E Release | Small / frequent releases |
| F Learn | Production feedback; retrospective |

## 6. Flow details (walkthrough)

**Iteration loop** — Short iterations: plan a small story batch, build with pairing/TDD/CI, acceptance, demo with customer, retrospective; replan with what you learned.

**TDD** — Red (failing test) → Green (minimal code) → Refactor (keep tests green); repeat within the story so design stays test-guided and CI catches regressions.

**Story lifecycle** — Acceptance tests agreed before implementation define customer-visible *done*; then implement with unit tests and green CI; customer acceptance closes the story.

**Planning game** — Customer orders by value; team estimates; pull stories until capacity fits. If top value does not fit, split, defer, or negotiate scope explicitly.

## 7. Authoritative sources & further reading

- [Wikipedia — Extreme programming](https://en.wikipedia.org/wiki/Extreme_programming) — Stable overview of practices and history.
- [Agile Alliance — Agile glossary](https://www.agilealliance.org/agile101/agile-glossary/) — Shared vocabulary.
- [Ron Jeffries — XP](https://ronjeffries.com/xprog/) — Practitioner site.
- [Martin Fowler — XP (Bliki)](https://martinfowler.com/bliki/ExtremeProgramming.html) — Short expert summary.
- [Wiki.c2 — Extreme Programming Roadmap](https://wiki.c2.com/?ExtremeProgrammingRoadmap) — Classic wiki index of XP topics.

Full curated list: [`REFERENCE-LINKS.md`](../REFERENCE-LINKS.md).

## 8. Internal links

- [Ceremonies](ceremonies-prescriptive.md) · [Overview](https://forgesdlc.com/methodology-xp.html)
