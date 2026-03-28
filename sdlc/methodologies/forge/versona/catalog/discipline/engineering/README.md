# Engineering family — Versona ancestry

This folder holds **discipline** Versona templates for the **Engineering** domain and the **family aggregator**. It normatively describes how those templates relate: **Software Engineering (`versona-se`)** is the **conceptual ancestor** for craft and CS fundamentals; **specialists** extend that story with domain-specific bridges.

**Related:** [`../../ANCESTRY.md`](../../ANCESTRY.md) (kinds and domains) · [`../../VERSONA-FRAMEWORK.md`](../../VERSONA-FRAMEWORK.md) (sessions, processes) · [`versona-family-engineering.mdc.template`](family/versona-family-engineering.mdc.template) (family aggregator)

---

## 1. Conceptual family tree

Cursor rules do **not** inherit at runtime—each `.mdc` duplicates the shared baseline for self-containment. **Ancestry** here means **documented layering**, not OO subclassing:

1. **Layer 0** — Generic Versona baseline (`versona-generic.mdc.template`, `_includes/GENERIC-VERSONA-BASELINE.md`).
2. **Software Engineering** — [`versona-se.mdc.template`](versona-se.mdc.template): shared **craft** lens—algorithms, idioms, patterns and antipatterns, review and refactoring principles, code-level quality. This is the **foundational Engineering discipline** Versona for **implementation craft** (not a substitute for methodology/process documentation).
3. **Specialists** — One template per narrow discipline, each with its own bridge under `blueprints/disciplines/engineering/`:
   - [`versona-architecture.mdc.template`](versona-architecture.mdc.template)
   - [`versona-devops.mdc.template`](versona-devops.mdc.template)
   - [`versona-testing.mdc.template`](versona-testing.mdc.template)
   - [`versona-frontend.mdc.template`](versona-frontend.mdc.template)
   - [`versona-mobile.mdc.template`](versona-mobile.mdc.template)
   - [`versona-iot.mdc.template`](versona-iot.mdc.template)
4. **Family aggregator** — [`versona-family-engineering.mdc.template`](family/versona-family-engineering.mdc.template): merges **relevant** disciplines into one consolidated §5-style report.

The **baseline set** may **grow** over time (e.g. cloud- or platform-specific templates). New specialists should follow the same pattern: **narrow scope**, **explicit bridge**, **hand off** work outside that scope.

---

## 2. When to invoke which rule

| Situation | Preferred rule |
|-----------|----------------|
| **Unclear** which engineering lens applies, or **multiple** surfaces (e.g. code + ops + tests) | **`versona-family-engineering`** first — **default entry** for cross-cutting Engineering review |
| **Pure craft / code-quality** pass (fundamentals, readability, patterns at implementation level) | **`versona-se`** alone |
| Work clearly in **one** domain only (e.g. only CI/CD, only web UI, only embedded constraints) | The matching **specialist** template |

For **which disciplines apply** when unsure, see also [`../../routing/versona-all.mdc.template`](../../routing/versona-all.mdc.template) (routing).

---

## 3. Process vs engineering “done”

Separate **delivery process** from **engineering completion signals**:

| Layer | Role |
|-------|------|
| **Process / methodology** | How work flows (Forge Sparks, Scrum, Kanban, etc.—often coordinated under the **Forge** umbrella in this repo). Lived in methodology docs and project `sdlc/` / ceremonies—not duplicated in full inside each Versona. |
| **Engineering discipline** | Whether the **work product** meets discipline expectations: documentation, tests (unit / UI / integration as appropriate), user-facing docs where applicable, **evidence and reporting** back to a human or invoker (another Versona, session, or Ember Log). Exact DoD is **team-defined**; Versonas **assess** fit to stated criteria. |

---

## 4. Narrow specialists and handoffs

A specialist Versona **works only within its bridge** (architecture vs DevOps vs frontend, etc.). It **does not** assert authority outside that scope—recommend **handoff** to another discipline Versona or use **`versona-all`** when routing is unclear. Future **deep** specialists (e.g. single-cloud) should **defer** out-of-scope stacks explicitly (same handoff rule).

---

## 5. Activities beyond a single §5 report

Discipline Versonas are **virtual personas**; **§5 structured output** is **normative** when teams use that shape—see [`VERSONA-CONTRACT.md`](../../VERSONA-CONTRACT.md) §5. Other **activities** (advise, draft, orchestration of handoffs within discipline scope) are allowed per [`VERSONA-FRAMEWORK.md`](../../VERSONA-FRAMEWORK.md) §1–2 until additional output schemas ship. This Engineering ancestry still applies: **SE as craft ancestor**, **specialists as extensions**, **family first** for multi-lens work, **process vs discipline** as in §3.
