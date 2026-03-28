# DevOps practices (blueprint)

**Purpose:** Deep, **project-agnostic** guides for core DevOps practices. Each practice describes its principles, implementation patterns, maturity progression, and lifecycle mapping.

DevOps practices are the **how** of continuous delivery: they turn culture and goals from [`DEVOPS.md`](https://forgesdlc.com/discipline-devops.html) into repeatable workflows — automated pipelines, codified infrastructure, observable systems, and resilient response — so teams ship small batches safely and learn from production.

**Non-goals:** These blueprints do not mandate a single vendor or cloud; they emphasize patterns you can map to your stack. Product-specific SLAs, pipeline definitions, and environment names stay in repository documentation, not here.

**Audience:** Teams adopting [`blueprints/disciplines/engineering/devops/`](../README.md); project-specific CI/CD and operations configuration stays in **`docs/development/`** (see [`docs/development/CI-CD.md`](../../../../../docs/development/CI-CD.md)) and **`docs/operations/`**.

```blueprint-diagram
key: linear
alt: Diagram
```

| Practice | Guide | Focus |
|----------|-------|-------|
| **CI/CD pipelines** | [`ci-cd.md`](ci-cd.md) | Continuous integration and delivery/deployment — pipeline design, stages, quality gates, deployment strategies, DORA-aligned metrics |
| **Infrastructure as Code & GitOps** | [`iac-gitops.md`](iac-gitops.md) | Declarative infra, plan/apply workflows, pull vs push deploy, drift, secrets — Terraform-class tools and Argo CD / Flux |
| **SRE and observability** | [`sre-observability.md`](sre-observability.md) | SLOs/SLIs/error budgets, logs/metrics/traces, alerting, chaos engineering, on-call, blameless postmortems |
| **Incident management** | [`incident-management.md`](incident-management.md) | Severity, roles, comms templates, on-call, SEV1 flow, metrics (MTTA/MTTR), learning loops |

**Suggested reading order for adoption:** (1) align on [`DEVOPS.md`](https://forgesdlc.com/discipline-devops.html) vocabulary and DORA baselines; (2) harden [`ci-cd.md`](ci-cd.md) and [`iac-gitops.md`](iac-gitops.md); (3) define SLOs and observability in [`sre-observability.md`](sre-observability.md); (4) formalize response in [`incident-management.md`](incident-management.md). Maturity is not linear — revisit earlier guides when failure modes change.

**Core knowledge:** [`DEVOPS.md`](https://forgesdlc.com/discipline-devops.html) — CALMS, Three Ways, DORA metrics, SRE, DevSecOps. For operational signals and SLO-driven delivery, start from [`sre-observability.md`](sre-observability.md) alongside [`ci-cd.md`](ci-cd.md).

**Bridge:** [`DEVOPS-SDLC-PDLC-BRIDGE.md`](../DEVOPS-SDLC-PDLC-BRIDGE.md) — how DevOps maps to delivery and product lifecycles.

**Related:** Tool choices and platform categories are summarized in [`../tooling/README.md`](../tooling/README.md). Chaos engineering and on-call depth live primarily under [`sre-observability.md`](sre-observability.md); incident process detail under [`incident-management.md`](incident-management.md).

**Quick links:** [CI/CD](ci-cd.md) · [IaC & GitOps](iac-gitops.md) · [SRE / observability](sre-observability.md) · [Incidents](incident-management.md) · [DevOps body of knowledge](https://forgesdlc.com/discipline-devops.html)

---

*Keep project-specific DevOps configuration in docs/development/CI-CD.md and infrastructure documentation in docs/operations/, not in this file.*
