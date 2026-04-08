---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# External reference URLs (methodology guides)

Curated list of **https** targets cited in [`blueprints/sdlc/methodologies/`](README.md) and mirrored in [`docs/methodologies-*.html`](../docs/methodologies.html) and in generated **Process & flows** pages (`methodologies-*-process.html`). When you change a URL in Markdown, update the matching handbook page’s “Authoritative sources” / “Authoritative sources & further reading” section (and re-run `build_methodology_chapters.py` for generated HTML).

Each row includes an **executive summary**: what the link is and **why this blueprint points to it**, so readers can decide whether to open it.

| Topic | URL | Executive summary (why it’s linked here) |
|-------|-----|----------------------------------------|
| Agile Manifesto | https://agilemanifesto.org/ | The original **four values** (2001); defines what “Agile” means before you pick Scrum, Kanban, or XP. |
| Twelve Principles | https://agilemanifesto.org/principles.html | Turns the manifesto into **concrete principles** (delivery, feedback, sustainability)—useful for aligning SDLC phases with Agile intent. |
| Agile Alliance (home) | https://www.agilealliance.org/ | Nonprofit **community hub**: articles, events, and pointers—neutral background, not a replacement for your process docs. |
| Agile Alliance — Subway map | https://www.agilealliance.org/subway | **Visual map** of Agile-related practices; good orientation, not a prescribed workflow. |
| Agile Alliance — Agile glossary | https://www.agilealliance.org/agile101/agile-glossary/ | **Searchable terms** (e.g. Scrum, Kanban, XP)—shared vocabulary for teams using this blueprint. |
| Scrum Guide | https://scrumguides.org/scrum-guide.html | **Official** definition of Scrum (accountabilities, events, artifacts)—the authority for mapping Phases A–F to Scrum. |
| Scrum.org — What is Scrum? | https://www.scrum.org/resources/what-is-scrum | Training org’s **intro and learning context**; complements the Guide, not a second standard. |
| Scrum.org — Kanban Guide for Scrum Teams | https://www.scrum.org/resources/kanban-guide-scrum-teams | How **Kanban flow** practices integrate **with** Scrum—for teams blending both under one cadence. |
| Agile Alliance — Kanban (glossary) | https://www.agilealliance.org/glossary/kanban/ | Short **definition** and manufacturing roots—quick grounding before reading Kanban guides. |
| Kanban University — The Kanban Guide | https://kanban.university/kanban-guide | **Current guide text** for the Kanban method (practices, evolution of the Guide). |
| ProKanban.org | https://prokanban.org/ | **Professional Kanban** community—training and certification paths; optional depth. |
| Agile Alliance — Scrum (glossary) | https://www.agilealliance.org/glossary/scrum/ | Short **Scrum** entry plus community context—handy glossary alongside the Guide. |
| ISO/IEC/IEEE 12207 (catalogue) | https://www.iso.org/standard/63712.html | **International standard** for software life-cycle processes—formal anchor for phased/regulated delivery (catalogue entry; full text is paid/licensed). |
| PMI — Standards & guides | https://www.pmi.org/standards | **PMBOK** and related standards—common vocabulary for phases, knowledge areas, and governance when formalizing gates and project framing (complements ISO 12207). *Note:* some environments get **HTTP 403** to `pmi.org` from automated `curl`; try a normal browser. |
| Wikipedia — PMBOK | https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge | **Overview** of PMI’s Project Management Body of Knowledge—phases and knowledge areas in encyclopedia form when licensed PMBOK text is unavailable. |
| Wikipedia — Waterfall model | https://en.wikipedia.org/wiki/Waterfall_model | **Informal** history and diagram of sequential phases—context for phased delivery, not a standard. |
| Wikipedia — Software development process (Waterfall section) | https://en.wikipedia.org/wiki/Software_development_process#Waterfall_development | **Waterfall as one lifecycle** among many—helps compare with iterative approaches. |
| Wikipedia — Agile software development | https://en.wikipedia.org/wiki/Agile_software_development | **Contrast** between iterative Agile and plan-driven lifecycles—useful when arguing hybrids (phased gates + iterative build). |
| Wikipedia — Extreme programming | https://en.wikipedia.org/wiki/Extreme_programming | **Stable overview** of XP practices and history—entry point before deeper books or practitioner sites. |
| Ron Jeffries — XP | https://ronjeffries.com/xprog/ | **Practitioner** perspective on XP—stories and guidance from a signatory-level voice. |
| Martin Fowler — XP (Bliki) | https://martinfowler.com/bliki/ExtremeProgramming.html | Short **expert summary** of XP on a widely cited blog—quick read. |
| Wiki.c2 — Extreme Programming Roadmap | https://wiki.c2.com/?ExtremeProgrammingRoadmap | **Classic wiki** index of XP topics—dated but historically influential. |
| Wikipedia — Lean software development | https://en.wikipedia.org/wiki/Lean_software_development | **Stable overview** of the seven Poppendieck principles, history, and relationship to manufacturing Lean—entry point before the books. |
| Wikipedia — Toyota Production System | https://en.wikipedia.org/wiki/Toyota_Production_System | **Manufacturing roots** of Lean—understanding TPS clarifies why "waste" and "pull" matter in software. |
| Agile Alliance — Lean software development | https://www.agilealliance.org/glossary/lean-software-development/ | **Short definition** in the Agile glossary—shared vocabulary for Lean. |
| Lean Enterprise Institute | https://www.lean.org/ | **Practitioner community** for Lean thinking—manufacturing and beyond; optional depth. |
| Wikipedia — Spiral model | https://en.wikipedia.org/wiki/Spiral_model | **Stable overview** of Boehm's risk-driven model—quadrants, anchor-point milestones, history. |
| Wikipedia — Barry Boehm | https://en.wikipedia.org/wiki/Barry_Boehm | **Author** biography—context for the Spiral Model's origins in defense/aerospace. |
| Wikipedia — V-model (software development) | https://en.wikipedia.org/wiki/V-model_(software_development) | **Stable overview** of the V-Model—phases, traceability pairing, and comparison with Waterfall. |
| Wikipedia — Verification and validation | https://en.wikipedia.org/wiki/Verification_and_validation | **Foundational** V&V concepts—"building the right product" vs "building the product right." |
| ISO 26262 (catalogue) | https://www.iso.org/standard/68383.html | **Automotive** functional safety standard mandating V-Model-style development (catalogue; full text licensed). |
| Wikipedia — DevOps | https://en.wikipedia.org/wiki/DevOps | **Stable overview** of DevOps history, practices, and culture—entry point before vendor-specific guidance. |
| Wikipedia — CI/CD | https://en.wikipedia.org/wiki/CI/CD | **Continuous integration and delivery**—the technical backbone of DevOps pipelines. |
| DORA — DevOps Research and Assessment | https://dora.dev/ | **Research-backed** DevOps metrics and capabilities; the four key metrics (deployment frequency, lead time, CFR, MTTR). |
| Google SRE Book | https://sre.google/sre-book/table-of-contents/ | **Free online** SRE practices and principles—companion to DevOps methodology. |
| Wikipedia — Feature-driven development | https://en.wikipedia.org/wiki/Feature-driven_development | **Stable overview** of FDD's five activities, roles, and feature-centric approach. |
| Agile Alliance — FDD | https://www.agilealliance.org/glossary/fdd/ | **Short definition** of Feature-Driven Development in the Agile glossary. |
| Wikipedia — Crystal Clear | https://en.wikipedia.org/wiki/Crystal_Clear_(software_development) | **Stable overview** of the most common Crystal variant—properties and scaling. |
| Wikipedia — DSDM | https://en.wikipedia.org/wiki/Dynamic_systems_development_method | **Stable overview** of DSDM phases, principles, and MoSCoW prioritization. |
| Agile Business Consortium | https://www.agilebusiness.org/ | **Official** DSDM body—framework documentation, training, certification. |
| Shape Up (free book) | https://basecamp.com/shapeup | **Official** Shape Up book by Ryan Singer—complete methodology description, free online. |
| PMI — Disciplined Agile | https://www.pmi.org/disciplined-agile | **Official** DA body of knowledge—goal diagrams, lifecycles, process options (PMI-owned). |
| Wikipedia — Disciplined agile delivery | https://en.wikipedia.org/wiki/Disciplined_agile_delivery | **Stable overview** of DA's approach, lifecycles, and relationship to other Agile methods. |
| Wikipedia — Behavior-driven development | https://en.wikipedia.org/wiki/Behavior-driven_development | **Stable overview** of BDD—Given-When-Then, tools, relationship to TDD. |
| Dan North — Introducing BDD | https://dannorth.net/introducing-bdd/ | **Original** BDD article by its creator—motivation and initial formulation. |
| Cucumber — BDD overview | https://cucumber.io/docs/bdd/ | **Practitioner** guide to BDD with a popular tool—process and anti-patterns. |
| Wikipedia — Rapid application development | https://en.wikipedia.org/wiki/Rapid_application_development | **Stable overview** of RAD—phases, tools, prototyping-centric approach. |
| OWASP — Top 10 for LLM Applications | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | **Security risks** when LLMs touch design, code, or data in the SDLC—essential for agentic / AI-assisted workflows. |

## Quick verification (maintainers)

From a shell, expect HTTP **200** (some sites return **301** then 200 when following redirects):

```bash
urls=(
  https://agilemanifesto.org/
  https://www.scrum.org/resources/what-is-scrum
  https://kanban.university/kanban-guide
  https://owasp.org/www-project-top-10-for-large-language-model-applications/
)
for u in "${urls[@]}"; do
  printf '%s ' "$(curl -sS -o /dev/null -w '%{http_code}' -L --max-time 15 "$u")"
  echo "$u"
done
```

Expand the array with any new links before merging doc changes.
