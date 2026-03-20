# Methodology guides (blueprint)

**Purpose:** Deeper, **product-agnostic** guides than the short tables in [`SDLC.md`](../SDLC.md) or project [`TRACKING-METHODOLOGIES.md`](../../../sdlc/TRACKING-METHODOLOGIES.md) (in a consuming repo’s `sdlc/`). Each file explains the methodology on its own terms, links to **authoritative external** material, and states how it **fits** an **agentic** workflow (humans + automation + optional coding agents) and the **engineering-tracking foundation** (contributor → events → work units).

**Audience:** Teams adopting [`blueprints/sdlc/`](../README.md); project-specific overrides stay in **`sdlc/`** and **`docs/`**.

| Guide | Topics |
|-------|--------|
| [**Roles & archetypes**](roles-archetypes.md) | Five archetypes: summary + **detail** (responsibilities, artifacts, ceremonies) + **methodology tweaks** (Scrum/Kanban/phased/XP per archetype); **Owner/Implementer**; title quick-reference; **methodology roll-up**; specialty hats vs **Contributor**. Handbook: [`methodologies-roles.html`](../docs/methodologies-roles.html). |
| [**Ceremonies**](ceremonies/README.md) | **Foundation** ([`ceremony-foundation.md`](ceremonies/ceremony-foundation.md)): C1–C6, phase + archetype matrices, **practice suggestions** per intent. **Bridge** ([`methodology-bridge.md`](ceremonies/methodology-bridge.md)): intents ↔ methodology names, blends, calendar mapping. **Forks** + event suggestions: [Scrum](ceremonies/scrum.md), [Kanban](ceremonies/kanban.md), [Phased](ceremonies/phased.md), [XP](ceremonies/xp.md). Tied to [`SDLC.md`](../SDLC.md) §2. Handbook: [`methodologies-ceremonies.html`](../docs/methodologies-ceremonies.html). |
| [**Agile (umbrella)**](agile.md) | Values, principles, how Scrum/Kanban/XP combine. |
| [**Scrum**](scrum.md) | Roles, events, artifacts, sprint flow; agentic fit; tracking. **Prescriptive package:** [`scrum/README.md`](scrum/README.md) (foundation, roles, ceremonies I/O, process maps). |
| [**Kanban**](kanban.md) | Flow, WIP, policies, service classes; board vs git. **Prescriptive package:** [`kanban/README.md`](kanban/README.md). |
| [**Phased delivery**](phased-delivery.md) | Sequential phases, gates, baselines vs incremental. **Prescriptive package:** [`phased/README.md`](phased/README.md). |
| [**Extreme Programming (XP)**](xp.md) | Practices, technical excellence, pairing, CI. **Prescriptive package:** [`xp/README.md`](xp/README.md). |
| [**Agentic SDLC**](agentic-sdlc.md) | Cross-cutting: agents, review, identity, limits — not a replacement for the guides above. |
| [**Spec-driven development**](spec-driven-development.md) | Written intent leads implementation; docs↔code loop; agentic fit. **SDD I/O:** [`spec-driven/README.md`](spec-driven/README.md) (C1–C6 + P1–P6 tables & examples), templates [`templates/sdd/`](../templates/sdd/). Handbook: [`spec-driven.html`](../docs/spec-driven.html) + nested **SDD schema / Ceremonies / Process** pages. |

**Handbook (HTML):** [`docs/methodologies.html`](../docs/methodologies.html) (hub) and `docs/methodologies-*.html`; **spec-driven** is [`docs/spec-driven.html`](../docs/spec-driven.html). **Scrum/Kanban/phased/XP** subchapters (Foundation, Ceremonies, Process) are generated with tables + Mermaid via [`docs/build_methodology_chapters.py`](../docs/build_methodology_chapters.py); **Scrum — Roles** is hand-maintained in HTML.

**Maintainers:** curated external URLs, **executive summaries** (why each link matters here), and a quick `curl` check pattern — [`REFERENCE-LINKS.md`](REFERENCE-LINKS.md). Keep handbook [`methodologies-*.html`](../docs/methodologies.html) blurbs in sync when URLs or intent change.

**Project tracking (optional):** [`sdlc/TRACKING-FOUNDATION.md`](../../../sdlc/TRACKING-FOUNDATION.md) pattern in repos that add `sdlc/`.
