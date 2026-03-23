# Lean ceremonies → ceremony foundation

**Purpose:** Map **Lean Software Development** practices and improvement rituals to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical Lean narrative:** [`https://forgesdlc.com/methodology-lean.html`](https://forgesdlc.com/methodology-lean.html) · [Wikipedia — Lean software development](https://en.wikipedia.org/wiki/Lean_software_development)

**Note:** Lean does not mandate a fixed ceremony calendar. It provides **improvement practices** that teams schedule based on need and cadence. Below maps **typical** Lean practices to foundation intents.

---

## Practices / meetings × intent types

| Common practice | Foundation intents (primary → secondary) | Notes |
|-----------------|------------------------------------------|--------|
| **Value-stream mapping** | **C1 Align** → **C5 Improve** | End-to-end flow analysis; identify waste and improvement opportunities. |
| **Pull-based selection** (replenishment) | **C2 Commit** | Items pulled when capacity allows; commitment is flow-based, governed by WIP limits. |
| **Stand-up / flow sync** | **C3 Sync** | Board walk focused on flow, blockers, and aging items — not individual status. |
| **Gemba walk** | **C3 Sync** → **C4 Inspect** | Management observes actual work; builds understanding, surfaces impediments. |
| **Customer feedback / delivery review** | **C4 Inspect** | Validate that delivered value matches customer need; measure outcomes. |
| **Kaizen event** | **C5 Improve** | Time-boxed improvement sprint on a specific waste or bottleneck. |
| **A3 problem-solving review** | **C5 Improve** → **C6 Assure** | Structured root-cause analysis and countermeasures; knowledge capture. |
| **Retrospective (Lean-flavored)** | **C5 Improve** | Data-driven reflection using flow metrics; improvement experiments. |
| **Built-in quality practices** | **C6 Assure** (embedded) | TDD, CI, pairing, automated deployment — quality is a practice, not a phase. |

**C6** in Lean is typically **embedded** in engineering practices rather than a separate ceremony. Release readiness is a **policy** (automated gates, DoD), not a meeting.

---

## Tracking

**Lead time** (demand → delivery) and **cycle time** (start → done) are the primary Lean metrics. Git shows **activity timestamps**, not **queue time** or **blocked time** — use board/tracker data for accurate flow measurement. See [`https://forgesdlc.com/methodology-lean.html`](https://forgesdlc.com/methodology-lean.html).

---

## Suggestions (Lean-specific)

| Practice | Suggestions |
|----------|-------------|
| **Value-stream mapping** | Do this **before** adding ceremonies — you may discover the existing calendar is part of the waste. Revisit quarterly or when lead times drift. |
| **Stand-up** | Walk the **board right-to-left** (closest to done first); focus on **flow** and **aging**, not yesterday's activity. Keep under 15 min. |
| **Kaizen** | Pick **one** measurable target; implement **during** the event, not after. Measure before/after. Standardize what works. |
| **A3** | Use for **complex** problems (not everything). The review validates **thinking quality**, not just the conclusion. |
| **Retrospective** | Bring **data** (cycle time, defect rate, WIP age). Frame improvements as **experiments** with a target condition and check date. |

Crosswalk to other methodologies: [`methodology-bridge.md`](methodology-bridge.md).
