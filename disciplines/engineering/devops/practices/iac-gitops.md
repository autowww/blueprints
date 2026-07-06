---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Infrastructure as Code & GitOps (blueprint)

**Infrastructure as Code (IaC)** treats infrastructure definition as software: versioned, reviewed, and applied by automation. **GitOps** extends that idea by using Git as the authoritative desired state and reconciling live systems to that state. Together they reduce drift, improve auditability, and align delivery with [`ci-cd.md`](ci-cd.md) pipelines.

---

## 1. IaC principles

| Principle | Meaning | Practical signal |
|-----------|---------|------------------|
| **Declarative** | Describe desired end state, not imperative steps | `terraform plan` shows diff to goal |
| **Idempotent** | Re-applying converges; no duplicate resources from repeats | Safe automation in CI |
| **Version-controlled** | Infra changes are PRs with history | Blameless audit trail |
| **Reviewable** | Peers review infra like application code | Security and cost feedback early |

---

## 2. IaC tool comparison (high level)

| Tool | Paradigm | Language / style | Cloud / scope | State / model notes |
|------|----------|------------------|---------------|---------------------|
| **Terraform** | Declarative | HCL | Multi-cloud, providers | State file; plan/apply workflow |
| **Pulumi** | Declarative + imperative | TS, Go, Python, etc. | Multi-cloud | State in backend; real languages |
| **CloudFormation** | Declarative | JSON/YAML | AWS-native | Stack state in AWS |
| **AWS CDK** | Imperative → synthesized templates | TS, Python, Java, etc. | AWS | CloudFormation output |
| **Ansible** | Imperative (desired state modules) | YAML playbooks | Hybrid (SSH + APIs) | Inventory; less “state file” than TF |
| **Chef** | Imperative / convergent | Ruby DSL | Servers, cloud agents | Node state on server |
| **Puppet** | Declarative | Puppet DSL | Data centers, cloud agents | Catalog compilation |
| **Crossplane** | Declarative (K8s CRDs) | YAML in cluster | Cloud APIs via controllers | Desired state in etcd |

*Selection hint:* prefer **declarative + strong state** for large cloud estates; **imperative** automation fits ad-hoc or brownfield bootstrap until codified.

---

## 3. IaC workflow

```blueprint-diagram
key: linear
alt: IaC workflow
title: IaC plan and apply
summary: How version-controlled declarations become reviewable, idempotent infrastructure with drift detection.
node: Start
detail: Desired infrastructure is declared in version-controlled configuration.
more: Declarative modules describe end state; changes enter through pull requests like application code.
node: Core steps (see walkthrough below)
detail: Plan, peer review, and automated apply converge live resources to the declaration.
more: Tools such as Terraform emit a plan diff before apply; idempotent re-runs avoid duplicate resources from repeats.
node: Outcome
detail: Live infrastructure matches the reviewed desired state in Git.
more: Scheduled plans and drift detection close the loop when console edits or failed applies leave reality out of sync.
fallback_ascii: |
  IaC workflow

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

**Drift** occurs when console changes or failed applies leave reality ≠ desired state; detection closes the loop.

---

## 4. GitOps principles

| Principle | Implication |
|-----------|-------------|
| **Declarative** | Cluster and app config expressed as manifests |
| **Versioned** | Git history is the change log; tags and branches policy-driven |
| **Automated** | Controllers reconcile cluster to Git without manual `kubectl apply` |
| **Auditable** | Who merged what, when — same as code review |

OpenGitOps ([opengitops.dev](https://opengitops.dev/)) formalizes these for the CNCF.

---

## 5. GitOps architecture (pull model)

```blueprint-diagram
key: linear
alt: GitOps architecture (pull model)
title: GitOps pull reconciliation
summary: How cluster controllers reconcile live state to Git as the authoritative desired configuration.
node: Start
detail: Declarative manifests and environment config are committed to Git.
more: Version history records who merged what and when, matching the same audit trail as application code review.
node: Core steps (see walkthrough below)
detail: A cluster-bound controller polls or watches Git and applies declared changes.
more: Credentials stay on the cluster side, limiting blast radius compared with CI holding broad deploy keys across environments.
node: Outcome
detail: Running workloads and cluster config match the reviewed Git revision.
more: Sync status, diff UI, and metrics expose OutOfSync drift; remediation defaults to Git winning after review.
fallback_ascii: |
  GitOps architecture (pull model)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

---

## 6. Push vs pull deployment

| Dimension | Push (CI applies) | Pull (GitOps) |
|-----------|-------------------|---------------|
| **Trigger** | Pipeline on merge | Operator polls or watches Git |
| **Credentials** | CI needs cloud/cluster creds | Cluster-bound controller creds |
| **Blast radius** | Compromised CI can affect many envs | Scoped to controller RBAC |
| **Observability** | Pipeline logs | Sync status, diff UI, metrics |
| **Fit** | VMs, serverless, hybrid | Kubernetes-heavy estates |

Many teams use **CI for build/test** and **GitOps for deploy** to production clusters.

---

## 7. GitOps tool comparison

| Tool | Architecture | Notable features | Ecosystem |
|------|--------------|------------------|-----------|
| **Argo CD** | App controller + UI/API | App of Apps, multi-cluster, RBAC | CNCF; strong UI |
| **Flux** | Modular controllers (source, kustomize, helm, image) | Composable GitOps | CNCF; Git-native |
| **Jenkins X** | Pipeline + GitOps opinions | Preview envs, promotion | Kubernetes; Jenkins heritage |

---

## 8. Environment management patterns

| Pattern | Description | Pros / cons |
|---------|-------------|-------------|
| **Directory per env** | `envs/prod`, `envs/staging` in repo | Clear separation; duplication risk |
| **Branch per env** | `main` → prod, `staging` branch | Familiar; branch drift risk |
| **Overlay / Kustomize** | Base + env patches | DRY; K8s-native |
| **Helm values** | Chart + `values-prod.yaml` | Packaging + templating; chart complexity |

Prefer **directory or overlay** over long-lived **branch-per-env** unless policy mandates branch isolation.

---

## 9. Drift detection and remediation

| Strategy | Mechanism | Remediation |
|----------|-----------|-------------|
| **Scheduled plan** | `terraform plan` in CI; fail on diff | Re-apply from repo or fix manual change |
| **Controller drift** | Argo CD “OutOfSync” | Sync or deny manual edits |
| **Policy guard** | OPA/Gatekeeper, cloud policy | Block non-IaC changes |
| **Import workflow** | Import discovered resources into state | Align state to reality once |

**Goal:** detect quickly, default to **Git wins** after review, or **freeze** console for critical scopes.

---

## 10. Secret management in IaC

| Approach | Description |
|----------|-------------|
| **Sealed Secrets** | Encrypt Secret for cluster; only cluster decrypts |
| **External Secrets Operator** | Sync from Vault, AWS SM, GCP SM into K8s |
| **Vault integration** | Dynamic secrets, encryption as a service; avoid long-lived static in Git |
| **CI inject** | Short-lived tokens at apply time; never commit plaintext |

**Rule:** no plaintext secrets in Git; reference secret stores and encrypt at rest.

---

## 11. Anti-patterns

| Anti-pattern | Why it hurts |
|--------------|--------------|
| **ClickOps** | No history; irreproducible; audit gaps |
| **Snowflake infrastructure** | Each env unique; incidents multiply |
| **State file mismanagement** | Lost state → recreate risk; leaked state → credential exposure |
| **Hardcoded secrets** | Breach and compliance failure |

---

## 12. External references

| Resource | Notes |
|----------|--------|
| *Infrastructure as Code* — Kief Morris | Patterns for managing cloud and systems as code |
| [gitops.tech](https://gitops.tech/) | Community overview and comparisons |
| [OpenGitOps](https://opengitops.dev/) | CNCF GitOps principles |

---

*Keep project-specific DevOps configuration in docs/development/CI-CD.md and infrastructure documentation in docs/operations/, not in this file.*
