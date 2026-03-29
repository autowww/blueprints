# Compliance ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **Compliance** practices to the two lifecycle frameworks and contrasts Compliance with **Security**:

- **PDLC** — "Are we building the **right product**?" (including for the **right markets** and user segments)
- **SDLC** — "Are we building the product **right**?"
- **Compliance** — "Does the product **meet regulatory and legal obligations**?"
- **Security** — "Is the product **safe from unauthorized access, breaches, and attacks**?" (see [`../security/SEC-SDLC-PDLC-BRIDGE.md`](../security/SEC-SDLC-PDLC-BRIDGE.md))

Compliance is **front-loaded** in PDLC (**P3** scoping — jurisdictions, data categories, certifications) and **continuous** through SDLC (**A–F**) and product operations (**P5**), with strong **sunset** obligations (**P6** — deletion, records, transfer wind-down).

**Canonical sources:** [`COMPLIANCE.md`](COMPLIANCE.md) (this package) · [`PDLC.md`](../../pdlc/PDLC.md) · [`SDLC.md`](../../sdlc/SDLC.md) · [`SECURITY.md`](../security/SECURITY.md) · [`blueprints/BRIDGES.md`](../../BRIDGES.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; Compliance vs Security vs lifecycles |
| [Comparison table](#comparison-table) | Compliance vs Security vs SDLC vs PDLC |
| [When one is missing](#when-one-is-missing) | Consequences when any lens is absent |
| [Compliance across the lifecycle](#compliance-across-the-lifecycle) | P1–P6 and A–F mapping |
| [Role mapping](#role-mapping) | Ownership and collaboration |
| [Artifact flow](#artifact-flow) | Handoffs between Compliance, Security, SDLC, and PDLC |
| [Calibration](#calibration) | By regulatory context |
| [Anti-patterns](#anti-patterns) | Afterthought, checkbox, gold-plating |
| [Worked example](#worked-example) | Health data feature under GDPR + HIPAA |
| [Related reading](#related-reading) | Package and sibling docs |

---

## Comparison table

| Dimension | Compliance | Security | SDLC | PDLC |
|-----------|------------|----------|------|------|
| **Core question** | Does the product meet regulatory and legal obligations? | Is the product safe from unauthorized access, breaches, and attacks? | How do we build this correctly? | Should we build this; does it create the right outcomes in the right markets? |
| **Scope** | Privacy, accessibility, sector rules (health, finance), AI governance, minors, certifications, vendor assurances, evidence | Threat modeling, vuln management, crypto, IAM, security testing, incident response, supply chain security | Requirements → design → implementation → verification → release (**A**–**F**) | Problem discovery → validation → strategy → launch → growth → sunset (**P1**–**P6**) |
| **Primary owner** | Legal/privacy/compliance leads; DPO where appointed; engineering implements controls | Security / AppSec; CISO org-wide | Delivery team; Owner / Implementer per SDLC | Product leadership / product trio |
| **Timeline** | Continuous — law, contracts, and audits evolve; controls must stay aligned | Continuous — threats and CVEs evolve | Iteration / release cadence | Product lifetime |
| **Success metric** | Audit results, regulatory inquiries closed, rights SLAs, accessibility conformance, certification maintenance | Vuln SLAs, incident metrics, penetration test outcomes, security gate pass rate | Quality, velocity, defect escape | Adoption, revenue, outcome KPIs, market expansion |
| **Key artifacts** | ROPA, DPIAs, VPAT/ACR, control matrix, evidence packs, DPAs/BAAs, AI documentation | Threat models, pentest reports, SBOM, security requirements | Specs, code, tests, release notes | Strategy, experiments, roadmap |
| **Risk focus** | Legal/regulatory exposure, fines, market access, contractual breach, class actions (jurisdiction-dependent) | Adversarial exploitation, confidentiality/integrity/availability | Technical and delivery risk | Market and outcome risk |
| **Failure mode** | Fines, stop-processing orders, delisting from enterprise sales, inaccessible product, forced rework | Breach, ransomware, account takeover | Late or brittle delivery | Right execution of the wrong or unlawful thing |

---

## When one is missing

| Scenario | What happens |
|----------|--------------|
| **Compliance without SDLC** | Policies and registers exist, but **implementation drifts** — evidence does not match production; rights requests fail in edge systems. |
| **Compliance without PDLC** | Controls are built for a product **nobody should have shipped** in that market — efficient execution of a non-viable or unlawful strategy. |
| **SDLC without Compliance** | Fast shipping of **non-conforming** software — accessibility gaps, unlawful processing, missing breach or vendor workflows. |
| **PDLC without Compliance** | Roadmap commits to **jurisdictions or data uses** without scoping — late redesign, blocked launch, or post-launch enforcement. |
| **Security without Compliance** | Strong technical protection but **missing legal mechanisms** — e.g., retention beyond lawful periods, or inaccessible security UX blocking users with disabilities. |
| **Compliance without Security** | Paper conformance while **systems remain exploitable** — breach destroys trust and triggers **both** security incident and regulatory notification. |
| **All lenses practiced** | Strategy picks viable markets; delivery embeds controls and evidence; threats are managed alongside obligations. |

---

## Compliance across the lifecycle

| Phase | Compliance role | Key activities | Outputs |
|-------|-----------------|----------------|---------|
| **P1 Discover** | **Obligations explorer** | Scan jurisdictions, user types (children, employees), sensitive data in problem space | Draft applicability matrix, stakeholder map for legal/privacy |
| **P2 Validate** | **Constraint tester** | Prototype flows for consent, notices, accessibility; test if value prop survives minimization | Validation learnings, “compliance feasible” hypotheses |
| **P3 Plan & Commit** | **Regulatory scoper** | Fix target markets; certification needs (SOC 2, ISO); vendor strategy; AI risk class | Compliance scope doc, budget for audits/legal, roadmap constraints |
| **A Discover** | **Requirements analyst (compliance)** | Elicit lawful basis, retention, rights, accessibility acceptance criteria | Compliance-related user stories, legal non-functionals |
| **B Specify** | **Control designer** | Specify data categories, flows, subprocessors; accessibility criteria per epic | Updated specs, DPIA trigger assessment |
| **C Design** | **Architectural compliance** | Privacy boundaries, residency, audit logs, segregation of duties, accessible component patterns | Architecture decision records (compliance), threat+privacy combined reviews |
| **D Build** | **Implementer** | Policy-as-code gates; consent/version APIs; retention jobs; secure configs per **both** security and privacy | Implemented controls, CI evidence hooks |
| **E Verify** | **Assurance** | Accessibility audit (auto+manual), control testing, DPIA closure actions | Test reports, evidence for samples |
| **F Release** | **Release evidence owner** | Final evidence pack slice; subprocessors list accuracy; accessibility statement scope | Release compliance checklist, updated external docs |
| **P4 Launch** | **Go-to-market compliance** | Marketing claims vs. reality; enterprise questionnaires; support scripts for rights/breaches | Launch comms review, support runbooks |
| **P5 Grow** | **Continuous compliance** | Regulatory change management; re-certification; new vendor onboarding; model drift monitoring (AI) | Change log, annual evidence cycles |
| **P6 Sunset** | **Decommission compliance** | Data deletion certificates; archive legal holds; contract terminations; user comms | Sunset attestations, BA/DPA closure |

---

## Role mapping

| Phase(s) | Compliance stance | PDLC accountability | SDLC accountability | Typical partners |
|----------|-------------------|---------------------|---------------------|------------------|
| **P1–P2** | Explore and validate constraints | PM, discovery | Spikes feeding A | Legal, privacy, accessibility |
| **P3** | Scope laws and certifications | PM, strategy | Owner (cost/feasibility) | Legal, DPO, CISO |
| **A–B** | Translate law into requirements | PM prioritization | Owner, BA | Privacy engineer, legal |
| **C** | Design-time proof | Architecture alignment | Implementer, architect | Security, data engineering |
| **D–E** | Build and verify | — | Implementer, QA | AppSec, a11y specialist |
| **F** | Evidence and release | GTM accuracy | Owner go/no-go | Compliance ops, RevOps |
| **P4–P5** | Launch and operate | PM, support, analytics | SRE, on-call | Legal, communications |
| **P6** | Wind-down | PM, legal | Implementer (deletion) | Records management |

---

## Artifact flow

### PDLC / SDLC → Compliance (inputs)

| Source | Compliance usage |
|--------|------------------|
| Market and persona choices (**P1–P3**) | Determine children’s rules, employment algorithms, health/finance triggers |
| Data flows and features (**B–C**) | DPIA/PIA, PCI scope, HIPAA PHI boundaries |
| Vendor selections (**C**, **P3**) | DPAs, BAAs, AI supplier terms, subprocessor registers |
| Security artifacts (**C–E**) | Input to transfer risk analysis, breach assessment, ISO/SOC control mapping |

### Compliance → SDLC (outputs)

| Compliance artifact | SDLC usage |
|---------------------|------------|
| Lawful basis + purpose statements (**A–B**) | Acceptance criteria, analytics constraints |
| Control matrix (**B–C**) | Non-functional requirements, IaC policies |
| Accessibility criteria (**B–E**) | Definition of Done, regression tests |
| Evidence requirements (**E–F**) | Ticket metadata, log retention configs, export jobs |

### Compliance → PDLC (feedback)

| Signal | PDLC usage |
|--------|------------|
| Certification gaps | **P3** reprioritization — defer enterprise segment until Type II |
| Rights backlog / complaints | **P5** product fixes; **P3** scope reduction |
| Regulatory guidance updates | Roadmap adjustments, kill switches for features |

### Security ↔ Compliance (shared boundary)

| Shared topic | Security emphasis | Compliance emphasis |
|--------------|-------------------|---------------------|
| Encryption | Strong crypto, key hygiene | Lawful transfers, adequacy, contractual encryption clauses |
| Logging | Detection and forensics | Retention limits, lawful access, transparency reports |
| Access control | Prevent abuse and lateral movement | Minimization, SoD, ISO/SOC evidence |
| Incidents | Containment and eradication | Breach assessment, notifications, regulator comms |

---

## Calibration

### By regulatory context

| Context | Compliance emphasis |
|---------|---------------------|
| **Unregulated consumer SaaS** | Baseline privacy notices; WCAG AA for broad reach; optional SOC 2 for sales |
| **GDPR / UK / EEA** | Lawful basis, ROPA, DPIAs, transfers, 72h breach playbook, DPO interface, UK Children’s Code if applicable |
| **Healthcare (US HIPAA-class)** | PHI inventory, BAAs, minimum necessary, technical safeguards, breach rule |
| **Financial (payments)** | PCI scope reduction, SAQ path, ASV, segmentation evidence |
| **Financial (public company SOX-relevant systems)** | ITGC, change tickets, access reviews, audit trail integrity |
| **Government / highly regulated procurement** | Accessibility (508 / EN 301 549), data residency, certification schemes |
| **AI-heavy / hiring / credit-adjacent** | EU AI Act class, NYC LL144-style audits, disparate impact analysis where legally relevant |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Compliance as afterthought** | Legal engaged **two weeks before launch**; DPIA written to justify a fait accompli | Involve compliance in **P3** and **A**; gate feasibility on obligations |
| **Checkbox compliance** | Controls chosen to “pass audit” **without operational truth** — screenshots staged, configs reverted | Map controls to **actual** processes; continuous monitoring; ownership by named roles |
| **Gold-plating** | Excessive process for low-risk features — **same DPIA depth** for every CRUD field | Proportionality; tiered assessments; risk-based sampling |
| **Legal-only compliance** | Policies updated but **engineering never implements** | Joint OKRs; compliance engineers embedded; CI policy gates |
| **Security substitutes for privacy** | “We encrypt therefore GDPR done” | Rights, basis, minimization, transfers, and UX are **separate** workstreams |
| **Accessibility last** | Overlay widgets; fixing only automated scan errors | Manual keyboard/screen reader testing; design-system defaults; VPAT scoped honestly |

---

## Worked example

**Scenario:** Launching a **health data feature** (symptom tracking + optional sharing with a clinician portal) for **EU and US** users.

| Step | Lifecycle | What happens |
|------|-----------|----------------|
| 1 | **P3** | Compliance scopes **GDPR** + **HIPAA** (US clinician flow). Decides PHI subset, BAA with clinic integration vendor, need for **DPIA** (special category health data under GDPR). Accessibility **AA** committed for patient-facing UI. |
| 2 | **A** | Requirements: lawful bases documented (consent vs. contract per flow), retention (e.g., delete after account closure with clinical hold exceptions), export for portability, **breach** escalation paths. |
| 3 | **B** | Data map: mobile app → API → regional storage; clinician share = separate channel. DPIA documents risks, mitigations, residual risk sign-off. Security runs overlapping **threat model** for API and tokens. |
| 4 | **C** | Architecture: EU residency option; encryption at rest and in transit; **audit logs** without excessive PHI in log lines; RBAC and SoD for support actions; accessible form components. |
| 5 | **D** | Implement consent versioning, **BAA-gated** environments, automated checks (no public buckets, TLS policies). Feature flags for US vs EU behavior where required. |
| 6 | **E** | Accessibility audit; penetration test on new endpoints; control test: **erasure** propagates to replicas and backups per policy; tabletop **breach** with Legal. |
| 7 | **F** | Evidence: sampled logs, config exports, test reports, updated **ROPA/subprocessors**, privacy notice + accessibility statement scope. |
| 8 | **P4** | Marketing claims reviewed; support trained on rights requests and clinical data corrections. |
| 9 | **P5** | Monitor regulatory updates; periodic vendor reassessment; recertification tasks if ISO/SOC in scope. |
| 10 | **P6** | If feature retired: delete PHI/health data per schedule; retain only legal hold subsets; revoke vendor access. |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`COMPLIANCE.md`](COMPLIANCE.md) | Principles, domains, certification, compliance-as-code |
| [`README.md`](README.md) | Package overview and cross-family relationships |
| [`frameworks/README.md`](frameworks/README.md) | Framework index |
| [`../security/SECURITY.md`](../security/SECURITY.md) | Threat-driven controls and S-SDLC |
| [`../security/SEC-SDLC-PDLC-BRIDGE.md`](../security/SEC-SDLC-PDLC-BRIDGE.md) | Security lifecycle mapping |
| [`../security/compliance/README.md`](../security/compliance/README.md) | Security package’s framework summaries (technical control angle) |
| [`SDLC.md`](../../sdlc/SDLC.md) | Phases A–F |
| [`PDLC.md`](../../pdlc/PDLC.md) | Phases P1–P6 |
| [`UX-SDLC-PDLC-BRIDGE.md`](../product/ux-design/UX-SDLC-PDLC-BRIDGE.md) | Accessibility and consent UX alignment |

---

*Keep project-specific compliance documentation in `docs/security/compliance/`, DPIAs in `docs/security/`, and compliance decisions in `docs/adr/`, not in this file.*
