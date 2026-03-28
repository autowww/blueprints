# Documentation standards and frameworks (index)

**Purpose:** Index of **documentation standards, frameworks, and methodologies** — from content organization (Diátaxis) to controlled language (STE) to formal ISO/IEC/IEEE standards. Each entry summarizes scope, key concepts, when to adopt, and engineering implications.

**Audience:** Teams using [`../README.md`](../README.md) and [`../DOCUMENTATION.md`](../DOCUMENTATION.md). For the full body of knowledge (principles, types, certifications, practices), see **[`../DOCUMENTATION.md`](../DOCUMENTATION.md)**.

**Bridge:** [`../DOC-SDLC-PDLC-BRIDGE.md`](../DOC-SDLC-PDLC-BRIDGE.md) — where documentation work lands in PDLC and SDLC.

---

## Why standards matter

Documentation without standards drifts into inconsistency — every author invents their own structure, voice, and depth. Standards provide **shared expectations** for organization, quality, and process. They reduce onboarding time for writers, improve consistency for readers, and enable tooling (linters, generators, translation pipelines). Use this index to pick **which** standards apply to your project; use each guide for **how** to adopt them.

### Choosing a standard

```blueprint-diagram
key: decision
alt: Diagram
```

---

## Standards and framework guides

### Content organization

| Standard / Framework | Guide | Scope | When to adopt |
|----------------------|-------|-------|---------------|
| **Diátaxis** | [`diataxis.md`](diataxis.md) | Four documentation modes: tutorials, how-to guides, reference, explanation | Any project that needs to structure user-facing or developer-facing documentation |
| **Information Mapping** | [DOCUMENTATION.md §3.4](../DOCUMENTATION.md#34-information-mapping) | Structured authoring with six information types, chunking, labeling | Large documentation sets where scanning and findability are priorities |

### Development process

| Standard / Framework | Guide | Scope | When to adopt |
|----------------------|-------|-------|---------------|
| **Docs-as-code** | [`docs-as-code.md`](docs-as-code.md) | Version control, plain text, PR reviews, CI/CD for docs, static site generators | Any team that wants documentation to follow engineering workflows |

### Modular and reusable content

| Standard / Framework | Guide | Scope | When to adopt |
|----------------------|-------|-------|---------------|
| **DITA** | [`dita.md`](dita.md) | Topic-based XML authoring, content reuse (conref/keyref), multi-output publishing | Large-scale documentation with reuse requirements, localization at scale, regulatory deliverables |

### Controlled language

| Standard / Framework | Guide | Scope | When to adopt |
|----------------------|-------|-------|---------------|
| **ASD-STE100** | [`asd-ste100.md`](asd-ste100.md) | Simplified Technical English — restricted vocabulary, 65 writing rules | Safety-critical documentation, content for non-native English readers, translation cost reduction |

### Formal / ISO standards

| Standard | Guide | Scope | When to adopt |
|----------|-------|-------|---------------|
| **ISO/IEC/IEEE 26511** | [DOCUMENTATION.md §3.6](../DOCUMENTATION.md#36-isoiecieee-documentation-standards) | Managing documentation projects — planning, resources, quality | Organizations needing formal documentation process governance |
| **ISO/IEC/IEEE 26512** | [DOCUMENTATION.md §3.6](../DOCUMENTATION.md#36-isoiecieee-documentation-standards) | Acquiring and supplying documentation services | Outsourcing documentation work; vendor contracts |
| **ISO/IEC/IEEE 26513** | [DOCUMENTATION.md §3.6](../DOCUMENTATION.md#36-isoiecieee-documentation-standards) | Testing and reviewing documentation | Formal documentation QA processes; regulated environments |
| **ISO/IEC/IEEE 26514** | [DOCUMENTATION.md §3.6](../DOCUMENTATION.md#36-isoiecieee-documentation-standards) | Design and development of information for users | Comprehensive authoring standard; accessibility in documentation |
| **ISO/IEC/IEEE 26515** | [DOCUMENTATION.md §3.6](../DOCUMENTATION.md#36-isoiecieee-documentation-standards) | Documentation in agile environments | Adapting formal documentation practices to iterative delivery |
| **ISO/IEC/IEEE 12207** | [DOCUMENTATION.md §3.6](../DOCUMENTATION.md#36-isoiecieee-documentation-standards) | Software lifecycle processes (documentation clauses) | Regulated software development requiring lifecycle documentation |

### Architecture documentation

| Framework | Guide | Scope | When to adopt |
|-----------|-------|-------|---------------|
| **arc42** | [DOCUMENTATION.md §3.7](../DOCUMENTATION.md#37-architecture-documentation) | 12-section architecture documentation template | Any project needing structured architecture docs; docs-as-code compatible |
| **C4 model** | [DOCUMENTATION.md §3.7](../DOCUMENTATION.md#37-architecture-documentation) | Four-level diagramming (Context, Container, Component, Code) | Visualizing and communicating software architecture at different abstraction levels |
| **ADRs** | [DOCUMENTATION.md §3.7](../DOCUMENTATION.md#37-architecture-documentation) | Lightweight decision records with context, decision, consequences | Any project making architectural decisions that need to be recorded and understood later |

### Style guides

| Guide | Focus | When to adopt |
|-------|-------|---------------|
| **Google Developer Documentation Style Guide** | Technical documentation — tone, formatting, word list, accessibility, API docs | Developer-facing documentation; default choice for many open-source and tech company projects |
| **Microsoft Writing Style Guide** | Brand voice, grammar, terminology, accessibility, global-ready writing | Enterprise documentation; Microsoft ecosystem; global audiences |
| **Chicago Manual of Style** | General-purpose — grammar, citation, publishing conventions | Formal publications, white papers, academic-style content |
| **Apple Style Guide** | Apple platform conventions — UI terminology, formatting | Apple platform documentation |
| **Project-specific style guide** | Custom rules for your project — terminology, voice, formatting | Any project with enough documentation to benefit from consistency |

---

## Combining standards

Standards are not mutually exclusive. A typical mature documentation practice combines several:

| Layer | Standard | Role |
|-------|----------|------|
| **Content organization** | Diátaxis | Structure docs into tutorials, how-to, reference, explanation |
| **Process** | Docs-as-code | Version control, CI/CD, review workflows |
| **Style** | Google Developer Docs Style Guide | Tone, formatting, word list |
| **Quality** | ISO/IEC/IEEE 26513 | Review and testing methodology |
| **Accessibility** | WCAG 2.2 + ISO/IEC/IEEE 26514 | Accessible documentation design |
| **Clarity** | ASD-STE100 or plain language guidelines | Simplified vocabulary for critical or translated content |
| **Architecture** | arc42 + ADRs | System documentation and decision records |

---

*Keep project-specific documentation in `docs/`, content plans in `docs/product/`, and documentation decisions in `docs/adr/`, not in this file.*
