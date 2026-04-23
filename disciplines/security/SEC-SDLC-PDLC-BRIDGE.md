---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Security ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **Security** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **Security** — "Is the product **safe from unauthorized access, breaches, and attacks**?"

Security integrates into both lifecycles as a shift-left discipline — embedding security thinking from the earliest product and engineering decisions through operations and incident response.

**Canonical sources:** [`SECURITY.md`](SECURITY.md) (this package) · [`PDLC.md`](../../pdlc/PDLC.md) · [`SDLC.md`](../../sdlc/SDLC.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; how Security relates to PDLC and SDLC |
| [Comparison table](#comparison-table) | Security vs SDLC vs PDLC — scope, ownership, metrics, risks |
| [When one is missing](#when-one-is-missing) | Consequences when Security, SDLC, or PDLC are practiced in isolation |
| [Security across the lifecycle](#security-across-the-lifecycle) | Activities and outputs mapped to PDLC P1–P6 and SDLC A–F |
| [Role mapping](#role-mapping) | Who owns security work at each phase |
| [Artifact flow](#artifact-flow) | Handoffs between Security, SDLC, and PDLC |
| [Calibration](#calibration) | When to invest more or less in security by initiative and context |
| [Anti-patterns](#anti-patterns) | Common failures when security is absent, siloed, or misapplied |
| [Security and SDLC methodologies](#security-and-sdlc-methodologies) | Emphasis across Scrum, Kanban, DevOps-methodology, phased |
| [Worked example](#worked-example) | End-to-end scenario — securing a payment integration |
| [Related reading](#related-reading) | Authoritative docs in this package and sibling lifecycles |

---

## Comparison table

| Dimension | Security | SDLC | PDLC |
|-----------|----------|------|------|
| **Core question** | Is the product safe from unauthorized access, breaches, and attacks? | How do we build this correctly? | Should we build this; does it create the right outcomes? |
| **Scope** | Threat modeling, secure design, authentication/authorization, cryptography, security testing, compliance, incident response, supply chain security | Requirements → design → implementation → verification → release (**A**–**F**) | Problem discovery → validation → strategy → launch → growth → sunset (**P1**–**P6**) |
| **Primary owner** | Security engineer / AppSec — often embedded in delivery teams; CISO for organization-wide governance | Delivery team; **Owner** and **Implementer** per [`SDLC.md`](../../sdlc/SDLC.md) | Product manager / product trio |
| **Timeline** | Continuous — threats evolve; vulnerabilities are disclosed; compliance requirements change | Sprint, iteration, or release train cadence | Product lifetime (months to years) |
| **Success metric** | Vulnerability remediation SLA, SAST/DAST finding trends, time-to-patch, compliance audit results, incident frequency/severity | Velocity, defect escape rate, CI/CD gate pass rate | Adoption, retention, revenue, outcome KPIs |
| **Key artifacts** | Threat models, security requirements, SAST/DAST reports, compliance evidence, incident postmortems, SBOMs | Specs, designs, code, tests, release notes | Research synthesis, experiments, strategy, metrics |
| **Risk focus** | Confidentiality, integrity, availability — can adversaries exploit the system? | Technical risk — correctness, performance, security (as quality attribute) | Market and outcome risk |
| **Failure mode** | Data breach, compliance violation, loss of customer trust, legal liability, operational disruption | Late or low-quality delivery | Right execution of the wrong thing |

---

## When one is missing

| Scenario | What happens |
|----------|-------------|
| **Security without SDLC discipline** | Security requirements exist but implementation is inconsistent — threat model says "encrypt at rest" but nobody verifies it. |
| **Security without PDLC** | Secure product that solves the wrong problem — compliance-heavy but no market fit. |
| **SDLC without Security** | Correct, performant software that is vulnerable — data breaches, compliance fines, customer trust loss. |
| **PDLC without Security** | Product strategy ignores regulatory landscape and data protection — launches in regulated markets without adequate controls; costly retroactive fixes. |
| **All three practiced** | Product direction considers regulatory and trust requirements; engineering embeds security throughout; continuous assurance keeps pace with evolving threats. |

---

## Security across the lifecycle

| Phase | Security role | Key activities | Outputs |
|-------|--------------|----------------|---------|
| **P1 Discover** | **Risk identifier** | Identify data sensitivity in proposed problem space; regulatory landscape scan | Data classification draft, regulatory applicability matrix |
| **P2 Validate** | **Trust assessor** | Evaluate trust implications of solution concepts; identify authentication/privacy needs | Trust requirements, privacy impact assessment (draft) |
| **P3 Plan & Commit** | **Compliance scoper** | Define compliance requirements; security budget; penetration testing cadence | Compliance requirements doc, security investment plan |
| **A Discover** | **Security requirements analyst** | Elicit security requirements; identify abuse cases; map data flows | Security requirements, abuse case catalog |
| **B Specify** | **Threat modeler** | STRIDE/PASTA threat modeling on specified design; security acceptance criteria | Threat model, security-specific acceptance criteria |
| **C Design** | **Secure architect** | Authentication/authorization design; encryption approach; network segmentation; API security | Security architecture document, crypto design, zero-trust boundaries |
| **D Build** | **Secure development enabler** | SAST in CI; dependency scanning; secure coding guidelines; secrets management setup | SAST results, SCA results, secure coding standards |
| **E Verify** | **Security tester** | DAST on staging; penetration testing; security-focused code review; fuzzing | Security test report, vulnerability tickets, compliance evidence |
| **F Release** | **Release security gatekeeper** | Artifact signing; release security checklist; final compliance evidence collection | Signed artifacts, compliance package, residual risk acceptance |
| **P4 Launch** | **Security readiness reviewer** | Pre-launch security review; incident response readiness; monitoring and alerting | Security launch checklist, IR plan activation |
| **P5 Grow** | **Continuous assurance** | Vulnerability management; ongoing compliance; threat intelligence; bug bounty | Vulnerability reports, compliance audit results, patching metrics |
| **P6 Sunset** | **Data protection officer** | Data retention/deletion; access revocation; credential rotation; archive security | Data deletion certificates, access audit, decommission security checklist |

---

## Role mapping

| Phase(s) | Security stance | PDLC accountability | SDLC accountability | Archetype |
|----------|----------------|---------------------|---------------------|-----------|
| **P1–P2** | **Risk identifier** — data sensitivity and regulatory scan | PM, discovery trio | — (upstream of SDLC) | Demand & value |
| **P3** | **Compliance scoper** — requirements and budget | PM, strategy | Owner (feasibility, compliance cost) | Steer & govern |
| **A** | **Security requirements analyst** | — | Owner (priorities); Implementer (security spikes) | Demand & value |
| **B** | **Threat modeler** | — | Owner (acceptance criteria); Implementer (threat modeling participation) | Build & integrate |
| **C** | **Secure architect** | — | Implementer (architecture); Owner (risk acceptance) | Build & integrate |
| **D** | **Secure dev enabler** | — | Implementer (secure code); Owner removes blockers | Build & integrate |
| **E** | **Security tester** | — | Implementer (remediate); Assure & ship (gate interpretation) | Assure & ship |
| **F** | **Release gatekeeper** | GTM for compliance comms | Implementer (signing, checklist); Owner (go/no-go on residual risk) | Assure & ship |
| **P4** | **Readiness reviewer** | PM, GTM | SDLC F overlaps — production cutover | Assure & ship |
| **P5** | **Continuous assurance** | PM, analytics | Iteration cycles A–F for patches | Flow & improvement |
| **P6** | **Data protection** | PM, legal | Implementer (deletion, revocation) | Steer & govern |

---

## Artifact flow

### PDLC / SDLC → Security (inputs)

| Source | Security usage |
|--------|---------------|
| Data classification and user personas (**P1**, **P3**) | Define what data to protect and at what level |
| Functional requirements and data flows (**B**) | Scope threat modeling; identify trust boundaries |
| Architecture diagrams (**C**) | Identify attack surface; map network segmentation |
| Deployment topology (DevOps, **C**) | Define infrastructure security controls; container security |
| Compliance requirements (**P3**, Steer & govern) | Map regulatory controls to technical implementation |

### Security → SDLC (outputs)

| Security artifact | SDLC usage |
|-------------------|------------|
| Threat model and security requirements (**B**, **C**) | Feed functional spec and acceptance criteria |
| SAST/SCA results (**D**) | Block merge on high-severity findings |
| DAST/pentest results (**E**) | Feed defect backlog with severity-rated security issues |
| Signed artifacts (**F**) | Deployment pipeline verifies signatures |
| Compliance evidence (**E**, **F**) | Audit readiness package |

### Security → PDLC (feedback)

| Security signal | PDLC usage |
|-----------------|------------|
| Vulnerability trends and incident metrics | Risk input to product strategy (**P3**, **P5**) |
| Compliance audit results | Go/no-go for market expansion, partnership, or certification |
| Threat landscape changes | Inform product roadmap — new authentication methods, privacy features |
| Incident postmortem themes | Surface systemic product or UX issues that increase security risk |

---

## Calibration

### By initiative type

| Situation | Security investment | Reasoning |
|-----------|-------------------|-----------|
| **Greenfield product** | **High** — threat model, authentication/authorization architecture, compliance scoping, SAST/SCA from day one | Security foundations are cheapest to establish early; retroactive fixes are 10–100x more expensive |
| **Feature touching auth/payments/PII** | **High** — targeted threat model, penetration testing, compliance impact assessment | These features are prime attack targets; regulatory implications |
| **Internal tool** | **Medium** — standard auth, network segmentation, input validation; reduced compliance burden | Lower exposure but insider threat and lateral movement risk remain |
| **API / integration** | **High** — API security review, rate limiting, input validation, OAuth scoping | APIs are the most common attack vector for modern applications |
| **UI-only change** | **Low–medium** — XSS review, CSRF tokens, content security policy verification | Lower risk but frontend vulnerabilities (XSS, open redirect) are common |
| **Spike / prototype** | **Low** — no real data, no production exposure; document known gaps | Match security investment to lifetime and data sensitivity |

### By regulatory context

| Context | Security emphasis |
|---------|-------------------|
| **Unregulated SaaS** | OWASP Top 10, SOC 2 Type II (for enterprise sales), standard vulnerability management |
| **Financial services** | PCI-DSS (if payment data), SOC 2, encryption mandates, audit trails, change management |
| **Healthcare** | HIPAA technical safeguards, BAAs, PHI encryption, access logging, breach notification |
| **Government** | FedRAMP, NIST 800-53, data sovereignty, supply chain requirements |
| **EU markets** | GDPR data protection, privacy by design, DPIA, right to erasure, breach notification |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Security as a gate at the end** | Security review only before release; findings are expensive to fix and delay launch | Shift left — threat modeling in C, SAST in D, DAST in E; continuous, not final |
| **Compliance checkbox** | Implementing controls to pass audit without understanding the threat they address | Threat-driven security — model threats first, then map controls to actual risks |
| **Security team as bottleneck** | Central security team reviews everything; becomes a queue | Enable teams with tooling, training, and guardrails; security reviews for high-risk changes only |
| **Vulnerability fatigue** | Thousands of unpatched findings; teams ignore scanner output | Risk-based prioritization; SLA by severity; fix high/critical within days, not months |
| **Security theater** | Visible but ineffective controls (complex password rules that cause post-it notes, CAPTCHA that frustrates users) | Evidence-based controls; measure effectiveness; balance security with usability |

---

## Security and SDLC methodologies

| Methodology | Security emphasis |
|-------------|-------------------|
| **Scrum** | Security stories in sprint backlog; threat modeling during refinement; SAST/DAST results in sprint review |
| **Kanban** | Security tasks flow through the board; WIP limits prevent security work from being deprioritized |
| **DevOps** | DevSecOps — security checks automated in CI/CD; infrastructure security as code; shift-left and continuous |
| **XP** | Pair programming catches security issues; TDD includes security test cases; simple design reduces attack surface |
| **Phased** | Formal security review at phase gates; penetration testing before phase transition; compliance evidence at each gate |

---

## Worked example

**Scenario:** A B2B SaaS product integrates a **third-party payment processor** to support in-app purchases. The integration handles credit card tokenization (no raw card data stored) and transaction records.

| Step | Lifecycle | What happens |
|------|-----------|--------------|
| 1 | **P3** | Compliance scoper identifies PCI-DSS SAQ A-EP applicability (redirected payment, but page hosted by merchant). Maps 40+ controls. Budget allocated for annual penetration test and quarterly ASV scan. |
| 2 | **A** | Security requirements analyst defines: tokenized card handling only, no PAN storage, TLS 1.2+ for all payment endpoints, audit logging for all transaction operations. |
| 3 | **B** | Threat modeler runs STRIDE on the payment data flow: token exchange, callback verification, refund flow. Identifies risks: callback spoofing, IDOR on transaction history, CSRF on purchase action. Security acceptance criteria added to each story. |
| 4 | **C** | Secure architect designs: payment service isolated in separate container with restricted network policy; webhook signature verification; idempotency keys; encrypted transaction records; API key rotation mechanism. |
| 5 | **D** | Secure dev enabler adds SAST rules for payment code (no logging of tokens, no hardcoded API keys). SCA confirms payment SDK has no known CVEs. Secrets management via Vault for processor API keys. |
| 6 | **E** | Security tester runs DAST against payment endpoints in staging — verifies no IDOR, CSRF protection works, error messages do not leak transaction details. External penetration test confirms webhook signature validation. |
| 7 | **F** | Release gatekeeper verifies: artifact signed, PCI evidence collected (network segmentation proof, encryption verification, access log samples), residual risk documented and accepted by Owner. |
| 8 | **P4** | Security readiness reviewer confirms: incident response plan updated for payment-related incidents, monitoring alerts for unusual transaction patterns, fraud detection threshold set. |
| 9 | **P5** | Continuous assurance: quarterly ASV scans, annual pen test, payment SDK dependency monitoring, transaction anomaly alerts feeding incident response. |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`SECURITY.md`](SECURITY.md) | Threat modeling, OWASP, authentication, cryptography, S-SDLC, incident response |
| [`practices/README.md`](practices/README.md) | Threat modeling, security testing, incident response, supply chain security |
| [`compliance/README.md`](compliance/README.md) | SOC 2, GDPR, HIPAA, PCI-DSS control mappings |
| [`SDLC.md`](../../sdlc/SDLC.md) | Delivery phases A–F, DoD |
| [`PDLC.md`](../../pdlc/PDLC.md) | Product phases P1–P6 |
| [`DEVOPS-SDLC-PDLC-BRIDGE.md`](../engineering/devops/DEVOPS-SDLC-PDLC-BRIDGE.md) | DevSecOps — security automation in CI/CD |
| [`ARCH-SDLC-PDLC-BRIDGE.md`](../engineering/software-architecture/ARCH-SDLC-PDLC-BRIDGE.md) | Security as architecture quality attribute |
| [`roles-archetypes.md`](../../sdlc/methodologies/roles-archetypes.md) | SDLC role archetypes |
