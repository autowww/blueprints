# Methodology bridge — foundation intents ↔ named ceremonies

## Purpose

This file is the **crosswalk** between methodology-neutral **intent types** (C1–C6 in [`ceremony-foundation.md`](ceremony-foundation.md)) and what **Scrum, Kanban, phased delivery, and XP** usually **call** the rituals that satisfy those intents. Use it when:

- You **blend** frameworks (e.g. Scrum cadence + Kanban flow metrics).
- You rename meetings but want to verify **no intent is orphaned**.
- You **onboard** people who know one methodology and need to map vocabulary.

**Forks (detail + event-level suggestions):** [Scrum](scrum.md) · [Kanban](kanban.md) · [Phased](phased.md) · [XP](xp.md)

---

## Bridge matrix — intent × methodology (typical “nodes”)

Cells list **common names** for practices that **primarily** serve that intent. One **calendar event** may cover **multiple** intents (e.g. planning = C1 + C2); see fork files for primary → secondary ordering.

| Intent | Scrum (typical) | Kanban (typical) | Phased (typical) | XP (typical) |
|--------|-----------------|------------------|------------------|--------------|
| **C1 Align** | Sprint Goal conversation; backlog refinement themes | Replenishment context; service strategy | Requirements / design **reviews**; charter alignment | Planning game (scope negotiation); onsite customer dialogue |
| **C2 Commit** | Sprint Planning (forecast + Sprint Backlog) | **Replenishment**; pulling into “ready/doing” | Phase entry authorization; **baseline** sign-off to enter build | Stories selected for immediate iteration |
| **C3 Sync** | **Daily Scrum** | Stand-up / flow meeting | **Coordination** meetings inside a phase; integration forums | Pair rotation check-ins; implicit in pairing |
| **C4 Inspect** | **Sprint Review** | Service delivery review (service vs expectations) | **UAT**; milestone demos; validation reviews | **Small release** feedback; customer acceptance |
| **C5 Improve** | **Sprint Retrospective** | Ops review; Kaizen / retrospective cadence | **Post-phase** lessons; process audits (lighter between gates) | Team reflection; coach feedback loops |
| **C6 Assure** | **Definition of Done** + increment quality; release may be separate | **Policies** / DoD per column; release train | **IV&V**; test phase exit; **release approval** | **TDD**, **CI**, collective ownership |

**Empty-looking cells:** XP often **embeds** C3/C6 in practices rather than a named meeting—see [XP fork](xp.md).

---

## Cross-methodology suggestions

These apply **regardless** of framework; tune with your [roles](../roles-archetypes.md) and [phases](../../SDLC.md).

| Topic | Suggestion |
|-------|------------|
| **Cover every intent** | Over a **horizon** (e.g. two weeks), you should **touch** C1–C6 somehow—not necessarily six meetings. Missing **C5** shows up as repeating mistakes; missing **C4** as surprise rejection at release. |
| **Don’t double-book intents** | If **C2** happens only in a giant monthly meeting, **C3** still needs a **lighter** rhythm or async channel so blockers don’t wait four weeks. |
| **Name intents in invites** | e.g. “Daily — **C3** sync; not for backlog reorder (**C2**)” reduces PO hijack. |
| **Blends** | **Scrumban:** keep Scrum **C2/C4** time-boxes if helpful; add Kanban **WIP** and **aging** to **C3/C5**. **Phased + iterative:** use **gates** for **C6** at phase exits; use **Sprint Review–style C4** inside implementation for stakeholders. |
| **Evidence** | For **C6** in regulated contexts, store **decisions** where **Steer** expects them ([`phased-delivery.md`](../phased-delivery.md)); git activity alone is rarely enough. |
| **Tracking** | Ceremonies **consume** aggregates from [`sdlc/TRACKING-FOUNDATION.md`](../../../../sdlc/TRACKING-FOUNDATION.md) pattern repos—they don’t replace **work-unit ids** in commits. |

---

## Per-intent bridge notes (how methodologies differ)

### C1 Align

- **Scrum:** Sprint Goal + Product Goal connection.  
- **Kanban:** Alignment often **continuous** via policy and replenishment **context**, less a single “goal statement.”  
- **Phased:** Alignment **frozen** at baselines—later change is **change control**, not casual replanning.  
- **XP:** **Customer** proximity compresses alignment into **ongoing** conversation.

### C2 Commit

- **Scrum:** Explicit **forecast** for one Sprint.  
- **Kanban:** **Pull** when capacity and policy allow—commitment is **flow-based**, not necessarily a batch.  
- **Phased:** Commitment = **authorized to enter next phase** with a **package**.  
- **XP:** **Small batches**—commitment horizon is **short** by design.

### C3 Sync

- **Scrum:** Daily, **Developers**-centric per Guide.  
- **Kanban:** Frequency scales with **interrupt** rate and **dependency** count.  
- **Phased:** Sync may be **weekly** status + **ad hoc** integration when handoffs are heavy.  
- **XP:** **Pairing** reduces need for status **broadcast** but not for **dependency** sync across pairs.

### C4 Inspect

- **Scrum:** Stakeholder-facing **Review** each Sprint.  
- **Kanban:** May be **on demand** or **service review** on a slower cadence than delivery.  
- **Phased:** **Formal** inspection at **gate** with evidence.  
- **XP:** **Frequent** slices to customer or proxy.

### C5 Improve

- **Scrum:** **Retro** every Sprint.  
- **Kanban:** Often **separate** service / ops improvement cadence.  
- **Phased:** Improvement may lag until **post-project** unless you add **explicit** retro inside phases.  
- **XP:** **Values** + coach; retro optional if team is **disciplined** elsewhere.

### C6 Assure

- **Scrum:** **DoD** is team-owned; PO **accepts** increment.  
- **Kanban:** **Policies** are first-class; quality is **of the system**.  
- **Phased:** **Independent** verification is common.  
- **XP:** **Technical practices** are the primary assurance mechanism.

---

## How to map your own calendar to C1–C6

1. List recurring events (and **async** rituals: e.g. “Friday PR digest”).  
2. For each, ask: which **outcome** (align, commit, sync, inspect, improve, assure) is **non-negotiable**?  
3. If an event tries to do **all six**, split or **time-box** parts—or accept **weak** outcomes.  
4. Compare to this matrix: if your methodology **expects** a node (e.g. Scrum **Review**) and you skipped it, decide whether another practice **covers** the same intent.  
5. Record **project-specific** names in `sdlc/` (consuming repo), not new blueprint intent IDs.

---

## Related reading

| Doc | Why |
|-----|-----|
| [`ceremony-foundation.md`](ceremony-foundation.md) | Phase × intent matrix; **suggestions by intent** |
| [`README.md`](README.md) | Package index |
| [`roles-archetypes.md`](../roles-archetypes.md) | Who leads each intent |
| [`agile.md`](../agile.md) | Blending under Agile umbrella |
