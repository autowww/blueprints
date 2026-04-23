---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Container orchestration & platform engineering (blueprint)

**Containers** package applications with dependencies. **Orchestration** schedules, networks, and heals those workloads at scale. **Platform engineering** builds internal abstractions (golden paths, self-service) so product teams ship faster without owning every low-level knob. This guide sits beside [`../practices/ci-cd.md`](../practices/ci-cd.md) and [`../practices/iac-gitops.md`](../practices/iac-gitops.md) for deploy and cluster operations.

---

## 1. Evolution: containers → orchestration → platform

| Stage | Focus | Typical owner |
|-------|--------|----------------|
| **Containers** | Immutable artifact, portable runtime | Application team |
| **Orchestration** | Scheduling, scaling, service discovery, rollouts | Platform / SRE |
| **Platform engineering** | IDP, templates, paved roads, developer experience | Platform team + internal customers |

---

## 2. Container runtime landscape

| Runtime | Notes | Common use |
|---------|-------|------------|
| **Docker** | Developer UX, `docker build`; engine may use containerd underneath | Local dev, many CI images |
| **containerd** | CNCF graduated; CRI-friendly | Node runtime under Kubernetes |
| **CRI-O** | Minimal OCI runtime for Kubernetes | OpenShift, security-focused K8s |
| **Podman** | Daemonless, rootless options | Dev laptops, some CI |

**Comparison dimensions:** OCI compliance, rootless support, Kubernetes CRI integration, ecosystem tooling.

---

## 3. Orchestration platform comparison

| Platform | Complexity | Scaling model | Ecosystem | Managed options |
|----------|------------|---------------|-----------|-----------------|
| **Kubernetes** | High | Declarative desired state, controllers | Largest (CNCF) | EKS, GKE, AKS, many others |
| **Docker Swarm** | Lower | Services and tasks | Smaller | Docker EE (legacy paths) |
| **Nomad** | Medium | Mixed workloads (container + batch) | HashiCorp stack | HCP Nomad |
| **ECS / Fargate** | Medium (AWS) | Task definitions, services | AWS-native | Fargate serverless tasks |
| **Cloud Run** | Lower (for services) | Request-driven or min instances | GCP | Fully managed |

**Heuristic:** default **Kubernetes** when you need portability and a rich extension ecosystem; choose **managed** control planes unless you have strong reasons to self-host.

---

## 4. Kubernetes core concepts

| Resource | Purpose |
|----------|---------|
| **Pod** | Smallest deployable unit; one or more containers sharing network/storage |
| **Deployment** | Declarative rollout and rollback of stateless apps |
| **Service** | Stable network endpoint for a set of pods |
| **Ingress** | HTTP(S) routing into cluster (often with controller) |
| **ConfigMap** | Non-secret configuration injection |
| **Secret** | Sensitive data (prefer external secret sync in prod) |
| **PersistentVolume** | Durable storage claim for stateful workloads |
| **Namespace** | Logical isolation, quotas, RBAC scope |
| **RBAC** | Roles and bindings for API access control |

---

## 5. Kubernetes architecture (simplified)

```blueprint-diagram
key: swimlane
alt: Diagram
```

---

## 6. Workload APIs: when to use which

| Workload | Use when |
|----------|----------|
| **Deployment** | Stateless HTTP services, workers with external state |
| **StatefulSet** | Stable identity, ordered rollout, persistent storage per replica |
| **DaemonSet** | One pod per node — agents, log collectors, CNI helpers |
| **Job** | Run-to-completion batch |
| **CronJob** | Scheduled jobs |

---

## 7. Service mesh comparison

| Mesh | Traffic management | Observability | Security |
|------|-------------------|---------------|----------|
| **Istio** | Rich (VirtualService, DestinationRule) | Telemetry, WASM extensibility | mTLS, authz policies |
| **Linkerd** | Simpler defaults | Golden metrics focus | mTLS |
| **Consul Connect** | Integrates with Consul service discovery | Via proxies and integrations | mTLS intentions |

**Trade-off:** operational complexity vs uniform mTLS and L7 policy — adopt when multiple languages/teams need consistent policy.

---

## 8. Platform engineering concepts

| Concept | Description |
|---------|-------------|
| **Internal Developer Platform (IDP)** | Curated services: deploy, DB, queues, observability templates |
| **Golden paths** | Opinionated templates that “just work” for common cases |
| **Self-service** | RBAC-guarded APIs/CLI/UI instead of tickets for routine needs |
| **Developer experience (DX)** | Time to first deploy, doc quality, fast feedback loops |

---

## 9. Platform stack layers

```blueprint-diagram
key: linear
alt: Diagram
```

---

## 10. Managed Kubernetes comparison (high level)

| Offering | Differentiators | Pricing intuition | Ecosystem |
|----------|-----------------|-------------------|-----------|
| **Amazon EKS** | Deep AWS integration (IAM, VPC, LB) | Control plane fee + worker cost | Largest marketplace |
| **Google GKE** | Autopilot mode, strong networking defaults | Per cluster / node / autopilot | Native GCP services |
| **Microsoft AKS** | Azure AD, Windows node options | Regional pricing models | Azure DevOps/GitHub synergy |

Verify current pricing pages before procurement; models change frequently.

---

## 11. Anti-patterns

| Anti-pattern | Risk |
|--------------|------|
| **Kubernetes for everything** | Complexity tax on simple batch or functions |
| **No resource limits** | Noisy neighbor; cluster instability |
| **No network policies** | Lateral movement after compromise |
| **Manual kubectl in production** | Untracked drift; violates GitOps — see [`../practices/iac-gitops.md`](../practices/iac-gitops.md) |

---

## 12. External references

| Resource | Notes |
|----------|--------|
| [kubernetes.io](https://kubernetes.io/docs/) | Official documentation |
| [CNCF Cloud Native Landscape](https://landscape.cncf.io/) | Projects and categories |
| *Platform Engineering on Kubernetes* — Mauricio Salatino | IDP patterns on K8s |
| [Backstage](https://backstage.io/) | Open-source developer portal framework |

---

*Keep project-specific DevOps configuration in docs/development/CI-CD.md and infrastructure documentation in docs/operations/, not in this file.*
