---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# GDPR: General Data Protection Regulation

**Purpose:** Project-agnostic summary of the EU **General Data Protection Regulation** (Regulation (EU) 2016/679) — the most influential modern privacy law for personal data processing. **Not legal advice**; confirm applicability and interpretation with qualified counsel.

**Audience:** Teams mapping EU/EEA personal data processing to engineering and organizational controls. Cross-ref: [`../COMPLIANCE.md`](../COMPLIANCE.md), [`README.md`](README.md).

---

## Overview

The GDPR governs **processing of personal data** relating to individuals in the EU/EEA. It applies to **controllers** and **processors**, establishes **lawful bases**, **data subject rights**, **accountability** (including DPIAs and ROPA), **cross-border transfers**, and **breach notification**. It has shaped privacy law globally and heavily influences product design, consent UX, and vendor contracts.

---

## Key definitions

| Term | Definition / notes |
|------|-------------------|
| **Personal data** | Any information relating to an identified or identifiable natural person. |
| **Special category data** | Sensitive data (e.g. health, biometrics, racial/ethnic origin, political opinions, religious beliefs, sex life/orientation, genetic data) — stricter rules; often requires explicit consent or specific legal grounds (Art. 9). |
| **Data subject** | The identified or identifiable person to whom personal data relates. |
| **Controller** | Determines **purposes and means** of processing; primary accountability. |
| **Processor** | Processes data **on behalf of** the controller under instructions and a contract (Art. 28). |
| **Sub-processor** | Processor’s further delegate — requires controller authorization (general or specific) and flow-down obligations. |
| **DPO** | **Data Protection Officer** — mandatory in some cases (Art. 37); advises, monitors compliance, cooperates with supervisory authorities. |
| **Supervisory authority** | Independent public authority per Member State; leads investigations, guidance, and some cross-border cases. |
| **BCR** | **Binding Corporate Rules** — approved intra-group transfer mechanism for multinational organizations. |

---

## Lawful bases (Art. 6)

| Basis | When appropriate | Documentation | Withdrawal |
|-------|------------------|---------------|------------|
| **Consent** | Freely given, specific, informed, unambiguous; where no other basis fits or where required (e.g. some marketing, some special categories). | **Record** of consent: what, when, how, version of notice; proof of granularity. | Withdrawal must be as easy as giving consent; must not affect lawfulness **before** withdrawal; stop processing that relied solely on consent. |
| **Contract** | Processing **necessary** for performance of a contract with the data subject or pre-contract steps. | Identify the contract and the **necessary** processing purposes. | N/A as such; if contract ends, retention/ other bases may apply. |
| **Legal obligation** | Processing required to comply with EU/Member State law to which the controller is subject. | Reference specific legal obligation. | N/A. |
| **Vital interests** | Protecting life of data subject or another person (typically emergencies). | Document urgency and why other bases don’t apply. | N/A. |
| **Public task** | Official authority or tasks in the public interest (often public bodies). | Legal basis in law. | N/A for typical public-sector context. |
| **Legitimate interests** | Processing necessary for controller’s or third party’s **legitimate interests**, unless overridden by data subject’s rights (balancing test). | **LIA**: purpose, necessity, balancing, safeguards; not a default for intrusive processing. | Right to **object** (Art. 21) may apply; must stop unless compelling legitimate grounds. |

### Lawful basis selection (decision tree)

```blueprint-diagram
key: decision
alt: Lawful bases (Art. 6)
title: Lawful basis selection gate
summary: How teams validate an Art. 6 basis and documentation before personal data processing proceeds.
node: Lawful bases (Art. 6)
detail: The proposed processing is framed against GDPR Article 6 grounds.
more: Each distinct purpose needs its own basis; consent, contract, and legitimate interests carry different evidence and withdrawal rules on this page.
node: Current state
detail: Capture purpose, data categories, and the processing context under review.
more: Aligns with the lawful-bases table: identify necessity, documentation needs, and whether withdrawal applies.
node: Checkpoint / gate
detail: Test whether one Art. 6 basis clearly and lawfully fits the described processing.
more: Legitimate interests require a documented balancing test; consent is not a default when another basis suffices.
node: refine or escalate
detail: Stop when no basis fits; narrow scope or involve qualified counsel.
more: Undocumented processing should not proceed; this page flags blanket legitimate-interest claims without a recorded LIA.
node: Continue flow
detail: Record the chosen basis and required evidence before engineering implementation.
more: Proceed with rights, retention, and transfer controls traceable in ROPA and DPIA artifacts.
fallback_ascii: |
  Lawful bases (Art. 6)

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

---

## Data subject rights — implementation sketch

| Right | Implementation requirements | SLA (typical reference) | Technical considerations |
|-------|----------------------------|-------------------------|---------------------------|
| **Access** | Verify identity; provide copy of data and purposes, recipients, retention, sources. | **Without undue delay**; often **one month** (extensions possible). | Unified export across DBs, object storage, caches; redact others’ data. |
| **Rectification** | Correct inaccurate data; complete incomplete data. | Same as access timeline expectations. | Propagation to derivatives, search indexes, vendors. |
| **Erasure** (“right to be forgotten”) | Where grounds apply (e.g. withdrawal of consent, no overriding grounds). | Same. | **Erasure pipeline**: primary DB, replicas, backups (policy), logs (where feasible), third parties. |
| **Restriction** | Limit processing in defined cases. | Same. | Feature flags, suspend automated processing, mark records “restricted.” |
| **Portability** | Structured, machine-readable, for data **provided by** subject where processing is automated and based on consent or contract. | Same. | Standard formats (e.g. JSON); APIs. |
| **Object** | To processing based on legitimate interests or direct marketing. | Stop without undue delay for marketing; assess for other objections. | Suppression lists; stop profiling segments. |
| **Automated decision-making** | Rights related to solely automated decisions with legal/significant effects (Art. 22 context). | Human review pathway; explain logic in appropriate cases. | Don’t rely on “black box” for in-scope decisions without safeguards. |

---

## Technical implementation themes

- **Consent management:** Granular purposes; **record** who consented, when, to what version; **withdrawal** in preference center and propagation to tags/SDKs/processors.
- **Privacy by design and by default:** Data protection integrated from architecture; default to least data / least access.
- **Data minimization:** Collect and retain only what is needed for specified purposes.
- **Pseudonymization:** Replace identifiers where useful to reduce risk (not a substitute for lawful basis or transfers analysis alone).
- **Encryption:** At rest and in transit; supports confidentiality and may factor into transfer risk assessments.

### Consent management flow

```blueprint-diagram
key: linear
alt: Technical implementation themes
title: Consent management flow
summary: How granular consent is captured, recorded, and withdrawn across product systems and processors.
node: Technical implementation themes
detail: Consent handling sits within broader privacy-by-design engineering obligations.
more: This section groups consent with minimization, pseudonymization, and encryption as technical themes supporting GDPR accountability.
node: Start
detail: The user encounters a granular, purpose-specific consent choice.
more: Consent must be freely given, specific, informed, and unambiguous per the lawful-bases table above.
node: Core steps (see walkthrough below)
detail: Record consent metadata and wire withdrawal paths to tags, SDKs, and vendors.
more: Capture who consented, when, and which notice version applied; propagate withdrawal to downstream processors under Art. 28 contracts.
node: Outcome
detail: Traceable consent records support accountability and data-subject rights requests.
more: Withdrawal must be as easy as opt-in; stop processing that relied solely on consent after withdrawal without affecting prior lawfulness.
fallback_ascii: |
  Technical implementation themes

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

---

## DPIA (Data Protection Impact Assessment)

**When often required (indicative — verify Art. 35 and WP248/EDPB guidance):**

| Trigger theme | Examples |
|---------------|----------|
| Systematic monitoring | Large-scale tracking, workplace monitoring, public area surveillance. |
| Large-scale processing | Vast datasets or many data subjects for sensitive operations. |
| Special categories | Health, biometrics, etc., at scale or with high risk. |
| Scoring / profiling | Automated profiling with legal or similarly significant effects. |
| Automated decision-making | Decisions with legal/significant effect without meaningful human input. |

**Process:** Describe processing → assess necessity/proportionality → identify risks to rights → measures to mitigate → residual risk → DPO advice → supervisory authority consultation if high residual risk.

**Template sections:** Scope; data flows; purposes and lawful bases; categories of data and subjects; retention; recipients; transfers; technologies; security measures; necessity and proportionality; rights impact; risks; mitigations; sign-off.

---

## Cross-border transfers

- **Adequacy decisions:** Transfers to countries deemed adequate by the European Commission.
- **SCCs:** **Standard Contractual Clauses** (current modules for controller-to-controller, controller-to-processor, etc.) with **Transfer Impact Assessment (TIA)** where local law may impinge on importer obligations.
- **BCRs:** For corporate groups, after approval.
- **Schrems II:** Court emphasis on **effective** protection; TIAs and supplementary measures (technical, organizational, contractual) when needed — encryption and key control may be relevant but are not automatic “fixes.”

---

## Breach notification

- **Supervisory authority:** Notify **without undue delay** and where feasible within **72 hours** unless unlikely to result in risk to individuals (Art. 33).
- **Data subjects:** If breach likely to result in **high risk**, communicate **without undue delay** unless exceptions (e.g. subsequent mitigation) (Art. 34).
- **Documentation:** Internal record of breaches, facts, effects, remedial action (Art. 33(5)).

---

## Records of Processing Activities (ROPA)

**Contents (Art. 30):** Controller/processor name and contact; DPO where applicable; purposes; categories of data subjects and personal data; categories of recipients; transfers and safeguards; retention; security measures. **Processors:** also categories of processing on behalf of each controller.

**Maintenance:** Living document updated when processing changes.

**Exemptions:** Organizations with fewer than 250 employees **unless** processing is not occasional, includes special categories, or is likely to result in risk to rights and freedoms — narrow in practice for many digital products.

---

## Penalty framework

Up to **€20 million** or **4% of global annual turnover** (whichever higher) for certain infringements; lower tier **2% / €10M** for other violations. Fines depend on factors in Art. 83.

| Example (illustrative; amounts/timing vary) | Context |
|---------------------------------------------|---------|
| **Meta** | Major fines tied to data protection / transfers / legal basis issues in EU. |
| **Google** | CNIL and other authorities — consent, transparency, ads. |
| **Amazon** | Luxembourg DPA — cookie/consent and processing practices. |

---

## GDPR vs CCPA / CPRA (high level)

| Topic | GDPR | CCPA / CPRA |
|-------|------|-------------|
| **Scope** | EU/EEA-focused; broad extraterritorial effect for offering services/monitoring behavior. | California consumers; business thresholds. |
| **Default model** | Lawful basis required; consent in specific cases. | Notice + opt-out of sale/share; “limit use” for sensitive data; opt-in for minors under 16. |
| **Rights** | Access, rectification, erasure, restriction, portability, objection, etc. | Know, delete, correct, opt-out, limit, portability (CPRA). |
| **Penalties** | Administrative fines (tiers above). | Statutory damages in private actions (some contexts); AG enforcement. |
| **DPO** | Mandatory in prescribed cases. | No DPO; CPRA requires some businesses to conduct risk assessments / cybersecurity reviews. |

---

## Technical controls mapping

| GDPR theme | Engineering implementation |
|------------|---------------------------|
| Confidentiality / integrity | Encryption, access control, secrets management. |
| Accountability / breach detection | Audit logging, SIEM, anomaly detection. |
| Retention limitation | TTL jobs, legal holds, backup rotation policies. |
| Erasure / portability | Idempotent deletion APIs, export jobs, vendor APIs. |
| Minimization | Schema review, feature flags, sampling for analytics. |

---

## Anti-patterns

- **Consent fatigue:** Walls of popups without real choice or clarity.
- **Data hoarding:** “Collect everything” without purpose or retention discipline.
- **Legitimate interest for everything** without documented LIA and balancing.
- **No data map / ROPA** — cannot demonstrate accountability or respond to rights.

---

## External references

- Full text and commentary: [gdpr-info.eu](https://gdpr-info.eu/)
- **EDPB** guidelines: [edpb.europa.eu](https://edpb.europa.eu/)
- **ICO** (UK) guidance: [ico.org.uk](https://ico.org.uk/)
- **IAPP CIPP/E** and training materials for certification prep

---

*Keep project-specific compliance documentation in docs/security/compliance/, DPIAs in docs/security/, and compliance decisions in docs/adr/, not in this file.*
