# Documentation body of knowledge

This document maps the core concerns of **Documentation** for digital products — types, standards, certifications, practices, tooling, and competencies — to the blueprint ecosystem.

**How documentation relates to PDLC and SDLC:** Documentation is **continuous** across all lifecycle phases — every phase produces and consumes documentation artifacts. See [`DOC-SDLC-PDLC-BRIDGE.md`](DOC-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Type guides:** The [`types/`](types/README.md) index lists documentation and content type deep dives as they are added to this package.

**Standards and frameworks:** The [`standards/`](standards/README.md) index covers Diátaxis, docs-as-code, DITA, ISO/IEC/IEEE series, and related methodologies.

**Practices:** The [`practices/`](practices/README.md) index covers content strategy, information architecture, localization, accessibility, review, analytics, and tooling.

**Templates:** The [`templates/`](templates/README.md) index provides reusable starting points for common documentation needs.

---

## 1. Documentation principles

| Principle | Description |
|-----------|-------------|
| **Audience-first** | Every document has a defined audience. Structure, depth, vocabulary, and format serve that audience — not the author's convenience. |
| **Docs-as-code** | Documentation lives in version control alongside code, follows the same review workflows (PRs, linting, CI), and is built/deployed through pipelines. |
| **Single source of truth** | Each concept is owned by one canonical document. Other documents cross-reference — they do not duplicate. |
| **Just enough** | Write what is needed, when it is needed. Over-documentation creates maintenance debt; under-documentation creates knowledge gaps. Proportionality matters. |
| **Continuous improvement** | Documentation is never "done." Feedback loops (analytics, user input, stale content audits) drive iterative refinement. |
| **Accessibility** | Documentation must be accessible to all audiences — consider screen readers, color contrast, alternative text, plain language, and multilingual needs. |
| **Discoverability** | Good documentation is useless if nobody can find it. Information architecture, search, navigation, and linking strategy are first-class concerns. |
| **Traceability** | Documentation artifacts trace to lifecycle phases, requirements, and decisions — enabling audits, onboarding, and change impact analysis. |

---

## 2. Documentation types taxonomy

### 2.1 Technical documentation

| Type | Purpose | Typical audience | Lifecycle phase |
|------|---------|-----------------|-----------------|
| **API documentation** | Describe endpoints, parameters, responses, authentication, errors | Developers (internal and external) | D Build, F Release |
| **System / infrastructure docs** | Describe topology, deployment, configuration, dependencies | Engineers, SREs, DevOps | C Design, D Build |
| **Developer guides** | Explain how to set up, build, test, and contribute to a codebase | Developers, new team members | D Build (ongoing) |
| **Architecture documentation** | Capture system structure, quality attributes, trade-offs, decisions (ADRs, C4 diagrams, arc42) | Architects, senior engineers, reviewers | C Design |
| **Code documentation** | Inline comments, docstrings, type annotations for non-obvious logic | Developers maintaining the code | D Build |
| **SDK / library documentation** | Usage guides, examples, migration guides for libraries | External/internal consumers | D Build, F Release |

### 2.2 User-facing documentation

| Type | Purpose | Typical audience | Lifecycle phase |
|------|---------|-----------------|-----------------|
| **User guides** | Step-by-step instructions for product features | End users | P4 Launch, P5 Grow |
| **Tutorials** | Learning-oriented walkthroughs for new users | Beginners | P4 Launch, P5 Grow |
| **How-to guides** | Goal-oriented recipes for specific tasks | Experienced users | P5 Grow |
| **FAQs** | Answers to common questions | All users | P4 Launch, P5 Grow |
| **Knowledge bases** | Searchable collections of articles, guides, troubleshooting | All users, support teams | P5 Grow |
| **Release notes / changelogs** | Communicate what changed and why | Users, stakeholders | F Release |
| **Interactive documentation** | Sandboxes, playgrounds, live examples | Developers, evaluators | P4 Launch, P5 Grow |

### 2.3 Process documentation

| Type | Purpose | Typical audience | Lifecycle phase |
|------|---------|-----------------|-----------------|
| **Runbooks** | Step-by-step operational procedures for incidents or tasks | SREs, on-call engineers | D Build, P5 Grow |
| **SOPs (Standard Operating Procedures)** | Formalized repeatable processes | Operations, compliance | All phases |
| **Playbooks** | Decision-oriented guides for complex scenarios (incident response, launch) | Cross-functional teams | P4 Launch, P5 Grow |
| **Post-mortems / incident reports** | Root cause analysis and improvement actions | Engineering, management | P5 Grow |
| **Onboarding guides** | Help new team members become productive | New hires | Ongoing |
| **Decision logs** | Record decisions with context, alternatives, and rationale | Team leads, architects | A–F |

### 2.4 Product documentation

| Type | Purpose | Typical audience | Lifecycle phase |
|------|---------|-----------------|-----------------|
| **Product specifications** | Define what the product does — capabilities, rules, constraints | Product trio, engineering | A Discover, B Specify |
| **Feature documentation** | Detailed descriptions of individual features | Users, support, sales | P4 Launch |
| **Journey maps** | Document user flows through the product | UX, product, engineering | P1 Discover, B Specify |
| **Data dictionaries** | Define data entities, fields, types, relationships | Data engineers, analysts, developers | B Specify, C Design |
| **Capability docs** | High-level descriptions of product capabilities and boundaries | Stakeholders, sales | P3 Plan & Commit |

### 2.5 Content and media

| Type | Purpose | Typical audience | Lifecycle phase |
|------|---------|-----------------|-----------------|
| **Websites / landing pages** | Communicate product value, drive conversion | Prospects, users | P4 Launch, P5 Grow |
| **Blog posts** | Share knowledge, announce features, build thought leadership | Community, users, prospects | P4 Launch, P5 Grow |
| **Presentations / slide decks** | Communicate ideas in meetings, conferences, pitches | Stakeholders, conference attendees | All phases |
| **Podcasts / audio content** | Deliver knowledge and stories in audio format | Community, users | P5 Grow |
| **Voiceovers / narration** | Audio accompaniment for videos, tutorials, product tours | Users, learners | P4 Launch, P5 Grow |
| **Video scripts** | Structured scripts for product demos, tutorials, explainers | Users, prospects | P4 Launch, P5 Grow |
| **Newsletters** | Regular updates to subscribers — features, tips, news | Users, community | P5 Grow |
| **Social media content** | Short-form content for engagement and awareness | Community, prospects | P4 Launch, P5 Grow |
| **White papers / case studies** | In-depth analysis or customer success stories for credibility | Decision-makers, enterprise buyers | P3 Plan & Commit, P5 Grow |

### 2.6 Governance and compliance documentation

| Type | Purpose | Typical audience | Lifecycle phase |
|------|---------|-----------------|-----------------|
| **Policy documents** | Formalize rules, standards, and expectations | All teams, auditors | All phases |
| **Audit evidence** | Prove that controls are designed and operating effectively | Auditors, compliance | E Verify, P5 Grow |
| **Compliance reports** | Document conformance status (SOC 2 reports, VPAT/ACR) | Customers, auditors, regulators | F Release, P5 Grow |
| **Privacy notices** | Inform users about data practices | Users, regulators | P4 Launch |
| **Accessibility statements** | Declare accessibility conformance and known limitations | Users, procurement | P4 Launch |
| **Risk registers** | Track identified risks, mitigations, and owners | Management, auditors | All phases |

---

## 3. Standards and frameworks

### 3.1 Diátaxis

A systematic framework for organizing documentation around **four modes of documentation**, each serving a different user need:

| Mode | User need | Orientation | Form |
|------|-----------|-------------|------|
| **Tutorials** | Learning | Learning-oriented | Lessons that take the reader through a series of steps |
| **How-to guides** | Goals | Task-oriented | Directions that guide the reader through a problem |
| **Reference** | Information | Information-oriented | Technical descriptions of the machinery |
| **Explanation** | Understanding | Understanding-oriented | Discursive clarification and discussion |

Diátaxis avoids mixing these modes: a tutorial should not become a reference; a how-to guide should not explain theory. Each mode has its own writing style and structure.

### 3.2 Docs-as-code

Treat documentation with the same rigor as source code:

| Practice | Description |
|----------|-------------|
| **Version control** | Docs live in Git alongside code — branching, history, blame, diffs |
| **Plain text formats** | Markdown, AsciiDoc, reStructuredText — diffable, tooling-friendly |
| **Review workflows** | Pull requests with doc reviews; technical accuracy + writing quality |
| **CI/CD for docs** | Automated builds, link checking, spell checking, style linting, deployment |
| **Static site generators** | MkDocs, Docusaurus, Hugo, Sphinx, Jekyll — build doc sites from source |
| **API doc generation** | OpenAPI/Swagger, AsyncAPI, TypeDoc, Javadoc, Doxygen — generate from code/specs |

### 3.3 DITA (Darwin Information Typing Architecture)

OASIS standard for modular, reusable technical content:

| Concept | Description |
|---------|-------------|
| **Topic-based authoring** | Content organized as self-contained topics (concept, task, reference) |
| **Content reuse** | Conref/keyref mechanisms allow single-source content used in multiple outputs |
| **Specialization** | Extend base topic types for domain-specific needs without breaking interoperability |
| **Output formats** | Single source → PDF, HTML, EPUB, help systems via DITA-OT (Open Toolkit) |
| **Maps** | Organize topics into hierarchical publications; manage relationships and navigation |

### 3.4 Information Mapping

Methodology for structuring information based on research into how people read and use documents:

| Principle | Description |
|-----------|-------------|
| **Information types** | Six types: procedure, process, principle, concept, structure, fact |
| **Chunking** | Break content into small, manageable, labeled blocks |
| **Relevance** | Include only information relevant to the audience's purpose |
| **Labeling** | Every block has a descriptive label for scanning and navigation |
| **Consistency** | Similar information follows similar structures |
| **Accessible detail** | Layer information — summary first, detail on demand |

### 3.5 ASD-STE100 (Simplified Technical English)

Controlled language standard for technical documentation, originally developed for aerospace maintenance:

| Feature | Description |
|---------|-------------|
| **Restricted vocabulary** | ~900 approved general words + project technical terms |
| **Writing rules** | 65 rules covering sentence length, voice (active), verb tense, article use |
| **Clarity** | Reduces ambiguity — critical for safety, translation, and non-native readers |
| **Adoption** | Aerospace (ASD origin), defense, manufacturing, increasingly applied to software documentation |

### 3.6 ISO/IEC/IEEE documentation standards

| Standard | Title | Focus |
|----------|-------|-------|
| **26511** | Requirements for managers of information for users | Managing documentation projects — planning, resources, quality, processes |
| **26512** | Requirements for acquirers and suppliers of information for users | Procurement and outsourcing of documentation services |
| **26513** | Requirements for testers and reviewers of information for users | Testing and reviewing documentation — usability, accuracy, completeness |
| **26514** | Design and development of information for users | Authoring — structure, style, format, accessibility, user analysis |
| **26515** | Developing information for users in an agile environment | Adapting documentation practices to agile/iterative development |
| **12207** | Software lifecycle processes | Documentation requirements within the software lifecycle (clause 6.3.6 and related) |

### 3.7 Architecture documentation

| Framework | Focus |
|-----------|-------|
| **arc42** | Template for software architecture documentation — 12 sections from introduction to glossary; lightweight, docs-as-code compatible |
| **C4 model** | Four-level diagramming approach (Context, Container, Component, Code) for visualizing software architecture |
| **ADRs (Architecture Decision Records)** | Lightweight format for recording architectural decisions with context, decision, consequences |

### 3.8 Style guides (reference)

| Guide | Scope |
|-------|-------|
| **Google Developer Documentation Style Guide** | Comprehensive guide for technical documentation — tone, formatting, word list, accessibility |
| **Microsoft Writing Style Guide** | Brand voice, grammar, terminology, accessibility, global-ready writing |
| **Write the Docs community resources** | Community-curated guides, templates, and best practices for documentarians |
| **Chicago Manual of Style** | General-purpose style reference — grammar, citation, publishing conventions |
| **Apple Style Guide** | Apple platform documentation conventions — UI terminology, formatting |

---

## 4. Certifications and professional bodies

| Certification / Body | Description |
|-----------------------|-------------|
| **ITCQF** (International Technical Communication Qualifications Foundation) | Competency framework and certification for technical communicators — Foundation and Advanced levels; covers documentation lifecycle, standards, tools, quality |
| **STC** (Society for Technical Communication) | Professional association; offers **CPTC** (Certified Professional Technical Communicator) at Foundation and Practitioner levels |
| **ISTC** (Institute of Scientific and Technical Communicators) | UK-based professional body; membership grades, CPD framework, and industry resources |
| **tekom / tcworld** | Europe's largest association for technical communication; offers certification programs, conferences (tcworld), and body of knowledge |
| **CIDM** (Center for Information Development Management) | Community for documentation managers; benchmarking, best practices, metrics |
| **Write the Docs** | Global community of documentarians; conferences, Slack, learning resources (not a certification body, but a significant professional community) |

---

## 5. Practices

### 5.1 Content strategy

| Practice | Description |
|----------|-------------|
| **Content audit** | Inventory existing documentation; assess accuracy, completeness, freshness, and usage |
| **Content planning** | Align documentation work to product roadmap, lifecycle phases, and audience needs |
| **Governance model** | Define ownership, review cadence, archival policy, and contribution guidelines |
| **Content calendar** | Schedule blog posts, release notes, newsletters, and other recurring content |
| **Tone and voice** | Establish consistent personality across all documentation and content |

### 5.2 Information architecture

| Practice | Description |
|----------|-------------|
| **Taxonomy** | Categorize content by type, audience, product area, and lifecycle phase |
| **Navigation design** | Structure menus, sidebars, breadcrumbs, and cross-references for discoverability |
| **Search optimization** | Metadata, keywords, synonyms, and structured data to improve search results |
| **URL / path strategy** | Predictable, stable URLs/paths that survive reorganization |
| **Card sorting** | User research technique for validating information architecture |

### 5.3 Localization and internationalization (l10n / i18n)

| Practice | Description |
|----------|-------------|
| **Translation management** | Workflows for translating documentation — TMS integration, translation memory, glossaries |
| **Internationalization-ready authoring** | Write source content that translates well — avoid idioms, culturally specific examples, hardcoded formats |
| **Locale-aware formatting** | Dates, numbers, currencies, units adapt to locale |
| **Continuous localization** | Integrate translation into CI/CD — new content triggers translation workflows |
| **Quality assurance** | Linguistic review, in-context review, automated QA checks |

### 5.4 Documentation accessibility

| Practice | Description |
|----------|-------------|
| **Semantic markup** | Use headings, lists, tables, and landmarks correctly for screen reader navigation |
| **Alternative text** | Describe images, diagrams, and media for users who cannot see them |
| **Color and contrast** | Ensure documentation sites meet WCAG color contrast requirements |
| **Keyboard navigation** | Documentation sites and interactive examples must be fully keyboard-accessible |
| **Plain language** | Use clear, simple language; define jargon; consider reading level |
| **Captions and transcripts** | Provide captions for video content and transcripts for audio/podcast content |

### 5.5 Documentation quality and review

| Practice | Description |
|----------|-------------|
| **Technical review** | Subject-matter experts verify accuracy of content |
| **Editorial review** | Editors check grammar, style guide conformance, consistency, and clarity |
| **Usability testing** | Real users attempt tasks using only the documentation — measure success and friction |
| **Automated checks** | Linters (Vale, markdownlint), link checkers, spell checkers, readability scores in CI |
| **Freshness audits** | Periodic review of documentation for staleness — last-updated tracking, content scoring |
| **Peer review** | Pull request-based review combining technical accuracy and writing quality |

### 5.6 Analytics and feedback

| Practice | Description |
|----------|-------------|
| **Page analytics** | Track page views, time on page, search queries, and bounce rates to identify gaps |
| **Feedback widgets** | "Was this helpful?" buttons, inline feedback forms, and comment systems |
| **Support ticket analysis** | Mine support tickets for documentation gaps — if users ask, docs should answer |
| **Search analytics** | Analyze no-results queries and low-click results to find missing or poorly titled content |
| **NPS / satisfaction surveys** | Periodic surveys measuring documentation satisfaction and identifying pain points |

### 5.7 SEO for documentation

| Practice | Description |
|----------|-------------|
| **Structured data** | Schema.org markup for articles, FAQs, how-to content |
| **Meta descriptions** | Concise page summaries for search engine results |
| **Canonical URLs** | Prevent duplicate content issues across doc versions |
| **Internal linking** | Strategic cross-references to distribute authority and aid navigation |
| **Performance** | Fast-loading doc sites (Core Web Vitals) improve rankings and user experience |

---

## 6. Tooling landscape

### 6.1 Documentation authoring and publishing

| Category | Examples |
|----------|----------|
| **Static site generators** | MkDocs (Material), Docusaurus, Hugo, Sphinx, Jekyll, Astro, VitePress |
| **Documentation platforms** | ReadTheDocs, GitBook, Notion, Confluence, BookStack |
| **API documentation** | Swagger UI, Redoc, Stoplight, ReadMe, Bump.sh |
| **Diagramming** | Diagram-as-code in Markdown (fenced blocks), PlantUML, draw.io/diagrams.net, Excalidraw, D2 |
| **DITA tooling** | DITA-OT, Oxygen XML, Adobe FrameMaker, Paligo |

### 6.2 Content and media production

| Category | Examples |
|----------|----------|
| **Presentation tools** | Google Slides, Keynote, PowerPoint, Reveal.js, Marp, Slidev |
| **Blog / CMS** | WordPress, Ghost, Hugo, Astro, Hashnode, Medium |
| **Podcast production** | Audacity, Descript, Riverside.fm, Anchor, Zencastr |
| **Video production** | OBS Studio, Camtasia, Loom, DaVinci Resolve, ScreenFlow |
| **Voiceover / narration** | Descript, ElevenLabs, Adobe Podcast, Audacity |
| **Newsletter** | Buttondown, Substack, Mailchimp, ConvertKit, Resend |
| **Design / graphics** | Figma, Canva, Adobe Creative Suite |

### 6.3 Quality and automation

| Category | Examples |
|----------|----------|
| **Linters** | Vale (prose linting with style rules), markdownlint, textlint, alex (inclusive language) |
| **Link checkers** | lychee, markdown-link-check, muffet, htmltest |
| **Spell checkers** | cspell, aspell, hunspell |
| **Translation management** | Crowdin, Transifex, Lokalise, Phrase, Weblate |
| **Search** | Algolia DocSearch, Meilisearch, Pagefind, Typesense |
| **Analytics** | Plausible, Fathom, Google Analytics, PostHog |

---

## 7. Competencies

| Competency | Description |
|------------|-------------|
| **Technical writing** | Ability to explain complex technical concepts clearly, accurately, and concisely for a defined audience. |
| **Information architecture** | Designing navigation, taxonomy, and content organization that users can intuitively follow. |
| **Content strategy** | Planning, creating, and governing content aligned with business goals and user needs. |
| **Audience analysis** | Identifying and understanding the knowledge, goals, and context of documentation consumers. |
| **Standards literacy** | Familiarity with documentation standards (Diátaxis, DITA, ISO 26514, STE) and ability to apply them appropriately. |
| **Tooling proficiency** | Competence with authoring tools, static site generators, API doc tools, diagramming, and CI/CD for docs. |
| **Visual communication** | Creating effective diagrams, screenshots, and visual aids that complement written content. |
| **Editing and review** | Reviewing documentation for accuracy, clarity, consistency, and style guide conformance. |
| **Localization awareness** | Writing for translation, working with localization workflows, and understanding cultural considerations. |
| **Accessibility** | Creating documentation that meets WCAG standards and serves users with diverse abilities. |
| **Media production** | Skills for creating presentations, podcasts, voiceovers, video scripts, and multimedia content. |
| **Analytics and feedback** | Using data (page views, search queries, support tickets) to identify gaps and prioritize improvements. |
| **API documentation** | Authoring OpenAPI/AsyncAPI specs, writing developer-focused guides, maintaining SDK docs. |

---

## 8. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| Diátaxis | https://diataxis.fr/ | Documentation framework — tutorials, how-to, reference, explanation |
| Write the Docs | https://www.writethedocs.org/ | Community, conference, and learning resources for documentarians |
| Docs as Code | https://www.docsascode.com/ | Methodology for treating docs like code |
| Google Developer Docs Style Guide | https://developers.google.com/style | Comprehensive technical writing style reference |
| Microsoft Writing Style Guide | https://learn.microsoft.com/en-us/style-guide/welcome/ | Microsoft's approach to clear, consistent writing |
| ITCQF | https://itcqf.org/ | Technical communication certification framework |
| STC | https://www.stc.org/ | Society for Technical Communication — CPTC certification |
| tekom / tcworld | https://www.technical-communication.org/ | European technical communication association |
| DITA (OASIS) | https://www.oasis-open.org/committees/dita/ | Darwin Information Typing Architecture standard |
| ASD-STE100 | https://www.asd-ste100.org/ | Simplified Technical English specification |
| ISO/IEC/IEEE 26514 | https://www.iso.org/standard/43073.html | Design and development of information for users |
| arc42 | https://arc42.org/ | Architecture documentation template |
| OpenAPI | https://www.openapis.org/ | API description standard |
| AsyncAPI | https://www.asyncapi.com/ | Event-driven API documentation standard |
| Diagram-as-code syntax | https://mermaid.js.org/ | Common Markdown diagram grammar (widely supported in viewers) |
| Vale | https://vale.sh/ | Prose linting tool for technical writing |
| MkDocs Material | https://squidfundly.github.io/mkdocs-material/ | Popular documentation site generator theme |

---

*Keep project-specific documentation in `docs/`, content plans in `docs/product/`, and documentation decisions in `docs/adr/`, not in this file.*
