---
slug: discipline-devops
tier: 201
lens: discipline
nav_section: Disciplines
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# DevOps body of knowledge

This document maps the core concerns of **DevOps** — culture, automation, measurement, continuous delivery, observability, and incident management — to the blueprint ecosystem.

**How DevOps relates to PDLC and SDLC:** DevOps is a **cross-cutting discipline** that enables continuous delivery and operational excellence across both lifecycles. See [`DEVOPS-SDLC-PDLC-BRIDGE.md`](DEVOPS-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Practices:** Deep guides for specific practices (CI/CD, IaC, observability, etc.) are in [`practices/`](practices/README.md).

**Tooling:** Framework and platform guidance is in [`tooling/`](tooling/README.md).

---

## 1. The Three Ways

The Three Ways (from *The Phoenix Project* by Gene Kim) provide the philosophical foundation for DevOps:

| Way | Principle | Practices |
|-----|-----------|-----------|
| **First Way: Flow** | Accelerate the flow of work from development to operations to the customer | CI/CD, small batch sizes, WIP limits, automation of manual steps, trunk-based development |
| **Second Way: Feedback** | Create fast, frequent feedback loops from right to left | Automated testing, monitoring/alerting, A/B testing, fast rollback, telemetry in production |
| **Third Way: Continuous Learning** | Create a culture of experimentation, learning from failure, and improvement | Blameless postmortems, game days/chaos engineering, innovation time, shared knowledge bases |

---

## 2. CALMS framework

CALMS describes the five pillars of DevOps adoption:

| Pillar | Description | Indicators of maturity |
|--------|-------------|----------------------|
| **Culture** | Shared responsibility between dev and ops; trust, transparency, psychological safety | Blameless postmortems are standard; devs participate in on-call; cross-functional teams |
| **Automation** | Eliminate manual, repetitive work through tooling and scripting | CI/CD pipelines for all services; infrastructure as code; automated testing; self-service provisioning |
| **Lean** | Apply lean principles — eliminate waste, small batches, continuous improvement | WIP limits enforced; value stream mapping done; bottlenecks identified and addressed |
| **Measurement** | Use data to drive decisions about delivery performance and system health | DORA metrics tracked; SLOs defined; dashboards for pipeline health, system health, business metrics |
| **Sharing** | Break down silos; share knowledge, tools, and responsibilities | Runbooks maintained; cross-team code review; shared tooling; guilds/chapters for practices |

---

## 3. DORA metrics

The four key metrics from the DORA (DevOps Research and Assessment) program, validated across thousands of organizations:

| Metric | Definition | Elite | High | Medium | Low |
|--------|-----------|-------|------|--------|-----|
| **Deployment frequency** | How often code is deployed to production | On-demand (multiple/day) | Daily to weekly | Weekly to monthly | Monthly to semi-annually |
| **Lead time for changes** | Time from commit to production | Less than 1 hour | 1 day to 1 week | 1 week to 1 month | 1 to 6 months |
| **Change failure rate** | % of deployments causing production failure | 0–15% | 16–30% | 16–30% | 46–60% |
| **Time to restore** | Time from failure to restoration | Less than 1 hour | Less than 1 day | 1 day to 1 week | More than 6 months |

**Fifth metric — Reliability:** Added in 2021, measuring operational performance against targets (SLOs).

### How to use DORA metrics

- **Baseline** — measure current state before making changes
- **Trend** — track improvement over time, not absolute values
- **System-level** — measure per service or value stream, not per team (avoids gaming)
- **Complement with SDLC and PDLC metrics** — DORA measures delivery performance; SDLC metrics measure engineering quality; PDLC metrics measure product outcomes

---

## 4. DevOps maturity model

| Level | Characteristics | Focus areas |
|-------|----------------|-------------|
| **1 — Initial** | Manual processes, siloed teams, infrequent releases, long stabilization periods | Basic CI, version control, automated build |
| **2 — Managed** | CI pipeline, some automated testing, environments managed but not codified | Extend test automation, introduce IaC, define deployment process |
| **3 — Defined** | CD pipeline, IaC for all environments, monitoring in place, defined incident process | Shift-left security, observability (tracing, structured logging), SLO definition |
| **4 — Measured** | DORA metrics tracked, SLOs enforced, chaos engineering practiced, self-service platforms | Error budgets, advanced deployment strategies, platform engineering |
| **5 — Optimized** | Continuous improvement culture, fast experimentation, proactive capacity planning | Innovation time, cross-org knowledge sharing, contributing to internal platforms |

---

## 5. Site Reliability Engineering (SRE)

SRE (from Google) is an implementation of DevOps principles with specific practices:

| SRE concept | Description |
|-------------|-------------|
| **SLO / SLI / SLA** | Service Level Objectives (internal targets), Indicators (measurements), Agreements (external contracts) |
| **Error budgets** | Acceptable failure rate derived from SLO; budget remaining determines whether to prioritize features or reliability |
| **Toil** | Manual, repetitive, automatable work that scales linearly with service size; SRE aims to keep toil below 50% |
| **Capacity planning** | Proactive resource provisioning based on demand forecasting |
| **Blameless postmortems** | Learning from incidents without blame; focus on systemic improvements |

---

## 6. DevSecOps

Integrating security into the DevOps pipeline rather than treating it as a separate gate:

| Practice | Where in pipeline | Purpose |
|----------|-------------------|---------|
| **SAST (Static Application Security Testing)** | Build | Find vulnerabilities in source code |
| **SCA (Software Composition Analysis)** | Build | Identify vulnerable dependencies |
| **DAST (Dynamic Application Security Testing)** | Verify | Find vulnerabilities in running application |
| **Container scanning** | Build / Deploy | Verify container image security |
| **Secret detection** | Commit / Build | Prevent secrets from entering the codebase |
| **Infrastructure compliance** | Deploy | Verify IaC against security policies |
| **Runtime protection** | Operate | WAF, RASP, anomaly detection |

---

## 7. Competencies

| Competency | Description |
|------------|-------------|
| **Systems thinking** | Understanding the full delivery pipeline and its interactions; seeing bottlenecks and feedback loops |
| **Automation mindset** | Default to automating repetitive tasks; script-first approach to operations |
| **Collaboration** | Working across team boundaries; shared ownership of delivery and operations |
| **Incident response** | Structured approach to detecting, responding to, and learning from production incidents |
| **Infrastructure knowledge** | Understanding cloud platforms, networking, containers, orchestration |
| **Security awareness** | Integrating security practices into daily delivery work |

---

## 8. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| DORA — State of DevOps Report | https://dora.dev/ | Canonical research on DevOps performance metrics |
| Google SRE Books | https://sre.google/books/ | Free online SRE handbook, workbook, and security engineering |
| The Phoenix Project (Gene Kim) | https://itrevolution.com/product/the-phoenix-project/ | Narrative introduction to DevOps principles (Three Ways) |
| The DevOps Handbook (Kim, Humble, Debois, Willis) | https://itrevolution.com/product/the-devops-handbook-second-edition/ | Comprehensive DevOps practices guide |
| Continuous Delivery (Humble, Farley) | https://continuousdelivery.com/ | Foundational text on deployment pipelines and release engineering |
| DevOps Institute | https://www.devopsinstitute.com/ | Certification and competency framework |

---

*Keep project-specific CI/CD and operational documentation in `docs/development/CI-CD.md` and `docs/operations/`, not in this file.*