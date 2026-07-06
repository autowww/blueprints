---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Kanban — major processes & flow maps

## 1. Pull through the value stream

```blueprint-diagram
key: linear
alt: Pull through the value stream
title: Kanban value stream pull
summary: Move work through agreed columns only when downstream capacity can accept it.
node: Pull through the value stream
detail: Frames the Kanban value stream as governed pull, not push.
node: Start
detail: Work enters from upstream options or replenishment.
more: Items arrive from discovery or committed backlog when policy allows pull.
node: Core steps (see walkthrough below)
detail: Traverse workflow columns under WIP limits and DoD gates.
more: Columns are agreed states in your Definition of Workflow; pull only when the next column has capacity.
node: Outcome
detail: Delivered value with traceable flow metrics and reviewable Done criteria.
more: Lead time stays visible when teams avoid pushing into overloaded Doing columns without capacity.
fallback_ascii: |
  Pull through the value stream

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: Definition of Workflow
```

Customize column names to your **Definition of Workflow**.

## 2. Replenishment decision

```blueprint-diagram
key: decision
alt: Replenishment decision
title: Replenishment pull decision
summary: Decide which options enter the system when capacity and dependencies allow.
node: Replenishment decision
detail: Governs which backlog options may enter committed flow.
node: Current state
detail: Assess queue depth, WIP limits, and class-of-service mix.
more: Replenishment reviews downstream capacity against the Definition of Workflow before adding work.
node: Checkpoint / gate
detail: Verify WIP headroom, dependencies, and readiness to pull.
more: Items must fit WIP rules and class-of-service policy with clear dependencies resolved.
node: refine or escalate
detail: Defer, split, or run alignment when pull criteria fail.
more: Run spikes or stakeholder alignment before retrying pull when scope or dependencies remain unclear.
node: Continue flow
detail: Pull the item into the next column when the gate passes.
more: Committed work enters Doing only after replenishment confirms bounded, reviewable scope.
fallback_ascii: |
  Replenishment decision

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

## 3. Blocked work escalation

```blueprint-diagram
key: decision
alt: Blocked work escalation
title: Blocked work escalation gate
summary: Route blockers to fast team response or formal escalation when policy thresholds hit.
node: Blocked work escalation
detail: Governs how blocked cards leave the wait state.
node: Current state
detail: Capture blocker type, owner, and time in blocked column.
more: Teams track aging blocked items against service-delivery policy thresholds.
node: Checkpoint / gate
detail: Check whether team policy can resolve the blocker locally.
more: Swarm or fast team response applies when policy allows same-team resolution.
node: refine or escalate
detail: Escalate when trade-offs or time limits exceed team authority.
more: Service delivery or steering decides priority trade-offs; record the decision before resuming flow.
node: Continue flow
detail: Resume pull once the blocker clears or is accepted.
more: Unblock only after the recorded decision restores a reviewable path through the value stream.
fallback_ascii: |
  Blocked work escalation

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

## 4. Release train (optional policy)

```blueprint-diagram
key: linear
alt: Release train (optional policy)
title: Release train policy flow
summary: Batch Done work to production on an optional train or calendar cadence.
node: Release train (optional policy)
detail: Frames how board Done maps to production release.
more: Optional policy layers release cadence onto Kanban Done without replacing column workflow.
node: Start
detail: Items reach Done on the board per DoD.
more: Board completion and production deployment may follow different schedules under train policy.
node: Core steps (see walkthrough below)
detail: Batch, validate, and deploy per your release train or calendar.
more: Align steps with continuous delivery when that is your Definition of Workflow instead of a train.
node: Outcome
detail: Production reflects governed releases aligned with board Done.
more: Release policy stays traceable whether you ship on a train or continuously from Done.
fallback_ascii: |
  Release train (optional policy)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 5. Phase mapping (A–F)

| Phase | Kanban locus |
|-------|----------------|
| A | Options / discovery |
| B | Replenishment |
| C | Doing |
| D | Verify / DoD |
| E | Release policy |
| F | Ops feedback → options |

## 6. Flow details (walkthrough)

**Value stream** — Columns are agreed workflow states, governed by your Definition of Workflow and WIP limits. Pull when downstream capacity is available; pushing work into *Doing* without capacity hides queueing and inflates lead time.

**Replenishment** — Chooses which options enter the committed system. Items must fit WIP and class-of-service rules and have clear dependencies; otherwise defer, split, or run alignment/spikes before pull.

**Escalation** — Blockers get fast team response (e.g. swarm) when policy allows. If resolution needs priority trade-offs or misses a time threshold, escalate to service delivery or steering; record the decision before resuming flow.

**Release train** — *Done* on the board may still batch to production on a train or calendar. Align the diagram with your release policy (or continuous delivery if that is your Definition of Workflow).

## 7. Authoritative sources & further reading

- [Kanban University — The Kanban Guide](https://kanban.university/kanban-guide) — Current guide text for the Kanban method.
- [Agile Alliance — Kanban (glossary)](https://www.agilealliance.org/glossary/kanban/) — Short definition and roots.
- [Kanban Guide for Scrum Teams](https://www.scrum.org/resources/kanban-guide-scrum-teams) — Integrating Kanban with Scrum.
- [ProKanban.org](https://prokanban.org/) — Professional Kanban community and training paths.

Full curated list: [`REFERENCE-LINKS.md`](../REFERENCE-LINKS.md).

## 8. Internal links

- [Ceremonies](ceremonies-prescriptive.md) · [Overview](https://forgesdlc.com/methodology-kanban.html)
