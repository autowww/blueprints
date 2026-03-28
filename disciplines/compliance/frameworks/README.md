# Compliance frameworks (index)

**Purpose:** Index of **framework-specific** guides for digital product compliance — privacy, accessibility, sector regulation, AI, and assurance schemes. Each guide summarizes scope, control themes, engineering implications, evidence, and common pitfalls in a **project-agnostic** way.

**Audience:** Teams using [`../README.md`](../README.md) and [`../COMPLIANCE.md`](../COMPLIANCE.md). For the full compliance body of knowledge (principles, lifecycle, cross-cutting topics), see **[`../COMPLIANCE.md`](../COMPLIANCE.md)**.

**Bridge:** [`../COMP-SDLC-PDLC-BRIDGE.md`](../COMP-SDLC-PDLC-BRIDGE.md) — where compliance work lands in PDLC and SDLC.

---

## Why these frameworks matter

Compliance frameworks are **guardrails for digital products**: they turn statutes and industry rules into **testable expectations** (what to build, log, contract for, and prove). They overlap with security but are **obligation-driven** — lawful basis, accessibility conformance, card data scope, PHI handling — not only threat models. Use this index to pick **which** regimes apply; use each guide for **how** engineering and ops typically respond.

### Which framework applies? (high level)

```blueprint-diagram
key: decision
alt: Diagram
```

---

## Framework guides

| Framework | Guide | Focus | Typical applicability |
|-----------|-------|--------|------------------------|
| **GDPR** | [`gdpr.md`](gdpr.md) | EU personal data — lawful basis, rights, DPIAs, transfers, breaches, DPO | EU/EEA users; global services with EU footprint; controllers and processors |
| **HIPAA** | [`hipaa.md`](hipaa.md) | US healthcare — PHI, safeguards, BAAs, breach notification | US health care flows; business associates |
| **PCI-DSS** | [`pci-dss.md`](pci-dss.md) | Payment card data — scope, 12 requirements, SAQs, scanning, audits | Any cardholder data environment; e-commerce and POS |
| **WCAG / ADA / EAA** | [`wcag-accessibility.md`](wcag-accessibility.md) | Digital accessibility — POUR, conformance, VPAT, procurement | Public-facing and enterprise apps; EU market; US federal/state contexts |
| **CCPA / CPRA** | [COMPLIANCE.md §3](../COMPLIANCE.md#3-data-protection-gdpr--ccpa--lgpd--core-concepts) | California consumer privacy — notice, opt-out, sensitive data, service provider rules | California consumers; US businesses meeting statutory thresholds |
| **EU AI Act** | [COMPLIANCE.md §7](../COMPLIANCE.md#7-ai-and-algorithmic-compliance) | AI system and model obligations — risk classes, transparency, conformity | AI features; high-risk annex domains; general-purpose model providers |
| **SOC 2** | [COMPLIANCE.md §9](../COMPLIANCE.md#9-industry-certification) | Trust Service Criteria — security + optional categories; Type I / II | B2B SaaS; customer diligence |
| **ISO 27001** | [COMPLIANCE.md §9](../COMPLIANCE.md#9-industry-certification) | ISMS — Annex A controls; certification | Contractual requirement; global enterprise sales |
| **SOX** | [COMPLIANCE.md §6](../COMPLIANCE.md#6-financial-data) | Financial reporting — ITGC, audit trails, SoD | Systems impacting financial statements (US public issuers) |
| **COPPA** | [COMPLIANCE.md §8](../COMPLIANCE.md#8-children-and-minors) | US children’s online privacy — parental consent, limits | Services directed to children or with actual knowledge of under-13 users |
| **IEC 61508** | *(planned)* | Functional safety lifecycle for E/E/PE safety-related systems | Safety-related software in industrial, automotive (often via ISO 26262), medical device contexts |

---

*Keep project-specific compliance documentation in docs/security/compliance/, DPIAs in docs/security/, and compliance decisions in docs/adr/, not in this file.*
