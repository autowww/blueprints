# HIPAA: Health Insurance Portability and Accountability Act

**Purpose:** Project-agnostic overview of **US HIPAA** (and related **HITECH**) obligations for **PHI** in covered healthcare flows. **Not legal advice**; confirm coverage (covered entity vs business associate) with counsel.

**Audience:** Teams building or operating systems that create, receive, maintain, or transmit **PHI** in the United States. Cross-ref: [`../COMPLIANCE.md`](../COMPLIANCE.md), [`README.md`](README.md).

---

## Overview

HIPAA is US federal law protecting **health information** held by **covered entities** and their **business associates**. It combines **Privacy**, **Security**, and **Breach Notification** rules (among others) with **enforcement** through OCR and state AGs in some cases. Engineering must align with **minimum necessary**, **safeguards**, **BAAs**, and **auditability** — not only “encryption on the wire.”

---

## Key definitions

| Term | Definition / notes |
|------|-------------------|
| **PHI** | **Protected Health Information** — individually identifiable health information held or transmitted by a covered entity or BA in any form or medium (with specific exclusions, e.g. certain education/employment records in defined contexts). |
| **ePHI** | PHI in **electronic** form — primary focus of the **Security Rule**. |
| **Covered entity** | **Health plans**, **health care providers** who transmit covered transactions electronically, **health care clearinghouses**. |
| **Business associate** | Person/entity performing **covered functions or activities** involving PHI on behalf of a covered entity (or another BA) — requires **BAA**. |
| **Minimum necessary** | Use, disclosure, and requests limited to the **minimum** PHI necessary for the purpose (exceptions apply, e.g. treatment, individual access). |
| **Designated record set** | Group of records used to make decisions about individuals — informs access/amendment rights under Privacy Rule. |

---

## HIPAA rules overview

| Rule | Scope / key requirements |
|------|-------------------------|
| **Privacy Rule** | Permitted uses/disclosures; individual rights (access, amendment, accounting); notices of privacy practices; minimum necessary. |
| **Security Rule** | Administrative, physical, and **technical** safeguards for **ePHI**; risk analysis; policies and procedures. |
| **Breach Notification Rule** | Notify individuals, HHS, and media (when applicable) for **unsecured** PHI breaches per defined timelines and thresholds. |
| **Enforcement Rule** | Penalties; complaint investigation; CMP procedures. |
| **Omnibus Rule** | BA liability extensions; strengthened Privacy/Security provisions (2013) — aligns with HITECH themes. |

---

## Security Rule — Administrative safeguards (45 CFR §164.308)

| Standard | Key expectations |
|----------|------------------|
| **Security management process** | Risk analysis; risk management; sanction policy; information system activity review. |
| **Assigned security responsibility** | Identify security official. |
| **Workforce security** | Authorization/supervision; workforce clearance; termination procedures. |
| **Information access management** | Access authorization; access establishment/modification. |
| **Security awareness and training** | Security reminders; protection from malware; log-in monitoring; password management. |
| **Security incident procedures** | Identify, report, respond to incidents. |
| **Contingency plan** | Data backup; disaster recovery; emergency mode; testing. |
| **Evaluation** | Periodic technical/non-technical evaluation. |
| **Business associate contracts** | BAAs and required provisions for BAs. |

---

## Physical safeguards (§164.310)

| Standard | Key expectations |
|----------|------------------|
| **Facility access controls** | Contingency operations; facility security plan; access control/validation; maintenance records. |
| **Workstation use** | Appropriate use of workstations. |
| **Workstation security** | Physical protections for workstations. |
| **Device and media controls** | Disposal; media re-use; accountability; data backup/storage. |

---

## Technical safeguards (§164.312)

| Standard | Key expectations |
|----------|------------------|
| **Access control** | Unique user identification; emergency access procedure; automatic logoff; **encryption and decryption** of ePHI where appropriate. |
| **Audit controls** | Hardware, software, procedural mechanisms to **record and examine** activity in systems with ePHI. |
| **Integrity** | Mechanisms to authenticate ePHI (e.g. against improper alteration/destruction). |
| **Person or entity authentication** | Verify persons/entities seeking access. |
| **Transmission security** | Integrity controls; **encryption** for ePHI transmitted over electronic communications networks where appropriate. |

### HIPAA compliance architecture (conceptual)

```blueprint-diagram
key: swimlane
alt: Diagram
```

---

## BAA (Business Associate Agreement)

**Typical required themes:** Permitted uses/disclosures; **not** use beyond agreement; safeguards; **subcontractor** flow-down; breach notification to CE; access to records for HHS; return/destruction of PHI at termination; agent status where applicable.

**Chain:** CE → BA → **subcontractor BA** — each link needs appropriate assurances; **due diligence** on vendor practices.

---

## Minimum necessary — implementation

- **Role-based access** to PHI aligned with job function.
- **Data segmentation** — separate PHI stores from general app data where feasible; avoid broad replication.
- **UI/API design** — expose only fields needed for the workflow (not full charts for a billing-only role).

---

## Breach notification (unsecured PHI)

**Unsecured PHI:** PHI not rendered unusable/unreadable/indistinguishable through a method specified in guidance (e.g. valid encryption per HHS guidance).

| Audience | Requirement (simplified) |
|----------|-------------------------|
| **Individuals** | **Without unreasonable delay**, no later than **60 days** from discovery; content per rule. |
| **HHS** | Timing depends on size of breach (e.g. >500 in a state/jurisdiction → **within 60 days**; smaller → annual log). |
| **Media** | **>500** residents of a state/jurisdiction → prominent media outlet in that jurisdiction. |

**Risk assessment:** Four-factor assessment (nature/extent of PHI; unauthorized person; acquisition/view; extent of mitigation) may determine if notification is **not** required for unsecured PHI in limited cases — document carefully.

---

## HIPAA and cloud computing

Major clouds offer **HIPAA-eligible** services and will enter a **BAA** — **shared responsibility**: cloud secures the **platform**; customer configures access, encryption, logging, app-layer PHI handling.

**Implications:** No PHI in **non-eligible** services; correct encryption key ownership; logging to compliant stores; subprocessors reviewed under BAA.

---

## HIPAA compliance checklist (engineering-oriented)

1. **Risk analysis** (Security Rule) — inventory ePHI, threats, vulnerabilities, mitigations.
2. **Policies and procedures** — access, incident response, backup, workforce.
3. **Training** — workforce on policies and phishing/social engineering.
4. **BAAs** — before any BA receives/maintains/transmits PHI.
5. **Incident response** — detect, contain, assess breach definition, notify per rule.
6. **Audit controls** — logging, review, alerting on sensitive access.

---

## HITECH Act (high level)

- **Increased penalties** and tiered structure (see below).
- **Breach notification** strengthened and aligned with practical enforcement.
- **Business associates** directly liable for certain HIPAA Security/Privacy Rule compliance and civil penalties.

---

## Penalty tiers (illustrative — verify current amounts)

| Tier | Mental state / correction | Characterization |
|------|---------------------------|------------------|
| **1** | Did not know and could not have known | Lowest range. |
| **2** | Reasonable cause, not willful neglect | Mid-low range. |
| **3** | Willful neglect, **corrected** within required time | Mid-high range. |
| **4** | Willful neglect, **not corrected** | Highest range. |

OCR publishes **enforcement** examples and settlement agreements illustrating real failures (e.g. lack of risk analysis, missing BAAs, insufficient access controls).

---

## Technical implementation mapping

| HIPAA / Security Rule theme | Engineering control |
|----------------------------|---------------------|
| Access | Unique IDs, RBAC, MFA, break-glass with logging. |
| Audit | Immutable or WORM-capable logs, SIEM, periodic review. |
| Integrity | Checksums, signed artifacts, DB constraints. |
| Transmission | TLS; VPN where appropriate; no PHI in query strings. |
| Availability | Backup, RTO/RPO tested restores. |
| Minimum necessary | Field-level authorization, scoped APIs, views not tables. |

---

## Anti-patterns

- **“We’re on AWS/Azure/GCP so we’re HIPAA compliant”** — without BAA, eligible services, and correct configuration.
- **Vendors touching PHI without a BAA.**
- **PHI in application or access logs** — stack traces, URL params, debug dumps.
- **Over-collection** of health-adjacent data “just in case.”

---

## External references

- **HHS HIPAA:** [hhs.gov/hipaa](https://www.hhs.gov/hipaa/index.html)
- **NIST SP 800-66** — HIPAA Security Rule implementation guide (maps to NIST CSF concepts).
- **ONC Health IT** — health IT certification and related guidance.
- **HITRUST CSF** — harmonized control framework often used in healthcare vendor diligence.

---

*Keep project-specific compliance documentation in docs/security/compliance/, DPIAs in docs/security/, and compliance decisions in docs/adr/, not in this file.*
