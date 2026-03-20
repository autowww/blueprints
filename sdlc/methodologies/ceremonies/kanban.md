# Kanban ceremonies → ceremony foundation

**Purpose:** Map **Kanban** feedback loops and common rituals to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical Kanban narrative:** [`../kanban.md`](../kanban.md) · [Kanban Guide for Scrum Teams](https://www.scrum.org/resources/kanban-guide-scrum-teams) (when blending) · [Kanban University — Kanban Guide](https://kanban.university/kanban-guide)

**Note:** Kanban does not mandate **one** global meeting set; names and cadence are **team and service** specific. Below maps **typical** practices.

---

## Practices / meetings × intent types

| Common practice | Foundation intents (primary → secondary) | Notes |
|-----------------|------------------------------------------|--------|
| **Replenishment** (pull selection) | **C2 Commit** → **C1 Align** | What gets pulled next given WIP and policies; may be event-driven or on a rhythm. |
| **Stand-up / sync** | **C3 Sync** | Flow, blockers, handoffs—often daily or more frequent for urgent services. |
| **Service delivery review** | **C4 Inspect** → **C5 Improve** | Service performance vs expectations (lead time, throughput, customer). |
| **Operations review** | **C5 Improve** → **C1 Align** | Cross-team or dependency health; may feed portfolio **Steer**. |
| **Delivery planning** (if used) | **C1 Align** → **C2 Commit** | Horizon planning without necessarily a Sprint boundary. |
| **Explicit policies / DoD per column** | **C6 Assure** (embedded) | Quality and readiness **as work moves**—not only a terminal gate. |

**C6** in Kanban is often **continuous** via **policies** and **Definition of Done** per state; formal **release** may still map to **C6** at train or deploy boundaries.

---

## Tracking

**Cycle time** and **queue time** need **board/tracker** data; git shows **activity**, not **waiting** or **blocked** time—[`../kanban.md`](../kanban.md).
