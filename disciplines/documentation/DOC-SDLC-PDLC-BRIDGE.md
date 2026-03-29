# Documentation ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **Documentation** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **Documentation** — "How do we **create, maintain, and deliver** effective documentation and content?"

Documentation is **continuous** across all lifecycle phases — every phase produces artifacts, every phase consumes knowledge that documentation captures. Unlike compliance (front-loaded in P3) or security (emphasis on shift-left), documentation has a **uniform presence** with **peaks** at launch (P4) and growth (P5) for user-facing and media content.

**Canonical sources:** [`DOCUMENTATION.md`](DOCUMENTATION.md) (this package) · [`PDLC.md`](../../pdlc/PDLC.md) · [`SDLC.md`](../../sdlc/SDLC.md) · [`blueprints/BRIDGES.md`](../../BRIDGES.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists |
| [Comparison table](#comparison-table) | Documentation vs Security vs Compliance vs SDLC vs PDLC |
| [When documentation is missing](#when-documentation-is-missing) | Consequences when documentation is absent |
| [Documentation across the lifecycle](#documentation-across-the-lifecycle) | P1–P6 and A–F mapping |
| [Role mapping](#role-mapping) | Ownership and collaboration |
| [Artifact flow](#artifact-flow) | Handoffs between Documentation and other disciplines |
| [Calibration](#calibration) | By project type and audience |
| [Anti-patterns](#anti-patterns) | Common documentation failures |
| [Worked example](#worked-example) | Documentation plan for a developer platform launch |
| [Related reading](#related-reading) | Package and sibling docs |

---

## Comparison table

| Dimension | Documentation | Security | Compliance | SDLC | PDLC |
|-----------|--------------|----------|------------|------|------|
| **Core question** | How do we create, maintain, and deliver effective documentation and content? | Is the product safe from unauthorized access, breaches, and attacks? | Does the product meet regulatory and legal obligations? | How do we build this correctly? | Should we build this; does it create the right outcomes? |
| **Scope** | All documentation types (technical, user-facing, process, product, media, governance), standards, practices, tooling | Threat modeling, vuln management, crypto, IAM, security testing, incident response | Privacy, accessibility, sector rules, AI governance, certifications, vendor assurance | Requirements → design → implementation → verification → release (A–F) | Problem discovery → validation → strategy → launch → growth → sunset (P1–P6) |
| **Primary owner** | Technical writers, content strategists, developer advocates; every team member contributes | Security / AppSec; CISO | Legal/privacy/compliance leads; DPO | Delivery team | Product leadership |
| **Timeline** | Continuous — documentation evolves with the product, codebase, and audience | Continuous — threats evolve | Continuous — laws evolve | Iteration / release cadence | Product lifetime |
| **Success metric** | Discoverability, accuracy, freshness, user satisfaction, reduced support tickets, time-to-productivity | Vuln SLAs, incident metrics, pentest outcomes | Audit results, regulatory inquiries, certification maintenance | Quality, velocity, defect escape | Adoption, revenue, outcome KPIs |
| **Key artifacts** | User guides, API docs, tutorials, ADRs, runbooks, blog posts, presentations, knowledge bases | Threat models, pentest reports, SBOM | ROPA, DPIAs, VPAT/ACR, evidence packs | Specs, code, tests, release notes | Strategy, experiments, roadmap |
| **Risk focus** | Knowledge loss, onboarding friction, support overhead, developer experience, adoption barriers | Adversarial exploitation, CIA | Legal/regulatory exposure, fines | Technical and delivery risk | Market and outcome risk |
| **Failure mode** | Tribal knowledge, stale docs, user frustration, slow onboarding, duplicated effort | Breach, ransomware | Fines, stop-processing orders | Late or brittle delivery | Right execution of the wrong thing |

---

## When documentation is missing

| Scenario | What happens |
|----------|--------------|
| **Documentation without SDLC** | Docs exist but **drift from reality** — descriptions don't match current code, APIs, or deployments. |
| **Documentation without PDLC** | Detailed docs for a product **nobody uses** — effort spent documenting features that should have been validated first. |
| **SDLC without Documentation** | Fast shipping but **knowledge silos** — new team members struggle, support tickets spike, architectural decisions are forgotten. |
| **PDLC without Documentation** | Product strategy exists but **nothing is written down** for users, developers, or stakeholders — adoption suffers. |
| **Security without Documentation** | Secure system that **nobody can operate safely** — missing runbooks, unclear incident procedures, undocumented security controls. |
| **Compliance without Documentation** | Controls implemented but **no evidence trail** — auditors cannot verify, rights requests fail from lack of process docs. |
| **All lenses practiced** | Product is well-understood, discoverable, operable, auditable, and adoptable. Knowledge survives team changes. |

---

## Documentation across the lifecycle

| Phase | Documentation role | Key activities | Outputs |
|-------|-------------------|----------------|---------|
| **P1 Discover** | **Knowledge capturer** | Document problem space research, user interviews, competitive analysis; capture discovery insights | Discovery reports, interview summaries, problem statements |
| **P2 Validate** | **Experiment recorder** | Document hypotheses, experiment designs, validation results, pivot decisions | Experiment logs, validation learnings, decision records |
| **P3 Plan & Commit** | **Strategy communicator** | Create strategy decks, roadmap docs, market briefs, white papers; plan documentation needs for target audience | Strategy presentations, roadmap docs, documentation plan, content strategy |
| **A Discover** | **Requirements documenter** | Document user stories, acceptance criteria, non-functional requirements; draft data dictionaries | Requirements docs, user stories, NFR catalog |
| **B Specify** | **Specification author** | Write detailed specs, create wireframe annotations, document data models and API contracts | Specifications, API contracts (OpenAPI/AsyncAPI), data dictionaries |
| **C Design** | **Architecture documenter** | Create/update architecture docs (C4, arc42), write ADRs, document design decisions and trade-offs | ADRs, architecture diagrams, design docs |
| **D Build** | **Developer documenter** | Write developer guides, code docs, inline documentation for non-obvious logic; draft API reference docs; create runbooks | Developer guides, API reference, code docs, draft runbooks |
| **E Verify** | **Test documenter** | Document test plans, test results, known issues; review documentation accuracy against implementation | Test documentation, known issues, doc review reports |
| **F Release** | **Release communicator** | Write release notes, changelogs; finalize user-facing docs; publish API docs; update knowledge base | Release notes, changelogs, published API docs, updated user guides |
| **P4 Launch** | **Launch content creator** | Create blog posts, landing pages, tutorials, onboarding guides, presentations, demo videos, press materials | Blog posts, landing pages, tutorials, presentations, video scripts, voiceovers |
| **P5 Grow** | **Content sustainer** | Maintain and expand knowledge base, write advanced tutorials, produce podcasts/newsletters, update docs for new features, run freshness audits | Knowledge base articles, advanced how-to guides, podcasts, newsletters, updated docs |
| **P6 Sunset** | **Archive curator** | Document migration paths, write sunset notices, archive documentation, maintain minimal support docs | Migration guides, sunset notices, archived docs |

---

## Role mapping

| Phase(s) | Documentation stance | PDLC accountability | SDLC accountability | Typical partners |
|----------|---------------------|---------------------|---------------------|------------------|
| **P1–P2** | Capture and share learnings | PM, discovery | Spikes feeding A | UX researcher, BA |
| **P3** | Plan content strategy | PM, strategy | Owner (feasibility) | Marketing, content strategist |
| **A–B** | Document requirements and specs | PM prioritization | Owner, BA | Architects, developers |
| **C** | Architecture documentation | Architecture alignment | Architect, implementer | Security, data engineering |
| **D** | Developer and API docs | — | Implementer, tech writer | Developer advocates |
| **E** | Test documentation and doc review | — | QA, tech writer | Subject-matter experts |
| **F** | Release content | GTM coordination | Owner go/no-go | Marketing, support |
| **P4** | Launch content production | PM, marketing | — | Content creators, designers, video/audio producers |
| **P5** | Ongoing content maintenance | PM, support, analytics | SRE, on-call | Community, support team, content creators |
| **P6** | Archive and migrate | PM, legal | Implementer | Records management |

---

## Artifact flow

### PDLC / SDLC → Documentation (inputs)

| Source | Documentation usage |
|--------|---------------------|
| User research and personas (**P1–P2**) | Define documentation audiences, reading levels, preferred formats |
| Product strategy and roadmap (**P3**) | Scope documentation plan, content calendar, localization targets |
| Requirements and specs (**A–B**) | Source material for user guides, feature docs, API docs |
| Architecture decisions (**C**) | ADRs, system diagrams, component docs |
| Code and tests (**D–E**) | API reference generation, developer guides, test documentation |
| Release artifacts (**F**) | Release notes, changelogs, version-specific docs |

### Documentation → SDLC (outputs)

| Documentation artifact | SDLC usage |
|------------------------|------------|
| API documentation (**D–F**) | Developer onboarding, integration testing, external adoption |
| Runbooks (**D, P5**) | Operational procedures for SRE and on-call |
| Architecture docs (**C**) | Design review input, onboarding, impact analysis |
| Developer guides (**D**) | New contributor onboarding, code review context |

### Documentation → PDLC (outputs)

| Documentation artifact | PDLC usage |
|------------------------|------------|
| Tutorials and user guides (**P4–P5**) | User adoption, activation, retention |
| Blog posts and landing pages (**P4–P5**) | Acquisition, awareness, SEO |
| Presentations and white papers (**P3–P5**) | Enterprise sales, partnerships, conferences |
| Knowledge base and FAQs (**P5**) | Support deflection, self-service |
| Podcasts, videos, newsletters (**P5**) | Community building, thought leadership |

### Documentation ↔ Security / Compliance (shared boundary)

| Shared topic | Documentation emphasis | Security / Compliance emphasis |
|--------------|----------------------|-------------------------------|
| Incident playbooks | Clear, tested procedures that anyone on-call can follow | Containment effectiveness, legal notification timelines |
| Audit evidence | Well-structured, discoverable documentation that proves controls exist | Control design and operating effectiveness |
| Privacy notices | Clear, accurate language that users understand | Legal conformance with GDPR/CCPA requirements |
| Accessibility statements | Honest conformance declaration with remediation roadmap | WCAG compliance level, procurement qualification |

---

## Calibration

### By project type

| Context | Documentation emphasis |
|---------|----------------------|
| **Internal tool** | Developer guide, runbooks, ADRs — minimal user-facing docs |
| **Developer platform / API** | API reference, tutorials, SDKs, interactive docs, changelog — documentation is the product |
| **Consumer SaaS** | User guides, onboarding flows, knowledge base, blog, landing pages, video tutorials |
| **Enterprise B2B** | White papers, security/compliance docs, admin guides, API docs, integration guides |
| **Open source** | README, contributing guide, code of conduct, tutorials, API reference, community content |
| **Regulated / safety-critical** | Formal documentation per ISO/IEC standards, traceability matrices, audit evidence |

### By team maturity

| Maturity | Documentation emphasis |
|----------|----------------------|
| **Starting out** | README, basic architecture doc, one key runbook — just enough to not lose knowledge |
| **Growing** | Docs-as-code pipeline, Diátaxis structure, API docs, content calendar for blog/updates |
| **Mature** | Full content strategy, localization, analytics-driven improvement, multi-format content (video, podcast), ITCQF-level quality |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Write-once documentation** | Docs created at launch and **never updated** — accuracy degrades with every release | Freshness audits, ownership model, docs-in-PR culture |
| **Tribal knowledge** | Critical knowledge **lives only in people's heads** — bus factor of one | Document decision rationale (ADRs), runbooks, onboarding guides |
| **Documentation dump** | Massive doc sites with **no information architecture** — users can't find what they need | Apply Diátaxis, invest in navigation, search, and IA |
| **Copy-paste duplication** | Same content in multiple places — **diverges** over time | Single source of truth, cross-references, content reuse (DITA conref or includes) |
| **Docs as afterthought** | Documentation planned **after** the feature ships — context is lost, shortcuts are taken | Include docs in Definition of Done, allocate time in sprints |
| **Screenshot-heavy docs** | Over-reliance on screenshots that **break** with every UI change | Prefer text descriptions; use screenshots sparingly; automate screenshot capture if needed |
| **Jargon overload** | Documentation full of **unexplained acronyms** and insider terminology | Glossary, plain language, audience-appropriate vocabulary |
| **No feedback loop** | Documentation published but **never measured** — no idea if it helps users | Analytics, feedback widgets, support ticket analysis |

---

## Worked example

**Scenario:** Launching a **developer platform** with a REST API, SDKs (Python, Node.js), and a web dashboard for **global developers**.

| Step | Lifecycle | What happens |
|------|-----------|--------------|
| 1 | **P3** | Content strategist scopes documentation: API reference, 3 tutorials, SDK guides, architecture overview, blog series. Localization planned for EN, ES, DE. Documentation site tooling selected (Docusaurus + OpenAPI). |
| 2 | **A** | Requirements include "developer can integrate in < 30 min" — implies quickstart tutorial, clear auth docs, copy-pasteable examples. |
| 3 | **B** | API contract (OpenAPI spec) finalized; spec becomes single source for generated API reference. Data dictionary documents all entities. |
| 4 | **C** | Architecture documented using C4 (context + container diagrams); ADR for API versioning strategy; ADR for webhook delivery guarantees. |
| 5 | **D** | API reference auto-generated from OpenAPI spec in CI. Developer writes quickstart tutorial, auth guide, and SDK getting-started for Python and Node.js. Runbook for API incident response drafted. |
| 6 | **E** | Tech writer reviews all docs for accuracy against implementation. Automated link checking and Vale linting in CI. Usability test: 3 external developers attempt quickstart — friction points fixed. |
| 7 | **F** | Changelog published. API docs versioned (v1). User-facing docs deployed to docs site. SDK docs published to package registries. |
| 8 | **P4** | Launch blog post published. Landing page live. "Getting started in 5 minutes" video produced with voiceover. Presentation deck for DevRel conference. Newsletter announcement to waitlist. |
| 9 | **P5** | Knowledge base grows with how-to guides based on support tickets. Monthly blog cadence. Podcast episode interviewing early adopters. Analytics show quickstart has 40% drop-off at step 3 — rewritten. Spanish and German translations shipped. |
| 10 | **P6** | If API v1 sunset: migration guide from v1 → v2 published 6 months before deprecation. Blog post explaining timeline. Sunset notice in dashboard. v1 docs archived but remain accessible. |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`DOCUMENTATION.md`](DOCUMENTATION.md) | Principles, types, standards, certifications, practices, tooling, competencies |
| [`README.md`](README.md) | Package overview and cross-family relationships |
| [`types/README.md`](types/README.md) | Documentation and content type index |
| [`standards/README.md`](standards/README.md) | Standards and frameworks index |
| [`practices/README.md`](practices/README.md) | Practices index |
| [`templates/README.md`](templates/README.md) | Reusable templates index |
| [`../security/SEC-SDLC-PDLC-BRIDGE.md`](../security/SEC-SDLC-PDLC-BRIDGE.md) | Security lifecycle mapping |
| [`../compliance/COMP-SDLC-PDLC-BRIDGE.md`](../compliance/COMP-SDLC-PDLC-BRIDGE.md) | Compliance lifecycle mapping |
| [`SDLC.md`](../../sdlc/SDLC.md) | Phases A–F |
| [`PDLC.md`](../../pdlc/PDLC.md) | Phases P1–P6 |

---

*Keep project-specific documentation in `docs/`, content plans in `docs/product/`, and documentation decisions in `docs/adr/`, not in this file.*
