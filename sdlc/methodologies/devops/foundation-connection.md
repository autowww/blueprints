# DevOps — connection to the SDLC foundation

DevOps treats the **entire** delivery pipeline — from code commit to production operation — as a **single system** to be optimized. The blueprint's **A–F** phases still apply; DevOps adds **automation**, **monitoring**, and **operational feedback** as first-class concerns.

## 1. SDLC phases A–F (DevOps lens)

| Phase | DevOps expression | Notes |
|-------|-------------------|-------|
| **A — Shape** | Feature flagging strategy; infrastructure requirements alongside functional requirements | Consider operability from the start |
| **B — Plan** | Pipeline design; deployment strategy; SLO targets | Plan how you will deploy and monitor, not just what you will build |
| **C — Build** | CI: automated build, lint, unit tests on every commit; IaC for environments | "Works on my machine" is not acceptable |
| **D — Verify** | Automated testing pyramid; security scanning; performance testing in pipeline | Shift quality left; automated gates replace manual checkpoints |
| **E — Release** | CD: automated deployment; canary/blue-green releases; feature flags | Decouple deployment from release; make deployments boring |
| **F — Operate & learn** | Monitoring, alerting, incident response, post-mortems; production feedback → A | Close the loop; production is not "someone else's problem" |

**Prescriptive rule:** DevOps is not just "automate deployment." It requires **cultural** change: shared ownership between Dev and Ops, blameless learning, and continuous improvement of the entire pipeline.

## 2. Tracking spine (mandatory link)

DevOps teams maintain the blueprint tracking spine with pipeline emphasis:

| Artifact | DevOps mapping |
|----------|----------------|
| **Intent / request** | Feature request, bug report, or operational improvement |
| **Spec** | Acceptance criteria + operability requirements (SLOs, monitoring, rollback) |
| **Plan** | Pipeline configuration; deployment plan; runbook |
| **Tasks** | Development + infrastructure tasks; pipeline improvements |
| **PRs** | Code + IaC + pipeline config changes in the same review |
| **Reviews** | Code review + deployment review + security review |
| **Release** | Automated deployment; release notes; monitoring confirmation |

**Prescriptive rule:** Infrastructure and pipeline changes should go through the **same review process** as application code. "ClickOps" (manual infrastructure changes) is technical debt.

## 3. Ceremony intents (C1–C6) ↔ DevOps practices

| Intent | DevOps practice | Notes |
|--------|-----------------|-------|
| **C1 — Align & decide** | Architecture review with operability lens; SLO setting | Include Ops perspective in design decisions |
| **C2 — Plan the slice** | Sprint/iteration planning includes deployment and monitoring tasks | Operational readiness is part of "done" |
| **C3 — Execute & unblock** | Stand-up (includes pipeline health); on-call coordination | Pipeline failures are blockers, not afterthoughts |
| **C4 — Review & quality** | Deployment review; DORA metrics review; SLO review | Measure the pipeline, not just the product |
| **C5 — Reflect & improve** | Blameless post-mortem; pipeline retrospective | Learn from incidents and near-misses |
| **C6 — Knowledge share** | Runbook updates; incident learnings; monitoring dashboards | Operational knowledge is team knowledge |

## 4. Role archetypes (blueprint hats on a DevOps team)

| DevOps role | Typical archetype emphasis | Notes |
|-------------|----------------------------|-------|
| **SRE (Site Reliability Engineer)** | **Assure & ship** + **Build** | Reliability engineering; SLOs; error budgets; automation |
| **Platform engineer** | **Build** + **Assure** | Internal developer platform; CI/CD infrastructure; developer experience |
| **Release engineer** | **Assure & ship** + **Orchestrator** | Release process; deployment automation; rollback procedures |
| **Development team** | **Build** (primary) + **Assure** (shared ownership) | "You build it, you run it" — shared production accountability |
| **On-call engineer** | **Assure** (incident response) | Rotated among team; first responder for production issues |

## 5. What DevOps adds beyond the foundation

- **Automation** — CI/CD pipelines, IaC, automated testing as first-class engineering.
- **Shared ownership** — "you build it, you run it" culture.
- **Feedback loops** — production monitoring feeds development priorities.
- **DORA metrics** — research-backed measures of delivery performance.
- **Blameless culture** — incidents are learning opportunities, not blame opportunities.

## 6. Anti-patterns (prescriptive "don't")

| Anti-pattern | Fix |
|--------------|-----|
| "DevOps team" as a separate silo | DevOps is a culture, not a team name; embed practices across all teams |
| Automating a broken process | Fix the process first, then automate; automation amplifies both efficiency and dysfunction |
| No production ownership by developers | "You build it, you run it" — developers participate in on-call and incident response |
| Measuring only deployment frequency | Use all four DORA metrics; frequency without quality is just faster failure |

## 7. References in-repo

- [`https://forgesdlc.com/methodologies-devops.html`](https://forgesdlc.com/methodologies-devops.html) — methodology summary + diagram  
- [`../ceremonies/devops.md`](../ceremonies/devops.md) — fork table C1–C6  
- [`../../SDLC.md`](../../SDLC.md) — phases and ceremony-intent overview  
