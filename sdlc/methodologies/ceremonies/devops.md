# DevOps ceremonies → ceremony foundation

**Purpose:** Map **DevOps** operational practices and feedback loops to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical DevOps narrative:** [`../devops.md`](../devops.md) · [DORA](https://dora.dev/) · [Wikipedia — DevOps](https://en.wikipedia.org/wiki/DevOps)

**Note:** DevOps ceremonies **complement** development ceremonies (Scrum, Kanban, XP). Below covers **operational** and **pipeline** practices.

---

## Practices / meetings × intent types

| Common practice | Foundation intents (primary → secondary) | Notes |
|-----------------|------------------------------------------|--------|
| **Architecture review** (with operability lens) | **C1 Align** → **C2 Commit** | Include SLOs, monitoring, and deployment strategy in design decisions. |
| **Sprint/iteration planning** (DevOps-aware) | **C2 Commit** | Include deployment tasks, infrastructure work, and reliability improvements in the plan. |
| **Stand-up** (pipeline-aware) | **C3 Sync** | Pipeline health and deployment status are part of daily sync. |
| **Deployment review** | **C4 Inspect** → **C6 Assure** | Pre-deployment check: changes, rollback plan, monitoring readiness. |
| **SLO review** | **C4 Inspect** → **C1 Align** | Review reliability performance; inform feature vs reliability investment decisions. |
| **Blameless post-mortem** | **C5 Improve** → **C6 Assure** | Learn from incidents; prevent recurrence through systemic fixes. |
| **Pipeline retrospective** | **C5 Improve** | Review DORA metrics; identify pipeline improvements and toil reduction. |
| **On-call handoff** | **C3 Sync** → **C6 Assure** | Context transfer between on-call rotations; awareness of active issues. |
| **Automated pipeline gates** | **C6 Assure** (embedded) | CI/CD quality gates: build, test, scan, deploy — automated assurance. |

**C6** in DevOps is heavily **automated**: CI/CD pipelines, automated testing, security scanning, and deployment automation provide continuous assurance without manual ceremony.

---

## Tracking

**DORA metrics** (deployment frequency, lead time, change failure rate, MTTR) are the primary DevOps health indicators. Collect from pipeline and monitoring tools; review in SLO reviews and pipeline retros.

---

## Suggestions (DevOps-specific)

| Practice | Suggestions |
|----------|-------------|
| **Deployment review** | For fully automated CD, replace with **policy checks** and **automated gates**. Reserve manual review for high-risk changes. |
| **Post-mortem** | Write and share within 5 business days. Focus on **contributing factors** and **systemic fixes**, not blame. Track action items to completion. |
| **SLO review** | Use **error budgets** to make feature vs reliability trade-offs explicit. If error budget is exhausted, prioritize reliability work. |
| **Pipeline retro** | Measure **toil** (manual, repetitive operational work). Set a target to automate the top toil item each cycle. |
| **On-call** | Keep rotation sustainable (no more than 1 week in 4). Compensate fairly. Review on-call burden in retros. |

Crosswalk to other methodologies: [`methodology-bridge.md`](methodology-bridge.md).
