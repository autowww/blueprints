# UX / UI Design ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **UX / UI Design** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **UX Design** — "Is the product **usable, desirable, and accessible**?"

UX Design fuels PDLC discovery and validation with user evidence, and shapes SDLC deliverables with interaction patterns, visual standards, and accessibility requirements.

**Canonical sources:** [`UX-DESIGN.md`](UX-DESIGN.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; how UX Design relates to PDLC and SDLC |
| [Comparison table](#comparison-table) | UX Design vs SDLC vs PDLC — scope, ownership, metrics, risks |
| [When one is missing](#when-one-is-missing) | Consequences when UX Design, SDLC, or PDLC are practiced in isolation |
| [UX Design across the lifecycle](#ux-design-across-the-lifecycle) | Activities and outputs mapped to PDLC P1–P6 and SDLC A–F |
| [Role mapping](#role-mapping) | Who owns UX work at each phase; SDLC roles and archetypes |
| [Artifact flow](#artifact-flow) | Handoffs between UX Design, SDLC, and PDLC |
| [Calibration](#calibration) | When to invest more or less in UX by initiative and context |
| [Anti-patterns](#anti-patterns) | Common failures when UX is absent or siloed |
| [UX Design and SDLC methodologies](#ux-design-and-sdlc-methodologies) | Emphasis across Scrum, Kanban, Lean, phased |
| [Worked example](#worked-example) | End-to-end scenario — redesigning an onboarding flow |
| [Related reading](#related-reading) | Authoritative docs in this package and sibling lifecycles |

---

## Comparison table

| Dimension | UX Design | SDLC | PDLC |
|-----------|-----------|------|------|
| **Core question** | Is the product usable, desirable, and accessible? | How do we build this correctly? | Should we build this; does it create the right outcomes? |
| **Scope** | User research, interaction design, visual design, information architecture, accessibility, design systems, usability validation | Requirements → design → implementation → verification → release (**A** Discover through **F** Release) | Problem discovery → validation → strategy → launch → growth → sunset (**P1**–**P6**) |
| **Primary owner** | UX Designer / UX Researcher — part of the **product trio** (PM + Designer + Tech Lead) | Delivery team; **Owner** and **Implementer** per [`SDLC.md`](../../../sdlc/SDLC.md) | Product manager / product trio; GTM where relevant |
| **Timeline** | Continuous discovery and iteration — UX work runs ahead of and alongside engineering sprints | Sprint, iteration, or release train cadence | Product lifetime (months to years) |
| **Success metric** | Task success rate, SUS score, time on task, accessibility conformance, user satisfaction (CSAT/NPS), design system adoption | Velocity, defect escape rate, CI/CD gate pass rate | Adoption, retention, revenue, NPS, outcome KPIs |
| **Key artifacts** | Personas, journey maps, wireframes, prototypes, interaction specs, design tokens, usability reports, accessibility audits | Specs, designs, code, tests, release notes | Research synthesis, experiments, strategy, launch and growth metrics |
| **Risk focus** | Usability, desirability, accessibility — can users accomplish their goals without friction? | Technical risk — correctness, performance, security | Market and outcome risk — desirability, viability, fit |
| **Failure mode** | Beautiful or technically sound product that users cannot or will not use; accessibility lawsuits; high support volume from confusing UI | Late or low-quality delivery; weak feedback from production | Right execution of the wrong thing |

---

## When one is missing

| Scenario | What happens |
|----------|-------------|
| **UX Design without SDLC discipline** | Validated designs exist but engineering introduces inconsistencies, drops accessibility, or ships a degraded version of the design intent. |
| **UX Design without PDLC** | Good usability on features that do not move business outcomes. Research answers "can users do X?" but not "should we build X?" |
| **SDLC without UX Design** | Technically sound features that confuse, frustrate, or exclude users. High support cost; poor adoption despite working software. |
| **PDLC without UX Design** | Product strategy is set by stakeholder opinion, not user evidence. Validation relies on surveys and interviews without observing actual behavior. |
| **All three practiced** | User evidence informs product direction (PDLC), design specifications ensure usability and accessibility (UX), and disciplined delivery preserves design intent through implementation (SDLC). |

---

## UX Design across the lifecycle

| Phase | UX Design role | Key activities | Outputs |
|-------|---------------|----------------|---------|
| **P1 Discover** | **User researcher** | Generative research — interviews, contextual inquiry, diary studies, analytics review | Personas, empathy maps, journey maps, opportunity areas |
| **P2 Validate** | **Concept designer** | Concept testing, prototype testing, Wizard-of-Oz experiments | Validated concepts, usability findings, pivot/persevere recommendations |
| **P3 Plan & Commit** | **Design strategist** | Design principles, experience vision, accessibility requirements scoping | Design principles doc, experience strategy, accessibility conformance target |
| **A Discover** | **Interaction designer** | Translate product requirements into user flows, task analysis, edge-case identification | User flows, task models, content requirements |
| **B Specify** | **Specification designer** | Wireframes, interaction specs, design token definitions, accessibility annotation | Wireframes, interaction specs, component specs, WCAG mapping |
| **C Design** | **Visual / system designer** | High-fidelity mockups, design system components, motion design, responsive layouts | Mockups, Figma/Sketch files, design tokens (code-ready), Storybook stories |
| **D Build** | **Design QA partner** | Pair with engineers on component implementation; review in-progress builds against specs | Design review comments, component approval, visual regression baseline |
| **E Verify** | **Usability evaluator** | Usability testing on implemented features, accessibility audit, heuristic evaluation | Usability report, accessibility audit results, defect tickets |
| **F Release** | **Experience monitor** | Review release for design fidelity; ensure error states, empty states, and edge cases are handled | Release design sign-off, known UX debt items |
| **P4 Launch** | **Onboarding designer** | First-run experience, help content, tooltips, walkthroughs | Onboarding flows, contextual help, success metrics definition |
| **P5 Grow** | **Optimization researcher** | A/B experiments, funnel analysis, satisfaction surveys, iterative refinement | Experiment results, redesign recommendations, updated journey maps |
| **P6 Sunset** | **Transition designer** | Migration UX, data export flows, sunset communication, archival of design assets | Migration guides, sunset notification UX, archived design system |

---

## Role mapping

| Phase(s) | UX Design stance | PDLC accountability | SDLC accountability | Archetype |
|----------|-----------------|---------------------|---------------------|-----------|
| **P1–P2** | **User researcher / concept designer** — evidence generation | PM, UX research, discovery trio | — (upstream of formal SDLC) | Demand & value |
| **P3** | **Design strategist** — experience vision and principles | PM, strategy, GTM alignment | Owner (feasibility, initiative framing) | Steer & govern; Demand & value |
| **A Discover** | **Interaction designer** — user flows and task analysis | — | Owner (priorities); Implementer (spikes) | Demand & value; Build & integrate |
| **B Specify** | **Specification designer** — wireframes and interaction specs | — | Owner (acceptance criteria); Implementer (technical specs) | Build & integrate |
| **C Design** | **Visual / system designer** — mockups and design tokens | — | Implementer (component build); Owner consulted on trade-offs | Build & integrate |
| **D Build** | **Design QA partner** — review implementations against design | — | Implementer (code); Owner removes blockers | Build & integrate |
| **E Verify** | **Usability evaluator** — test with real users | — | Implementer (fix issues); Assure & ship (gate interpretation) | Assure & ship |
| **F Release** | **Experience monitor** — design fidelity check | GTM for launch comms | Implementer executes; Owner for go/no-go | Assure & ship |
| **P4–P5** | **Optimization researcher** — experiment and refine | PM, analytics — outcomes | Iteration cycles A–F for improvements | Flow & improvement |
| **P6** | **Transition designer** — sunset UX | PM, legal/comms | Implementer executes migration UX | Steer & govern |

---

## Artifact flow

### PDLC / SDLC → UX Design (inputs)

| Source | UX Design usage |
|--------|----------------|
| Problem statements and success criteria (**P1**, **P3**) | Frame research questions; define what "good UX" means for this product |
| NFRs and constraints (**B**, **C**) | Inform technical feasibility of design choices (performance budgets, platform constraints) |
| Analytics and production data (**P5**, DevOps) | Identify usability issues in live product; prioritize redesign targets |
| Accessibility compliance requirements (**P3**, **Steer & govern**) | Set conformance level (A, AA, AAA); determine audit cadence |

### UX Design → SDLC (outputs)

| UX artifact | SDLC usage |
|-------------|------------|
| Wireframes and interaction specs (**B**) | Input to functional specs and acceptance criteria |
| Design tokens and component specs (**C**) | Implementation contracts for frontend engineering |
| Usability test results (**E**) | Feed defect backlog with severity-rated UX issues |
| Accessibility audit findings (**E**) | Compliance defects that may block release |
| Design system updates (**C**, **D**) | Component library evolution; visual regression baselines |

### UX Design → PDLC (feedback)

| UX signal | PDLC usage |
|-----------|------------|
| Research insights (**P1**, **P2**) | Evidence for problem validation and solution direction |
| Usability metrics (SUS, task success, time on task) | Quantitative input to product health dashboards |
| A/B experiment results (**P5**) | Data-driven decisions on feature iteration vs. pivot |
| Journey map evolution | Updated understanding of user experience across touchpoints |

---

## Calibration

### By initiative type

| Situation | UX investment | Reasoning |
|-----------|--------------|-----------|
| **Greenfield product** | **High** — full discovery, persona development, concept testing, design system foundation | Mistakes in information architecture and interaction patterns compound; changing them later is expensive |
| **Feature on mature product** | **Medium** — wireframes, usability test on key flows, leverage existing design system | Marginal design within established patterns; focus on novel interactions |
| **Internal / admin tool** | **Medium** — efficiency-focused design, consistent patterns, lower visual polish acceptable | Users are captive but productivity matters; poor UX wastes employee time |
| **API / developer product** | **Low–medium** — documentation UX, developer portal, error message design | The "interface" is the API; UX applies to docs, SDKs, and developer experience |
| **Bug fix / small change** | **Targeted** — review for consistency; no new research | Use existing design system components |
| **Spike / throwaway prototype** | **Low** — quick sketches, no design system overhead | Match fidelity to prototype lifetime |

### Signals of under- or over-investment

| Signal | Interpretation |
|--------|---------------|
| **Under-invested** | High support ticket volume for "how do I…?"; low feature adoption despite marketing; accessibility complaints or legal risk; engineers guessing at interaction details |
| **Well calibrated** | Users accomplish tasks without training; design system covers 80%+ of UI needs; usability issues caught before release; accessibility conformance maintained |
| **Over-engineered (for context)** | Pixel-perfect mockups for throwaway prototypes; full research studies for obvious changes; design system governance slows feature delivery |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Design handoff wall** | Designers produce mockups then disappear; engineers interpret ambiguities alone | Embed designers in delivery teams; pair on implementation; design reviews during D and E |
| **Usability testing theater** | Tests are run but findings are deprioritized indefinitely | Severity-rate findings; integrate critical issues into sprint backlog; track fix rate |
| **Accessibility bolt-on** | Accessibility is treated as a final audit checkbox, not a design constraint | Include accessibility in design reviews from B onward; automate checks in CI; train all designers |
| **Design system ivory tower** | System team builds components nobody asked for; product teams route around the system | Federated contribution model; product teams propose components; system team curates and maintains |
| **Research without action** | Extensive research produces insights that do not influence product decisions | Tie research to upcoming decisions; present findings with actionable recommendations; PM co-owns research plan |

---

## UX Design and SDLC methodologies

| Methodology | UX emphasis |
|-------------|-------------|
| **Scrum** | Dual-track: UX runs 1–2 sprints ahead of engineering; usability testing within each sprint; design review in sprint review |
| **Kanban** | Continuous flow of design work; WIP limits apply to design tasks; design review as a column |
| **Lean** | Minimum viable design — test the cheapest representation that answers the question; kill ideas fast |
| **XP** | Pair design-development on UI components; on-site customer as ongoing usability signal |
| **Phased** | Formal design phases with gate reviews; comprehensive wireframes before build; accessibility audit at phase boundary |

---

## Worked example

**Scenario:** A B2B SaaS product team discovers through **P5** analytics that onboarding completion has dropped from 72% to 54% over three months. The PM initiates a redesign.

| Step | Lifecycle | What happens |
|------|-----------|--------------|
| 1 | **P1** | UX researcher conducts 8 user interviews with recent signups; contextual inquiry with 3 churned users. Discovers that a new required integration step is confusing and the setup wizard does not match users' mental model. |
| 2 | **P2** | Concept designer creates 3 alternative onboarding flows as click-through prototypes. Unmoderated usability test with 15 users reveals Flow B achieves 89% completion. |
| 3 | **A** | Interaction designer details Flow B: user flows for happy path, error states, skip/resume behavior, and mobile variant. |
| 4 | **B** | Specification designer produces wireframes with accessibility annotations (keyboard nav, screen reader flow, ARIA roles). Acceptance criteria include: task completion >= 80%, WCAG 2.2 AA compliance. |
| 5 | **C** | Visual designer creates high-fidelity mockups using the design system; adds 2 new components (stepper and integration card) with design tokens and Storybook stories. |
| 6 | **D** | Design QA partner pairs with frontend engineers on stepper component; reviews integration card implementation in Storybook before wiring into the onboarding flow. |
| 7 | **E** | Usability evaluator runs moderated test with 6 users on staging; 5/6 complete onboarding without assistance. Accessibility audit passes AA except one focus-order issue — defect logged and fixed. |
| 8 | **F** | Experience monitor reviews release candidate for design fidelity and edge cases (empty integration list, error recovery, browser compat). Release approved. |
| 9 | **P4** | Launched behind a feature flag (50% canary). Onboarding completion for variant: 83% vs 54% control. |
| 10 | **P5** | Full rollout. UX researcher runs follow-up survey at day 7 — SUS score improved from 62 to 78. Journey map updated. Remaining drop-off points queued for next discovery cycle. |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`UX-DESIGN.md`](UX-DESIGN.md) | Design thinking, interaction design, visual design, research methods, design systems |
| [`techniques/README.md`](techniques/README.md) | Research and design technique guides |
| [`accessibility/README.md`](accessibility/README.md) | WCAG compliance, ARIA, inclusive design |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, discovery and validation |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | How product and delivery lifecycles align |
| [`BA-SDLC-PDLC-BRIDGE.md`](../ba/BA-SDLC-PDLC-BRIDGE.md) | Requirements analysis — UX and BA converge during specification |
| [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) | SDLC role archetypes |
