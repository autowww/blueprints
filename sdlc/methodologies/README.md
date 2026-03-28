# Methodology guides (blueprint)

**Purpose:** Deeper, **product-agnostic** guides than the short tables in [`SDLC.md`](../SDLC.md) or project [`TRACKING-METHODOLOGIES.md`](../../../sdlc/TRACKING-METHODOLOGIES.md) (in a consuming repo's `sdlc/`). Each file explains the methodology on its own terms, links to **authoritative external** material, and states how it **fits** an **agentic** workflow (humans + automation + optional coding agents) and the **engineering-tracking foundation** (contributor → events → work units).

**Audience:** Teams adopting [`blueprints/sdlc/`](../README.md); project-specific overrides stay in **`sdlc/`** and **`docs/`**.

---

## Foundation (methodology-neutral)

These documents apply **regardless** of which methodology you choose.

| Guide | Topics |
|-------|--------|
| [**Roles & archetypes**](roles-archetypes.md) | Five archetypes: summary + **detail** (responsibilities, artifacts, ceremonies) + **methodology tweaks** per archetype; **Owner/Implementer**; title quick-reference; **methodology roll-up**; specialty hats vs **Contributor**. Handbook: [`methodologies-roles.html`](../docs/methodologies-roles.html). |
| [**Ceremonies**](ceremonies/README.md) | **Foundation** ([`ceremony-foundation.md`](ceremonies/ceremony-foundation.md)): C1–C6, phase + archetype matrices, **practice suggestions** per intent. **Bridge** ([`methodology-bridge.md`](ceremonies/methodology-bridge.md)): intents ↔ methodology names, blends, calendar mapping. **Forks** per methodology. Handbook: [`methodologies-ceremonies.html`](../docs/methodologies-ceremonies.html). |

---

## Iterative Agile frameworks

Frameworks that organize work in **iterations** or **cadences** with cross-functional teams and regular feedback. Most share roots in the [Agile Manifesto](https://agilemanifesto.org/).

| Guide | Topics |
|-------|--------|
| [**Agile (umbrella)**](https://forgesdlc.com/methodologies-agile.html) | Values, principles, how Scrum/Kanban/XP combine; choosing a primary rhythm. |
| [**Scrum**](https://forgesdlc.com/methodology-scrum.html) | Roles, events, artifacts, sprint flow; agentic fit; tracking. **Prescriptive package:** [`scrum/README.md`](scrum/README.md). |
| [**Kanban**](https://forgesdlc.com/methodology-kanban.html) | Flow, WIP, policies, service classes; board vs git. **Prescriptive package:** [`kanban/README.md`](kanban/README.md). |
| [**Extreme Programming (XP)**](https://forgesdlc.com/methodology-xp.html) | Practices, technical excellence, pairing, CI. **Prescriptive package:** [`xp/README.md`](xp/README.md). |
| [**Feature-Driven Development (FDD)**](https://forgesdlc.com/methodologies-fdd.html) | Model-driven, feature-centric; five activities; chief programmers and class ownership; designed for larger teams. |
| [**Crystal**](https://forgesdlc.com/methodologies-crystal.html) | Family of methods scaled by team size and criticality; seven properties shared across variants (Clear, Yellow, Orange, Red). |
| [**DSDM**](https://forgesdlc.com/methodologies-dsdm.html) | Agile governance framework; MoSCoW prioritization; fixed time/cost, variable scope; integrates with PRINCE2. |
| [**Shape Up**](https://forgesdlc.com/methodologies-shape-up.html) | Basecamp's methodology: 6-week cycles, appetites, shaping, betting table, hill charts; full team autonomy during build. |

---

## Sequential and risk-driven models

Models that emphasize **upfront planning**, **formal verification**, or **risk-driven iteration**. Common in regulated industries and safety-critical systems.

| Guide | Topics |
|-------|--------|
| [**Phased delivery**](https://forgesdlc.com/methodologies-phased-delivery.html) | Sequential phases, gates, baselines vs incremental. **Prescriptive package:** [`phased/README.md`](phased/README.md). |
| [**V-Model**](https://forgesdlc.com/methodologies-v-model.html) | Verification and validation pairing; each development level maps to a test level; traceability-driven. **Prescriptive package:** [`v-model/README.md`](v-model/README.md). |
| [**Spiral Model**](https://forgesdlc.com/methodologies-spiral.html) | Risk-driven iterative development; four quadrants per cycle; anchor-point milestones (LCO, LCA, IOC). **Prescriptive package:** [`spiral/README.md`](spiral/README.md). |
| [**RAD (Rapid Application Development)**](https://forgesdlc.com/methodologies-rad.html) | Prototyping-centric; rapid iterations, user involvement, timeboxing; historical precursor to modern Agile. |

---

## Scaling frameworks

Frameworks designed to coordinate **multiple teams** delivering a **shared product** or **portfolio** of products.

| Guide | Topics |
|-------|--------|
| [**SAFe (Scaled Agile Framework)**](https://forgesdlc.com/methodology-safe.html) | Multi-team coordination, PI Planning, ART, portfolio governance; scaling Lean-Agile. **Prescriptive package:** [`safe/README.md`](safe/README.md). |
| [**Disciplined Agile (DA)**](https://forgesdlc.com/methodologies-disciplined-agile.html) | PMI's process-decision toolkit: goal-driven approach with multiple lifecycle options (Agile, Lean, CD, Exploratory, Program). |

---

## Lean and continuous delivery

Principles and practices focused on **optimizing flow**, **eliminating waste**, and **unifying development with operations**.

| Guide | Topics |
|-------|--------|
| [**Lean Software Development**](https://forgesdlc.com/methodology-lean.html) | Seven principles (eliminate waste, amplify learning, decide late, deliver fast, empower, build integrity, optimize the whole); value-stream thinking; Kaizen. **Prescriptive package:** [`lean/README.md`](lean/README.md). |
| [**DevOps**](https://forgesdlc.com/methodologies-devops.html) | Culture + practices + toolchain unifying Dev and Ops; CI/CD, IaC, monitoring, DORA metrics, incident response. **Prescriptive package:** [`devops/README.md`](devops/README.md). |

---

## Complementary practices

Practices that **enhance** any methodology rather than replacing it. They address specific aspects of specification, testing, or development.

| Guide | Topics |
|-------|--------|
| [**Spec-driven development**](https://forgesdlc.com/methodology-spec-driven.html) | Written intent leads implementation; docs↔code loop; agentic fit. **SDD I/O:** [`spec-driven/README.md`](spec-driven/README.md), templates [`templates/sdd/`](../templates/sdd/). Handbook: [`spec-driven.html`](../docs/spec-driven.html). |
| [**BDD (Behavior-Driven Development)**](https://forgesdlc.com/methodologies-bdd.html) | Given-When-Then scenarios as living specifications and automated acceptance tests; complements TDD and spec-driven development. |

---

## AI-native delivery

Methodologies designed for **AI-augmented** development with explicit discipline Versonas, decision memory, and evidence-based release rigor.

| Guide | Topics |
|-------|--------|
| [**Forge SDLC**](https://forgesdlc.com/methodology-overview.html) | AI-native delivery methodology: Ore→Ingot→Spark→Charge pipeline; Versonas (discipline virtual personas across 16 disciplines); Ember Log (decision memory); Assay Gate (evidence-based release); hat-switching for solo-to-enterprise scaling. **Prescriptive package:** [`forge/README.md`](forge/README.md). |

---

## Cross-cutting

Guides that apply **alongside** any methodology, addressing how **agents**, **automation**, **AI**, and **testing** interact with the SDLC.

| Guide | Topics |
|-------|--------|
| [**Agentic SDLC**](https://forgesdlc.com/agentic-sdlc.html) | Cross-cutting: agents, review, identity, limits — not a replacement for the guides above. |
| [**Testing knowledge base**](../../disciplines/engineering/testing/README.md) | Test levels, types, and design techniques (ISTQB-aligned); modern strategies (shift-left, TDD, BDD, contract testing, AI-augmented); test automation frameworks landscape and selection guidance. Not a methodology — a **reference** that all methodologies draw from. Now a standalone discipline package under [`blueprints/disciplines/engineering/testing/`](../../disciplines/engineering/testing/README.md). |

---

**Handbook (HTML):** [`docs/methodologies.html`](../docs/methodologies.html) (hub) and `docs/methodologies-*.html`; **spec-driven** is [`docs/spec-driven.html`](../docs/spec-driven.html). **Scrum/Kanban/phased/XP** subchapters (Foundation, Ceremonies, Process) may use [`docs/build_methodology_chapters.py`](../docs/build_methodology_chapters.py) when present; handbook diagrams use **` ```blueprint-diagram `** in Markdown. **Scrum — Roles** is hand-maintained in HTML.

**Maintainers:** curated external URLs, **executive summaries** (why each link matters here), and a quick `curl` check pattern — [`REFERENCE-LINKS.md`](REFERENCE-LINKS.md). Keep handbook [`methodologies-*.html`](../docs/methodologies.html) blurbs in sync when URLs or intent change.

**Project tracking (optional):** [`sdlc/TRACKING-FOUNDATION.md`](../../../sdlc/TRACKING-FOUNDATION.md) pattern in repos that add `sdlc/`.
