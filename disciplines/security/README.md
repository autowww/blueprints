# Security / Cybersecurity

Reusable, **project-agnostic** blueprint for **Security** — the discipline of protecting digital products from unauthorized access, data breaches, and attacks through threat modeling, secure design, security testing, and compliance.

Security answers **"is the product safe from unauthorized access, data breaches, and attacks?"** — a question that spans every SDLC phase (shift-left through operate) and every PDLC phase where data, users, or systems are at stake.

| Document | Purpose |
|----------|---------|
| [**SECURITY.md**](SECURITY.md) | Threat modeling, OWASP, authentication/authorization patterns, cryptography, secure SDLC, compliance, competencies |
| [**SEC-SDLC-PDLC-BRIDGE.md**](SEC-SDLC-PDLC-BRIDGE.md) | How Security maps across SDLC phases A–F and PDLC phases P1–P6 — emphasis on shift-left and continuous assurance |
| [**practices/**](practices/README.md) | Deep guides: threat modeling (STRIDE, PASTA), secure code review, security testing (SAST/DAST/SCA), incident response, supply chain security |
| [**Compliance** *(cross-cutting)*](../compliance/README.md) | Standalone compliance discipline — GDPR, HIPAA, PCI-DSS, WCAG, SOC 2, AI Act, ISO 27001; technical controls mapping and audit readiness |

## Relationship to other packages

| Package | How Security relates |
|---------|---------------------|
| [`blueprints/sdlc/`](../../sdlc/README.md) | Security practices integrate into every SDLC phase — security requirements in A/B, threat modeling in C, secure code review in D, security testing in E, release signing in F. The secure SDLC (S-SDLC) is a cross-cutting overlay on the standard lifecycle. |
| [`blueprints/pdlc/`](../../pdlc/README.md) | PDLC P3 (Plan & Commit) scopes compliance requirements. P4 (Launch) includes security readiness review. P5 (Grow) involves incident response and ongoing vulnerability management. |
| [`blueprints/disciplines/engineering/devops/`](../engineering/devops/README.md) | DevSecOps is the intersection — security checks in CI/CD pipelines, infrastructure security, secrets management, container scanning. DevOps provides the **automation mechanism**; Security provides the **policy and controls**. |
| [`blueprints/disciplines/engineering/software-architecture/`](../engineering/software-architecture/README.md) | Security is a core quality attribute in architecture decisions. Authentication/authorization architecture, network segmentation, encryption design, and zero-trust patterns are architecture concerns with security expertise. |
| [`blueprints/disciplines/engineering/testing/`](../engineering/testing/README.md) | Security testing (SAST, DAST, penetration testing, fuzzing) extends the test pyramid. Vulnerability scanning is a quality gate alongside functional testing. |
| [`blueprints/disciplines/product/ux-design/`](../product/ux-design/README.md) | Security controls (login flows, MFA, consent, error messages) have direct UX implications. Secure-by-default patterns must remain usable — the security-usability trade-off is a shared concern. |
| [`blueprints/disciplines/data/bigdata/`](../data/bigdata/README.md) | Data security (classification, access control, encryption, audit logging) is a DMBOK knowledge area. BigData governance intersects with compliance (GDPR data protection, right to erasure). |
| [`blueprints/disciplines/documentation/`](../documentation/README.md) | Security produces documentation artifacts (threat models, incident playbooks, audit evidence, security policies). The Documentation discipline provides standards for structuring, reviewing, and maintaining these artifacts effectively. |

## Scope

This package covers **Security as a discipline** — not just vulnerability scanning tools. It includes:

- **Threat modeling** — STRIDE, PASTA, attack trees, data flow diagramming, threat library
- **Secure design** — authentication/authorization patterns (OAuth2, OIDC, RBAC, ABAC, zero trust), cryptographic design, input validation, secure defaults
- **Secure development** — secure coding guidelines, code review for security, dependency management
- **Security testing** — SAST, DAST, IAST, SCA, penetration testing, fuzzing, red teaming
- **Compliance** — see the standalone [**Compliance**](../compliance/README.md) discipline for GDPR, HIPAA, PCI-DSS, WCAG, SOC 2, AI Act, ISO 27001 and audit evidence collection
- **Supply chain security** — SBOM, dependency scanning, artifact signing, provenance attestation
- **Incident response** — detection, containment, eradication, recovery, lessons learned
- **Identity and access management** — authentication flows, session management, API security, secrets management

Reference bodies of knowledge: OWASP (Top 10, ASVS, SAMM), NIST CSF / SP 800-53, ISC2 (CISSP CBK), CIS Controls, MITRE ATT&CK.

---

*Keep project-specific security documentation in `docs/security/`, threat models in `docs/security/threat-models/`, and security decisions in `docs/adr/`, not in this file.*
