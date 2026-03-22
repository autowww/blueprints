# Security body of knowledge

This document maps the core concerns of **Security / Cybersecurity** — threat modeling, secure design, authentication, cryptography, security testing, compliance, and incident response — to the blueprint ecosystem.

**How security relates to PDLC and SDLC:** Security is a **cross-cutting discipline** that integrates into every lifecycle phase as a shift-left practice. See [`SEC-SDLC-PDLC-BRIDGE.md`](SEC-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Practices:** Threat modeling, secure code review, security testing, and incident response guides are in [`practices/`](practices/README.md).

**Compliance:** Regulatory compliance is now a standalone cross-cutting discipline — see [`Compliance`](../compliance/README.md) for framework-specific control mappings (GDPR, HIPAA, PCI-DSS, WCAG, SOC 2, AI Act, ISO 27001).

---

## 1. Security principles

| Principle | Description |
|-----------|-------------|
| **Defense in depth** | Layer multiple controls so that failure of one does not compromise the system |
| **Least privilege** | Grant only the minimum access necessary for each role, service, or process |
| **Secure by default** | Systems ship with secure configurations; insecure options require explicit opt-in |
| **Fail securely** | Error conditions default to denial of access; exceptions do not leak sensitive information |
| **Zero trust** | Verify explicitly, assume breach — authenticate and authorize every request regardless of network location |
| **Separation of duties** | Critical operations require approval from multiple parties; no single actor can complete a sensitive workflow alone |
| **Minimize attack surface** | Remove unnecessary features, endpoints, dependencies, and permissions |
| **Audit and accountability** | Log security-relevant events; maintain tamper-evident audit trails; support forensic investigation |

---

## 2. Threat modeling

### STRIDE model

| Threat | Definition | Example | Mitigation category |
|--------|-----------|---------|---------------------|
| **Spoofing** | Impersonating a user or system | Stolen credentials, forged tokens | Authentication |
| **Tampering** | Modifying data or code | SQL injection, parameter manipulation, supply chain attack | Integrity controls |
| **Repudiation** | Denying having performed an action | User claims they did not authorize a transaction | Audit logging, non-repudiation |
| **Information disclosure** | Exposing data to unauthorized parties | Verbose error messages, unencrypted storage, API over-fetching | Confidentiality controls |
| **Denial of service** | Making the system unavailable | Resource exhaustion, algorithmic complexity attacks | Availability controls |
| **Elevation of privilege** | Gaining unauthorized capabilities | Broken access control, insecure deserialization | Authorization |

### Threat modeling process

| Step | Activity | Output |
|------|----------|--------|
| 1. **Scope** | Define what is being modeled (system, feature, data flow) | Scope document, data flow diagram |
| 2. **Identify threats** | Apply STRIDE (or PASTA, attack trees) to each element in the DFD | Threat list with affected components |
| 3. **Assess risk** | Rate likelihood and impact (DREAD, CVSS, or qualitative) | Prioritized threat register |
| 4. **Mitigate** | Define controls for high-risk threats; accept, transfer, or avoid remainder | Mitigation plan, security requirements |
| 5. **Validate** | Verify mitigations through testing, review, or audit | Test results, residual risk acceptance |

---

## 3. OWASP Top 10 (web applications)

| # | Risk | Prevention |
|---|------|------------|
| A01 | **Broken access control** | Server-side enforcement, deny by default, RBAC/ABAC, rate limiting, CORS configuration |
| A02 | **Cryptographic failures** | TLS everywhere, strong algorithms (AES-256, SHA-256+), key management, no secrets in code |
| A03 | **Injection** | Parameterized queries, input validation, context-aware output encoding, ORM usage |
| A04 | **Insecure design** | Threat modeling, secure design patterns, abuse case analysis, security requirements |
| A05 | **Security misconfiguration** | Hardened defaults, automated configuration scanning, no default credentials, minimal permissions |
| A06 | **Vulnerable and outdated components** | SCA scanning, dependency update policy, SBOM generation, known-vulnerability monitoring |
| A07 | **Identification and authentication failures** | MFA, credential stuffing protection, secure session management, password policy |
| A08 | **Software and data integrity failures** | CI/CD pipeline security, artifact signing, subresource integrity, update verification |
| A09 | **Security logging and monitoring failures** | Centralized logging, security event detection, alerting, incident response integration |
| A10 | **Server-side request forgery (SSRF)** | Input validation, allowlist outbound connections, network segmentation, disable redirects |

---

## 4. Authentication and authorization

### Authentication patterns

| Pattern | Use case | Trade-off |
|---------|----------|-----------|
| **Session-based** | Traditional web apps; server-rendered pages | Simple; requires server-side session store; harder to scale horizontally |
| **JWT (stateless)** | APIs, SPAs, microservices | Scalable; cannot revoke individual tokens without a blocklist |
| **OAuth 2.0 + OIDC** | Third-party login, API authorization, federated identity | Standard; complex grant flows; requires understanding of token types |
| **API keys** | Server-to-server, developer APIs | Simple; no user context; hard to rotate at scale |
| **mTLS** | Service-to-service in zero-trust environments | Strong; complex certificate management |
| **Passkeys / WebAuthn** | Passwordless authentication | Phishing-resistant; device-bound; recovery flows are complex |

### Authorization models

| Model | Description | Best fit |
|-------|-------------|----------|
| **RBAC** (Role-Based Access Control) | Permissions assigned to roles; users assigned to roles | Applications with well-defined role hierarchies |
| **ABAC** (Attribute-Based Access Control) | Policies evaluate attributes of user, resource, action, and context | Fine-grained, dynamic access decisions |
| **ReBAC** (Relationship-Based Access Control) | Authorization based on relationships between entities (e.g. Zanzibar/OpenFGA) | Document sharing, social features, multi-tenant systems |
| **ACL** (Access Control List) | Per-resource permission lists | File systems, simple resource-level control |

---

## 5. Cryptography fundamentals

| Concern | Guidance |
|---------|----------|
| **Encryption at rest** | AES-256 for data stores; use platform-managed keys (KMS) unless compliance requires customer-managed |
| **Encryption in transit** | TLS 1.2+ mandatory; TLS 1.3 preferred; HSTS headers; certificate management and rotation |
| **Hashing** | bcrypt, scrypt, or Argon2 for passwords; SHA-256+ for integrity; never MD5 or SHA-1 |
| **Key management** | Centralized KMS; automatic rotation; separation of key custodians; never store keys in code |
| **Signing** | Ed25519 or RSA-PSS for signatures; artifact and commit signing; JWT signature verification |
| **Secrets management** | Vault, cloud secret managers; inject at runtime, not build time; audit access; rotate regularly |

---

## 6. Security testing

| Type | When | What it catches | Tools (examples) |
|------|------|----------------|-----------------|
| **SAST** (Static Application Security Testing) | Build / PR | Code-level vulnerabilities — injection, hardcoded secrets, insecure patterns | Semgrep, SonarQube, CodeQL |
| **DAST** (Dynamic Application Security Testing) | Staging / pre-release | Runtime vulnerabilities — XSS, CSRF, auth bypass, header misconfig | OWASP ZAP, Burp Suite, Nuclei |
| **SCA** (Software Composition Analysis) | Build / continuous | Known vulnerabilities in dependencies; license compliance | Snyk, Dependabot, Trivy |
| **IAST** (Interactive Application Security Testing) | Test execution | Instrumented runtime analysis combining SAST and DAST signals | Contrast Security |
| **Container / image scanning** | Build / deploy | Vulnerable base images, misconfigurations, excessive permissions | Trivy, Grype, Snyk Container |
| **Infrastructure scanning** | Continuous | IaC misconfigurations, cloud security posture | Checkov, tfsec, Prowler |
| **Penetration testing** | Periodic (quarterly–annually) | Business-logic flaws, chained exploits, social engineering | Manual testing, Cobalt, HackerOne |
| **Fuzzing** | Build / integration | Input handling crashes, buffer overflows, unexpected behavior | AFL++, libFuzzer, Jazzer |

---

## 7. Secure SDLC (S-SDLC)

Integrating security into each SDLC phase rather than bolt-on testing at the end.

| SDLC phase | Security activity | Output |
|------------|-------------------|--------|
| **A Discover** | Security requirements elicitation; regulatory scoping | Security requirements, compliance checklist |
| **B Specify** | Abuse cases; security acceptance criteria; data classification | Abuse case catalog, data classification matrix |
| **C Design** | Threat modeling; secure architecture review; authentication/authorization design | Threat model, security architecture document |
| **D Build** | Secure coding practices; SAST in CI; dependency scanning; secrets management | Clean SAST results, no high-severity SCA findings |
| **E Verify** | DAST on staging; penetration testing; security-focused code review | Security test report, vulnerability remediation tickets |
| **F Release** | Artifact signing; release security checklist; compliance evidence collection | Signed artifacts, compliance evidence package |

---

## 8. Incident response

| Phase | Activities | Key outputs |
|-------|-----------|-------------|
| **Preparation** | Incident response plan, runbooks, communication templates, tabletop exercises | IR plan, contact lists, escalation matrix |
| **Detection** | Security monitoring, SIEM, anomaly detection, threat intelligence | Alert triage, incident classification |
| **Containment** | Isolate affected systems, preserve evidence, limit blast radius | Containment actions, forensic images |
| **Eradication** | Remove threat actor access, patch vulnerabilities, rotate credentials | Root cause identification, remediation actions |
| **Recovery** | Restore services, verify integrity, monitor for recurrence | Recovery verification, enhanced monitoring |
| **Lessons learned** | Blameless postmortem, timeline reconstruction, improvement actions | Postmortem document, backlog items |

---

## 9. Supply chain security

| Practice | Description |
|----------|-------------|
| **SBOM generation** | Produce Software Bill of Materials (SPDX or CycloneDX) for every release |
| **Dependency pinning** | Pin dependency versions; use lockfiles; review updates before merging |
| **Artifact signing** | Sign container images (cosign/Notation) and release artifacts; verify signatures in deployment |
| **Provenance attestation** | SLSA framework — record build provenance to prove artifacts were built from expected source |
| **Registry security** | Private registries with access control; vulnerability scanning on push; no `latest` tags in production |
| **Commit signing** | GPG or SSH signature on commits; branch protection requiring signed commits |

---

## 10. Competencies

| Competency | Description |
|------------|-------------|
| **Threat modeling** | Identifying, analyzing, and prioritizing threats to a system using structured methodologies |
| **Secure design** | Applying security patterns and principles to system and feature architecture |
| **Application security** | Understanding common vulnerability classes and their prevention in code |
| **Cryptography** | Selecting and applying appropriate cryptographic primitives; key management |
| **Compliance** | Mapping regulatory requirements to technical controls; preparing audit evidence |
| **Incident handling** | Detecting, responding to, and learning from security incidents |
| **Security testing** | Planning and executing security assessments (automated and manual) |
| **Risk communication** | Explaining security risks and trade-offs to non-security stakeholders |

---

## 11. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| OWASP | https://owasp.org/ | Open-source application security — Top 10, ASVS, testing guides, cheat sheets |
| OWASP SAMM | https://owaspsamm.org/ | Software Assurance Maturity Model — assess and improve security practices |
| NIST Cybersecurity Framework | https://www.nist.gov/cyberframework | Risk-based framework — identify, protect, detect, respond, recover |
| NIST SP 800-53 | https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final | Security and privacy control catalog |
| CIS Controls | https://www.cisecurity.org/controls | Prioritized security controls for cyber defense |
| MITRE ATT&CK | https://attack.mitre.org/ | Adversary tactics, techniques, and procedures knowledge base |
| SLSA | https://slsa.dev/ | Supply-chain Levels for Software Artifacts framework |
| CISA KEV | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | Known Exploited Vulnerabilities catalog for prioritization |

---

*Keep project-specific security documentation in `docs/security/`, threat models in `docs/security/threat-models/`, and security decisions in `docs/adr/`, not in this file.*
