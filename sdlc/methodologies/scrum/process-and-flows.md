---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Scrum — major processes & flow maps

Diagrams below use **` ```blueprint-diagram `** fences on the published handbook; GitHub shows the source as a fenced block. For print/PDF, use the site or export static SVG.

## 1. Sprint lifecycle (high level)

```blueprint-diagram
key: swimlane
alt: Sprint lifecycle (high level)
title: Scrum sprint lifecycle
summary: How refinement, sprint events, and empirical feedback loop through one bounded iteration.
node: Sprint lifecycle (high level)
detail: Frames one sprint as parallel delivery and inspect-adapt lanes.
node: handoff
detail: Teams pass refined backlog intent into sprint commitment and execution.
more: Refinement keeps the Product Backlog transparent enough for Sprint Planning to commit with confidence.
node: shared outcome
detail: The sprint produces a working increment toward the agreed Sprint Goal.
more: Planning, daily execution, and review align on one shared outcome the team can demonstrate.
node: inspect / adapt
detail: Scrum events surface progress, quality, and process gaps for adjustment.
more: Daily Scrum, Review, and Retrospective embody transparency, inspection, and adaptation each sprint.
node: feedback
detail: Review and retrospective outputs feed the next refinement and planning cycle.
more: Stakeholder and team learnings return to backlog ordering and how the team works.
fallback_ascii: |
  Sprint lifecycle (high level)

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
```

## 2. Planning flow (Part 1 → Part 2)

```blueprint-diagram
key: decision
alt: Planning flow (Part 1 → Part 2)
title: Sprint Planning two parts
summary: How Part 1 sets the Sprint Goal and Part 2 turns selection into a bounded execution plan.
node: Planning flow (Part 1
detail: Clarifies why this sprint matters and what value it will deliver.
more: Ordered backlog items are reviewed; unclear value or ordering returns to refinement or a timeboxed spike.
node: Part 2)
detail: Breaks selected work into a plan the Developers can execute.
more: Teams often capture tasks on a Sprint Backlog; the sprint starts when execution approach is agreed.
fallback_ascii: |
  Planning flow (Part 1
      |
      v
  Part 2)
```

## 3. Daily execution loop

```blueprint-diagram
key: decision
alt: Daily execution loop
title: Daily Scrum inspect loop
summary: How Developers inspect progress toward the Sprint Goal each day and adapt before continuing.
node: Daily execution loop
detail: A bounded daily rhythm keeps sprint execution transparent and aligned.
node: Current state
detail: The team reviews work toward the Sprint Goal as it stands now.
more: Board and backlog should reflect actual progress by end of day.
node: Checkpoint / gate
detail: The Daily Scrum inspects whether the team remains on track.
more: This 15-minute event is for Developers; detailed problem-solving happens outside the timebox.
node: refine or escalate
detail: Off-track work triggers replanning, scope negotiation, or impediment escalation.
more: Impediments are cleared through the day rather than hidden until review.
node: Continue flow
detail: On-track teams proceed with the agreed sprint plan for the day.
fallback_ascii: |
  Daily execution loop

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

## 4. Definition of Done gate (increment)

```blueprint-diagram
key: decision
alt: Definition of Done gate (increment)
title: Definition of Done gate
summary: How work earns Done status so the increment stays releasable and transparent.
node: Definition of Done gate (increment)
detail: Shared criteria govern when backlog items truly complete.
node: Current state
detail: Work is assessed against the team's agreed Definition of Done.
more: Only finished work counts toward a transparent, potentially shippable increment.
node: Checkpoint / gate
detail: Each item must meet every DoD criterion before labeled Done.
more: Incomplete quality gaps are not masked as complete work.
node: refine or escalate
detail: Failing items are fixed, descoped, or negotiated with the Product Owner.
more: Teams fix quality or negotiate scope rather than labeling incomplete work as Done.
node: Continue flow
detail: Accepted work joins the sprint increment as truly Done.
fallback_ascii: |
  Definition of Done gate (increment)

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

## 5. Stakeholder feedback loop (Review → Backlog)

```blueprint-diagram
key: linear
alt: Stakeholder feedback loop (Review → Backlog)
title: Review to backlog feedback
summary: How Sprint Review findings return to governed Product Backlog ordering for the next planning cycle.
node: Stakeholder feedback loop (Review
detail: Stakeholders inspect the working increment and share grounded feedback.
more: Discussion anchors on demonstrated working software, not slides or promises alone.
node: Backlog)
detail: The Product Owner synthesizes feedback into backlog clarity and ordering.
more: Refined ordering and item clarity prepare the next Sprint Planning commitment.
fallback_ascii: |
  Stakeholder feedback loop (Review
      |
      v
  Backlog)
```

## 6. Cross-phase mapping (A–F) in one sprint

| Phase | Where it happens in Scrum |
|-------|-------------------------|
| A Shape | Continuous refinement + PO/stakeholder work |
| B Plan | Sprint Planning |
| C Build | Sprint execution + Daily Scrum |
| D Verify | DoD, testing in sprint, Review validation |
| E Release | Ship when business chooses (increment is releasable) |
| F Operate & learn | Retrospective; production learnings feed backlog |

## 7. Flow details (walkthrough)

**Sprint lifecycle** — Refinement keeps the top of the Product Backlog transparent enough for Sprint Planning to commit. Inside the Sprint, the Daily Scrum inspects progress toward the Sprint Goal; Sprint Review inspects the increment with stakeholders; Sprint Retrospective improves how the team works. Review and Retro outputs feed the next refinement and planning cycle (empirical process: transparency, inspection, adaptation).

**Sprint Planning** — Part 1 clarifies *why* this Sprint matters: ordered backlog items; if value or ordering is unclear, return to refinement or a timeboxed spike. Developers select work that fits capacity and agree one Sprint Goal; if confidence is low, remove or swap items. Part 2 breaks work into a plan (often a Sprint Backlog); the Sprint starts when the team agrees how it will meet the goal.

**Daily execution** — The Daily Scrum is a 15-minute inspect-and-adapt for Developers toward the Sprint Goal; detailed problem-solving happens outside the timebox. Impediments are cleared through the day. The board or backlog should reflect reality by end of day.

**Definition of Done** — Work is only Done when it meets the shared DoD so the increment stays releasable and transparent. Otherwise fix quality or negotiate scope with the Product Owner—do not label incomplete work as Done.

**Review → backlog** — The Review grounds discussion in a working increment; the Product Owner synthesizes stakeholder feedback into Product Backlog ordering and clarity for the next Sprint Planning.

## 8. Authoritative sources & further reading

- [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — Official definition of Scrum (events, accountabilities, artifacts).
- [Scrum.org — What is Scrum?](https://www.scrum.org/resources/what-is-scrum) — Learning-oriented intro; complements the Guide.
- [Agile Alliance — Scrum (glossary)](https://www.agilealliance.org/glossary/scrum/) — Short glossary entry alongside the Guide.
- [Kanban Guide for Scrum Teams](https://www.scrum.org/resources/kanban-guide-scrum-teams) — Blending flow practices with Scrum cadence.

Full curated URL list with executive summaries: [`REFERENCE-LINKS.md`](../REFERENCE-LINKS.md).

## 9. Internal links

- [Ceremonies detail](ceremonies-prescriptive.md) · [Foundation](foundation-connection.md) · [Overview](https://forgesdlc.com/methodology-scrum.html)
