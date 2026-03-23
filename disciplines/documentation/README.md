# Documentation

Reusable, **project-agnostic** blueprint for **Documentation** — the discipline of creating, structuring, maintaining, and delivering effective documentation and content (technical, user-facing, product, process, and media) through audience analysis, information architecture, standards adoption, and continuous improvement.

Documentation answers **"how do we create, maintain, and deliver effective documentation and content?"** — a question that spans every SDLC phase (from requirements through operations) and every PDLC phase where knowledge must be captured, communicated, or published.

| Document | Purpose |
|----------|---------|
| [**DOCUMENTATION.md**](DOCUMENTATION.md) | Body of knowledge — principles, types taxonomy, standards, certifications, practices, tooling, competencies |
| [**DOC-SDLC-PDLC-BRIDGE.md**](DOC-SDLC-PDLC-BRIDGE.md) | How Documentation maps across SDLC phases A–F and PDLC phases P1–P6 — continuous through every phase |
| [**types/**](types/README.md) | Index of documentation and content types (technical, user-facing, process, product, content & media, governance) |
| [**standards/**](standards/README.md) | Index of documentation standards and frameworks (Diátaxis, docs-as-code, DITA, ISO/IEC/IEEE 26511–26515, style guides) |
| [**practices/**](practices/README.md) | Index of documentation practices (content strategy, information architecture, localization, accessibility, review, analytics) |
| [**templates/**](templates/README.md) | Reusable documentation templates (README, ADR, API doc, runbook, blog post, release notes, presentation, user guide) |

## Cross-cutting nature

Documentation is **not owned by a single family** of disciplines. It cuts across:

| Family / area | Typical documentation touchpoints |
|---------------|-----------------------------------|
| **Engineering** | API documentation, architecture decision records, developer guides, code documentation, runbooks, infrastructure docs, CI/CD pipeline docs |
| **Data** | Data dictionaries, schema docs, model cards, pipeline documentation, data lineage docs, experiment logs |
| **Product** | Product specs, user guides, feature docs, journey maps, knowledge bases, FAQs, onboarding content |
| **Governance** | Process documentation, project plans, status reports, retrospective records, policy documents |
| **Security** | Threat model docs, security policies, incident response playbooks, audit evidence documentation |
| **Compliance** | Privacy notices, accessibility statements, DPIA records, VPAT/ACR, regulatory filings, audit trails |

Canonical lifecycles: [`blueprints/sdlc/`](../../sdlc/README.md) (build and operate **right**) · [`blueprints/pdlc/`](../../pdlc/README.md) (build the **right** product in the **right** markets). Bridge concept and index: [`blueprints/BRIDGES.md`](../../BRIDGES.md).

## Relationship to other packages

| Package | How Documentation relates |
|---------|---------------------------|
| [`blueprints/disciplines/security/`](../security/README.md) | Security produces threat models, incident playbooks, and audit evidence — all documentation artifacts. Documentation provides standards for structuring, reviewing, and maintaining security docs. |
| [`blueprints/disciplines/compliance/`](../compliance/README.md) | Compliance requires extensive documentation (DPIAs, ROPA, accessibility statements, policy suites). Documentation discipline provides the methodology for creating, versioning, and evidencing these artifacts. |
| [`blueprints/sdlc/`](../../sdlc/README.md) | Every SDLC phase produces documentation artifacts — requirements, specs, ADRs, test plans, release notes. The SDLC documentation structure proposal defines **where** docs live; this discipline defines **how** to write them well. |
| [`blueprints/pdlc/`](../../pdlc/README.md) | PDLC phases generate discovery reports, validation learnings, strategy decks, launch content (blogs, landing pages), growth materials (tutorials, knowledge bases), and sunset notices. |
| [`blueprints/disciplines/engineering/software-architecture/`](../engineering/software-architecture/README.md) | Architecture documentation (C4, arc42, ADRs) is a first-class documentation type with its own standards and templates. |
| [`blueprints/disciplines/engineering/devops/`](../engineering/devops/README.md) | DevOps enables **docs-as-code** — versioned docs, CI/CD for documentation sites, automated API doc generation, linting, and link checking. |
| [`blueprints/disciplines/product/ux-design/`](../product/ux-design/README.md) | UX informs documentation information architecture, content design, accessibility, and user-facing content strategy. |
| [`blueprints/disciplines/product/marketing/`](../product/marketing/README.md) | Marketing produces blog posts, landing pages, newsletters, presentations, and SEO content — content types covered by this discipline. |
| [`blueprints/product/`](../../product/README.md) | Product-functional documentation IA — capabilities, journeys, features. This discipline provides the authoring methodology; the product package provides the structure. |
| [`blueprints/agents/`](../../agents/README.md) | Agents can automate documentation tasks — generating API docs, checking links, building doc sites, publishing content. |

## Scope

This package addresses **Documentation as a discipline** for digital products — not a single style guide or tool recommendation. It includes:

- **Technical documentation** — API docs (OpenAPI, AsyncAPI), system/infrastructure docs, developer guides, architecture docs (ADRs, C4, arc42), code documentation, SDK/library docs
- **User-facing documentation** — user guides, tutorials, how-to guides, FAQs, knowledge bases, release notes, changelogs, interactive documentation
- **Process documentation** — runbooks, SOPs, playbooks, post-mortems, onboarding guides, decision logs
- **Product documentation** — product specs, capability docs, journey maps, feature documentation, data dictionaries
- **Content and media** — websites, landing pages, blog posts, presentations, slide decks, podcasts, voiceovers, video scripts, newsletters, social media content
- **Governance and compliance documentation** — policy documents, audit evidence, compliance reports, accessibility statements, privacy notices
- **Standards and frameworks** — Diátaxis, docs-as-code, DITA, Information Mapping, ISO/IEC/IEEE 26511–26515, ASD-STE100, arc42
- **Certifications** — ITCQF, STC/CPTC, ISTC, tekom/tcworld
- **Practices** — content strategy, information architecture, style guides, localization/i18n, accessibility (WCAG for docs), documentation review, analytics, SEO, tooling

**Reference bodies of knowledge and authorities:** Write the Docs community, ITCQF (International Technical Communication Qualifications Foundation), STC (Society for Technical Communication), tekom (European Association for Technical Communication), ISO/IEC JTC 1/SC 7 (software lifecycle documentation standards), W3C WAI (accessibility in documentation), Google Developer Documentation Style Guide, Microsoft Writing Style Guide.

---

*Keep project-specific documentation in `docs/`, content plans in `docs/product/`, and documentation decisions in `docs/adr/`, not in this file.*
