---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Roles, archetypes & methodology titles

## Purpose

This guide is **product-agnostic**. It names **delivery archetypes** (kinds of accountability), **detailed** expectations for each, and **how Scrum, Kanban, phased delivery, and XP** respectively **emphasize, split, or merge** those accountabilities. It extends—but does not replace—the minimal pair in [`SDLC.md`](../SDLC.md) §1 (**Owner**, **Implementer**).

**Audience:** Teams adopting [`blueprints/sdlc/`](../README.md). Project-specific RACI or named people belong in the consuming repo’s **`sdlc/`** or **`docs/`**, not here.

**Handbook:** [`../docs/methodologies-roles.html`](../docs/methodologies-roles.html) (summary + navigation).

---

## Document map

| Section | Contents |
|---------|----------|
| [Vocabulary](#vocabulary) | Archetype, accountability, title, Owner/Implementer, Contributor |
| [Attribute key](#attribute-key) | How to read the summary tables |
| [1–5 Archetypes (detailed)](#1-demand--value) | Full breakdown + **methodology tweaks** per archetype |
| [Blueprint defaults](#blueprint-defaults-owner--implementer) | Owner / Implementer vs archetypes |
| [Quick reference: titles](#quick-reference-titles-on-archetypes) | One matrix — typical titles |
| [Methodology roll-up](#methodology-roll-up-all-archetypes-at-a-glance) | Scrum / Kanban / phased / XP — how each shifts the whole model |
| [Specialty hats](#specialty-hats-common-expansions) | Tech lead, QA, DevOps, … |
| [Tracking foundation](#tracking-foundation-same-repo-pattern) | Process roles vs **Contributor** |
| [Related reading](#related-reading) | Links to methodology guides |

---

## Vocabulary

| Term | Meaning here |
|------|----------------|
| **Archetype** | A **stable pattern of accountability**—what class of questions someone answers—**independent** of job title or framework. |
| **Accountability** | An obligation to produce an outcome; may be **shared** or **rotated**. Distinct from a person’s **employment role**. |
| **Title / hat** | A **named role** in a methodology or org chart (e.g. Product Owner, Developer). One person often wears **several hats**. |
| **Tweak** | How a **methodology** changes **emphasis** (what is explicit, time-boxed, merged, or handed off)—not a different archetype. |
| **Owner / Implementer** | This blueprint’s **default** minimal pair for phase obligations in [`SDLC.md`](../SDLC.md); they map to archetypes below. |
| **Contributor** (tracking) | In repos that adopt [`sdlc/TRACKING-FOUNDATION.md`](../../../sdlc/TRACKING-FOUNDATION.md), a **Contributor** is **identity in the event stream** (e.g. git author)—**not** the same as “Product Owner” unless that person also commits. |

---

## Attribute key

For each archetype, the **summary table** uses:

| Attribute | What it captures |
|-----------|-------------------|
| **Primary accountability** | The outcome they are expected to secure. |
| **Questions they answer** | Decisions and clarifications that stall without them. |
| **Typical decision rights** | Where “final say” usually sits (adjust locally). |
| **Touches (SDLC phases)** | Where [`SDLC.md`](../SDLC.md) work usually engages this archetype—**A** Discover → **F** Release. |
| **Should not (anti-patterns)** | Common confusions that create bottlenecks or gaps. |

Below each summary table, **Detail** sections spell out work and handoffs; **Methodology tweaks** spell out **Scrum**, **Kanban**, **Phased delivery**, and **XP**.

---

## 1. Demand & value

### Summary

| Attribute | Content |
|-----------|---------|
| **Primary accountability** | **What** is built **next** and **why it matters**; clarity of outcomes; **acceptance** that delivered work meets intent. |
| **Questions they answer** | What is the next most valuable slice? What is **in** / **out** of scope for this increment? What does “good enough” look like for users and business? |
| **Typical decision rights** | **Ordering** of work, **scope trade-offs**, **acceptance** at story/epic boundaries (often shared with **Steer & govern** on regulated work). |
| **Touches (SDLC phases)** | **A–B** strongly (priorities, specs, acceptance criteria); **C–D** consulted; **E–F** acceptance and release **intent** (business go/no-go where applicable). |
| **Should not** | Micromanage implementation details; own **how** the team executes day-to-day engineering (that belongs with **Build & integrate**). |

**Default blueprint hat:** **Owner** (primary).

### Detail: responsibilities

- **Prioritize** the funnel of ideas into an **ordered** backlog (or equivalent) aligned to strategy and risk.
- **Frame** outcomes and constraints so **Build** can specify and implement without constant renegotiation of “what.”
- **Accept** or reject completed work against agreed criteria; escalate when **Steer** must resolve policy or funding conflicts.
- **Represent** user and business perspective in trade-offs (scope, date, quality)—without bypassing the team’s **Definition of Done**.
- **Communicate** changes in priority visibly (backlog, WBS, tracker) so traceability and ceremonies stay honest.

### Detail: artifacts & interfaces

| Produces / curates (typical) | Consumes / depends on |
|------------------------------|------------------------|
| Ordered backlog, roadmap views, acceptance notes | Feasibility input from **Build**; constraints from **Steer** |
| “Ready” criteria alignment with specs | Quality bar from **Assure** (DoD, release policy) |
| Stakeholder summaries for reviews | Flow health signals from **Flow** (impediments that are really priority conflicts) |

**Interfaces:** strongest with **Build** (clarity of scope), **Assure** (what evidence counts as done), **Steer** (non-negotiables). Weak or missing **Demand** shows up as **priority churn** or **no one who can accept**.

### Detail: ceremony touchpoints (methodology-neutral)

- **Planning horizons:** participates in whatever replaces “what’s next” conversations (sprint planning, replenishment, phase scoping).
- **Review / demo:** confirms value delivered and feeds **next** ordering.
- **Backlog refinement / analysis:** sharpens items before **Build** commits deep implementation effort.

### Methodology tweaks

| Methodology | How it tweaks **Demand & value** |
|-------------|-----------------------------------|
| **Scrum** | [**Product Owner**](https://scrumguides.org/scrum-guide.html) is the **named** accountability for product backlog **ordering** and maximizing value. **Sprint Review** is the formal inspect-and-adapt moment with stakeholders; **Sprint Goal** concentrates *this* increment. PO is **one** voice into the Scrum Team for product direction—Developers still own *how* to meet the goal within the Sprint. |
| **Kanban** | **No single prescribed title**; **requester**, **customer**, or **product manager** often plays this archetype. **Replenishment** (or equivalent) replaces sprint-bound selection with **continuous or rolling** prioritization. Demand may sit **off the board** (portfolio) while the delivery board executes pull—clarity of **who pulls what when** is a policy choice, not framework magic. |
| **Phased delivery** | **Sponsor** and **PM/BA** dominate **early phases** (requirements baselines). After a **baseline freeze**, reordering is **harder**—this archetype shifts toward **change control** and **gate evidence** rather than weekly reprioritization. **Acceptance** may be formal **UAT** or regulated sign-off, not only a sprint review. |
| **XP** | Classic **Customer** / **onsite customer** is embedded with the team for **fast feedback** and **story acceptance**. Modern teams often use a **PO-like** person in the same archetype. **Small releases** mean this hat accepts **very frequently**; thin handoffs between “ask” and “build.” |
| **Lean** | Demand is defined through **value-stream** analysis—focus on what the customer values, eliminate everything else. Ordering follows **last responsible moment** and **pull-based** selection. No prescribed title; value-stream manager or product manager typically holds this archetype. |
| **Spiral** | Demand is framed as **objectives** in each spiral’s Q1. Stakeholders define goals and constraints; **risk analysis** (Q2) may reshape demand before commitment. **Anchor-point milestones** (LCO, LCA, IOC) are the formal acceptance gates. |
| **V-Model** | Demand is captured as **formal requirements** at the top-left of the V. Requirements must be **testable** — untestable requirements are reworked. **Acceptance testing** (top-right) formally validates against stakeholder needs. |
| **DevOps** | Demand includes **operability requirements** (SLOs, monitoring, deployment strategy) alongside functional requirements. "Done" means **deployed and observable**, not just "code complete." |

---

## 2. Build & integrate

### Summary

| Attribute | Content |
|-----------|---------|
| **Primary accountability** | **Turning** agreed work into a **working**, integrated product: design where needed, implementation, tests, docs updates per team rules. |
| **Questions they answer** | How do we implement this safely? What is the smallest shippable slice? What technical trade-offs are we making? |
| **Typical decision rights** | **How** to build within agreed scope; **engineering standards** and **internal quality** (refactoring, patterns) unless org policy overrides. |
| **Touches (SDLC phases)** | **B–E** core (specify, design, build, verify); **A** consulted; **F** hands-on release engineering often here or with **Assure & ship**. |
| **Should not** | Silently expand scope or bypass acceptance; ignore **Definition of Done** agreed with **Demand & value**. |

**Default blueprint hat:** **Implementer** (primary).

### Detail: responsibilities

- **Specify** technical approach at the right level: APIs, data, UX implementation, performance where it matters.
- **Implement** and **integrate** continuously or on cadence; keep the product **releasable** per team policy.
- **Maintain** traceability (commits, PRs, REQ ids) so **Assure** and **Steer** can audit.
- **Collaborate** with **Demand** on feasibility and slicing; push back with **options**, not silent slips.
- **Participate** in quality practices (tests, reviews, pairing) even when a separate **Assure** role exists—**build-quality** is not “someone else’s phase” by default.

### Detail: artifacts & interfaces

| Produces / curates (typical) | Consumes / depends on |
|------------------------------|------------------------|
| Code, automated tests, migrations, configs | Prioritized, “ready” backlog items from **Demand** |
| Design notes, ADRs, API docs | Architecture constraints from **Steer** / **Architect** when mandated |
| PRs, CI configuration | Release and quality policies from **Assure** |

**Interfaces:** daily tension is healthy with **Demand** (scope vs time). **Flow** helps remove **process** blockers; **Assure** defines **evidence** for done.

### Detail: ceremony touchpoints (methodology-neutral)

- **Planning:** commits to a realistic slice of work given capacity and unknowns.
- **Daily sync:** surfaces blockers and coordination needs.
- **Review:** demonstrates increment; receives feedback for **next** cycle.

### Methodology tweaks

| Methodology | How it tweaks **Build & integrate** |
|-------------|---------------------------------------|
| **Scrum** | **Developers** (Scrum Guide term) are **accountable** for creating the **Done** increment, **owning the Sprint Backlog**, and the **Definition of Done** (with the whole Scrum Team). **No sub-roles** are required inside Developers—the framework is intentionally **minimal**. |
| **Kanban** | **Delivery team** / **workers** who **pull** items through explicit policies. Emphasis on **WIP limits** and **flow** over sprint commitment; **roles are organizational**, not defined by the Kanban method itself. **Specialists** (e.g. ops) may appear as **swimlanes** or **classes of service**. |
| **Phased delivery** | **Build** is often **split by phase**: analysts produce specs, architects produce design packages, developers implement **after** gate approval. **Handoffs** increase the need for **documented** interfaces and **traceability**; “you built the wrong thing” is traced to **baseline** quality, not only to the last coder. |
| **XP** | **Collective ownership**, **pairing** / ensemble, **coding standard**, **TDD**, **refactoring**—**Build** is a **discipline**, not only a role title. **Sustainable pace** is an explicit value: **Build** should not normalize heroics as process. |
| **Lean** | **Small batches**, **eliminate waste** (task switching, partially done work, handoffs). Build is empowered to **improve their own process**. Value-stream thinking asks: does this build activity add value or is it waste? |
| **Spiral** | Build scope is **risk-adjusted** per spiral. Early spirals may produce **disposable prototypes**; later spirals produce production-grade code. Team composition may change across spirals. |
| **V-Model** | Build descends the left side of the V: system design → detailed design → implementation. Each level’s output defines what the corresponding right-side test level will verify. **Traceability** is a build-time concern, not an afterthought. |
| **DevOps** | Build includes **infrastructure** (IaC), **pipeline configuration**, and **monitoring instrumentation** alongside application code. "You build it, you run it" — developers own operational readiness. |

---

## 3. Flow & improvement

### Summary

| Attribute | Content |
|-----------|---------|
| **Primary accountability** | **Health of the delivery system**: predictability, impediments, clarity of process, **continuous improvement**—without owning product priorities or line management by default. |
| **Questions they answer** | What is blocking flow? Are ceremonies useful? What experiments will we run to improve how we work? |
| **Typical decision rights** | **Process facilitation** and **impediment escalation**; **not** product backlog ordering (that stays with **Demand & value** unless explicitly merged). |
| **Touches (SDLC phases)** | Cross-cuts **A–F** via cadence; strongest in **iterative** methods (standups, planning, retro). |
| **Should not** | Become a **proxy Product Owner** or sole gate for all technical work; replace the team’s own accountability for quality. |

**Default blueprint hat:** Often **absorbed by Owner or Implementer** on small teams; in Scrum, maps to **Scrum Master** when staffed.

### Detail: responsibilities

- **Facilitate** events so they stay **time-boxed**, inclusive, and outcome-oriented.
- **Surface** impediments; **escalate** when the team cannot resolve them (dependencies, policy, tooling).
- **Protect** the team from **destructive** interruptions—without isolating them from **Demand**’s legitimate need for answers.
- **Coach** toward agreed framework rules (Scrum, Kanban policies, phase entry criteria) and **experiments** from retrospectives.
- **Measure** system health (predictability, lead time, quality trends) where data exists—**without** using metrics for blame.

### Detail: artifacts & interfaces

| Produces / curates (typical) | Consumes / depends on |
|------------------------------|------------------------|
| Impediment lists, improvement actions | Team agreements, working agreements |
| Facilitation notes, retro outcomes | Board/tracker data, CI signals |
| Escalations to leadership / **Steer** | Priority conflicts raised honestly with **Demand** |

**Interfaces:** sits **between** **Demand**, **Build**, and **Steer** for **organizational** friction—not a substitute for any of them.

### Detail: ceremony touchpoints (methodology-neutral)

- Standups / syncs, planning facilitation, retrospectives, service reviews—whatever the team uses to **inspect and adapt the system**.

### Methodology tweaks

| Methodology | How it tweaks **Flow & improvement** |
|-------------|--------------------------------------|
| **Scrum** | **Scrum Master** is **accountable** for **establishing Scrum** as defined, **coaching**, and **removing impediments**. Serves **PO**, **Developers**, and the **organization**. **Not** the task master for the team’s technical work. |
| **Kanban** | Often **merged** into a **service delivery manager**, **team lead**, or **rotating facilitator**. **Kanban** explicitly includes **feedback loops** (e.g. service delivery review, operations review)—who facilitates is **context-specific**. |
| **Phased delivery** | **PMO**, **phase manager**, or **QA manager** may own **process compliance** and **gate readiness** more than “team coach.” Improvement is **between phases** or **audit-driven** as much as retro-driven. |
| **XP** | **Coach** is optional; many XP teams **self-facilitate** improvement with **lightweight** rituals. **Values** (communication, feedback, courage) substitute for a named process role when discipline is high. |
| **Lean** | **Lean coach / sensei** teaches problem-solving (A3, Five Whys) and facilitates **Kaizen** events. **Value-stream manager** owns end-to-end flow health. Improvement is **continuous and systematic**, not ad-hoc. |
| **Spiral** | **Project manager** plans spirals and coordinates stakeholders. **Risk analyst** drives Q2 risk identification and resolution. Flow is managed through **quadrant transitions** rather than sprint/flow cadence. |
| **V-Model** | **Project manager** coordinates design and test phases. **Test manager** orchestrates verification across V-levels. Flow is **sequential** with formal handoffs between levels. |
| **DevOps** | **Platform engineers** maintain CI/CD infrastructure. **SRE** owns reliability and error budgets. Flow is **automated** — the pipeline itself is the primary flow mechanism. **Pipeline retrospectives** improve delivery speed. |

---

## 4. Assure & ship

### Summary

| Attribute | Content |
|-----------|---------|
| **Primary accountability** | **Fit for use / fit for release**: verification, evidence, operational readiness, and **release mechanics** appropriate to risk. |
| **Questions they answer** | Are we **confident** this is safe to ship? What evidence do we need (tests, sign-offs, checklists)? What happens after deploy? |
| **Typical decision rights** | **Quality gates**, test strategy, **release approval** (sometimes shared with **Steer & govern** in regulated contexts). |
| **Touches (SDLC phases)** | **D–F** strong (build, verify, release); **B–C** consulted (testability, design for verification). |
| **Should not** | Become a **late-stage only** bottleneck if quality is not built in earlier (**Build** owns ongoing quality too). |

**Default blueprint hat:** Often **part of Implementer** until volume or regulation warrants **QA**, **release manager**, or **SRE** titles.

### Detail: responsibilities

- **Define** or **enforce** Definition of Done, test pyramids, environments, and **release checklists** aligned to risk.
- **Execute or oversee** verification: automated suites, exploratory testing, performance/security where required.
- **Package** releases: notes, migrations, rollback plans, monitoring hooks.
- **Coordinate** with **Steer** when **compliance evidence** (signatures, baselines) is mandatory.

### Detail: artifacts & interfaces

| Produces / curates (typical) | Consumes / depends on |
|------------------------------|------------------------|
| Test plans, reports, release artifacts | Increments from **Build** |
| CI/CD quality gates | Policies from **Steer** |
| Operational runbooks | Acceptance criteria from **Demand** |

**Interfaces:** **Build** provides **testable** increments; **Demand** confirms **value**; **Steer** may require **independent** verification.

### Detail: ceremony touchpoints (methodology-neutral)

- Release readiness reviews, go/no-go, post-release monitoring handoff.

### Methodology tweaks

| Methodology | How it tweaks **Assure & ship** |
|-------------|-----------------------------------|
| **Scrum** | **Definition of Done** is created by the **Scrum Team**; **Developers** cannot declare work **Done** outside it. **Product Owner** **accepts** the increment (product/value lens)—distinct from “all tests green.” Separate **QA org** is **optional** and must not split accountability in a way that confuses **Done**. |
| **Kanban** | **Policies explicit**: per-column **DoD**, **SLAs**, maybe **release train** cadence. **Assure** is often **embedded** in columns (“ready for release”) rather than a separate phase. **Metrics** (cycle time, defects) inform policies. |
| **Phased delivery** | **Verification** is often a **dedicated phase** with **formal** test levels, **IV&V**, or regulatory **validation**. **Evidence packages** for **gates** are central; **Assure** may be **organizationally separate** from **Build**. |
| **XP** | **TDD**, **CI**, **collective ownership** **merge** much of **Assure** into **Build**. **Small releases** shrink the batch between “integrated” and “in users’ hands.” Separate QA is **less** common in textbook XP; **discipline** replaces **phase**. |
| **Lean** | **Built-in quality** — integrity is designed in, not tested in later. Quality practices (TDD, CI, automation) are part of **flow**, not a separate assurance phase. Defects are **waste** to be eliminated at the source. |
| **Spiral** | **Risk review** (Q2) provides systematic assurance before build commitment. **Anchor-point milestones** (LCO, LCA, IOC) are formal quality/readiness gates. Prototypes in early spirals provide assurance evidence for later build decisions. |
| **V-Model** | **Formal verification** at each V-level (unit → integration → system → acceptance). **Traceability matrix** links requirements to test evidence. **IV&V** (independent verification and validation) common in regulated contexts. |
| **DevOps** | **Automated pipeline gates** provide continuous assurance. **SLOs and error budgets** measure production reliability. **Blameless post-mortems** learn from failures. Assurance is **automated and continuous**, not a separate phase. |

---

## 5. Steer & govern

### Summary

| Attribute | Content |
|-----------|---------|
| **Primary accountability** | **Boundary conditions** outside the team’s day-to-day: funding, **portfolio** alignment, **compliance**, formal **gates**, legal/policy constraints. |
| **Questions they answer** | Are we still funded and aligned with strategy? What **must** be true for a phase or release to be **approved**? |
| **Typical decision rights** | **Go/hold/stop** at **tollgates**; may **override** scope or timing (with visible change control). |
| **Touches (SDLC phases)** | **A** (charter), **phase exits**, **F** (organizational release approval); intermittent through **B–E** as risk dictates. |
| **Should not** | Dictate **daily backlog order** for an empowered product team without a clear escalation path—that erodes **Demand & value** clarity. |

**Default blueprint hat:** Often **outside** the minimal Owner/Implementer pair; **Owner** may represent **Steer** on small internal products until a **sponsor** or **board** is named.

### Detail: responsibilities

- **Set** non-negotiables: regulatory targets, security classes, contractual milestones.
- **Approve** major scope/cost/timeline changes through **change control** ([`change.html`](../docs/change.html) in the handbook).
- **Allocate** capacity across portfolios; resolve **priority** deadlocks escalated from **Demand** or **Flow**.
- **Accept** organizational risk for **release** when law or contract requires executive sign-off.

### Detail: artifacts & interfaces

| Produces / curates (typical) | Consumes / depends on |
|------------------------------|------------------------|
| Charters, gate minutes, compliance baselines | Roadmaps and requests from **Demand** |
| Audit responses, risk registers (org level) | Evidence from **Assure** |
| Funding decisions | Team forecasts from **Build** / **Flow** |

**Interfaces:** **Demand** operates **within** the steering box; **Flow** escalates **systemic** blockers; **Assure** supplies **proof** for gates.

### Detail: ceremony touchpoints (methodology-neutral)

- Portfolio reviews, phase-exit / tollgate meetings, executive release approval.

### Methodology tweaks

| Methodology | How it tweaks **Steer & govern** |
|-------------|-----------------------------------|
| **Scrum** | **Explicitly outside** the Scrum Team: **stakeholders** engage at **Sprint Review**; **organizational** impediments are **Scrum Master** territory to surface, **Steer** to resolve. Scrum does **not** define a “sponsor role”—that lives in org design. |
| **Kanban** | **Portfolio Kanban** or **strategy** boards may sit **above** the delivery board; **Steer** sets **WIP** and **funding** across streams. **Service orientation** can hide weak steering if **Demand** is fragmented—clarity at **portfolio** level still matters. |
| **Phased delivery** | **Steer & govern** is **central**: **tollgates**, **CCB**, **baselines**, **compliance** artifacts. This archetype is often **heavier** than in pure Scrum/XP teams. |
| **XP** | **Thin** explicit layer; **Customer** (Demand) is **close** to the team so many **trade-offs** resolve without a large **governance** apparatus—until **regulation** forces **Steer** back in. |
| **Lean** | **Management as servant-leader** — sets vision and constraints, removes organizational impediments, practices **Gemba** and **Hoshin Kanri** (policy deployment). Steer is about **context**, not commands. |
| **Spiral** | **Anchor-point milestones** (LCO, LCA, IOC) are the primary steering mechanism. Stakeholders make **explicit go/no-go** decisions based on risk evidence. Governance is **integrated** into the quadrant cycle, not layered on top. |
| **V-Model** | **Design reviews** (left-side gates) and **test reviews** (right-side gates) provide structured governance. Regulatory standards (ISO 26262, IEC 62304) may mandate specific gate criteria. |
| **DevOps** | Governance through **automated gates** and **SLO policies**. Error budgets make feature vs reliability trade-offs **explicit and data-driven**. Steer is less about meetings and more about **policies embedded in automation**. |

---

## Blueprint defaults (Owner / Implementer)

| Blueprint role | Archetype coverage (typical) | Notes |
|----------------|------------------------------|--------|
| **Owner** | **Demand & value** (primary); may hold **Steer & govern** proxy; sometimes **Flow & improvement** on tiny teams | Single face for priorities and acceptance per [`SDLC.md`](../SDLC.md). |
| **Implementer** | **Build & integrate** (primary); often **Assure & ship**; may share **Flow & improvement** | Updates specs, WBS, traceability per phase table in [`SDLC.md`](../SDLC.md). |

**One person** may be both Owner and Implementer; archetypes still help **split attention** (“which hat am I wearing for this decision?”).

---

## Quick reference: titles on archetypes

Typical titles—your org may differ. Cells marked **—** mean the methodology is **silent** or **org-specific**.

| Archetype | Scrum ([Guide](https://scrumguides.org/scrum-guide.html)) | Kanban | Phased delivery | XP |
|-----------|------------------------------------------------------------|--------|-----------------|-----|
| **Demand & value** | **Product Owner** | Customer / requester / PM | Sponsor; BA / PM (requirements) | Customer / onsite customer; often PO-like |
| **Build & integrate** | **Developers** | Delivery team / workers | Role-specialized implementers by phase | Developers; collective ownership |
| **Flow & improvement** | **Scrum Master** | Service mgr / coach / team lead | PMO / PM / phase manager | Coach (optional); self-organized |
| **Assure & ship** | DoD (team) + PO acceptance; QA org optional | Policies; column DoD; release cadence | QA / IV&V; formal release sign-off | TDD + CI embedded in Developers |
| **Steer & govern** | Stakeholders; org outside team | Portfolio / steering | Tollgates; CCB; compliance | Light; regulation adds weight |

**Deep dives:** [Scrum](https://forgesdlc.com/methodology-scrum.html) · [Kanban](https://forgesdlc.com/methodology-kanban.html) · [Phased delivery](https://forgesdlc.com/methodologies-phased-delivery.html) · [XP](https://forgesdlc.com/methodology-xp.html) · [Lean](https://forgesdlc.com/methodology-lean.html) · [Spiral](https://forgesdlc.com/methodologies-spiral.html) · [V-Model](https://forgesdlc.com/methodologies-v-model.html) · [DevOps](https://forgesdlc.com/methodologies-devops.html) · [Agile umbrella](https://forgesdlc.com/methodologies-agile.html)

---

## Methodology roll-up (all archetypes at a glance)

Use this when you think **methodology-first** (“we picked Scrum—what happens to each archetype?”).

### Scrum

- **Demand:** **Product Owner** is **explicit** and **singular** for backlog order and value focus; **Sprint** and **Sprint Goal** **time-box** prioritization conversations.
- **Build:** **Developers** own **how**, **Sprint Backlog**, and **Done** increment; **minimal** internal dev sub-roles in the Guide.
- **Flow:** **Scrum Master** is **explicit** for Scrum adoption, impediments, coaching—**distinct** from PO and Developers.
- **Assure:** **DoD** is **team-owned**; **acceptance** is **PO** for the product increment; optional external QA must **map** clearly to Done.
- **Steer:** **Outside** the team; **Review** connects stakeholders; escalations via SM.

### Kanban

- **Demand:** Often **unnamed** in the method; **continuous replenishment** and **policies** define how **pull** gets **authorized**.
- **Build:** **Pull** and **WIP limits** dominate; roles follow **org**, not the method.
- **Flow:** **Embedded** in **feedback loops** and **service reviews**; facilitator may **rotate**.
- **Assure:** **Policies** and **per-state DoD**; **cycle time** and **quality** metrics replace sprint boundaries.
- **Steer:** **Portfolio** and **funding** layers are common; **Steer** must not **starve** policy work (explicit WIP for improvements).

### Phased delivery

- **Demand:** **Front-loaded** in requirements; **baseline** and **change control** **constrain** late reordering.
- **Build:** **Sequential** specialization and **handoffs**; **traceability** across phases is **critical**.
- **Flow:** **Process compliance** and **gate readiness** can outweigh **team retros** as improvement drivers.
- **Assure:** **Separate verification phase** and **formal evidence** are **normal**; **independent** testing frequent.
- **Steer:** **Strongest** expression—**tollgates**, **CCB**, **signatures**; **git ≠ approval record**.

### XP

- **Demand:** **Customer proximity**; **frequent** acceptance; modern teams often **PO-shaped**.
- **Build:** **Practices** (TDD, pairing, CI, refactoring) **thicken** this archetype without new **titles**.
- **Flow:** **Light** named role; **team** owns improvement **culturally**.
- **Assure:** **Merged** into **Build** by default; **release** still needs **operational** clarity.
- **Steer:** **Minimal** unless **domain regulation** forces **phased-style** **Steer** on top of XP practices.

### Lean Software Development

- **Demand:** Defined through **value-stream** analysis; focus on customer value; **last responsible moment** ordering. No prescribed title; product manager or value-stream owner typically holds this.
- **Build:** **Empowered** team eliminates waste; small batches; collective process improvement.
- **Flow:** **Lean coach / sensei** teaches problem-solving; **value-stream manager** owns end-to-end flow. **Kaizen** is continuous, not episodic.
- **Assure:** **Built-in quality**; defects are waste eliminated at the source. Quality is a practice, not a phase.
- **Steer:** **Management as servant-leader**; sets context via **Gemba** and **Hoshin Kanri**. Steering is about enabling, not commanding.

### Spiral Model

- **Demand:** Objectives defined per spiral (Q1); risk analysis may reshape demand before commitment. **Anchor-point milestones** are formal acceptance gates.
- **Build:** Risk-adjusted scope per spiral. Early spirals produce **disposable prototypes**; later spirals produce production-grade work.
- **Flow:** **Project manager** coordinates spirals; **risk analyst** drives Q2. Flow follows **quadrant transitions**, not sprint/flow cadence.
- **Assure:** **Risk review** (Q2) provides systematic assurance. **Anchor-point milestones** (LCO, LCA, IOC) are formal gates.
- **Steer:** Governance **integrated** into quadrant cycle. Stakeholders make explicit **go/no-go** decisions based on risk evidence at milestones.

### V-Model

- **Demand:** Formal **requirements** at the top of the V; must be **testable**. Acceptance testing formally validates against stakeholder needs.
- **Build:** Descends the left side: system design → detailed design → implementation. Each level defines corresponding test targets.
- **Flow:** **Sequential** with formal handoffs. Project manager coordinates phases; test manager orchestrates verification levels.
- **Assure:** **Formal verification** at each V-level. Traceability matrix links requirements → tests → evidence. IV&V for regulated contexts.
- **Steer:** **Design and test review gates** provide structured governance. Regulatory standards may mandate specific criteria.

### DevOps

- **Demand:** Includes **operability requirements** (SLOs, monitoring, deployment) alongside functional needs. Done = deployed and observable.
- **Build:** Includes **infrastructure**, **pipeline**, and **monitoring** alongside application code. "You build it, you run it."
- **Flow:** **Automated** via CI/CD pipelines. Platform engineers maintain infrastructure. Pipeline retrospectives improve delivery speed.
- **Assure:** **Automated pipeline gates** and **SLO/error budget** management. Post-mortems extract learning from incidents. Continuous, not phase-based.
- **Steer:** Governance through **automation and policies**. Error budgets make feature vs reliability trade-offs data-driven.

### Agile umbrella ([`agile.md`](https://forgesdlc.com/methodologies-agile.html))

**Agile** does not add a sixth archetype. Teams **blend**: e.g. **Scrum** cadence + **Kanban** flow metrics + **XP** practices. **Tweaks stack**: name **who** holds each archetype after you choose the **primary** cadence (iteration vs flow vs gates).

---

## Specialty hats (common expansions)

When teams grow, titles **slice** **Build** or **Assure** further. Map them back to archetypes to avoid duplicate accountability.

| Typical title | Primary archetype | Secondary touch |
|---------------|-------------------|-----------------|
| **Tech / engineering lead** | Build & integrate | Demand & value (consulted on feasibility and sequencing) |
| **QA / test engineer** | Assure & ship | Build & integrate (shift-left, automation) |
| **DevOps / SRE / platform** | Assure & ship | Build & integrate (tooling, pipelines) |
| **Security champion / AppSec** | Assure & ship | Steer & govern (policy), Build (secure design) |
| **Release manager** | Assure & ship | Steer & govern (compliance evidence) |
| **UX / product designer** | Demand & value | Build & integrate (interaction detail, specs) |
| **Architect** | Build & integrate | Steer & govern (standards, NFRs) when mandated |

---

## Tracking foundation (same repo pattern)

If the project adds **`sdlc/TRACKING-FOUNDATION.md`**, remember:

- **Archetypes / titles** answer **process** (“who decides?”).
- **Contributor** answers **telemetry** (“who appears in commits or logged events?”).

A **Product Owner** who never commits may be **invisible** in commit-only dashboards; that is a **reporting limit**, not proof they did not contribute. See [agentic SDLC](https://forgesdlc.com/agentic-sdlc.html) for **human vs bot** identity policy.

---

## Related reading

| Doc | Why |
|-----|-----|
| [`SDLC.md`](../SDLC.md) §1–2 | Minimal **Owner** / **Implementer** and phase obligations |
| [Ceremonies — foundation](ceremonies/ceremony-foundation.md) | **Intent types** C1–C6 × phases × archetypes (who leads rituals) |
| [Scrum](https://forgesdlc.com/methodology-scrum.html) | Official **accountabilities** and events |
| [Kanban](https://forgesdlc.com/methodology-kanban.html) | Service-oriented **roles** and policies |
| [Phased delivery](https://forgesdlc.com/methodologies-phased-delivery.html) | **Gates** and **Steer & govern** |
| [XP](https://forgesdlc.com/methodology-xp.html) | Practices that **merge** quality into **Build** |
| [Lean](https://forgesdlc.com/methodology-lean.html) | Value-stream thinking; eliminate waste; empower the team |
| [Spiral](https://forgesdlc.com/methodologies-spiral.html) | Risk-driven iteration; anchor-point milestones |
| [V-Model](https://forgesdlc.com/methodologies-v-model.html) | Verification/validation pairing; traceability |
| [DevOps](https://forgesdlc.com/methodologies-devops.html) | Culture + practices unifying Dev and Ops; CI/CD, monitoring |
| [Agentic SDLC](https://forgesdlc.com/agentic-sdlc.html) | Agents, review, contributor identity |
