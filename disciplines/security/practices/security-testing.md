---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Security testing — strategy and implementation

**Purpose:** A **project-agnostic** blueprint for layering automated and manual security testing so vulnerabilities are found **before** attackers exploit them.

**Audience:** Engineers, DevSecOps, and security teams designing CI/CD gates, toolchains, and remediation workflows.

---

## Overview

Security testing is not a single scan at the end of a release. It is a **layered program**: fast, broad checks run continuously; deeper, manual work targets high-risk areas. The goal is **signal over noise** — tuned rules, triage discipline, and tracked fixes — so teams trust the process enough to act on findings.

---

## Security test pyramid

```blueprint-diagram
key: linear
alt: Security test pyramid
title: Layered security test pyramid
summary: How automated scans, dynamic tests, and manual exercises stack for defense in depth.
node: Start
detail: Begin shaping a layered program rather than a single end-of-release scan.
node: Core steps (see walkthrough below)
detail: Layer SAST, SCA, DAST, IAST, pen tests, and red team by depth and cost.
more: SAST and SCA scale across every commit; DAST and IAST validate running behavior; pen tests and red team stress detection and response.
node: Outcome
detail: Surface vulnerabilities before attackers with trustworthy, actionable signal.
more: Tuned rules, triage discipline, and tracked fixes keep noise low so teams act on real risk.
fallback_ascii: |
  Security test pyramid

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: Interpretation:
```

**Interpretation:** **SAST** and **SCA** scale across every commit; **DAST** (and **IAST**, see below) validates running behavior; **pen tests** and **red team** exercises stress real-world creativity and detection/response.

---

## SAST (static application security testing)

**How it works:** Analyzes source or bytecode **without execution**, matching code patterns and data flows to rules for issues like injection, unsafe crypto, and hard-coded secrets.

**Rule sets:** Language-specific; often OWASP/CWE-oriented; customizable for frameworks.

**Integration:** IDE (fast feedback), PR checks (shift-left), full-repo CI (coverage).

**False positives:** Tune rules, suppress with justification, prioritize reachable paths, and feed back to rule owners.

| Tool | Notes |
|------|--------|
| **Semgrep** | Fast, customizable rules; strong OSS and CI fit |
| **CodeQL** | Deep semantic queries; strong for supported languages |
| **SonarQube / SonarCloud** | Broad quality + security rules; enterprise governance |
| **Checkmarx** | Enterprise SAST, workflow integration |
| **Fortify** | Mature enterprise SAST and reporting |

---

## SCA (software composition analysis)

**How it works:** Inspects manifests and lockfiles (and sometimes binaries) to map **dependencies** to known vulnerabilities and licenses.

**Outputs:** Vulnerability reports, license compliance flags, **SBOM** (CycloneDX, SPDX) for audits and incident response.

**Databases:** [NVD](https://nvd.nist.gov/), [OSV](https://osv.dev/), GitHub Security Advisories, vendor feeds.

| Tool | Notes |
|------|--------|
| **Snyk** | Developer-centric UI and PR fixes |
| **Dependabot** | Native GitHub dependency PRs |
| **Trivy** | Containers, IaC, and deps; CLI-friendly |
| **Grype** | SBOM and image scanning aligned with Syft |
| **OWASP Dependency-Check** | OSS CLI/reporting for Java-heavy stacks |

---

## DAST (dynamic application security testing)

**How it works:** Sends requests to a **running** application to find issues like XSS, injection, and misconfigurations visible at the HTTP layer.

| Mode | When to use |
|------|----------------|
| **Crawler-based** | Traditional web UIs, session flows |
| **API-based** | OpenAPI-defined services; combine with auth tokens and test data |

**Authentication:** Use test accounts, token injection, or scripted login; avoid production credentials.

**CI:** Run against **ephemeral staging** with seeded data; gate on severity thresholds after baseline tuning.

| Tool | Notes |
|------|--------|
| **OWASP ZAP** | OSS; automation API and packaged scans |
| **Burp Suite** | Manual + automated; professional for testers |
| **Nuclei** | Template-driven fast scanning |
| **StackHawk** | CI-native DAST with developer workflow focus |

---

## IAST (interactive application security testing)

**How it works:** **Instruments** the running app (agent) to observe real execution paths, taint propagation, and sink hits — bridging static and dynamic views.

**Advantages vs SAST + DAST alone:** Fewer false positives on **reachable** issues; insight into runtime context (frameworks, serializers).

**Limitations:** Agent overhead; language/runtime support; needs meaningful test traffic (quality of tests drives coverage).

---

## Security testing in CI/CD

```blueprint-diagram
key: linear
alt: Security testing in CI/CD
title: Security gates in CI/CD
summary: How security scans integrate into pipelines with governed, context-aware release gates.
node: Start
detail: Map security test types to IDE, pull-request, and continuous integration stages.
node: Core steps (see walkthrough below)
detail: Wire SAST, SCA, and DAST into builds and staging deploys with tuned baselines.
more: Run fast checks at PR time; point DAST at ephemeral staging with test accounts and seeded data.
node: Outcome
detail: Gate releases on severity, exploitability, and context—not raw finding counts.
more: Allow a baseline tuning period before hard thresholds; suppress false positives only with documented justification.
fallback_ascii: |
  Security testing in CI/CD

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: severity + exploitability + context
```

Gates should use **severity + exploitability + context** (not raw counts alone) after a **baseline** period.

---

## Penetration testing

| Topic | Guidance |
|-------|----------|
| **Scope** | URLs/APIs, excluded systems, data classes, hours of testing, cloud boundaries |
| **Rules of engagement** | Legal authorization, emergency contacts, destructive testing limits, data handling |
| **Methodologies** | PTES phases; [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) techniques |
| **Reporting** | Executive summary, technical findings with repro steps, severity, evidence |
| **Remediation** | Track IDs, owners, retest criteria, SLA by severity |

---

## Comparison matrix: techniques

| Technique | What it finds | False positives | SDLC fit | Cost | Skill |
|-----------|---------------|-----------------|----------|------|-------|
| **SAST** | Flaws in code before run | Can be high without tuning | IDE, PR, CI | Low–high license | Appsec to tune |
| **DAST** | Exposed runtime vulns | Medium; auth/config sensitive | Staging CI | Medium | Tester for deep use |
| **IAST** | Reachable issues under test | Lower than raw SAST | Test env + agent | Medium–high | Appsec + QA alignment |
| **SCA** | Known vulns in deps | Low on version match; noise on disputed CVEs | Every build | Low–medium | Build owner |
| **Pen test** | Chains, logic, ops gaps | Low (validated) | Milestone / annual | High | External or internal expert |

---

## Container and infrastructure scanning

| Area | Practice | Example tools |
|------|----------|----------------|
| **Container images** | Scan OS packages and app layers in registry and CI | Trivy, Grype, vendor scanners |
| **IaC** | Policy-as-code for Terraform, K8s manifests, CloudFormation | Checkov, tfsec, Kube-score |
| **CSPM** | Cloud misconfiguration and drift | Native cloud tools, Wiz, Prisma Cloud, etc. |

---

## Vulnerability management lifecycle

1. **Discover** — scanners, pen tests, bug bounty, threat intel  
2. **Triage** — valid vs false positive, affected assets  
3. **Prioritize** — CVSS + exploitability + business context  
4. **Remediate** — patch, config, compensating control  
5. **Verify** — retest, regression tests  
6. **Close** — record rationale and residual risk  

---

## Vulnerability triage decision tree

```blueprint-diagram
key: decision
alt: Vulnerability triage decision tree
title: Vulnerability triage gate
summary: How teams decide whether a finding is valid, scoped, and ready for remediation.
node: Current state
detail: A scanner, pen test, or bug-bounty finding enters the triage queue.
node: Checkpoint / gate
detail: Confirm validity, affected assets, and whether the issue is reachable in production.
more: Separate true positives from false positives and map the finding to repos, images, or environments in scope.
node: refine or escalate
detail: Retune noisy rules, dismiss false positives, or escalate unclear high-risk items.
more: Record suppression rationale for audit; escalate when exploitability or business impact needs expert judgment.
node: Continue flow
detail: Advance confirmed issues into prioritization, ownership, and tracked remediation.
more: Feed verified findings into patch, verify, and close steps with retest criteria and severity-based SLAs.
fallback_ascii: |
  Vulnerability triage decision tree

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

## Metrics

| Metric | Use |
|--------|-----|
| **Mean time to remediate (MTTR) by severity** | SLA health |
| **Vulnerability density** | Trends per service or team |
| **Scan coverage** | % repos / images / envs in scope |
| **False positive rate** | Tuning quality for SAST/DAST |
| **SLA compliance** | % closed within target windows |

---

## Anti-patterns

| Anti-pattern | Fix |
|--------------|-----|
| **Scan-and-forget** | Ticket every confirmed issue; measure MTTR |
| **SAST without tuning** | Baseline, suppress with reason, retrain rules |
| **Pen test as checkbox** | Scope for real risk; fix and retest material items |
| **No remediation tracking** | Single system of record linked to releases |

---

## External references

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP SAMM](https://owaspsamm.org/) (security assurance maturity)
- NIST SP 800-115 (technical security testing)
- [Semgrep documentation](https://semgrep.dev/docs/)
- [Snyk Learn](https://learn.snyk.io/)

---

*Keep project-specific security documentation in docs/security/, threat models in docs/security/threat-models/, and security decisions in docs/adr/, not in this file.*
