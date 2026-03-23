# SAFe ceremonies → ceremony foundation

**Purpose:** Map **SAFe events** (team-level and program-level) to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical SAFe narrative:** [`https://forgesdlc.com/methodology-safe.html`](https://forgesdlc.com/methodology-safe.html) · [**Scaled Agile Framework**](https://scaledagileframework.com/)

---

## Events × intent types

SAFe events operate at **two levels**: team (identical to Scrum) and program (ART). Program-level events are unique to SAFe.

### Program-level events

| SAFe event | Foundation intents (primary → secondary) | Notes |
|------------|------------------------------------------|--------|
| **PI Planning** | **C1 Align** → **C2 Commit** | Two-day event; vision + architecture briefing (C1), then team breakouts + PI Objectives (C2). Program board captures dependencies. |
| **System Demo** | **C4 Inspect** → **C6 Knowledge share** | Every iteration; integrated demo across all ART teams; Product Management accepts features. |
| **Inspect & Adapt (I&A)** | **C4 Inspect** → **C5 Improve** | End of PI; quantitative review + problem-solving workshop; improvement backlog items. |
| **ART Sync** | **C3 Sync** | Weekly/bi-weekly; Scrum of Scrums + PO Sync; cross-team impediments and dependencies. |

### Team-level events

| SAFe event | Foundation intents (primary → secondary) | Notes |
|------------|------------------------------------------|--------|
| **Iteration Planning** | **C2 Commit** → **C1 Align** | Select stories that advance PI Objectives; same as Sprint Planning. |
| **Daily Stand-up** | **C3 Sync** | 15-minute timebox; surface cross-team blockers for ART Sync escalation. |
| **Iteration Review** | **C4 Inspect** → **C1 Align** | Team demo; feeds into System Demo. |
| **Iteration Retrospective** | **C5 Improve** | Team improvement; ART-level themes escalated to I&A. |

### Large Solution events (when applicable)

| SAFe event | Foundation intents (primary → secondary) | Notes |
|------------|------------------------------------------|--------|
| **Pre-PI Planning** | **C1 Align** | Cross-ART alignment on solution context and objectives. |
| **Post-PI Planning** | **C2 Commit** | Integrate PI plans across ARTs; resolve cross-ART dependencies. |
| **Solution Demo** | **C4 Inspect** | Integrated demo across multiple ARTs. |

**C6 Assure / release** is **continuous** in SAFe via the **continuous delivery pipeline**, **Definition of Done**, and **built-in quality** practices. **Release on demand** (Phase F) is a separate business decision — see project release docs.

---

## What git-based tracking approximates vs what ceremonies need

| Event | Git / commits approximate | You still need (ALM / human) |
|-------|---------------------------|-------------------------------|
| PI Planning | Activity trends, prior PI throughput | Vision, feature priorities, **capacity**, business value, dependency mapping |
| System Demo | Merged PRs, integrated branches | **Stakeholder feedback**, feature acceptance, cross-team coordination |
| I&A | Throughput, defect trends, cycle time | **Root-cause analysis**, psychological safety, improvement experiments |
| ART Sync | Cross-repo activity, blocked PRs | **Verbal/async** impediment escalation, dependency resolution |
| Iteration Planning | Recent activity, linked work units | PI Objectives context, PO ordering, **capacity** |
| Daily | Activity per contributor | Verbal/async **blockers**, coordination |

See project [`TRACKING-CHALLENGES.md`](../../../../sdlc/TRACKING-CHALLENGES.md).

---

## Suggestions (SAFe-specific)

| Event | Suggestions |
|-------|-------------|
| **PI Planning** | Ensure **architecture briefing** is concrete (enabler epics, not just principles). Timebox team breakouts; avoid "planning theater." Use the confidence vote honestly — revote if average < 3/5. |
| **System Demo** | Demo **integrated, working software** — not slides. Product Management should actively accept/reject features against criteria, not defer to later. |
| **I&A** | Dedicate real time to the **problem-solving workshop** — do not let the quantitative review consume the entire session. Limit improvement items to top 1–3 that will actually be actioned. |
| **ART Sync** | Keep focused on **impediments and dependencies** — not a status report. If no blockers, keep it short. |
| **Iteration events** | Same as Scrum suggestions — see [`scrum.md`](https://forgesdlc.com/methodology-scrum.html). Ensure team retro themes that affect the ART bubble up to I&A. |

For **cross-methodology** blend tips (e.g. SAFe ART with Kanban teams), see [`methodology-bridge.md`](methodology-bridge.md).

---

## Agentic note

Human **accountability** for PI Objectives, feature acceptance, and improvement experiments stays with [**roles**](../roles-archetypes.md). Agents can prepare data (velocity charts, dependency graphs, draft PI Objectives) but **PI Planning negotiations**, **I&A problem-solving**, and **confidence votes** require human judgment — [`../agentic-sdlc.md`](../agentic-sdlc.md).
