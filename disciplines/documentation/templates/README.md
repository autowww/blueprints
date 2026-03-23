# Documentation templates (index)

**Purpose:** Reusable, **project-agnostic** templates for common documentation needs. Copy a template into your project's `docs/` directory and adapt it. Templates provide structure and prompts — fill in what applies, remove what doesn't.

**Audience:** Teams adopting [`blueprints/disciplines/documentation/`](../README.md). For the full body of knowledge (types, standards, practices), see **[`../DOCUMENTATION.md`](../DOCUMENTATION.md)**.

**Bridge:** [`../DOC-SDLC-PDLC-BRIDGE.md`](../DOC-SDLC-PDLC-BRIDGE.md) — where documentation work lands in PDLC and SDLC.

---

## Why templates matter

Templates reduce the **blank page problem** — instead of wondering what to write and how to structure it, teams start from a proven outline. They enforce **consistency** across documents of the same type, embed **best practices** from documentation standards (Diátaxis, ADR format, Keep a Changelog), and reduce the time from "we need docs" to "docs are published."

### How to use templates

1. **Choose** the template that matches your documentation need from the table below.
2. **Copy** the template file into your project's `docs/` directory (or appropriate subdirectory).
3. **Adapt** — fill in the sections that apply; remove sections that don't; add project-specific sections if needed.
4. **Review** — use your team's review workflow (PR-based if following docs-as-code).
5. **Maintain** — templates give you a starting structure; keep the content accurate as the project evolves.

---

## Template catalog

### Project and repository

| Template | File | Purpose | When to use | Related standard |
|----------|------|---------|-------------|-----------------|
| **README** | [`readme.template.md`](readme.template.md) | Project overview, quickstart, contributing, license | Every repository / project | — |
| **CONTRIBUTING guide** | [`contributing.template.md`](contributing.template.md) | How to contribute — setup, coding standards, PR process, CoC | Open-source or multi-team projects | — |

### Architecture and decisions

| Template | File | Purpose | When to use | Related standard |
|----------|------|---------|-------------|-----------------|
| **ADR (Architecture Decision Record)** | [`adr.template.md`](adr.template.md) | Record an architectural decision with context, options, decision, consequences | Every significant architectural choice | Michael Nygard's ADR format |
| **Architecture overview (arc42-lite)** | [`architecture-overview.template.md`](architecture-overview.template.md) | Lightweight architecture document — context, containers, key decisions, quality, risks | Projects needing structured architecture docs without full arc42 | arc42, C4 |

### API documentation

| Template | File | Purpose | When to use | Related standard |
|----------|------|---------|-------------|-----------------|
| **API documentation** | [`api-documentation.template.md`](api-documentation.template.md) | API overview, authentication, endpoints, errors, rate limits, versioning | Any project exposing an API (REST, GraphQL, gRPC) | OpenAPI, Diátaxis (reference) |

### Operations

| Template | File | Purpose | When to use | Related standard |
|----------|------|---------|-------------|-----------------|
| **Runbook / SOP** | [`runbook.template.md`](runbook.template.md) | Step-by-step operational procedure — prerequisites, steps, rollback, escalation | Every critical operational procedure | SRE practices |
| **Post-mortem / incident report** | [`postmortem.template.md`](postmortem.template.md) | Blameless incident analysis — timeline, impact, root cause, action items | After every significant incident | Google SRE post-mortem format |

### User-facing content

| Template | File | Purpose | When to use | Related standard |
|----------|------|---------|-------------|-----------------|
| **User guide** | [`user-guide.template.md`](user-guide.template.md) | Structured user documentation — overview, getting started, features, troubleshooting | Products with end users who need guidance | Diátaxis, Information Mapping |
| **Tutorial** | [`tutorial.template.md`](tutorial.template.md) | Learning-oriented walkthrough — prerequisites, step-by-step, what you learned | Teaching users a new skill or feature | Diátaxis (tutorial mode) |
| **How-to guide** | [`how-to-guide.template.md`](how-to-guide.template.md) | Task-oriented recipe — goal, prerequisites, steps, variations | Users who know what they want to achieve | Diátaxis (how-to mode) |

### Release and changelog

| Template | File | Purpose | When to use | Related standard |
|----------|------|---------|-------------|-----------------|
| **Release notes** | [`release-notes.template.md`](release-notes.template.md) | What changed, why, migration steps, known issues | Every release | Keep a Changelog |
| **Changelog** | [`changelog.template.md`](changelog.template.md) | Running log of all notable changes by version | Projects following semantic versioning | Keep a Changelog, SemVer |

### Content and media

| Template | File | Purpose | When to use | Related standard |
|----------|------|---------|-------------|-----------------|
| **Blog post** | [`blog-post.template.md`](blog-post.template.md) | Structured blog post — hook, body, conclusion, CTA, metadata | Feature announcements, thought leadership, tutorials-as-posts | SEO best practices |
| **Presentation outline** | [`presentation-outline.template.md`](presentation-outline.template.md) | Slide deck structure — title, agenda, narrative arc, key messages, Q&A | Conference talks, internal presentations, pitch decks | Visual communication principles |
| **Podcast episode plan** | [`podcast-episode.template.md`](podcast-episode.template.md) | Episode structure — topic, guests, outline, questions, show notes | Podcast production | — |
| **Video script** | [`video-script.template.md`](video-script.template.md) | Script with visual/audio columns — intro, segments, outro, CTA | Product demos, tutorials, explainer videos | Accessibility (captions) |
| **Newsletter issue** | [`newsletter.template.md`](newsletter.template.md) | Newsletter structure — header, sections, links, CTA, footer | Regular subscriber communications | CAN-SPAM, GDPR consent |

### Governance

| Template | File | Purpose | When to use | Related standard |
|----------|------|---------|-------------|-----------------|
| **Policy document** | [`policy.template.md`](policy.template.md) | Formal policy — purpose, scope, policy statements, responsibilities, review cycle | Organizational or project policies | ISO 27001 |
| **Data dictionary** | [`data-dictionary.template.md`](data-dictionary.template.md) | Entity/field definitions — name, type, description, constraints, owner | Projects with data models that need documentation | DMBOK |

---

## Template conventions

All templates follow these conventions:

- **Markdown format** — compatible with GitHub rendering, static site generators, and docs-as-code workflows
- **Placeholder markers** — `{PLACEHOLDER}` for values you must fill in; `<!-- Optional: ... -->` for sections you can remove
- **Frontmatter** — optional YAML frontmatter for metadata (title, date, author, tags)
- **Relative links** — internal cross-references use relative paths
- **No binary content** — text only; images referenced via paths or URLs

---

**Core knowledge:** [`DOCUMENTATION.md`](../DOCUMENTATION.md) — principles, types, standards, certifications, tooling, competencies.

**Bridge:** [`DOC-SDLC-PDLC-BRIDGE.md`](../DOC-SDLC-PDLC-BRIDGE.md) — how Documentation maps to delivery and product lifecycles.

---

*Keep project-specific documentation in `docs/`, content plans in `docs/product/`, and documentation decisions in `docs/adr/`, not in this file.*
