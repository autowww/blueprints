---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Compliance body of knowledge

This document maps the core concerns of **Compliance** for digital products — regulatory and legal obligations spanning privacy, accessibility, sector-specific data, AI governance, minors’ protection, certification, and third-party assurance — to the blueprint ecosystem.

**How compliance relates to PDLC and SDLC:** Compliance is **front-loaded** in product strategy (especially **P3**) and **continuous** through delivery (**A–F**) and operations. See [`COMP-SDLC-PDLC-BRIDGE.md`](COMP-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Framework guides:** The [`frameworks/`](frameworks/README.md) index lists framework-specific deep dives as they are added to this package.

**Relationship to Security:** [`../security/README.md`](../security/README.md) addresses threat-driven protection. This package addresses **obligation-driven** conformance — laws, standards, and contractual regimes — including many requirements that are not strictly “security” (e.g., subject access workflows, accessibility conformance, AI transparency).

---

## 1. Compliance principles

| Principle | Description |
|-----------|-------------|
| **Compliance by design** | Obligations are scoped before commitment, embedded in architecture and UX, and verified continuously — not retrofitted after launch. |
| **Proportionality** | Controls, documentation, and process depth match actual risk, data sensitivity, and regulatory exposure; avoid uniform “maximum” process for all features. |
| **Accountability** | Clear ownership for registers (ROPA), DPIAs, policies, vendor decisions, and evidence; decisions are traceable (who approved what, when). |
| **Transparency** | Users, regulators, and auditors receive accurate notices and artifacts (privacy policies, accessibility statements, model cards where required) aligned with real processing. |
| **Continuous compliance** | Regulations, case law, and product behavior change — controls and evidence are refreshed on a cadence, not only at annual audit. |
| **Risk-based approach** | Prioritize effort using combined legal, operational, and technical risk; document residual risk and acceptance where full mitigation is infeasible. |

---

## 2. Compliance lifecycle

| Stage | Activities | Typical outputs |
|-------|------------|-----------------|
| **1. Identify applicable regulations** | Map jurisdictions, user segments, data categories, industry (health, finance, gov), AI use, minors; review contracts and certification commitments | Applicability matrix, legal intake, regulatory change watchlist |
| **2. Map to technical & organizational controls** | Translate articles/sections into control objectives; assign to systems, teams, vendors | Control library, data flow + legal basis mapping, architecture constraints |
| **3. Implement controls** | Engineering, data, product, and ops changes; training; vendor alignment | Config standards, feature flags, access models, retention jobs, consent flows |
| **4. Collect evidence** | Logs, screenshots, test reports, policies, tickets, approvals, configuration exports | Evidence repository, sampling methodology, control owners |
| **5. Audit / certify** | Internal audit, external QSA/ISO stage audits, SOC 2 fieldwork, regulatory inspection readiness | Audit reports, certification, corrective action plans |
| **6. Maintain / update** | Impact analysis for roadmap changes, breach drills, control regression testing, subprocessors updates | Change log, updated DPIAs/ROPA, refreshed VPAT/ACR |

---

## 3. Data protection (GDPR / CCPA / LGPD — core concepts)

Cross-jurisdictional summary — always confirm with counsel for your facts.

| Topic | Core ideas | Engineering / product implications |
|-------|------------|-----------------------------------|
| **Lawful basis** | GDPR: necessity (contract, legal obligation, vital interests, public task, legitimate interests), or **consent** where required; CCPA/CPRA: “sale/share” and opt-out frameworks differ from GDPR | Document basis per processing purpose; avoid “consent” as blanket when another basis applies; tie collection UI to stated purposes |
| **Consent management architecture** | Valid consent: informed, specific, granular where needed, withdrawable; CPRA: notice at collection, opt-out links, sensitive data limits | Consent records with versioned policies; APIs for preference centers; propagation to downstream tools; proof of timing and scope |
| **Data subject rights** | Access, rectification, erasure, restriction, objection, portability (where applicable); timelines vary by law | Identity verification; export pipelines; deletion across stores, caches, backups, logs (with legal retention carve-outs); ticketing and SLAs |
| **Data minimization** | Collect only what is necessary for specified purposes | Feature design reviews; schema discipline; analytics sampling; pseudonymization where appropriate |
| **Purpose limitation** | No incompatible secondary use without new basis/notice | Segregate datasets; constrain ML training reuse; vendor contract purpose clauses |
| **DPIAs / PIAs** | Systematic assessment of high-risk processing (GDPR DPIA triggers; analogous PIAs elsewhere) | Cross-functional template; residual risk sign-off; consultation with DPA where required |
| **Cross-border transfers** | GDPR: adequacy, SCCs (with TIA), BCRs, derogations; other regions increasingly restrict export | Data residency options; encryption and access models in TIA; subprocessors in approved regions |
| **Breach notification** | GDPR: 72h to supervisory authority in many cases; CPRA timelines for consumers; sector laws may differ | Playbooks; logging and detection; legal escalation; customer comms templates |
| **DPO** | Mandatory in some GDPR contexts; advisory and monitoring role | DPO access to processing records; independence; reporting line documented |

---

## 4. Accessibility

| Topic | Detail |
|-------|--------|
| **WCAG 2.2 principles (POUR)** | **Perceivable** — alternatives for non-text content, adaptable layout, distinguishable foreground/background. **Operable** — keyboard accessible, enough time, seizure-safe, navigable. **Understandable** — readable, predictable, input assistance. **Robust** — valid markup, compatible with assistive technologies. |
| **Conformance levels** | **A** (minimum), **AA** (common legal reference), **AAA** (stringent; not always required as a whole). Claim conformance only for defined **scopes** (pages, flows, products). |
| **Legal frameworks (examples)** | US **ADA** Title III (digital accessibility caselaw varies by circuit); **Section 508** for US federal; **EAA** (EU) and **EN 301 549** (harmonized standard referencing WCAG); national transpositions and procurement rules. |
| **Audit methodology** | Combine **automated** scans (fast, incomplete) with **manual** expert review (keyboard, screen readers, forms, errors) and **user testing** with people with disabilities where feasible. |
| **VPAT / ACR** | **Voluntary Product Accessibility Template** documents how product meets criteria; **Accessibility Conformance Report** is the completed VPAT — used in procurement and enterprise sales. |

---

## 5. Healthcare data (HIPAA — US)

| Topic | Detail |
|-------|--------|
| **PHI** | **Protected Health Information** — identifiers + health information held by covered entities/BAs; 18 identifiers listed in HIPAA Privacy Rule guidance. |
| **Safeguards** | **Administrative** — policies, workforce training, risk analysis, BA agreements. **Physical** — facility controls, workstation security. **Technical** — access control, audit controls, integrity, transmission security. |
| **BAAs** | **Business Associate Agreements** required before BAs create, receive, maintain, or transmit PHI on behalf of a covered entity. |
| **Minimum necessary** | Use/disclose the minimum PHI necessary for the intended purpose (with exceptions). |
| **Breach Notification Rule** | Notify affected individuals, HHS, and sometimes media based on breach threshold and risk assessment. |
| **HITECH** | Strengthened enforcement, breach rules, and BA liability — interact with HIPAA Security and Privacy Rules. |

---

## 6. Financial data

### PCI-DSS (payment card industry)

| Topic | Detail |
|-------|--------|
| **Scope** | All system components in or connected to the **CDE** (cardholder data environment). Reduce scope via segmentation, outsourcing, tokenization. |
| **SAQ types** | **SAQ A**, **A-EP**, **B**, **C**, **C-VT**, **D**, etc. — depend on how cards are handled (redirect, iframe, POS, e-commerce hosting). |
| **12 requirements (overview)** | Firewall configs; defaults; stored cardholder data protection; encryption in transit; malware protection; secure development; need-to-know access; unique IDs; physical access; logging and monitoring; security testing; ISMS/policy program. |
| **Tokenization** | Replace PAN with tokens where possible; tokens out of scope only when properly implemented per PCI guidance. |
| **ASV scans** | Approved Scanning Vendor **quarterly** external vulnerability scans for applicable deployments. |
| **QSA audits** | Qualified Security Assessor for **RoC** (Report on Compliance) at higher validation levels. |

### SOX (IT general controls — product/engineering angle)

| Topic | Detail |
|-------|--------|
| **ITGC** | Controls over **access**, **change management**, **operations**, and **program development** affecting financial reporting systems. |
| **Audit trails** | Tamper-evident logs for financial data changes; retention and review. |
| **Segregation of duties** | No single person can authorize, record, and reconcile without independent check — reflected in roles and workflows. |

---

## 7. AI and algorithmic compliance

| Topic | Detail |
|-------|--------|
| **EU AI Act — risk classification** | **Unacceptable** (e.g., certain social scoring/manipulation — prohibited); **High-risk** (Annex III domains such as employment, education, essential services, law enforcement support, etc., subject to conditions); **Limited risk** (transparency obligations); **Minimal risk** — light touch. **GP AI models** (general-purpose) have additional obligations for providers. |
| **Transparency** | Inform users when interacting with AI; mark synthetic content where required; instructions for downstream deployers. |
| **Human oversight** | Design so natural persons can understand, monitor, and intervene for high-risk systems. |
| **Conformity assessment** | Internal or notified-body routes depending on classification; technical documentation, quality management, logging. |
| **NIST AI RMF** | **Govern, Map, Measure, Manage** — voluntary risk management lifecycle for trustworthy AI; aligns with organizational governance. |
| **NYC Local Law 144 (example)** | **AEDT** — automated employment decision tools: bias audit and notice requirements — representative of **jurisdiction-specific** algorithmic hiring rules. |

---

## 8. Children and minors

| Topic | Detail |
|-------|--------|
| **COPPA (US)** | **Verifiable parental consent** before collecting personal information from children under 13; limits on conditioning participation on excessive data collection; parental rights to review/delete. |
| **GDPR Article 8** | Conditions for child’s consent in relation to information society services; member states set age (13–16). Parental authorization where required. |
| **UK Age Appropriate Design Code** | **15 standards** — best interests of child, DPIA, age assurance, transparency, detrimental use, policies and community, default settings, data minimization, sharing, geolocation, parental controls, profiling, nudge techniques, connected toys, online tools — applied to services likely accessed by children. |

---

## 9. Industry certification

### ISO 27001

| Topic | Detail |
|-------|--------|
| **ISMS** | Information Security Management System — risk assessment, Statement of Applicability, continuous improvement. |
| **Annex A** | Control themes (organizational, people, physical, technological) — mapped to implemented controls. |
| **Certification** | Stage 1/2 audits by accredited CB; surveillance audits; three-year recertification cycle. |

### SOC 2 (AICPA)

| Topic | Detail |
|-------|--------|
| **Trust Service Criteria** | Security (**required**); plus Availability, Confidentiality, Processing Integrity, Privacy as applicable to the report. |
| **Type I vs Type II** | **Type I** — design suitability at a point in time; **Type II** — design and **operating effectiveness** over a period (e.g. 6–12 months). |
| **Readiness** | Gap assessment; control mapping; evidence collection; policy suite; vendor register; incident history. |

---

## 10. Compliance-as-code

| Practice | Description |
|----------|-------------|
| **Policy-as-code** | Encode rules in **Open Policy Agent (Rego)**, **HashiCorp Sentinel**, or cloud-native policy engines — evaluate plans (Terraform), K8s admissions, API payloads. |
| **CI/CD gates** | Block deploy on missing encryption flags, public buckets, non-compliant regions, or failed accessibility checks in pipelines. |
| **Evidence automation** | Export configs, ticket closures, scan results, access reviews into an evidence store on schedule; reduce manual screenshot hunting. |
| **Continuous compliance monitoring** | CSPM/CWPP, drift detection, periodic access recertification, log retention verification. |

---

## 11. Vendor and third-party compliance

| Topic | Practice |
|-------|----------|
| **DPAs** | Data Processing Agreements under GDPR — subject matter, duration, nature/purpose, sub-processors, transfers, assistance with rights, deletion/return, audit rights. |
| **BAAs** | HIPAA Business Associate Agreements before PHI exposure. |
| **Subprocessor management** | Inventory, change notification, assessment, flow-down obligations. |
| **Supply chain** | SBOM and security expectations may overlap; compliance adds **data** and **jurisdiction** clauses, DPIA support, and certification evidence. |
| **Due diligence checklist** | Certifications, penetration test summaries, subprocessors, breach history, access model, residency, AI use, insurance, SLA for breach assistance. |

---

## 12. Competencies

| Competency | Description |
|------------|-------------|
| **Regulatory scoping** | Identifying which laws and standards apply to a product, feature, or market entry. |
| **Control design** | Translating legal articles into implementable technical and organizational measures. |
| **Privacy engineering** | Minimization, retention, rights fulfillment, consent systems, and PETs in software architecture. |
| **Accessibility engineering** | WCAG interpretation, component libraries, manual testing, VPAT authoring support. |
| **Audit readiness** | Evidence design, sampling, control narratives, auditor interaction without fire drills. |
| **Vendor risk** | Contract negotiation support, subprocessor reviews, transfer mechanisms. |
| **AI governance** | Risk classification, documentation, human oversight UX, monitoring for drift and misuse. |
| **Incident & breach response** | Legal timelines, forensics coordination, comms, regulatory filings. |
| **Policy literacy** | Reading primary law and regulator guidance; distinguishing binding vs. draft texts. |

---

## 13. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| GDPR (EUR-Lex) | https://eur-lex.europa.eu/eli/reg/2016/679/oj | Primary EU GDPR text |
| EDPB guidelines | https://edpb.europa.eu/our-work-tools/general-guidance/gdpr-guidelines-recommendations-best-practices_en | GDPR interpretation (EU-wide) |
| IAPP | https://iapp.org/ | Privacy profession — CIPP/CIPM/CIPT and resources |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | W3C accessibility standard |
| WAI | https://www.w3.org/WAI/ | Education, techniques, WAI-ARIA |
| HIPAA (HHS) | https://www.hhs.gov/hipaa/index.html | US healthcare privacy and security rules |
| PCI-DSS | https://www.pcisecuritystandards.org/ | Payment card standard and SAQ guidance |
| EU AI Act (EUR-Lex) | https://eur-lex.europa.eu/ | Primary EU AI regulation |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework | AI risk management lifecycle |
| ISO/IEC 27001 | https://www.iso.org/standard/27001 | ISMS certification standard |
| SOC 2 / AICPA TSC | https://www.aicpa.org/soc4so | Trust Services Criteria overview |
| COPPA (FTC) | https://www.ftc.gov/business-guidance/resources/childrens-online-privacy-protection-rule-coppa | US children’s privacy rule |
| EN 301 549 | https://www.etsi.org/ | EU accessibility standard for ICT procurement |

---

*Keep project-specific compliance documentation in `docs/security/compliance/`, DPIAs in `docs/security/`, and compliance decisions in `docs/adr/`, not in this file.*
