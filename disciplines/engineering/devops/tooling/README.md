---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# DevOps tooling (blueprint)

**Purpose:** Taxonomy and selection guidance for DevOps tooling categories. Each category describes the problem space, common tools, selection criteria, and trade-offs.

**Tooling selection principles:** Prefer tools that match your **constraints** (cloud, compliance, team skills), reduce **toil** through APIs and Git-native workflows, and compose with **existing** source control and identity. Favor **boring** proven options for the critical path; adopt **new** tools where they remove a clear bottleneck. Document irreversible choices as ADRs in **`docs/adr/`**.

**When to split a new tooling guide:** Add a dedicated file when a category’s trade-offs routinely exceed a short section, or when multiple practice guides need a stable, shared comparison table (as with [`container-orchestration.md`](container-orchestration.md)).

**Category overview — selection criteria:**

| Lens | Ask |
|------|-----|
| **Fit** | Does it integrate with your repo, cloud, and on-call stack? |
| **Operability** | Who runs upgrades, backups, and incident response for the tool itself? |
| **Cost** | License, egress, seat pricing, and engineer time to maintain |
| **Security** | SSO, RBAC, audit logs, secret handling, supply chain (SBOM, signing) |
| **Exit** | Portability of pipelines, data, and IaC if you migrate |

**Audience:** Teams adopting [`blueprints/disciplines/engineering/devops/`](../README.md); project-specific tool choices are documented as ADRs in **`docs/adr/`**.

| Category | Guide | Scope |
|----------|-------|-------|
| **Container orchestration** | [`container-orchestration.md`](container-orchestration.md) | Runtimes, Kubernetes vs alternatives, workload APIs, service mesh, platform engineering, managed K8s |
| **Artifact management** | *(taxonomy; pair with [`../practices/ci-cd.md`](../practices/ci-cd.md))* | Container registries, package repositories, artifact versioning, promotion pipelines |
| **Secrets management** | *(taxonomy; pair with [`../practices/iac-gitops.md`](../practices/iac-gitops.md))* | Vault, cloud-native secret stores, rotation, access policies, secret injection patterns |
| **Deployment strategies** | [`../practices/ci-cd.md`](../practices/ci-cd.md) | Blue-green, canary, rolling, feature flags, dark launches — selection by risk tolerance |
| **Platform engineering** | [`container-orchestration.md`](container-orchestration.md) (platform layer) | Internal developer platforms, self-service provisioning, golden paths, developer experience |

**Core knowledge:** [`DEVOPS.md`](https://forgesdlc.com/discipline-devops.html) — CALMS, Three Ways, DORA metrics, and how tooling supports the Three Ways.

**Practices:** [`practices/README.md`](../practices/README.md) — CI/CD, IaC/GitOps, observability, incident management.

**Note:** Artifact and secrets tooling evolves quickly; compare vendor roadmaps against your compliance tier (e.g. FedRAMP, SOC 2) before standardizing. Deep pipeline patterns remain in [`../practices/ci-cd.md`](../practices/ci-cd.md); cluster delivery patterns in [`../practices/iac-gitops.md`](../practices/iac-gitops.md).

**Quick links:** [Container & platform](container-orchestration.md) · [Practices index](../practices/README.md) · [DevOps body of knowledge](https://forgesdlc.com/discipline-devops.html)

---

*Keep project-specific DevOps configuration in docs/development/CI-CD.md and infrastructure documentation in docs/operations/, not in this file.*
