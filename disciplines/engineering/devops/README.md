# DevOps

Reusable, **project-agnostic** blueprint for **DevOps** — the discipline of bridging development and operations to enable continuous, reliable delivery through culture, automation, measurement, and sharing.

DevOps answers **"how do we bridge development and operations for continuous, reliable delivery?"** — a question that spans the entire SDLC (especially Build → Verify → Release → Operate) and connects to PDLC launch (P4) and growth (P5).

| Document | Purpose |
|----------|---------|
| [**DEVOPS.md**](DEVOPS.md) | CALMS framework, Three Ways, DORA metrics, maturity model, cultural principles, competencies |
| [**DEVOPS-SDLC-PDLC-BRIDGE.md**](DEVOPS-SDLC-PDLC-BRIDGE.md) | How DevOps maps across SDLC phases A–F and PDLC phases P1–P6 — emphasis on Build/Verify/Release/Operate |
| [**practices/**](practices/README.md) | Deep guides: CI/CD pipelines, infrastructure as code, GitOps, observability, incident management, chaos engineering |
| [**tooling/**](tooling/README.md) | Container orchestration, artifact management, secrets management, deployment strategies |

## Relationship to other packages

| Package | How DevOps relates |
|---------|---------------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | DevOps practices underpin SDLC phases D–F (Build, Verify, Release) and extend into Operate. The [`sdlc/methodologies/devops/`](../../../sdlc/methodologies/devops/README.md) package is the **methodology lens** — how DevOps shapes SDLC phases, ceremonies, and roles. This discipline package is the broader **knowledge base**. |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | PDLC P4 (Launch) relies on DevOps deployment pipelines. P5 (Grow) depends on observability and incident management to measure outcomes and maintain reliability. |
| [`blueprints/disciplines/engineering/testing/`](../testing/README.md) | DevOps CI/CD pipelines automate test execution. The test pyramid informs pipeline stage design. Shift-left testing is a shared concern between testing and DevOps. |
| [`blueprints/disciplines/engineering/software-architecture/`](../software-architecture/README.md) | Architecture decisions (microservices, containers, cloud-native) enable or constrain DevOps practices. Infrastructure as code is an architecture-DevOps intersection. |
| [`blueprints/disciplines/data/bigdata/`](../../data/bigdata/README.md) | DataOps applies DevOps principles to data pipelines — CI/CD for data, data quality gates, pipeline observability. |

## Scope

This package covers **DevOps as a discipline** — not just CI/CD tooling. It includes:

- **Culture** — collaboration between dev and ops, shared responsibility, blameless postmortems
- **Automation** — CI/CD pipelines, infrastructure as code, configuration management
- **Measurement** — DORA metrics (deployment frequency, lead time, change failure rate, MTTR)
- **Continuous delivery** — deployment strategies (blue-green, canary, feature flags), release management
- **Observability** — monitoring, logging, tracing, alerting, SLOs/SLIs/SLAs
- **Incident management** — on-call, incident response, postmortem process
- **Site reliability engineering (SRE)** — error budgets, toil reduction, capacity planning
- **Security integration (DevSecOps)** — shift-left security, supply chain security, compliance automation

The DevOps methodology lens (how DevOps shapes SDLC phases, ceremonies, and roles) remains in [`blueprints/sdlc/methodologies/devops/`](../../../sdlc/methodologies/devops/README.md). This package provides the broader **discipline knowledge base** that the methodology lens references.

Reference bodies of knowledge: DORA State of DevOps, Google SRE handbook, DevOps Institute, The Phoenix Project / The Unicorn Project.

---

*Keep project-specific CI/CD configuration in `docs/development/CI-CD.md` and `.github/workflows/`, not in this file.*
