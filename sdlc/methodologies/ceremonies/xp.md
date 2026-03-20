# Extreme Programming (XP) → ceremony foundation

**Purpose:** Map **XP practices** that behave like **recurring collaboration** to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical narrative:** [`../xp.md`](../xp.md)

XP emphasizes **values** and **technical practices**; some map cleanly to **ceremony intents**, others are **habits** rather than meetings.

---

## Practices × intent types

| XP practice / ritual | Foundation intents (primary → secondary) | Notes |
|----------------------|------------------------------------------|--------|
| **Planning game** | **C1 Align** → **C2 Commit** | Customer and developers negotiate **scope** for a **small** horizon. |
| **Small releases** | **C4 Inspect** → **C6 Assure** | Frequent **feedback** from real use; **CI** and **TDD** embed **C6** continuously. |
| **Stand-up** (if team uses one) | **C3 Sync** | Not uniquely “XP”—often borrowed with Scrum/Kanban cadence. |
| **Retrospective** (if adopted) | **C5 Improve** | Common **blend** with Scrum-style process. |
| **Pair programming / ensemble** | **C3 Sync** (micro) + **C6** (continuous review) | **Review in the moment**; not a calendar ceremony but satisfies **coordination** and **quality** intent. |
| **On-site customer** | **C1** + **C4** (ongoing) | **Demand** archetype **embedded**—reduces need for heavy periodic **C4** batches. |

**C6** is **strongly embedded** in **TDD**, **CI**, and **collective ownership**—see [`../xp.md`](../xp.md).
