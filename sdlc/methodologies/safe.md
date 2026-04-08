---
slug: methodology-safe
tier: 201
lens: methodology
nav_section: Methodology Comparisons
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# SAFe (Scaled Agile Framework)

## What it is

**SAFe** is a framework for scaling **Lean-Agile** practices across **multiple teams** and organizational levels. It builds on Scrum, Kanban, XP, and Lean thinking to coordinate development at **team**, **program (Agile Release Train)**, **large solution**, and **portfolio** levels through shared cadence, alignment events, and architectural runway.

It is **not** a lightweight single-team framework — if one Scrum or Kanban team covers your product, SAFe's coordination overhead is unnecessary. It **is** a strong fit when **5–125+ developers** across **multiple teams** must deliver a **single solution** on a shared timeline with enterprise-level governance.

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**SAFe — Scaled Agile Framework**](https://scaledagileframework.com/) | **Official** SAFe body of knowledge — configurations, roles, events, artifacts — the authority for mapping this blueprint's Phases A–F to SAFe. |
| [SAFe Practice Consultants (SPCs)](https://scaledagile.com/training/) | Training and certification paths — complements the framework site, not a second standard. |
| [Agile Alliance — SAFe](https://www.agilealliance.org/glossary/safe/) | Short **glossary** entry and community perspective — shared vocabulary alongside the framework site. |

**Trademark:** "SAFe" and "Scaled Agile Framework" are registered trademarks of Scaled Agile, Inc.; this document summarizes concepts for adoption alongside this blueprint, not for certification prep.

---

## Core structure (summary)

### Configurations

| Configuration | Scope |
|---------------|-------|
| **Essential SAFe** | Minimum viable: one or more ARTs (Agile Release Trains); team and program levels. |
| **Large Solution SAFe** | Multiple ARTs coordinated via a Solution Train for complex systems. |
| **Portfolio SAFe** | Strategic themes, Lean budgets, portfolio Kanban — connects strategy to execution. |
| **Full SAFe** | All levels combined. |

### Key roles

| Role | Essence |
|------|---------|
| **Release Train Engineer (RTE)** | Servant leader for the ART; facilitates program-level events; removes impediments across teams. |
| **Product Management** | Owns the **Program Backlog**; defines features and priorities at the ART level. |
| **System Architect / Engineer** | Defines **architectural runway** and system-level enablers; guides cross-team technical decisions. |
| **Business Owners** | Key stakeholders accountable for business outcomes of the ART. |
| **Scrum Master / Team Coach** | Facilitates team-level Agile practices (Scrum, Kanban, XP); same as single-team Scrum Master. |
| **Product Owner** | Owns the **Team Backlog**; defines stories and priorities at the team level. |

**Cross-reference:** methodology-neutral **delivery archetypes** and how SAFe roles sit on them — [`roles-archetypes.md`](roles-archetypes.md).

### Cadences and events

| Event | Level | Purpose |
|-------|-------|---------|
| **PI Planning** | ART (program) | Two-day event every PI (8–12 weeks); teams commit to **PI Objectives**, identify dependencies, build a program board. |
| **Iteration Planning** | Team | Same as Sprint Planning — select stories from the team backlog for the iteration. |
| **Daily Stand-up** | Team | Same as Daily Scrum — inspect progress, surface blockers. |
| **Iteration Review** | Team | Demo working increment; stakeholder feedback. |
| **Iteration Retrospective** | Team | Inspect and adapt team process. |
| **System Demo** | ART | Every iteration — integrated demo of the full system across all teams on the ART. |
| **Inspect & Adapt (I&A)** | ART | End of PI — quantitative + qualitative review; problem-solving workshop; improvement backlog. |
| **ART Sync** | ART | Weekly or bi-weekly — cross-team dependency, risk, impediment sync (Scrum of Scrums + PO sync). |
| **Solution Demo** | Large Solution | Integrated demo across multiple ARTs. |
| **Pre- and Post-PI Planning** | Large Solution | Coordinate PI objectives across ARTs in a Solution Train. |

### Artifacts

| Artifact | Scope |
|----------|-------|
| **Portfolio Backlog** | Epics (business + enabler) managed via portfolio Kanban. |
| **Program Backlog** | Features (functional + enabler) owned by Product Management. |
| **Team Backlog** | Stories (user + enabler) owned by Product Owner. |
| **PI Objectives** | Team and ART commitments for the PI — committed + stretch. |
| **Program Board** | Visualizes features, dependencies, and milestones across teams for the PI. |
| **Architectural Runway** | Existing technical infrastructure enabling near-term features without excessive redesign. |

---

## Mapping to this blueprint's SDLC

[`SDLC.md`](../SDLC.md) uses **Phases A–F** (discover → release). SAFe does **not** replace those phases; it **layers** multi-team coordination on top:

| SAFe idea | Blueprint touchpoint |
|-----------|---------------------|
| Portfolio Kanban / strategic themes | Phase A: discovery, vision, roadmap in `docs/requirements/`. |
| PI Planning + PI Objectives | Phase A–B: alignment, backlog, specs, WBS. PI Objectives are the program-level "what done means." |
| Iterations (sprints) | Phase B–D: plan, build, verify per team — same as Scrum mapping. |
| System Demo + I&A | Phase D–E: integrated quality, cross-team review — see [`cicd.html`](../docs/cicd.html). |
| Release on demand | Phase F: shipping; SAFe decouples release from PI cadence — release when business value warrants it. |

If your repo uses **milestone → epic → story** specs, a **PI** often maps to a **milestone**, **features** to **epics**, and **stories** to iteration-level work items.

---

## Agentic SDLC: SAFe + agents + tracking

**Agentic** here means humans steer while **tools and AI agents** assist. SAFe still applies to **human** commitments and **team/ART** ceremonies; agents are **enablers**, not Product Managers.

| Topic | Guidance |
|-------|----------|
| **PI Planning** | PI Objectives are **human** commitments. Agents can prepare capacity data, dependency visualizations, and draft feature descriptions — but **business owners and teams** negotiate scope. |
| **Iteration execution** | Same as Scrum agentic guidance — agent output is not "free" capacity; review and integration cost people. |
| **System Demo** | Demo **integrated, working software**; agent-assisted features must meet DoD and align with PI Objectives. |
| **I&A** | Quantitative data (velocity, quality, cycle time) can be **agent-gathered**; problem-solving and improvement experiments stay **human-driven**. |
| **Cross-team sync** | Agents can surface **dependency risks** and **blocked work** across teams; humans own resolution and re-planning. |
| **Tracking foundation** | Repos that add [`sdlc/TRACKING-FOUNDATION.md`](../../../sdlc/TRACKING-FOUNDATION.md) model **contributor → events → work units**. SAFe ceremonies consume **aggregates** (e.g. velocity per iteration, features completed per PI); **PI Objectives / capacity** usually live in the **ALM tool**, not in git alone. |

**Caution:** High agent throughput can **amplify** coordination costs at the ART level — more integrated work means more cross-team review and System Demo preparation. Address in **I&A** if review becomes the bottleneck.

---

## Ceremonies

**Methodology-neutral intent types** (Align, Commit, Sync, …) live in [`ceremonies/ceremony-foundation.md`](ceremonies/ceremony-foundation.md). **SAFe events mapped to those intents** + git vs ALM gaps: [`ceremonies/safe.md`](ceremonies/safe.md).

See project [`TRACKING-CHALLENGES.md`](../../../sdlc/TRACKING-CHALLENGES.md) for limits of commit-based metrics.

---

## SAFe vs single-team Agile (when to adopt)

| Signal | Recommendation |
|--------|----------------|
| **1 team, 1 product** | Use Scrum, Kanban, or XP — SAFe overhead is not justified. |
| **2–3 loosely coupled teams** | Consider lightweight coordination (Scrum of Scrums) before full SAFe. |
| **5+ teams, shared codebase or platform** | Essential SAFe (ART) provides structure for alignment and integration. |
| **Multiple products / value streams** | Portfolio SAFe connects strategy to execution across ARTs. |
| **Regulatory / compliance requirements at scale** | SAFe's built-in governance (Lean budgets, compliance milestones) reduces ad-hoc process. |

This blueprint does not mandate SAFe for multi-team work; [`agile.md`](agile.md) describes the umbrella.

---

## Prescriptive deep dive (teams)

Package **[`safe/README.md`](safe/README.md)** — foundation fit, roles, ceremonies (PI Planning, I&A, System Demo, ART Sync), process maps.

---

## Further reading

- [SAFe 6.0 — Framework overview](https://scaledagileframework.com/) — **Official** framework site for the latest version.
- [Agile Manifesto](https://agilemanifesto.org/) — **Values** that SAFe builds on; not a SAFe process.
- [Ceremonies — SAFe fork](ceremonies/safe.md) · [foundation intents](ceremonies/ceremony-foundation.md)
- Companion blueprint guides: [Scrum](scrum.md), [Kanban](kanban.md), [XP](xp.md), [Agentic SDLC](agentic-sdlc.md)