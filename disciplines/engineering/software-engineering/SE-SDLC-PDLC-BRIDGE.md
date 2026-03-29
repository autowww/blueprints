# Software engineering ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **software engineering (SE)** craft to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **Software engineering** — "Are we **skilled makers** — readable, correct, evolvable code and systems thinking?"

SE is not a separate delivery lane; it is the **competence substrate** for implementation quality, learning speed, and sustainable change. Strong SE shortens the loop between product hypotheses (PDLC) and trustworthy delivery (SDLC).

**Canonical sources:** [`SOFTWARE-ENGINEERING.md`](SOFTWARE-ENGINEERING.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; how SE relates to PDLC and SDLC |
| [Comparison table](#comparison-table) | SE vs SDLC vs PDLC — scope, ownership, metrics, risks |
| [When one is missing](#when-one-is-missing) | Consequences when craft, SDLC, or PDLC are practiced in isolation |
| [SE across the lifecycle](#se-across-the-lifecycle) | Activities and outputs mapped to PDLC P1–P6 and SDLC A–F |
| [Role mapping](#role-mapping) | Who carries SE accountability at each phase; SDLC roles and archetypes |
| [Artifact flow](#artifact-flow) | Handoffs between SE practice, SDLC, and PDLC |
| [Calibration](#calibration) | When to invest more or less in SE depth by initiative and context |
| [Anti-patterns](#anti-patterns) | Common failures when craft is neglected or fetishized |
| [Software engineering and SDLC methodologies](#software-engineering-and-sdlc-methodologies) | Emphasis across Scrum, Kanban, XP, phased, and continuous delivery |
| [Worked example](#worked-example) | End-to-end scenario — performance-sensitive feature with review and profiling |
| [Related reading](#related-reading) | Authoritative docs in this package and sibling lifecycles |

---

## Comparison table

| Dimension | Software engineering | SDLC | PDLC |
|-----------|---------------------|------|------|
| **Core question** | Are we skilled makers — clear structure, correctness, performance awareness, collaborative code? | How do we build this correctly? | Should we build this; does it create the right outcomes? |
| **Scope** | Paradigms, DS&A, patterns, principles, clean code, concurrency, networking literacy, VCS, debugging/profiling | Requirements → design → implementation → verification → release (**A** Discover through **F** Release) | Problem discovery → validation → strategy → launch → growth → sunset (**P1**–**P6**) |
| **Primary owner** | Every **Implementer**; shared standards via tech leadership — **Build & integrate** and **Assure & ship** archetypes | Delivery team; **Owner** (priorities, acceptance) and **Implementer** (build, verify) per [`SDLC.md`](../../../sdlc/SDLC.md) | Product manager / product trio; GTM where relevant |
| **Timeline** | Continuous — every commit and review | Sprint, iteration, or release train cadence | Product lifetime (months to years) |
| **Success metric** | Defect density trends, review turnaround, refactor safety, p95 latency vs budget, onboarding time to first commit | Velocity, escape rate, CI health, DoD satisfaction | Adoption, retention, revenue, NPS, outcome KPIs |
| **Key artifacts** | Code, tests, small ADRs at module level, profiling notes, runbooks for diagnostics | Specs, designs, code, tests, release notes | Research synthesis, experiments, strategy, launch and growth metrics |
| **Risk focus** | Complexity debt, subtle bugs, performance cliffs, insecure defaults | Technical risk — correctness, scalability, security | Market and outcome risk — desirability, viability, fit |
| **Failure mode** | Clever unreadable code; no tests; "works on my machine"; hero debugging | Late delivery; quality gaps; opaque changes | Right execution of the wrong thing; learning too slow to matter |

### How common SE ideas appear in this bridge

| Idea | Where it is reflected |
|------|----------------------|
| **Principles (SOLID, DRY, KISS, YAGNI)** | Design (**C**), implementation quality (**D**), review gates (**E**), refactoring cadence (**P5**) |
| **Patterns & paradigms** | **C** decomposition; **D** structure; **E** test doubles and integration seams |
| **Clean code & reviews** | **D**–**E** collaboration; **Assure & ship** interpretation of DoD |
| **Concurrency & networking literacy** | **C** NFR design; **D** implementation; **E** load and chaos-adjacent tests; **P4**–**P5** incidents |
| **VCS discipline** | **D** throughput; **F** release hygiene; **Flow & improvement** history readability |
| **Debugging & profiling** | **E** defect resolution; **P5** performance work; feedback into **P1**–**P2** when UX is system-limited |

---

## When one is missing

| Scenario | What happens |
|----------|-------------|
| **SE strength without SDLC discipline** | Elegant code and debates, but unclear priorities, weak specs, or skipped verification — **locally beautiful, globally late**. |
| **SE strength without PDLC** | High craft on features that do not move outcomes — polished irrelevance. |
| **SDLC without SE craft** | Process artifacts exist, but code is fragile, slow, or unreadable — **process theater** with technical churn. |
| **PDLC without SE** | Discovery is rich, but spikes lie or timelines ignore implementation risk — **feasibility surprises** at **P3**–**P4**. |
| **PDLC + SDLC, weak SE** | The right backlog items ship with ceremony, yet regressions, operational toil, and onboarding tax compound. |
| **All three practiced** | Hypotheses become measured experiments quickly; code stays evolvable; production signals are trustworthy. |

---

## SE across the lifecycle

| Phase | SE role | Key activities | Outputs |
|-------|---------|----------------|---------|
| **P1–P2 Discover/Validate** | **Prototype engineer** | Time-boxed spikes; throwaway or branch experiments; instrumented mocks | Spike code, complexity notes, feasibility flags |
| **P3 Plan & Commit** | **Technical sounding board** | Estimate implementation surfaces; call out paradigm and concurrency constraints; DS&A risks for scale | T-shirt sizes grounded in structure, risk register inputs |
| **A Discover** | **Exploration coder** | Read codebase; trace dependencies; propose seams for change | Onboarding notes, risk list for **B** |
| **B Specify** | **Contract thinker** | Clarify APIs, error models, SLIs that code must satisfy; define acceptance tests shape | API sketches, test outline, complexity budget |
| **C Design** | **Module designer** | Apply patterns/principles; decide data structures; concurrency model; logging/metrics hooks | Design notes, interface boundaries, diagram or ADR pointer |
| **D Build** | **Implementer** | Write readable code; follow VCS hygiene; unit-level correctness | Feature code, commits, local docs in code |
| **E Verify** | **Reviewer & fixer** | Code review; static analysis; tests; reproduce bugs systematically | Review feedback, green CI, defect fixes |
| **F Release** | **Release-aware engineer** | Feature flags; migration safety; rollback drills; observability for new paths | Release notes snippets, dashboards, runbook updates |
| **P4 Launch** | **Diagnosability partner** | Ensure logs/metrics/traces support launch criteria; guard hot paths | Dashboards, alert queries, SLO probes |
| **P5 Grow** | **Evolving maintainer** | Profile-guided improvement; targeted refactors; debt paydown | Performance reports, refactors, complexity reduction |
| **P6 Sunset** | **Deleter** | Remove dead code safely; data migration scripts; feature teardown | Shrinking modules, migration validators |

---

## Role mapping

Who carries SE accountability at each lifecycle step, alongside PDLC and SDLC. In small teams, the same person covers prototype, implementation, and review; in larger orgs, **tech leads** set standards while every **Implementer** owns craft. SDLC uses **Owner** and **Implementer**; archetypes follow [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md).

| Phase(s) | SE stance | PDLC accountability (typical) | SDLC accountability | Archetype |
|----------|-----------|------------------------------|---------------------|-----------|
| **P1–P2** | **Prototype engineer** | PM, UX research, discovery | Implementer for spikes; Owner sets time box | Demand & value; Build & integrate |
| **P3** | **Technical sounding board** | PM, strategy | Owner weighs trade-offs; Implementer supplies estimates | Steer & govern; Build & integrate |
| **A Discover** | **Exploration coder** | — | Implementer explores; Owner prioritizes learning | Build & integrate; Flow & improvement |
| **B Specify** | **Contract thinker** | — | Owner accepts AC; Implementer clarifies feasibility | Build & integrate; Assure & ship |
| **C Design** | **Module designer** | — | Implementer leads design; Owner consulted on trade-offs | Build & integrate |
| **D Build** | **Implementer** | — | Implementer codes; Owner unblocks | Build & integrate |
| **E Verify** | **Reviewer & fixer** | — | Implementer fixes; peer review; Assure & ship for gates | Assure & ship; Build & integrate |
| **F Release** | **Release-aware engineer** | GTM for launch comms | Implementer executes; Owner go/no-go | Assure & ship; Flow & improvement |
| **P4 Launch** | **Diagnosability partner** | PM, GTM | Overlap with **F** — cutover readiness | Assure & ship; Demand & value |
| **P5 Grow** | **Evolving maintainer** | PM, analytics | Iteration **A**–**F** for improvements | Flow & improvement; Build & integrate |
| **P6 Sunset** | **Deleter** | PM, legal/comms | Implementer removes code; Steer & govern on policy | Steer & govern; Build & integrate |

---

## Artifact flow

### PDLC / SDLC → SE (inputs)

| Source | SE usage |
|--------|----------|
| Hypotheses and metrics (**P1**–**P5**) | Choose spike depth, profiling scenarios, and what to instrument |
| Acceptance criteria (**B**) | Drives tests, API shapes, and error handling contracts |
| NFRs (**B**, **C**) | Data structure selection, concurrency model, caching, backoff |
| Architecture boundaries (**C**) | Module boundaries, allowed dependencies, performance budgets |
| Release policy (**F**, **P4**) | Feature flags, migration ordering, observability for rollback |

### SE → SDLC (outputs)

| SE artifact | SDLC usage |
|-------------|------------|
| Code and tests (**D**, **E**) | Executable spec; CI gates; regression safety |
| Design notes / small ADRs (**C**) | Explains invariants and trade-offs for future **D**–**E** |
| Profiling and debugging write-ups (**E**, **P5**) | Evidence for defects, performance stories, and DoD |
| Commit history (**D**–**F**) | Auditability, bisect, cherry-pick, and incident correlation |

### SE → PDLC (feedback)

| SE signal | PDLC usage |
|-----------|------------|
| Spike outcomes | Validate or invalidate **P1**–**P2** assumptions cheaply |
| Implementation cost learning | Refine **P3** scope and sequencing |
| Production latency/error budgets | Inform **P4**–**P5** UX and reliability investments |
| Complexity hotspots | Input to **P5** debt vs feature debates |

### Closed-loop summary

| Direction | Essence |
|-----------|---------|
| **Into SE** | Product intent, AC, and NFRs become **code structure, tests, and observability**. |
| **Out to SDLC** | Craft quality determines **how cheaply** the lifecycle can iterate. |
| **Out to PDLC** | Feasibility, pace, and production behavior answer **whether learning can keep up with strategy**. |

---

## Calibration

### By initiative type

| Situation | SE investment | Reasoning |
|-----------|---------------|-----------|
| **Greenfield product** | **High** — establish style guides, test patterns, module boundaries, and profiling baselines early | Cheap now to prevent uniform spaghetti before the team scales |
| **Feature on mature codebase** | **Medium** — follow existing seams; add tests at boundaries; watch p95 | Marginal risk is regression and coupling |
| **Performance-sensitive change** | **High** — measurement-first, benchmarks, concurrency review | Wrong structure is expensive to fix live |
| **Bug fix / small change** | **Targeted** — minimal blast radius; add regression test | Avoid gold-plating abstractions |
| **Spike / throwaway prototype** | **Low to medium** — optimize for learning speed; capture limitations explicitly | Do not confuse spike quality with production readiness |
| **Sunset / migration** | **Medium** — safe deletion, compatibility shims, data checks | Failure modes are data loss and partial teardown |

### By organizational context

| Context | SE emphasis |
|---------|-------------|
| **Startup / small team** | Convention over heavy process; strong reviews; automate format/lint |
| **Growing product org** | Shared libraries and examples; onboarding paths; internal tech talks |
| **Enterprise** | Coding standards aligned to compliance; readable audit trails in code and VCS |
| **Regulated** | Traceability from requirement to test; controlled branching; peer review evidence |

### Concepts that guide depth

| Lens | When to lean on it |
|------|-------------------|
| **Paradigm fit** | Domain is event-heavy → reactive thinking; rules engine → FP; UI composition → OOP/components |
| **Complexity theory** | Large data or tight SLAs → explicit DS&A choices and profiling |
| **Concurrency model** | Multi-threaded or distributed → spend on invariants, tests, and tooling |
| **Clean code** | High churn areas → readability and small modules beat cleverness |

### Signals you may be over- or under-investing

| Signal | Interpretation |
|--------|----------------|
| **Under-invested** | Reviews rubber-stamp; flakiness normalized; onboarding takes weeks for small tasks |
| **Well calibrated** | Refactors are boring and safe; incidents trace to code paths quickly; estimates stabilize |
| **Over-engineered (for context)** | Abstractions without callers; pattern bingo; optimization without measurement |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Resume-driven development** | Choosing stacks or patterns for novelty, not forces | Tie choices to requirements and team skill; time-box spikes |
| **Big ball of mud** | No modules; everything imports everything | Introduce seams incrementally; enforce dependency rules |
| **Golden hammer** | One paradigm/pattern for all problems | Use the comparison tables in [`SOFTWARE-ENGINEERING.md`](SOFTWARE-ENGINEERING.md) |
| **No-tests culture** | Manual only; fear of CI | Start with critical paths; characterize bugs with regression tests |
| **Hero debugging** | Tribal knowledge replaces instrumentation | Add logs/metrics; reproduce minimally; share playbooks |
| **Premature optimization** | Micro-tuning before profiling | Measure; optimize hotspots; document budgets |
| **Review theater** | LGTM without reading | Checklists; small diffs; rotate reviewers |

---

## Software engineering and SDLC methodologies

SE practices apply across all SDLC methodologies, with different emphasis:

| Methodology | SE emphasis |
|-------------|-------------|
| **Scrum** | Sustainable pace; Definition of Done includes reviewable code and tests each sprint |
| **Kanban** | Limit WIP on defect rework; fast review flow; reduce context switching cost |
| **XP** | Pairing, TDD, continuous integration — SE craft as explicit practices |
| **Phased** | Code quality gates at phase boundaries; formal reviews where policy requires |
| **Continuous delivery** | Trunk discipline, feature flags, and observability as extensions of daily SE habits |

---

## Worked example

**Scenario:** In **P3**, a team commits to a **search autocomplete** that must stay under **120 ms p95** at expected load. The feature touches API, cache, and UI.

| Step | Lifecycle | What happens |
|------|-----------|----------------|
| 1 | **P1**–**P2** | Prototype engineer builds a spike: trie vs prefix SQL vs search engine query — records rough latency and ops cost. |
| 2 | **B** | Contract thinker defines API pagination, debounce expectations, and error behavior when backend degrades. |
| 3 | **C** | Module designer picks data structure (e.g., trie in service + CDN edge cache), defines cache TTL and stampede mitigation. |
| 4 | **D** | Implementer wires code with structured logs (query id, stages), metrics (hit rate, latency histograms), and feature flag. |
| 5 | **E** | Reviewer checks concurrency around cache fill, tests for eviction and timeout; adds load test scenario in CI staging. |
| 6 | **F** | Release-aware engineer rolls out behind flag; validates dashboards; rehearses disable path. |
| 7 | **P4**–**P5** | Evolving maintainer profiles after launch; finds serialization hotspot; switches to cheaper codec — updates ADR note. |

**Outcome:** Product gets responsive search; leadership sees latency and error metrics tied to the hypothesis; technical learning feeds the next **P1**–**P2** iteration.

| Without strong PDLC | Without disciplined SDLC | Without SE craft |
|--------------------|-------------------------|------------------|
| Fast search for queries users do not care about | Right spec but integration chaos and missed AC | Clever index but opaque failures and unmeasurable **p95** |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`SOFTWARE-ENGINEERING.md`](SOFTWARE-ENGINEERING.md) | Paradigms, DS&A, patterns, principles, clean code, concurrency, networking, VCS, debugging |
| [`paradigms/README.md`](paradigms/README.md) | Index for OOP, FP, reactive, procedural, multi-paradigm guides |
| [`patterns/README.md`](patterns/README.md) | Index for GoF and integration/concurrency pattern guides |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD, roles |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6 |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | Product ↔ delivery alignment — complements this discipline view |
| [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) | SDLC role archetypes and Owner / Implementer expectations |
| [`BRIDGES.md`](../../../BRIDGES.md) | Index of discipline lifecycle bridges |

---

*Keep project-specific engineering standards in `docs/development/` and architecture decisions in `docs/adr/`, not in this file.*
