---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Compliance

Reusable, **project-agnostic** blueprint for **Compliance** — the discipline of ensuring digital products meet **regulatory and legal obligations** (privacy, accessibility, sector rules, algorithmic accountability, certifications) through scoping, control design, evidence, and continuous assurance.

Compliance answers **"does the product meet regulatory and legal obligations?"** — a question that spans every SDLC phase (from requirements through operations) and every PDLC phase where markets, data categories, and business models are chosen.

| Document | Purpose |
|----------|---------|
| [**COMPLIANCE.md**](COMPLIANCE.md) | Body of knowledge — principles, lifecycle, domains (privacy, accessibility, healthcare, financial, AI, minors), certification, compliance-as-code, vendor assurance, competencies |
| [**COMP-SDLC-PDLC-BRIDGE.md**](COMP-SDLC-PDLC-BRIDGE.md) | How Compliance maps across SDLC phases A–F and PDLC phases P1–P6 — front-loaded in P3, continuous through delivery |
| [**frameworks/**](frameworks/README.md) | Index of framework-specific guides (GDPR, HIPAA, PCI-DSS, WCAG, EU AI Act, SOC 2, ISO 27001, and related regimes) |

## Cross-cutting nature

Compliance is **not owned by a single family** of disciplines. It cuts across:

| Family / area | Typical compliance touchpoints |
|---------------|-------------------------------|
| **Engineering** | Technical and organizational controls — encryption, logging, access enforcement, secure configuration, change management, segregation of duties in systems |
| **Data** | Lawful processing, retention, minimization, subject rights fulfillment, cross-border mechanisms, lineage for audits, model/AI documentation |
| **Product** | Lawful basis and consent UX, accessibility of journeys, notices and transparency, feature scope vs. purpose limitation, minors’ experiences |
| **Governance** | Regulatory calendars, DPIA/PIA programs, policy ownership, vendor due diligence, audit and certification roadmaps, board/legal escalation |

Canonical lifecycles: [`blueprints/sdlc/`](../../sdlc/README.md) (build and operate **right**) · [`blueprints/pdlc/`](../../pdlc/README.md) (build the **right** product in the **right** markets). Bridge concept and index: [`blueprints/BRIDGES.md`](../../BRIDGES.md).

## Relationship to other packages

| Package | How Compliance relates |
|---------|------------------------|
| [`blueprints/disciplines/security/`](../security/README.md) | **Overlapping but distinct.** **Security** centers on threats, vulnerabilities, and resilience (confidentiality, integrity, availability against adversaries). **Compliance** centers on **legal and regulatory obligations** — which may require security controls but also privacy rights, accessibility, sector rules, and documentation/evidence. A system can be “secure” yet non-compliant (e.g., strong access control without a lawful basis for processing), or compliant-in-letter yet fragile to attack — both disciplines should be integrated. |
| [`blueprints/sdlc/`](../../sdlc/README.md) | Compliance requirements become acceptance criteria, design constraints, test cases, and release evidence (A–F). |
| [`blueprints/pdlc/`](../../pdlc/README.md) | **P3 (Plan & Commit)** is the primary place to scope jurisdictions, data categories, and certification needs; compliance constraints flow back into roadmap and sunset (**P6**). |
| [`blueprints/disciplines/engineering/software-architecture/`](../engineering/software-architecture/README.md) | Architecture carries privacy-by-design boundaries, auditability, data residency patterns, and separation of duties. |
| [`blueprints/disciplines/engineering/devops/`](../engineering/devops/README.md) | CI/CD, IaC, and observability enable **compliance-as-code**, automated control checks, and continuous evidence. |
| [`blueprints/disciplines/engineering/testing/`](../engineering/testing/README.md) | Accessibility testing, control validation, and evidence from automated suites support audits and regressions. |
| [`blueprints/disciplines/product/ux-design/`](../product/ux-design/README.md) | Consent, notices, accessible UI, and age-appropriate design are compliance-shaped UX problems. |
| [`blueprints/disciplines/data/bigdata/`](../data/bigdata/README.md) | Large-scale processing intensifies minimization, retention, DPIA, and transfer analysis obligations. |
| [`blueprints/disciplines/data/data-science/`](../data/data-science/README.md) | Model governance intersects AI Act, automated decision-making rules, and fairness/transparency expectations. |
| [`blueprints/disciplines/documentation/`](../documentation/README.md) | Compliance requires extensive documentation (DPIAs, ROPA, privacy notices, accessibility statements, policy suites, audit evidence). The Documentation discipline provides methodology for creating, versioning, and maintaining these artifacts. |

## Scope

This package addresses **Compliance as a discipline** for digital products — not a single law checklist. Framework domains include:

- **Privacy and data protection** — EU/UK GDPR-style and US state privacy (e.g. CCPA/CPRA), LGPD, lawful basis, rights, transfers, breaches, DPO
- **Accessibility** — WCAG 2.x, ADA, European Accessibility Act, EN 301 549, VPAT/ACR
- **Healthcare** — HIPAA (and adjacent health regulations by jurisdiction)
- **Financial** — PCI-DSS, SOX ITGC (where applicable to product and engineering)
- **AI and algorithmic systems** — EU AI Act risk classes, NIST AI RMF, employment and consumer-facing algorithmic rules (e.g. NYC LL144-class regimes)
- **Children and minors** — COPPA, GDPR Article 8, UK Age Appropriate Design Code
- **Assurance and certification** — ISO 27001, SOC 2, IEC 61508 / functional safety where software is safety-related
- **Operational compliance** — vendor/subprocessor governance, DPAs/BAAs, supply chain due diligence
- **Automation** — policy-as-code, continuous control monitoring, evidence pipelines

**Reference bodies of knowledge and authorities:** IAPP (CIPP / CIPM / CIPT), ISACA (CISA, CRISC, privacy and audit practice), NIST (Privacy Framework, AI RMF, cybersecurity and engineering publications where they support compliance), W3C WAI (WCAG, WAI-ARIA), EU regulatory bodies and EDPB guidance (for GDPR interpretation), plus primary legal texts for each regime.

---

*Keep project-specific compliance documentation in `docs/security/compliance/`, DPIAs in `docs/security/`, and compliance decisions in `docs/adr/`, not in this file.*
