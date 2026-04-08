---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Process slots — SDD I/O (cross-methodology)

**Purpose:** **Spec-driven development** view of **named process slices** that appear under many methodologies (Scrum, Kanban, XP, phased). Each slot is **not** a calendar title—it is a **reusable I/O contract** you can attach to your own ceremonies or gates.

**Template:** [`../../templates/sdd/PROCESS-SLOT.template.md`](../../templates/sdd/PROCESS-SLOT.template.md)

**Handbook:** [Process (SDD I/O)](../../docs/spec-driven-sdd-process.html)

**Maps to intents:** Each slot lists **C1–C6** touch for traceability to [`ceremony-foundation.md`](../ceremonies/ceremony-foundation.md).

---

## P1 — Backlog refinement (options → ready)

| Field | Value |
|-------|-------|
| `sdd_id` | `SDD-P1-REFINEMENT` |
| `kind` | `process_slot` |
| `maps_to.ceremony_intents` | C1 (partial), C2 prep |
| `maps_to.sdlc_phases` | A, B |

### Summary

Increase **transparency** and **readiness** of top backlog items **before** commitment—without yet pulling into a timebox.

### Preconditions

| ID | Artifact | Example |
|----|----------|---------|
| PRE-P1-1 | Ranked options exist | Top 15 epics/stories in order |
| PRE-P1-2 | Definition of Ready documented | Team wiki §DoR |

### Inputs

| ID | Name | Example (snippet) |
|----|------|-------------------|
| IN-P1-1 | Raw story drafts | “As a user I want offline…” |
| IN-P1-2 | Tech constraints | “SQLite only; max 50MB cache” |

### Outputs

| ID | Name | Consumer | Example |
|----|------|----------|---------|
| OUT-P1-1 | Sized / clarified stories | Planning | AC bullets + mock link in `story.md` |
| OUT-P1-2 | Explicit “not ready” flags | Demand | “M2E4S1 blocked on legal — label `blocked`” |

### Postconditions

- [ ] Next planning can **name** items that meet DoR.
- [ ] **Estimates** or **t-shirt** size recorded where team policy requires.

### Filled example

Refined `M2E1S3`: AC added (3 Gherkin scenarios); spike closed on encryption; marked `ready`; still too large — split to `M2E1S3a/b` in WBS.

---

## P2 — Planning / commit slice

| `sdd_id` | `SDD-P2-PLANNING` | `maps_to` | **C2** (often + C1 tail) |

### Summary

Select work for **next execution boundary** and record **forecast** vs **capacity**.

### Preconditions

| ID | Ready when example |
|----|---------------------|
| PRE-P2-1 | DoR-met items ≥ team’s typical pull |
| PRE-P2-2 | Capacity known (PTO, holidays) |

### Inputs

| Example |
|---------|
| Ordered backlog, velocity/cycle data, dependency board |

### Outputs

| Example |
|---------|
| Sprint/iteration goal string; committed IDs in tracker; deferred list with reasons |

### Filled example

Sprint 14: goal “Ship conflict modal”; committed `M2E1S2`, `M2E1S3a`; deferred `M2E1S3b` (capacity); recorded in Linear + `WBS.md`.

---

## P3 — Daily execution sync (micro-loop)

| `sdd_id` | `SDD-P3-DAILY` | `maps_to` | **C3** |

### Summary

**24h** inspect-and-adapt toward **current goal**; **unblock** or **escalate**.

### Inputs

| Example |
|---------|
| Board state, CI status, “yesterday/today” per active work unit |

### Outputs

| Example |
|---------|
| Owner on each blocker; adjusted task order; optional note in standup channel linking issue # |

### Filled example

Blocker: emulator crash — `@devB` pairs with `@devA` 2h; PO notified if S2 slips to next day; board updated 10:05.

---

## P4 — Stakeholder inspection (demo / review)

| `sdd_id` | `SDD-P4-INSPECT` | `maps_to` | **C4** |

### Summary

**Working** increment vs **acceptance**; structured **feedback** to backlog.

### Preconditions

| Example |
|---------|
| Environment reachable; AC published; known defects listed |

### Outputs

| Example |
|---------|
| Signed-off AC table; new stories with IDs; meeting notes path |

### Filled example

`M2E1S1` AC met; `M2E1S2` AC3 → new `M2E6S1`; notes `…/notes/2026-01-22-demo.md`.

---

## P5 — Release candidate assurance

| `sdd_id` | `SDD-P5-RC` | `maps_to` | **C6** |

### Summary

Prove **release readiness**: tests, checks, sign-offs, **artifact immutability**.

### Inputs

| Example |
|---------|
| RC build id, test report, dependency audit, privacy checklist |

### Outputs

| Example |
|---------|
| Go/no-go; `CHANGELOG`; tag; store listing draft |

### Filled example

RC `1.4.0-rc2`: UI tests 142/142; Steer go; tag pushed; Play Store bundle `…aab` hash logged in `release/M2.md`.

---

## P6 — Phase / gate decision (phased delivery)

| `sdd_id` | `SDD-P6-GATE` | `kind` | `process_slot` | `gate_or_continuous` | `gate` |

### Summary

Formal **exit** from stage **N** to **N+1** with **evidence pack** and **steering decision**.

### Preconditions

| ID | Example |
|----|---------|
| PRE-P6-1 | Exit criteria checklist for stage |
| PRE-P6-2 | Gate pack assembled (design refs, test summary, risks) |

### Inputs

| Example |
|---------|
| Baseline IDs, CR impact if any, audit log excerpts |

### Outputs

| Example |
|---------|
| Signed gate record; updated baseline version; “hold” actions with owners |

### Approvals (typical)

| Approver | Evidence | Record |
|----------|----------|--------|
| Sponsor / Steer | Exit criteria matrix | `gates/G3-approve-2026-02-01.pdf` or signed wiki |

### Filled example

Design stage exit: TRR checklist green; one CR approved → rebaselined SRS v1.3; gate **approve** logged; build stage start date set.

---

## Using with agents / engineers / product

| Role | Use SDD slots to… |
|------|-------------------|
| **Product** | Ensure **OUT-* rows** land in **backlog/docs** before next C2. |
| **Engineers** | Tie **commits/PRs** to **IN/OUT** work-unit IDs; reject PRs missing trace row. |
| **Agents** | Read **Preconditions** + **Inputs** as **prompt context**; write **Outputs** only to **named paths** in spec. |

Copy any slot into your repo via [`PROCESS-SLOT.template.md`](../../templates/sdd/PROCESS-SLOT.template.md) and specialize.
