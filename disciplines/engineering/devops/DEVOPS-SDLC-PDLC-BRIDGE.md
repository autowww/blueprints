---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# DevOps ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **DevOps** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **DevOps** — "Can we deliver and operate **continuously and reliably**?"

DevOps accelerates the feedback loop between product intent (PDLC) and technical execution (SDLC) by automating delivery, improving observability, and enabling rapid iteration.

**Canonical sources:** [`DEVOPS.md`](https://forgesdlc.com/discipline-devops.html) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; how DevOps relates to PDLC and SDLC |
| [Comparison table](#comparison-table) | DevOps vs SDLC vs PDLC — scope, ownership, metrics, risks |
| [When one is missing](#when-one-is-missing) | Consequences when DevOps, SDLC, or PDLC are practiced in isolation |
| [DevOps across the lifecycle](#devops-across-the-lifecycle) | Activities and outputs mapped to PDLC P1–P6 and SDLC A–F |
| [Role mapping](#role-mapping) | Who owns DevOps work at each phase; SDLC roles and archetypes |
| [Artifact flow](#artifact-flow) | Handoffs between DevOps, SDLC, and PDLC |
| [Calibration](#calibration) | When to invest more or less in DevOps by initiative and context |
| [Anti-patterns](#anti-patterns) | Common failures when DevOps is siloed or misunderstood |
| [DevOps and SDLC methodologies](#devops-and-sdlc-methodologies) | Emphasis across Scrum, Kanban, XP, phased, and DevOps-as-methodology |
| [Worked example](#worked-example) | End-to-end scenario — pipeline for a new microservice |
| [Related reading](#related-reading) | Authoritative docs in this package and sibling lifecycles |

---

## Comparison table

| Dimension | DevOps | SDLC | PDLC |
|-----------|--------|------|------|
| **Core question** | Can we deliver and operate continuously and reliably? | How do we build this correctly? | Should we build this; does it create the right outcomes? |
| **Scope** | Culture, automation, measurement, and sharing (CALMS); CI/CD; IaC; GitOps; observability; incident management; platform capabilities | Requirements → design → implementation → verification → release (**A** Discover through **F** Release) | Problem discovery → validation → strategy → launch → growth → sunset (**P1**–**P6**) |
| **Primary owner** | Platform / SRE / embedded engineers — often **Flow & improvement** with **Build & integrate**; product may co-own SLOs tied to outcomes | Delivery team; **Owner** (priorities, acceptance) and **Implementer** (build, verify) per [`SDLC.md`](../../../sdlc/SDLC.md) | Product manager / product trio; GTM where relevant |
| **Timeline** | Continuous — pipelines and production never “pause” | Sprint, iteration, or release train cadence | Product lifetime (months to years) |
| **Success metric** | DORA metrics (deployment frequency, lead time for changes, change failure rate, time to restore); SLO attainment; error budget policy; MTTR | Velocity, defect escape rate, CI/CD gate pass rate, quality attributes in DoD | Adoption, retention, revenue, NPS, outcome KPIs |
| **Key artifacts** | Pipeline definitions, IaC modules, runbooks, dashboards, alerting rules, postmortems, SLO/error-budget docs | Specs, designs, code, tests, release notes | Research synthesis, experiments, strategy, launch and growth metrics |
| **Risk focus** | Delivery friction, operational surprise, security and compliance drift, toil, alert fatigue | Technical risk — correctness, performance, security | Market and outcome risk — desirability, viability, fit |
| **Failure mode** | Slow, manual releases; fragile production; opaque systems; learning does not flow back to product and engineering | Late or low-quality delivery; weak feedback from production | Right execution of the wrong thing; strategy disconnected from operational reality |

### How common DevOps ideas appear in this bridge

| Idea | Where it is reflected |
|------|------------------------|
| **CALMS** | Collaboration in role mapping; automation and measurement in phase alignment **D**–**F** and artifact flow; lean handoffs in calibration |
| **DORA metrics** | Comparison table success metrics; calibration signals for delivery health |
| **Three Ways** | Systems view across SDLC and ops; amplified feedback in **DevOps → PDLC** signals; experimentation bounded by error budgets in **P5** |
| **SRE** | SLOs and error budgets in **B**, **P4**, **P5**; toil reduction as a calibration lens |
| **CI/CD, IaC, GitOps** | **A**–**F** roles; pipeline and IaC artifacts in artifact flow |
| **Observability & incidents** | **P4**–**P5** operations enabler and reliability guardian; postmortems feeding PDLC and SDLC backlogs |

---

## When one is missing

| Scenario | What happens |
|----------|-------------|
| **DevOps without SDLC discipline** | Automation exists but delivery is inconsistent — ad hoc branching, skipped reviews, flaky tests, or pipelines that nobody trusts. Tooling without engineering rigor produces **green builds and red production**. |
| **DevOps without PDLC** | Excellent pipelines and uptime for software that does not move business outcomes. Reliability is optimized without questioning **what** is worth operating. |
| **SDLC without DevOps** | Code may be sound, but releases are batched and manual; feedback from production is slow; incidents are painful. **Lead time** and **recovery** suffer regardless of story quality. |
| **PDLC without DevOps** | Strategy and discovery are strong, but launches are risky and learning loops are long. Product decisions lack timely data from **deployment, usage, and incident** signals. |
| **PDLC + SDLC, weak DevOps** | The right thing is specified and built well, but shipping and operating remain expensive and scary. Common in organizations that “finished” a transformation slide deck but not the platform. |
| **All three practiced** | Validated direction feeds clear specs and sustainable delivery; automation and observability shorten the loop from idea to evidence, and operational learning informs the next PDLC and SDLC cycle. |

---

## DevOps across the lifecycle

| Phase | DevOps role | Key activities | Outputs |
|-------|-------------|----------------|---------|
| **P1–P2 Discover/Validate** | — | Minimal direct involvement; may support prototype environments | Sandbox environments for experiments |
| **P3 Plan & Commit** | **Infrastructure planner** | Estimate infrastructure needs; identify build/deploy constraints; cost modeling | Infrastructure requirements, cost estimates |
| **A Discover** | **Pipeline designer** | Define CI/CD strategy; select tools; plan environments (dev/staging/prod) | Pipeline architecture, environment strategy |
| **B Specify** | **Automation architect** | Define deployment topology; IaC approach; monitoring requirements; SLO targets | IaC templates, SLO definitions, monitoring plan |
| **C Design** | **Infrastructure designer** | Design cloud architecture; networking; container orchestration; secrets management | Cloud architecture diagrams, IaC modules |
| **D Build** | **Pipeline builder** | Implement CI/CD pipelines; configure quality gates; automate test execution; set up IaC | Working pipelines, automated builds, environment provisioning |
| **E Verify** | **Quality gate enforcer** | Run automated test suites; security scans; performance tests; compliance checks | Pipeline green/red, security scan results, performance baselines |
| **F Release** | **Release engineer** | Execute deployment strategy (blue-green, canary, rolling); feature flag management; rollback readiness | Deployed artifacts, deployment verification, rollback plan |
| **P4 Launch** | **Operations enabler** | Production monitoring; alerting; on-call setup; runbook creation | Monitoring dashboards, alerting rules, runbooks |
| **P5 Grow** | **Reliability guardian** | SLO tracking; error budget management; capacity planning; incident management; chaos engineering | SLO reports, incident postmortems, capacity forecasts |
| **P6 Sunset** | **Decommission operator** | Infrastructure teardown; data migration; DNS/traffic redirection | Decommission plan, migration scripts |

---

## Role mapping

Who carries DevOps accountability at each lifecycle step, alongside PDLC and SDLC. In small teams, one engineer may wear pipeline builder, release engineer, and on-call hats; in larger orgs, a **platform** or **SRE** function supplies templates while product teams retain service ownership. SDLC uses **Owner** and **Implementer**; archetypes follow [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md).

| Phase(s) | DevOps stance | PDLC accountability (typical) | SDLC accountability | Archetype |
|----------|---------------|------------------------------|---------------------|-----------|
| **P1–P2** | Optional enabler of experiments | PM, UX research, discovery | — (upstream of formal SDLC) | Demand & value |
| **P3** | **Infrastructure planner** — constraints and cost | PM, strategy, GTM alignment | Owner (initiative framing); Implementer consulted on feasibility | Steer & govern; Demand & value |
| **A Discover** | **Pipeline designer** | — | Owner (priorities, tooling budget); Implementer (spikes, tool evaluation) | Flow & improvement; Build & integrate |
| **B Specify** | **Automation architect** | — | Owner (acceptance of NFRs/SLOs); Implementer (technical specs) | Build & integrate; Assure & ship |
| **C Design** | **Infrastructure designer** | — | Implementer (architecture); Owner consulted on trade-offs | Build & integrate |
| **D Build** | **Pipeline builder** | — | Implementer (pipeline as code, IaC); Owner removes blockers | Build & integrate |
| **E Verify** | **Quality gate enforcer** | — | Implementer (fix failures); Assure & ship (gate interpretation) | Assure & ship; Build & integrate |
| **F Release** | **Release engineer** | GTM for launch comms | Implementer executes; Owner for business go/no-go where applicable | Assure & ship; Flow & improvement |
| **P4 Launch** | **Operations enabler** | PM, GTM — outcome and readiness | SDLC **F** overlaps — production cutover | Assure & ship; Demand & value |
| **P5 Grow** | **Reliability guardian** | PM, analytics — outcomes vs SLOs | Iteration cycles **A**–**F** for improvements | Flow & improvement; Assure & ship |
| **P6 Sunset** | **Decommission operator** | PM, legal/comms — customer and data | Implementer executes teardown; Steer & govern on policy | Steer & govern; Build & integrate |

---

## Artifact flow

### PDLC / SDLC → DevOps (inputs)

| Source | DevOps usage |
|--------|----------------|
| Success metrics and launch criteria (**P3**, **P4**) | Define SLOs, alerting thresholds, and dashboard views tied to product outcomes |
| NFRs and compliance constraints (**B**, **C**, **Steer & govern**) | Shape IaC policies, secrets handling, audit logging, and pipeline compliance stages |
| Release intent and windows (**Owner**, **F**) | Drive deployment strategy (canary vs blue-green), feature flags, and freeze policies |
| Acceptance criteria (**B**) | Configure quality gates — tests, scans, policy-as-code — that match Definition of Done |
| Architecture boundaries (**C**) | Inform service topology, network policies, and observability cardinality |

### DevOps → SDLC (outputs)

| DevOps artifact | SDLC usage |
|-----------------|------------|
| CI/CD pipeline definitions (**D**–**F**) | Enforce build, test, and deploy steps; encode team DoD in automation |
| Ephemeral environments (**A**–**D**) | Speed discovery and integration testing; reduce “works on my machine” |
| Test and scan results (**E**) | Gate merges and releases; feed defect backlog |
| Deployment manifests and IaC (**C**–**F**) | Executable representation of design; reviewable like application code |
| Release automation records (**F**) | Audit trail for who deployed what, when, and how rollback was exercised |

### DevOps → PDLC (feedback)

| DevOps signal | PDLC usage |
|---------------|------------|
| DORA metrics and lead time | Inform **P3** investment and **P5** pace of experimentation — can the org learn fast enough? |
| SLO / error budget reports | Guide trade-offs between reliability work and new features |
| Incident and postmortem themes | Surface systemic product or UX issues; input to **P1**–**P2** and **P5** |
| Cost and utilization data from infrastructure | Feed viability and pricing conversations in **P3** and **P5** |
| Production usage and performance baselines | Validate whether launches (**P4**) met scale and experience expectations |

### Closed-loop summary

| Direction | Essence |
|-----------|---------|
| **Into DevOps** | Product intent, NFRs, and release policy become **automated policy, SLOs, and environments**. |
| **Out to SDLC** | Pipelines and infrastructure encode **DoD, quality gates, and repeatable release mechanics**. |
| **Out to PDLC** | Telemetry, incidents, and delivery metrics answer **whether we can learn and operate at the pace the product needs**. |

---

## Calibration

### By initiative type

| Situation | DevOps investment | Reasoning |
|-----------|-----------------|-----------|
| **Greenfield product** | **High** — establish pipelines, IaC, observability, and incident process early; cheap to fix now, expensive later | Foundations set culture (CALMS) and prevent “retrofit DevOps” after users depend on the system |
| **Feature on mature product** | **Medium** — extend existing pipelines; focus on contract tests, flags, and canaries at service boundaries | Marginal cost is low when platform exists; risk is regression and blast radius |
| **Infrastructure / platform change** | **High** — migration runbooks, parallel environments, heavy verification and rollback drills | Users are other teams or systems; failure is widespread |
| **Bug fix / small change** | **Targeted** — use existing gates; add automation only when the gap caused the defect | Avoid gold-plating the pipeline for one-line fixes |
| **Spike / throwaway prototype** | **Low** — manual deploy or single shared sandbox; do not build production-grade IaC until **P3** commits | Match automation to expected lifetime |
| **Maintenance, hardening, or sunset** | **Medium to high** — automation for repeatable patching, backups, and teardown; **P6** needs migration and traffic-switch playbooks | Operational mistakes during low-glamour work cause outages; decommission is easy to defer until it becomes an incident |

### By organizational context

| Context | DevOps emphasis |
|---------|-----------------|
| **Startup / small team** | Single pipeline, shared on-call, minimal ceremony; strong **sharing** and **measurement** over heavy process |
| **Growing product org** | Platform team or internal enablement; standard templates; SRE partnership for critical services |
| **Enterprise** | Federated standards, centralized identity and secrets, change windows, and portfolio-level visibility |
| **Regulated** | Immutable audit trails, segregation of duties in pipelines, evidence collection for releases, controlled promotion paths |

### Concepts that guide depth

| Lens | When to lean on it |
|------|-------------------|
| **CALMS** | Culture and sharing before buying more tools; automation where repetition hurts; lean out waste in handoffs |
| **Three Ways** | Systems thinking across SDLC and ops; amplify feedback loops into PDLC; foster experimentation within error budgets |
| **DORA** | Baseline improvement conversations with leadership — connect delivery performance to outcomes |
| **SRE** | When reliability is contractual or brand-critical — explicit SLOs, error budgets, and toil budgets |

### Signals you may be over- or under-investing

| Signal | Interpretation |
|--------|------------------|
| **Under-invested** | Releases require heroics; on-call burns out; postmortems repeat the same themes; DORA metrics stall despite healthy SDLC practices |
| **Well calibrated** | Most deploys are routine; incidents are rare relative to change volume; error budget policy drives honest trade-offs with product |
| **Over-engineered (for context)** | Platform complexity exceeds team skill or product maturity — hard to change pipelines, long lead time to onboard a service, governance without enablement |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **DevOps team** | Creating a separate "DevOps team" that becomes a new silo between dev and ops | DevOps is a practice, not a team name; embed DevOps skills in delivery teams; platform team enables, doesn't gate |
| **Automate everything immediately** | Trying to automate all operations at once before understanding the manual process | Start with the highest-frequency manual tasks; understand before automating; iterate |
| **Monitoring without action** | Dashboards exist but nobody looks at them; alerts fire but nobody responds | Define SLOs first; alert on SLO violations, not individual metrics; establish on-call rotation |
| **Infrastructure as ClickOps** | Infrastructure provisioned through cloud console clicks, not code | Adopt IaC incrementally; start with new environments; backfill existing infrastructure |
| **CI without CD** | Automated build and test but manual deployment; "we do DevOps" because we have Jenkins | Extend pipeline to staging/production deployment; start with a single service; prove value then expand |

---

## DevOps and SDLC methodologies

DevOps practices apply across all SDLC methodologies, with different emphasis:

| Methodology | DevOps emphasis |
|-------------|-----------------|
| **Scrum** | CI/CD enables potentially shippable increment every sprint; automated testing supports sprint velocity |
| **Kanban** | Pipeline metrics (lead time, throughput) align with Kanban flow metrics; WIP limits apply to deployment queue |
| **XP** | CI is a core XP practice; DevOps extends CI to continuous delivery and deployment |
| **Phased** | DevOps provides automated quality gates at phase boundaries; infrastructure provisioning for each phase |
| **DevOps (methodology)** | The SDLC methodology lens in [`sdlc/methodologies/devops/`](../../../sdlc/methodologies/devops/README.md) describes how DevOps shapes phases, ceremonies, and roles |

---

## Worked example

**Scenario:** A product team commits in **P3** to extract a bounded context into a **new microservice**. Delivery must support independent deploys without breaking the monolith’s release train.

**Prerequisites:** A shared container registry, identity for CI, and agreement on observability standards already exist — the example focuses on **new** service onboarding, not greenfield platform creation.

| Step | Lifecycle | What happens |
|------|-----------|--------------|
| 1 | **P3** | Infrastructure planner works with PM and engineering to estimate compute, data store, and egress costs; flags regulatory logging needs. Outputs feed the business case. |
| 2 | **A** | Pipeline designer chooses CI/CD and container registry; defines dev/stage/prod parity goals and trunk-based vs branch strategy for the new repo. |
| 3 | **B** | Automation architect specifies IaC modules, deployment topology, initial SLO draft (availability, latency), and which security scans are release-blocking. |
| 4 | **C** | Infrastructure designer produces network diagrams, service mesh or ingress rules, secrets flow, and observability labels (trace correlation with the monolith). |
| 5 | **D** | Pipeline builder implements workflows: build, unit tests, container image, integration tests against contract stubs, push to staging. IaC creates namespaces and databases from templates. |
| 6 | **E** | Quality gate enforcer wires SAST/DAST (as appropriate), load test in staging, and policy checks (e.g. no latest tags in prod). Gates mirror the team DoD. |
| 7 | **F** | Release engineer runs a **canary** release with automated promotion on metrics; feature flags guard monolith call paths. Rollback is practiced once before go-live. |
| 8 | **P4** | Operations enabler completes dashboards, SLO-based alerts, on-call rotation, and runbooks — including “fail back to monolith” path. |
| 9 | **P5** | Reliability guardian tracks error budgets; postmortems from incidents feed backlog items that may span **P1**–**P2** (product) and **A**–**D** (technical debt). |

**Outcome:** Product gets faster iteration on the new service, leadership sees **lead time** and **change failure rate** improve for that slice, and operational feedback loops connect **P5** metrics to the next planning cycle.

| Without strong PDLC | Without disciplined SDLC | Without DevOps |
|--------------------|-------------------------|----------------|
| The service might ship on time but solve the wrong decomposition — observability shows usage patterns that contradict the split. | Correct design but manual deploys — the monolith train still gates value; incidents are hard to attribute. | Fast coding but production is opaque — **P4** launch risks a reputation hit; **P5** cannot tell whether issues are product or platform |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`DEVOPS.md`](https://forgesdlc.com/discipline-devops.html) | CALMS, Three Ways, DORA metrics, SRE, DevSecOps |
| [`practices/README.md`](practices/README.md) | CI/CD, IaC, GitOps, observability, incident management |
| [`tooling/README.md`](tooling/README.md) | Container orchestration, deployment strategies, secrets management |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD, CI/CD section |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, launch and growth |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | How product and delivery lifecycles align — complements this discipline view |
| [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) | SDLC role archetypes and Owner / Implementer expectations |
| [`sdlc/methodologies/devops/`](../../../sdlc/methodologies/devops/README.md) | DevOps as SDLC methodology — phases, ceremonies, roles |
