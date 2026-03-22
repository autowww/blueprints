# DevOps

## What it is

**DevOps** is a **culture, set of practices, and toolchain** that unifies **software development** (Dev) and **IT operations** (Ops) to shorten the systems development lifecycle while delivering features, fixes, and updates **frequently** and **reliably**. It emphasizes **automation**, **continuous integration and delivery (CI/CD)**, **infrastructure as code (IaC)**, **monitoring**, and **fast feedback loops** between development and production.

DevOps is **not** a single framework with prescribed roles and events (like Scrum). It is a **philosophy and capability** that complements any delivery methodology — Scrum teams, Kanban teams, and phased projects all benefit from DevOps practices.

## Process diagram (handbook)

![DevOps infinity loop](../docs/assets/methodology-devops-loop.svg)

*The infinity loop: Plan → Code → Build → Test → Release → Deploy → Operate → Monitor → Plan. Continuous feedback from operations informs development.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**Wikipedia — DevOps**](https://en.wikipedia.org/wiki/DevOps) | **Stable overview** of DevOps history, practices, and culture — entry point before vendor-specific guidance. |
| [Wikipedia — CI/CD](https://en.wikipedia.org/wiki/CI/CD) | **Continuous integration and delivery** — the technical backbone of DevOps pipelines. |
| [The DORA team (Google Cloud)](https://dora.dev/) | **Research-backed** DevOps metrics and capabilities; the four key metrics (deployment frequency, lead time, change failure rate, MTTR). |
| [The DevOps Handbook](https://itrevolution.com/product/the-devops-handbook-second-edition/) | **Practitioner** reference by Gene Kim et al. — principles, technical practices, and case studies (purchase/library). |

---

## Core practices (summary)

| Practice | Purpose |
|----------|---------|
| **Continuous Integration (CI)** | Merge and test code frequently; keep trunk/main green. |
| **Continuous Delivery (CD)** | Automate the path from integration to production-ready artifacts. |
| **Continuous Deployment** | Automatically deploy every change that passes the pipeline (subset of teams). |
| **Infrastructure as Code (IaC)** | Manage infrastructure through version-controlled definitions (Terraform, Ansible, etc.). |
| **Monitoring & observability** | Instrument systems for health, performance, and business metrics; alert on anomalies. |
| **Incident management** | Detect, respond, resolve, and learn from production incidents systematically. |
| **Automated testing** | Unit, integration, contract, performance, security tests in the pipeline. |
| **Configuration management** | Version-controlled, reproducible environments; no snowflake servers. |
| **Feature flags** | Decouple deployment from release; control rollout granularity. |

### DORA four key metrics

| Metric | What it measures |
|--------|-----------------|
| **Deployment frequency** | How often code is deployed to production. |
| **Lead time for changes** | Time from commit to production. |
| **Change failure rate** | Percentage of deployments causing failures. |
| **Mean time to restore (MTTR)** | Time to recover from a production failure. |

---

## Mapping to this blueprint's SDLC

| DevOps idea | Blueprint touchpoint |
|-------------|----------------------|
| CI/CD pipeline | Phase D–E: build, verify, release — [`SDLC.md`](../SDLC.md) §7, project `docs/development/CI-CD.md`. |
| IaC | Phase D–F: build, deploy, operate — version-controlled alongside application code. |
| Monitoring | Phase F: operate & learn — production signals feed next cycle. |
| Incident response | Phase F: operate — runbooks, escalation, post-incident reviews. |
| Automation | Cross-phase: reduce manual toil in build, test, deploy, and operate. |

**Ceremonies:** DevOps adds **operational** ceremonies (incident reviews, deployment reviews, SLO reviews) to development-focused ones. See [`ceremonies/devops.md`](ceremonies/devops.md).

**Roles:** DevOps introduces or emphasizes **SRE**, **platform engineer**, **release engineer** — see [`roles-archetypes.md`](roles-archetypes.md).

---

## Agentic SDLC: DevOps + agents + tracking

| Topic | Guidance |
|-------|----------|
| **CI/CD** | Agents can generate pipeline configurations, Dockerfiles, and IaC templates. **Human** review ensures security and correctness of deployment automation. |
| **Monitoring** | Agents can analyze logs and metrics, suggest alerts, and draft runbooks. **Human** sets SLOs and escalation policies. |
| **Incident response** | Agents can correlate alerts and suggest root causes. **Human** owns incident command and customer communication. |
| **Feature flags** | Agents can suggest flag configurations for gradual rollout. **Human** decides rollout strategy and risk tolerance. |
| **DORA metrics** | Agents can compute and visualize DORA metrics from pipeline data. **Human** interprets trends and drives improvements. |

---

## DevOps vs other methodologies

| Comparison | Relationship |
|------------|-------------|
| **DevOps → Lean** | DevOps applies **Lean thinking** to the full delivery pipeline: eliminate waste, optimize flow, build quality in. Value-stream mapping is a shared practice. |
| **DevOps → Kanban** | Kanban **visualizes** the flow that DevOps **automates**. DevOps pipelines are often modeled as Kanban stages. |
| **DevOps → Scrum** | Scrum defines **what** to build and **when** to review. DevOps defines **how** to build, deploy, and operate reliably. Complementary, not competing. |
| **DevOps → Phased** | DevOps practices (CI, automated testing) can be applied **within** phased gates to accelerate feedback without abandoning governance. |

---

## Prescriptive deep dive (teams)

Package **[`devops/README.md`](devops/README.md)** — foundation fit, roles (SRE, platform engineer, release engineer), ceremonies (deployment review, incident review, SLO review, blameless post-mortem), pipeline flow maps.

---

## Further reading

- [DORA — State of DevOps](https://dora.dev/) — **Research** on DevOps capabilities and metrics.  
- [The Phoenix Project](https://itrevolution.com/product/the-phoenix-project/) — **Novel** introducing DevOps concepts through story.  
- Companion: [Lean](lean.md), [Kanban](kanban.md), [Agile umbrella](agile.md), [Agentic SDLC](agentic-sdlc.md)
