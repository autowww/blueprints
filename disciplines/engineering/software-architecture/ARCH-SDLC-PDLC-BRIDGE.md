# Architecture ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **software architecture** practices to the two lifecycle frameworks it serves:

- **PDLC** (Product Development Life Cycle) — "Are we building the **right product**?"
- **SDLC** (Software Development Life Cycle) — "Are we building the product **right**?"
- **Architecture** — "**How** should the system be structured to satisfy both quality and business needs?"

Architecture provides the structural reasoning that connects product vision (PDLC) to technical execution (SDLC). Without it, products may be validated but poorly built, or well-coded but structurally unsound.

**Canonical sources:** [`SOFTWARE-ARCHITECTURE.md`](SOFTWARE-ARCHITECTURE.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; how architecture relates to PDLC and SDLC |
| [Canonical sources](#canonical-sources) | Authoritative docs for architecture and both lifecycles |
| [Comparison table](#comparison-table) | Architecture vs SDLC vs PDLC — scope, ownership, artifacts, failure modes |
| [When one is missing](#when-one-is-missing) | Consequences of practicing one domain without the others |
| [How architecture connects PDLC and SDLC](#how-architecture-connects-pdlc-and-sdlc) | Diagram plus PDLC / SDLC phase reference (P1–P6, A–F) |
| [Architecture across the lifecycle](#architecture-across-the-lifecycle) | Activities and outputs mapped to P1–P6 and A–F |
| [Role mapping](#role-mapping) | Who holds design authority at each phase; SDLC roles and archetypes |
| [Artifact flow](#artifact-flow) | Handoffs Architecture → SDLC, Architecture → PDLC, and feedback loops |
| [Calibration](#calibration) | Governance by context, initiative type, and tech debt lifecycle |
| [Anti-patterns](#anti-patterns) | Common failures when architecture is absent, isolated, or misapplied |
| [Worked example](#worked-example) | End-to-end scenario across PDLC and SDLC |
| [Related reading](#related-reading) | Deeper references in this repo |

---

## Canonical sources

| Domain | Authoritative doc |
|--------|-------------------|
| **Software architecture** (this package) | [`SOFTWARE-ARCHITECTURE.md`](SOFTWARE-ARCHITECTURE.md) |
| **PDLC** | [`PDLC.md`](../../../pdlc/PDLC.md) |
| **SDLC** | [`SDLC.md`](../../../sdlc/SDLC.md) |
| **Cross-lifecycle handoff** (optional) | [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) |
| **SDLC roles and archetypes** | [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) |

---

## Comparison table

| Dimension | Architecture | SDLC | PDLC |
|-----------|--------------|------|------|
| **Core question** | How should the system be structured to satisfy quality and business needs? | Are we building the product right? | Are we building the right product? |
| **Scope** | Structure, constraints, evolution — quality attributes, boundaries, decisions, technical debt | Requirements through release — specify, build, verify, ship increments | Problem discovery through sunset — validate, plan & commit, launch, grow, retire |
| **Primary owner** | Tech lead / architect / architecture chapter (calibrated by context) | Engineering / delivery team (Owner + Implementer) | Product manager / product trio |
| **Timeline** | Long-horizon — spans releases; decisions outlive individual projects | Sprint / iteration / release cycle | Product lifetime (months to years) |
| **Success metric** | Fitness for NFRs, sustainable evolution, decision traceability, controlled debt | Velocity, defect rate, DORA metrics, CI quality gates | Adoption, retention, revenue, outcome metrics |
| **Key artifacts** | ADRs, C4 views (context → code), NFR catalogs, fitness functions, quality-attribute workshop outputs, tech debt registers | Specs, code, tests, release notes, build pipelines | Research synthesis, experiments, vision, metrics dashboards |
| **Risk focus** | Structural risk — coupling, scalability, security posture, operability, debt accumulation | Technical execution risk — correctness, regressions, release readiness | Market and strategy risk — desirability, viability, timing |
| **Failure mode** | Accidental architecture, ungoverned debt, or ivory-tower designs that delivery ignores | Fragile or incorrect implementation despite good intent | A validated direction that the system cannot sustain affordably |

---

## When one is missing

| Scenario | What happens |
|----------|--------------|
| **Architecture without PDLC** | Sound technical reasoning with no validated product anchor — elegant systems for problems users do not care about, or NFRs misaligned with real success criteria |
| **Architecture without SDLC** | Diagrams and decisions that never land in code — paper architecture, stale views, no fitness functions or compliance feedback |
| **PDLC without Architecture** | Strategy and outcomes without structural guardrails — scope expands into unbounded integration cost, NFRs discovered late, rework when scale or compliance bites |
| **SDLC without Architecture** | Fast delivery of a growing ball of mud — local optimizations, inconsistent patterns, rising defect and operations tax |
| **PDLC + SDLC, weak architecture** | Features ship and metrics move short term while debt and coupling compound — predictable slowdowns, incident frequency, and expensive pivots |
| **All three practiced** | Validated direction, explicit structure, and disciplined delivery reinforce each other — traceable decisions, testable qualities, and sustainable evolution |

---

## How architecture connects PDLC and SDLC

```blueprint-diagram
key: swimlane
alt: Diagram
```

### PDLC phases (reference)

| Phase | Name |
|-------|------|
| **P1** | Discover Problem |
| **P2** | Validate Solution |
| **P3** | Plan & Commit |
| **P4** | Launch |
| **P5** | Grow |
| **P6** | Mature / Sunset |

### SDLC phases (reference)

| Phase | Name |
|-------|------|
| **A** | Discover |
| **B** | Specify |
| **C** | Design |
| **D** | Build |
| **E** | Verify |
| **F** | Release |

PDLC and SDLC run on **different clocks** — one product outcome may span many delivery increments, and P5 (Grow) often contains repeated A–F cycles. Use the [lifecycle table](#architecture-across-the-lifecycle) as the authoritative activity map, not a strict one-to-one phase equality.

---

## Architecture across the lifecycle

| Phase | Architecture role | Key activities | Outputs |
|-------|-------------------|----------------|---------|
| **P1 Discover** | — | Minimal; awareness of existing system constraints | — |
| **P2 Validate** | **Feasibility assessor** | Technical feasibility spikes; early NFR identification; "can we build this?" | Feasibility assessment, technology risk notes |
| **P3 Plan & Commit** | **Solution shaper** | Define NFRs from success criteria; high-level architectural options; build-vs-buy decisions | Architecture options paper, high-level diagrams (C4 L1–L2), NFR catalog |
| **A Discover** | **Design authority** | Decompose NFRs into architectural constraints; identify cross-cutting concerns; draft system context | C4 context diagram, initial ADRs, cross-cutting concerns register |
| **B Specify** | **Design authority** | Define component boundaries; specify interfaces and contracts; create data models | C4 container/component diagrams, API contracts, data models, ADRs |
| **C Design** | **Lead designer** | Detailed design of complex components; pattern selection; prototype critical paths | Detailed design docs, pattern decisions, spike results |
| **D Build** | **Reviewer / guardian** | Architecture review of PRs; enforce fitness functions; mentoring on patterns | Review comments, fitness function results, architectural guidance |
| **E Verify** | **Quality gatekeeper** | Verify NFRs met (performance, security, scalability tests); architecture compliance checks | NFR test results, architecture compliance report |
| **F Release** | **Deployment advisor** | Review deployment architecture; validate infrastructure readiness | Deployment architecture review, go/no-go input |
| **P4 Launch** | — | Operational readiness review | — |
| **P5 Grow** | **Evolution planner** | Assess scalability needs; identify tech debt; plan architectural evolution | Tech debt register, scalability assessment, evolution roadmap |
| **P6 Sunset** | **Migration advisor** | Plan data migration, service decomposition, or graceful shutdown | Migration architecture, sunset plan |

---

## Role mapping

### Across the lifecycle

| Phase(s) | Architecture accountability | PDLC role | SDLC role | Archetype |
|----------|----------------------------|-----------|-----------|-----------|
| **P1 Discover** | Passive context awareness | PM, UX Researcher | — (upstream) | Demand & value |
| **P2 Validate** | Feasibility and risk voice | PM, UX Researcher; engineering in spikes | Implementer (spikes) | Build & integrate + Demand & value |
| **P3 Plan & Commit** | Options, NFRs, major technical boundaries | PM, GTM Lead | Owner (prioritization), Implementer (estimates) | Steer & govern + Demand & value |
| **A–B Discover / Specify** | Design authority for structure and contracts | — | Owner (scope trade-offs), Implementer (detailed specs) | Build & integrate |
| **C Design** | Lead designer for complex or novel areas | — | Implementer (design execution), Owner (acceptance of trade-offs) | Build & integrate |
| **D Build** | Reviewer / guardian — patterns, boundaries, debt signals | — | Implementer (commits), Owner (ordering) | Build & integrate + Flow & improvement |
| **E Verify** | NFR and compliance interpretation | — | Implementer (fixes), QA / quality roles | Assure & ship |
| **F Release** | Deployment and operational architecture input | GTM Lead | Implementer (release engineering) | Assure & ship |
| **P4 Launch** | Light operational readiness | GTM Lead | — | Assure & ship |
| **P5 Grow** | Evolution planning, debt governance, scalability | PM, Data / Analytics | Owner (backlog), Implementer | Flow & improvement + Demand & value |
| **P6 Mature / Sunset** | Migration and decomposition design | PM, Exec sponsor | Owner / Implementer (if migration delivery) | Steer & govern |

### Architecture vs Product vs Delivery (typical split)

| Dimension | Architecture | Product (PDLC lead) | Delivery (SDLC Owner / Implementer) |
|-----------|--------------|---------------------|-------------------------------------|
| **Primary question** | Is the structure fit for purpose now and next? | Is this the right bet for users and business? | What ships this increment, and is it done to our bar? |
| **Decision rights** | Cross-cutting technical principles, major technology choices, NFR interpretation | Outcomes, scope, success metrics, stage gates | How to implement within agreed constraints |
| **Overlap to manage** | All three negotiate trade-offs among scope, time, quality, and debt — architecture supplies the **cost-of-change** view for technical options | — | — |

---

## Artifact flow

### Architecture → SDLC

| Architecture artifact | SDLC destination | Usage |
|----------------------|------------------|--------|
| ADRs (Architecture Decision Records) | Phases A–C (decision context); D–E (compliance checks) | Record constraints and rejected alternatives; anchor reviews and refactors |
| C4 diagrams (Context, Container, Component, Code) | Phases B–C (design); D (integration boundaries) | Shared vocabulary for modules, APIs, and deployment units |
| NFR catalog / quality-attribute workshop outputs | Phases B–E | Specify measurable thresholds; drive test plans and fitness functions |
| Fitness functions (automated checks) | Phases D–F | CI/CD gates for boundaries, dependency rules, performance budgets |
| API contracts / data models | Phase B–C | Implementer builds to agreed interfaces; reduces uncoordinated drift |
| Tech debt register items (as backlog inputs) | Phases A–D | Owner prioritizes remediation alongside features; Implementer executes |

### Architecture → PDLC

| Architecture artifact | PDLC destination | Usage |
|----------------------|------------------|--------|
| Feasibility assessments | P2 Validate | Evidence for build-vs-experiment decisions |
| Architecture options paper | P3 Plan & Commit | Informs investment, sequencing, and risk disclosures at stage gates |
| NFR catalog linked to success metrics | P3, P5 Grow | Aligns technical limits with outcome targets (latency, availability, cost) |
| Evolution roadmap / scalability assessment | P5 Grow | Supports capacity planning, pricing, and platform bets |
| Migration / sunset architecture | P6 Mature / Sunset | De-risks customer transition and data exit |

### PDLC / SDLC → Architecture (feedback)

| Source | Architecture usage |
|--------|-------------------|
| PDLC success metrics and usage patterns (P5) | Revisit context diagrams, capacity models, and service boundaries |
| PDLC stage-gate decisions (P2–P3) | Trigger ADR updates when scope or strategy shifts materially |
| SDLC Phase E NFR test results and incident postmortems | Refine fitness functions, patterns, and debt register |
| SDLC Phase D PR review comments and refactor themes | Identify recurring violations — signal missing guidance or wrong boundaries |
| SDLC Phase A–B backlog and acceptance criteria | Surface new cross-cutting concerns and interface stability needs |

---

## Calibration

### Architecture governance by context

| Context | Architecture governance level |
|---------|-------------------------------|
| **Solo / small startup** | Implicit — architect is the developer; decisions documented in code and light ADRs |
| **Single team (3–8)** | Light — tech lead holds architecture authority; ADRs for significant decisions; peer review |
| **Multi-team (8–25)** | Moderate — dedicated architect or architecture chapter; cross-team design reviews; fitness functions |
| **Enterprise** | Heavy — architecture board; TOGAF or similar framework; formal compliance; architecture runway |

### Calibration by initiative type

| Initiative type | Architecture investment | Reasoning |
|-----------------|------------------------|-----------|
| **Greenfield** | **Heavy** — context and container views, explicit NFR catalog, early ADRs, baseline fitness functions | Uncertainty is structural; early boundaries cheap, late rewrites expensive |
| **Feature on mature product** | **Medium** — targeted ADRs at integration points; update C4 where boundaries move; extend fitness functions for new paths | Most structure exists; risk concentrates at seams and shared data |
| **Infrastructure / platform** | **Heavy on NFRs and operations** — reliability, observability, security, and consumer contracts dominate | Users are other teams and systems; failures are widespread and costly |
| **Bug fix / maintenance** | **Light** — fix-level reasoning; add ADR only if the fix changes a principle; register debt if shortcut taken | Small surface area; avoid process drag — still record intentional debt |
| **Enterprise transformation** | **Heavy** — formal governance, cross-domain roadmaps, strong alignment to compliance and portfolio standards | Many stakeholders, long-lived commitments, audit and integration pressure |

### Tech debt lifecycle (across PDLC and SDLC)

| Stage | Lifecycle anchor | Architecture role | Typical artifacts |
|-------|------------------|-------------------|-------------------|
| **Detect** | P5 Grow; ongoing D Build / E Verify | Make debt visible — incidents, regressions, coupling metrics, manual workarounds | Tech debt register entries, links to ADRs or fitness-function failures |
| **Triage** | P3–P5 prioritization; SDLC A Discover | Frame **cost of delay** and **risk** with product and delivery — not all debt is equal | Ranked debt backlog; impact notes for Owner |
| **Remediate** | SDLC D Build (primary); sometimes dedicated increments | Execute with guardrails — ADR if principles change; extend tests / fitness functions | PRs, migration plans, updated diagrams |
| **Verify** | SDLC E Verify | Prove NFRs and boundaries hold after change; watch for new debt from the fix | NFR test results, compliance reports |
| **Govern** | Calibration (context) + P5 Grow reviews | Prevent **debt theater** (lists nobody acts on) and **silent debt** (undocumented shortcuts) | Cadenced register review; policy for "debt budget" per increment |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Ivory tower architecture** | Architects design in isolation; developers ignore the designs | Embed architects in delivery teams; architecture through code, not just diagrams |
| **Architecture astronaut** | Over-engineered solutions for problems that don't exist yet | YAGNI — design for current and near-term needs; evolve incrementally |
| **Accidental architecture** | No deliberate design; architecture emerges from developer convenience | Introduce lightweight governance — ADRs, C4 diagrams, fitness functions |
| **Resume-driven architecture** | Technology choices driven by what looks good on a CV, not fitness for purpose | Decision records with explicit trade-off analysis; team-based decisions |
| **Big bang rewrite** | Attempt to replace entire system at once | Strangler fig pattern; incremental migration; validate each step |

---

## Worked example

**Scenario:** A B2B API company launches **per-tenant usage analytics** so customers can justify spend and engineering can spot abusive traffic. The work crosses P2–P3 decisions, a full SDLC A–F increment, and P5 follow-up where debt and scale matter.

### P2 Validate — feasibility and early NFRs

Engineering runs a one-week spike: stream existing request logs into a warehouse vs serving aggregates from the operational store. **Architecture** concludes the operational store cannot support interactive filtering at expected tenant counts without risking API SLOs.

**Outputs:** Feasibility note, rough order-of-magnitude for storage growth, initial NFR candidates (query latency, data freshness, retention).

### P3 Plan & Commit — options and product-aligned qualities

Product defines success: self-serve dashboard, daily freshness acceptable, 13-month retention for enterprise tiers. **Architecture** publishes an options paper: (1) columnar warehouse + materialized views, (2) managed analytics DB with denormalized fact tables, (3) hybrid — recent data hot, historical cold.

| Option | Fit to NFRs | Cost / ops | Decision |
|--------|-------------|------------|----------|
| 1 | Strong for scale; more ops ownership | Medium-high | Shortlisted |
| 2 | Faster time-to-value; vendor limits on custom SQL | Medium | Shortlisted |
| 3 | Best long-term economics; highest build complexity | High initially | Deferred |

**ADRs drafted:** ADR-001 choose warehouse pattern; ADR-002 reject querying primary OLTP for analytics paths. **C4:** updated context (new read pipeline), container diagram (API, ingest worker, warehouse, dashboard UI).

### P3 — quality attribute workshop

A facilitated session ties P3 success metrics to **measurable** qualities that will drive specs and tests in SDLC B–E. **Architecture** facilitates trade-off discussion; PM holds outcome priority; security and SRE challenge assumptions.

| Quality concern | Measurable proxy | Workshop outcome |
|-----------------|------------------|------------------|
| Performance | P95 dashboard query time under expected data volume | ANA-NFR-01 threshold agreed |
| Security / tenancy | No cross-tenant reads; break-glass path documented | ANA-NFR-03 + exception process seed |
| Operability | Maximum acceptable ingest lag before alerting | SLO draft for ingest pipeline |

**Outputs:** Updated NFR catalog, inputs to API contracts and materialization design.

### SDLC A Discover — constraints on the backlog

Owner breaks epics: ingest, aggregate, dashboard, export CSV. **Architecture** flags cross-cutting concerns: tenant isolation in the warehouse, PII minimization, and a **fitness function** that fails builds if new API modules bypass the logging contract.

### SDLC B Specify — contracts and measurable NFRs

| NFR ID | Attribute | Threshold |
|--------|-----------|-----------|
| ANA-NFR-01 | Dashboard query latency (P95) | < 3s for 90-day window |
| ANA-NFR-02 | Data freshness | ≤ 24h lag vs source logs |
| ANA-NFR-03 | Tenant isolation | Row-level security enforced; cross-tenant queries impossible by construction |

**Outputs:** API contracts for aggregate endpoints, logical data model, updated component diagram for ingest and aggregate jobs.

### SDLC C Design — patterns and spikes

**Architecture** leads design for incremental backfill and late-arriving logs; pairing with Implementers on idempotent ingest and partition strategy. Spike validates warehouse costs against growth assumptions.

### SDLC D Build — guardian role

PR reviews enforce: no direct dashboard → OLTP paths; shared library for tenant context; dependency rules checked in CI. **Tech debt:** shortcut taken for manual CSV export (missing automation) — **registered** with Owner for prioritization.

### SDLC E Verify — NFR gates

Load tests on representative tenant sizes; security review for warehouse access paths; automated checks that ingest topics and schemas match the ADR.

| Check | Result |
|-------|--------|
| ANA-NFR-01 (P95 latency) | Met at 2.1s |
| ANA-NFR-02 (freshness) | Met |
| Isolation review | Passed; ADR-003 records exception process for break-glass support queries |

### SDLC F Release — operational architecture

**Architecture** signs off on backup retention for analytics, monitoring dashboards for ingest lag, and rollback: feature flag + pause materialization jobs.

### P4 Launch — operational readiness

Architecture role stays **light** (see lifecycle table): confirm observability covers new data paths, on-call runbooks reference ingest and warehouse failure modes, and feature-flag rollback was exercised in staging. No new structural decisions unless production readiness review surfaces gaps.

### P5 Grow — evolution and debt

Adoption exceeds forecast; two large tenants push ANA-NFR-01. **Architecture** updates the evolution roadmap: precompute heavier rollups, revisit ADR-001 assumptions, and **schedule** repayment of the CSV-export debt after QBR.

| Debt item | Detected | Triage outcome |
|-----------|----------|----------------|
| Manual CSV export | D Build | Scheduled remediation next quarter; interim runbook |
| Hot partition on one tenant | P5 monitoring | ADR-004 introduce shard-by-tenant for top N |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`SOFTWARE-ARCHITECTURE.md`](SOFTWARE-ARCHITECTURE.md) | Quality attributes, viewpoints, ADRs, governance, tech debt |
| [`approaches/README.md`](approaches/README.md) | C4, arc42, 4+1, TOGAF, DDD |
| [`patterns/README.md`](patterns/README.md) | Architectural patterns catalog |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, stage gates |
| [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) | Delivery role archetypes |
