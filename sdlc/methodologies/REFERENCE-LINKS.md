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
