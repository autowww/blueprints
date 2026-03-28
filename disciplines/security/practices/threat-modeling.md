# Threat modeling — methodologies and practice

**Purpose:** A **project-agnostic** blueprint for systematically identifying, analyzing, and mitigating security threats before they are exploited.

**Audience:** Architects, security champions, and delivery teams integrating threat modeling into design and architecture reviews.

---

## Overview

Threat modeling is a **structured, repeatable** way to understand what can go wrong in a system, who might abuse it, and what to do about it. It connects **assets, trust boundaries, and data flows** to concrete threats and mitigations, so security requirements emerge from design rather than from late-stage surprises.

Effective threat modeling is **iterative**: the model evolves with the architecture, and mitigations become trackable work items (often expressed as security requirements or backlog items).

---

## Methodology comparison

| Methodology | Scope | Approach | Typical outputs | Relative effort | Best for |
|-------------|--------|----------|-----------------|-----------------|----------|
| **STRIDE** | System / component | Categorize threats by type (Spoofing, Tampering, Repudiation, Information disclosure, DoS, Elevation) against diagrams and assets | DFD or architecture diagram, threat list, mitigations mapped to STRIDE | Low–medium | Microsoft-centric teams, fast workshops, teaching threat categories |
| **PASTA** | End-to-end risk | Seven-stage process from context to attack simulation and business impact | Risk register, attack narratives, prioritized scenarios | High | Regulated environments, risk-driven prioritization, alignment with business impact |
| **LINDDUN** | Privacy | Privacy threat taxonomy (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure, Unawareness, Non-compliance) | Privacy threat list, DPIA inputs | Medium | GDPR/privacy-by-design, personal data flows |
| **Attack trees** | Specific goals | Decompose attacker objective into sub-goals and steps | Tree diagrams, weakest-path analysis | Medium | High-value targets, red-team alignment, explaining exploit chains |
| **VAST** | Enterprise + agile | Visual, Agile, Simple Threat modeling — scales across org and sprints | Visual models, sprint-level deltas, portfolio view | Medium–high | Large programs needing consistent practice across many teams |
| **OCTAVE** | Organizational risk | Asset-driven, workshop-based operational risk assessment | Asset profiles, threat profiles, mitigation plans | High | Non-technical stakeholders, operational risk, maturity building |

---

## STRIDE deep dive: from diagram to mitigation

STRIDE works best when you **anchor threats to elements** of a data flow diagram (DFD) and **trust boundaries**.

```blueprint-diagram
key: swimlane
alt: Diagram
```

For each **element** (entity, process, store, flow), ask which STRIDE categories apply, document the threat in plain language, rate risk, and map to a mitigation or compensating control.

---

## DFD elements and STRIDE applicability

| Element | Notation / meaning | STRIDE lens |
|---------|-------------------|-------------|
| **External entity** | Person or system outside your control (user, partner API, browser) | Spoofing of identity; repudiation if actions are not logged |
| **Process** | Code or service that transforms data | Tampering of logic or inputs; elevation if process runs with excess privilege; DoS via resource abuse |
| **Data store** | Database, queue, bucket, file system | Information disclosure; tampering at rest; repudiation without audit |
| **Data flow** | Data in transit between elements | Information disclosure (sniffing, MITM); tampering in transit |
| **Trust boundary** | Where trust assumptions change (internet ↔ DMZ, tenant ↔ tenant) | Concentration of spoofing, disclosure, and elevation risks at crossing points |

---

## PASTA — seven stages

| Stage | Focus |
|-------|--------|
| 1 — **Technology environment** | Business context, crown jewels, stack inventory, external dependencies |
| 2 — **Application decomposition** | Architecture, components, data flows, trust boundaries, entry points |
| 3 — **Application analysis** | Trust relationships, assets, security controls already in place |
| 4 — **Threat analysis** | Threat agents, motives, capabilities mapped to the decomposed system |
| 5 — **Vulnerability analysis** | Design weaknesses, implementation flaws, configuration gaps |
| 6 — **Attack enumeration** | Attack paths, scenarios, likelihood, required attacker access |
| 7 — **Risk and impact analysis** | Business impact, risk scoring, countermeasures, residual risk |

---

## Threat modeling at different scales

| Scale | Scope | Typical frequency | Participants | Outputs |
|-------|--------|-------------------|--------------|---------|
| **Feature-level** | User story, API change, new integration | Each sprint or major feature | Dev, PM, security champion | Lightweight DFD or sequence sketch, STRIDE bullets, security tasks in backlog |
| **System-level** | Service boundaries, auth, data stores | Architecture reviews, major releases | Architect, SRE, security, leads | Full DFD, threat matrix, security requirements, ADRs |
| **Organizational** | Portfolio, shared platforms, third parties | Quarterly or annual risk cycles | Risk, security, business owners | Risk register, program roadmap, control gaps |

---

## Workshop flow (sequence)

```blueprint-diagram
key: sequence
alt: Diagram
```

---

## Risk rating approaches

| Approach | Dimensions / inputs | Strengths | Caveats |
|----------|---------------------|-----------|---------|
| **DREAD** | Damage, Reproducibility, Exploitability, Affected users, Discoverability (each scored, often 1–10) | Fast team conversation; intuitive | Subjective; Microsoft deprecated DREAD internally — still useful as a workshop scaffold |
| **CVSS** | Base / temporal / environmental vectors for vulnerabilities | Standardized for CVE-style issues; good for vuln management | Less natural for **design** threats not yet tied to a CVE |
| **Qualitative** | Low / Medium / High using criteria tables | Simple governance and SLAs | Needs calibration to avoid grade inflation |

Use **qualitative or DREAD** in design workshops; use **CVSS** when linking to published vulnerabilities or scanner findings.

---

## Threat library patterns (by STRIDE)

| STRIDE | Web apps | APIs | Mobile | IoT | Cloud |
|--------|----------|------|--------|-----|-------|
| **Spoofing** | Session fixation, weak cookie flags | Broken OAuth, API keys in clients | Stolen refresh tokens, device binding gaps | Default credentials, weak pairing | IAM misconfiguration, assumed roles |
| **Tampering** | CSRF, mass assignment | Parameter pollution, deserialization | Jailbreak / repackaged apps | OTA without signing | Mutable bucket policies, supply chain |
| **Repudiation** | Missing audit on admin actions | No correlation IDs on sensitive ops | Client-only “proof” of action | Sparse device logs | Centralized logging disabled |
| **Information disclosure** | IDOR, verbose errors | Over-exposure in GraphQL/BOLA | Local data on device, screenshots | Debug interfaces | Public snapshots, metadata leaks |
| **Denial of service** | Login flooding, expensive queries | Unauthenticated expensive endpoints | Local resource exhaustion | Radio jamming (adjacent) | Autoscaling abuse, Lambda bombs |
| **Elevation** | Broken access control | Broken object-level auth | Escaping app sandbox | Firmware update abuse | Over-privileged service accounts |

Treat this table as **prompts**, not an exhaustive catalog — always validate against **your** diagram and data classification.

---

## Tool comparison

| Tool | Features | Cost model | Integration notes |
|------|----------|------------|-------------------|
| **Microsoft Threat Modeling Tool** | STRIDE, DFD, threat generation | Free (legacy tooling; check current support) | Windows-centric; good for STRIDE teaching |
| **OWASP Threat Dragon** | Diagrams, STRIDE, export | Open source | Web/desktop; fits Git-friendly workflows |
| **IriusRisk** | Centralized models, risk scoring, workflows | Commercial | Enterprise GRC and Jira-style tracking |
| **Threagile** | Code-first / YAML models, automation | Open source | Fits GitOps and pipeline-driven updates |

---

## Integration with SDLC

| Phase | Threat modeling activity | Artifacts |
|-------|-------------------------|-----------|
| **Design (e.g., Phase C)** | Model new boundaries, flows, and stores; update trust assumptions | DFD or architecture threat model, security requirements |
| **Implementation** | Verify mitigations in code review and tests | Linked tickets, test cases |
| **Release / change** | Revalidate when auth, data paths, or integrations change | Updated model version, delta notes |

Track mitigations as **security requirements** with owners and dates; link to **`docs/adr/`** when a design decision materially changes the threat landscape.

---

## Threat model lifecycle

```blueprint-diagram
key: linear
alt: Diagram
```

---

## Anti-patterns

| Anti-pattern | Why it hurts | Better approach |
|--------------|--------------|-----------------|
| **Threat modeling too late** | Expensive rework; mitigations become “bolt-on” | Time-box a model **before** major build commitments |
| **Security-only participants** | Miss real constraints and ownership | Include engineers, PM, and ops in workshops |
| **No follow-through on mitigations** | Model becomes shelf-ware | Every threat has owner, priority, and tracking |
| **One-time exercise** | Drift as system evolves | Tie updates to architecture reviews and significant features |

---

## External references

- Adam Shostack, *Threat Modeling: Designing for Security*
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- Microsoft STRIDE and threat modeling documentation (archive / successor guidance as applicable)
- PASTA methodology publications and training (OWASP and industry sources)

---

*Keep project-specific security documentation in docs/security/, threat models in docs/security/threat-models/, and security decisions in docs/adr/, not in this file.*
