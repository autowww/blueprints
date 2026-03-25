# Kanban — major processes & flow maps

## 1. Pull through the value stream

```ks-diagram
key: linear
alt: Diagram
```

Customize column names to your **Definition of Workflow**.

## 2. Replenishment decision

```ks-diagram
key: decision
alt: Diagram
```

## 3. Blocked work escalation

```ks-diagram
key: decision
alt: Diagram
```

## 4. Release train (optional policy)

```ks-diagram
key: linear
alt: Diagram
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
