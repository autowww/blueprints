---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Testing ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **testing and quality assurance** practices to the two lifecycle frameworks:

- **PDLC** (Product Development Life Cycle) — "Are we building the **right product**?"
- **SDLC** (Software Development Life Cycle) — "Are we building the product **right**?"
- **Testing** — "Is the software **correct, reliable, and fit for purpose**?"

Testing is the discipline that verifies SDLC execution quality and validates that PDLC outcomes are met. Without it, both lifecycles produce artifacts that cannot be trusted.

**Canonical sources:** [`APPROACHES.md`](APPROACHES.md) · [`AUTOMATION-LANDSCAPE.md`](AUTOMATION-LANDSCAPE.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md) · [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [1. The three-domain model](#1-the-three-domain-model) | How Testing, PDLC, and SDLC relate — scope, ownership, overlap |
| [2. Testing across the lifecycle](#2-testing-across-the-lifecycle) | Testing activities mapped to PDLC P1–P6 and SDLC A–F |
| [3. Role mapping](#3-role-mapping) | Testing roles vs Product, Delivery, and Architecture roles |
| [4. Artifact flow](#4-artifact-flow) | What testing produces and where it goes |
| [5. Calibration — when to invest in testing](#5-calibration--when-to-invest-in-testing) | Lightweight vs heavyweight testing by context |
| [6. Anti-patterns](#6-anti-patterns) | Common failures when testing is missing or misapplied |
| [7. Worked example](#7-worked-example) | End-to-end scenario showing testing across PDLC and SDLC |

---

## 1. The three-domain model

```blueprint-diagram
key: swimlane
alt: Diagram
```

### Comparison table

| Dimension | Testing | SDLC | PDLC |
|-----------|---------|------|------|
| **Core question** | Is the software correct, reliable, and fit for purpose? | How do we build this correctly? | Should we build this at all? |
| **Scope** | Verification (does it meet specs?) + validation (does it meet needs?) | Requirements → design → code → test → deploy | Problem validation → strategy → build → launch → grow → sunset |
| **Primary owner** | QA engineer / test lead / whole team (shift-left) | Engineering / delivery team | Product manager / product trio |
| **Timeline** | Continuous — from requirements review through production monitoring | Sprint / iteration / release cycle | Product lifetime (months to years) |
| **Success metric** | Defect detection rate, test coverage, quality gate pass rate, escaped defects | Velocity, defect rate, DORA, CI pass rate | Adoption, retention, NPS, revenue |
| **Key artifacts** | Test plan, test cases, test results, quality reports, traceability matrix | Specs, code, tests, release notes | Research synthesis, experiments, vision, metrics dashboards |
| **Risk focus** | Quality risk (correctness, reliability, security, performance) | Technical risk (bugs, performance, security) | Market risk (desirability, viability) |
| **Failure mode** | Ship buggy, insecure, or unreliable software | Ship late or with poor architecture | Ship the wrong thing |

### When one is missing

| Scenario | What happens |
|----------|-------------|
| **Testing without SDLC discipline** | Tests exist but delivery is chaotic — tests are written but not run in CI, coverage targets are set but not enforced, quality gates are defined but bypassed |
| **Testing without PDLC** | Software is thoroughly tested against specifications, but nobody verified the specifications solve a real problem — high-quality software that nobody uses |
| **SDLC without Testing** | Code is built and deployed but never systematically verified — escaped defects, regression surprises, production incidents, eroding trust |
| **PDLC without Testing** | Product direction is validated and strategy is sound, but delivered software is unreliable — validated idea, broken execution, users churn from bugs |
| **All three practiced** | Validated problems become well-specified requirements that are built correctly and verified thoroughly, delivering trustworthy software that meets measurable outcomes |

---

## 2. Testing across the lifecycle

### PDLC phases

| Phase | Testing role | Key activities | Outputs |
|-------|-------------|----------------|---------|
| **P1 Discover** | — | Minimal direct involvement; may review testability of proposed concepts | Testability notes (informal) |
| **P2 Validate** | **Prototype tester** | Usability testing of prototypes; feasibility spike validation; identify high-risk areas | Usability test results, risk-based test scope estimate |
| **P3 Plan & Commit** | **Quality planner** | Define quality strategy; estimate testing effort; identify non-functional requirements from success criteria | Quality strategy, NFR catalog, test effort estimate |
| **P4 Launch** | **Acceptance gatekeeper** | Final acceptance testing; smoke tests in production; canary monitoring | Acceptance sign-off, production smoke results |
| **P5 Grow** | **Outcome validator** | Monitor production quality metrics; track escaped defects against outcomes; regression analysis | Quality dashboards, escaped defect reports, outcome validation |
| **P6 Sunset** | **Migration tester** | Test data migration; verify graceful degradation; validate sunset completeness | Migration test results, sunset verification report |

### SDLC phases

| Phase | Testing role | Key activities | Outputs | Test levels engaged |
|-------|-------------|----------------|---------|---------------------|
| **A Discover** | **Risk assessor** | Identify quality risks; assess testability of proposed features; plan test strategy | Risk-based test scope, testability feedback | — |
| **B Specify** | **Criteria reviewer** | Review acceptance criteria for testability; write behavioral contracts (Gherkin); plan test levels and scope; draft test plan | Test plan, BDD scenarios, testability review notes | — |
| **C Design** | **Test architect** | Select automation framework; define V-level pairing (if V-Model); design test data strategy; plan contract tests | Test architecture, framework selection, RTM draft | — |
| **D Build** | **Test builder** | Write unit tests (TDD); implement integration tests; configure static analysis; add tests to CI gates; generate AI-assisted tests | Unit tests, integration tests, CI pipeline config | Unit, integration |
| **E Verify** | **Quality gatekeeper** | Execute system and acceptance tests; run regression suites; perform exploratory testing; run performance/security tests; verify traceability | Test execution reports, quality gate results, RTM | System, acceptance |
| **F Release** | **Release validator** | Final acceptance; smoke tests in staging/production; monitor canary deployment; shift-right validation | Release sign-off, smoke results, monitoring baseline | Acceptance |

---

## 3. Role mapping

### Across the lifecycle

| Phase(s) | Testing role | PDLC role | SDLC role | Archetype |
|----------|-------------|-----------|-----------|-----------|
| **P1–P2** (Discovery) | Testability advisor (lightweight) | PM, UX Researcher | — (upstream) | Demand & value |
| **P3** (Plan & Commit) | Quality strategy definer | PM, GTM Lead | Owner (entering SDLC) | Steer & govern |
| **A–B** (Discover, Specify) | Requirements reviewer, BDD author | — | Owner (priorities), Implementer | Assure & ship |
| **C** (Design) | Test architect, framework selector | — | Implementer (architecture) | Build & integrate |
| **D** (Build) | Unit/integration test author, CI gate builder | — | Implementer | Build & integrate |
| **E** (Verify) | System/acceptance tester, exploratory tester | — | Implementer, QA | Assure & ship |
| **F** (Release) | Release validator, production monitor | GTM Lead | — (downstream) | Assure & ship |
| **P5** (Grow) | Quality metrics analyst, escaped defect tracker | PM, Data/Analytics | Owner (iteration) | Assure & ship |

### Testing vs other disciplines

| Dimension | Testing | BA | DevOps | Architecture |
|-----------|---------|------|--------|-------------|
| **Primary focus** | Verify correctness and fitness | Understand and specify needs | Automate delivery and operations | Structure systems for quality attributes |
| **What they give testing** | — | Acceptance criteria, requirements to trace | CI/CD pipelines that execute tests | Architectural boundaries that define integration points |
| **What testing gives them** | — | Verification that requirements are implementable | Quality gate results for pipeline decisions | Testability feedback on architectural choices |
| **Overlap** | Test design, quality assessment | Requirements review, acceptance criteria | CI pipeline configuration, test automation | NFR verification, integration test boundaries |

---

## 4. Artifact flow

### BA/PDLC → Testing (inputs)

| Source artifact | Testing usage |
|----------------|---------------|
| Acceptance criteria (BA, SDLC Phase B) | Primary input for test case design; defines "done" at the story level |
| Non-functional requirements (BA/Architecture, Phase B–C) | Drive performance, security, and reliability test plans |
| Success metrics (PDLC P3) | Define outcome-level acceptance thresholds for validation testing |
| Traceability matrix (BA) | Links requirements → test cases; ensures coverage completeness |
| Risk assessment (BA/PM) | Drives risk-based test prioritization — test high-risk areas first and deepest |

### Testing → SDLC (outputs)

| Testing artifact | SDLC usage |
|-----------------|------------|
| Test results (Phases D–E) | Quality gate input — pass/fail determines whether code advances |
| Coverage reports (Phase D) | CI gate metric — minimum coverage enforced before merge |
| Defect reports (Phase E) | Input to Phase D rework; tracked in WBS/backlog |
| Test plan (Phase B–C) | Governs testing scope, approach, and resource allocation |
| RTM (Phase B–E) | Proves all requirements have corresponding test coverage |

### Testing → PDLC (feedback)

| Testing artifact | PDLC usage |
|-----------------|------------|
| Acceptance test results (Phase E) | P4 launch gate — confirms product meets validated needs |
| Production quality metrics (P5) | Input to outcome measurement — escaped defects, reliability data |
| Usability test results (P2) | Validation evidence — prototype meets user expectations |
| Performance baselines (Phase E–F) | P5 growth capacity — can the product handle growth targets? |

---

## 5. Calibration — when to invest in testing

### By initiative type

| Situation | Testing investment | Reasoning |
|-----------|-------------------|-----------|
| **Greenfield product** (new market) | **Heavy** — full test strategy, shift-left practices, comprehensive automation, performance baselines | High uncertainty; untested assumptions propagate expensive defects |
| **Feature on mature product** | **Medium** — regression suite protects existing behavior; new feature tests; integration tests at boundaries | Existing test infrastructure reduces marginal cost; focus on boundaries and interactions |
| **Technical infrastructure** | **Heavy on non-functional** — performance, reliability, security, chaos testing | Users are other systems; functional testing is simpler but NFR testing is critical |
| **Bug fix / maintenance** | **Targeted** — reproduce-fix-verify cycle; add regression test for the specific defect | Fix scope is small; the missing test is the primary deliverable |
| **Prototype / spike** | **Minimal** — manual validation is sufficient; don't invest in automation for throwaway code | Code will be discarded; testing effort has no long-term return |

### By team size and context

| Context | Testing approach |
|---------|-----------------|
| **Solo developer** | TDD discipline; CI with basic quality gates; manual exploratory for UI |
| **Small agile team (3–8)** | Whole-team quality; developers write unit/integration tests; shared ownership of E2E; shift-left |
| **Medium team (8–25)** | Dedicated QA embedded in team; test automation engineer role; structured test plans for complex scope |
| **Large / multi-team** | QA chapter or guild; test architecture standards; shared test infrastructure; contract testing across services |
| **Regulated environment** | Formal test documentation (RTM, test evidence); independent verification and validation (IV&V); audit trail |

### The test pyramid as calibration tool

```
                    ╱╲
                   ╱  ╲
                  ╱ E2E╲          Few — slow, expensive, high confidence
                 ╱──────╲
                ╱  API /  ╲       Contract + integration tests
               ╱  contract ╲
              ╱──────────────╲
             ╱   Component /  ╲   Unit + component tests
            ╱     unit         ╲
           ╱────────────────────╲
          ╱  Static analysis /   ╲  Linters, SAST, type checking
         ╱   type checking        ╲
        ╱──────────────────────────╲
```

Invest most in the lower layers (fast, cheap, stable). Keep the E2E layer thin — only critical user journeys and smoke tests. Shift testing left to catch defects when they are cheapest to fix.

---

## 6. Anti-patterns

| Anti-pattern | Description | Symptom | Fix |
|-------------|-------------|---------|-----|
| **Ice cream cone** | Inverted test pyramid — most tests are slow E2E/manual; few unit tests | Slow CI pipelines (>30min); flaky tests block merges; "it works on my machine" | Invert the pyramid — add unit/integration tests; replace flaky E2E with contract tests; delete redundant E2E |
| **Testing as a phase** | Testing happens only after "development is done" — separate test phase at the end | Late defect discovery; compressed test cycles; bugs found in UAT that should have been caught in unit tests | Shift-left — QA reviews acceptance criteria in Phase B; TDD in Phase D; continuous testing in CI |
| **Coverage theater** | High coverage percentage (90%+) achieved by testing trivial paths; complex logic untested | Coverage target met but production defects persist; false confidence in test suite quality | Risk-based testing — prioritize coverage of complex, high-risk, and frequently-changed code; measure mutation testing score |
| **Test maintenance tax** | Tests are tightly coupled to implementation; every refactor breaks dozens of tests | Developers avoid refactoring because "it will break too many tests"; test suite becomes a drag on velocity | Test behavior, not implementation; reduce test coupling; use test doubles at appropriate boundaries |
| **Missing acceptance tests** | Unit and integration tests pass, but nobody tests whether the feature meets user needs | Features are "technically correct" but don't solve the user's problem; discovered only after launch | Connect tests to acceptance criteria from BA/PDLC; automate acceptance tests (BDD); include exploratory testing |
| **No production testing** | All testing happens pre-production; production is a black box until users report problems | Surprises from production-only conditions (load, data volume, network); reactive incident response | Add shift-right practices — canary releases, synthetic monitoring, chaos engineering, feature flags |
| **QA bottleneck** | All testing goes through a single QA person or team; developers don't write tests | QA backlog grows; releases are delayed waiting for QA; QA becomes a gate instead of an enabler | Whole-team quality — developers own unit/integration tests; QA focuses on test strategy, automation architecture, and exploratory testing |

---

## 7. Worked example

**Scenario:** A SaaS company builds a payment processing feature. The initiative flows through PDLC discovery, SDLC delivery, and testing at every stage.

### P2 Validate — prototype testing

The product trio builds a Figma prototype of the checkout flow. QA reviews the prototype and flags:
- Edge case: what happens when payment is declined mid-transaction?
- Accessibility: color-only status indicators will fail WCAG 2.1 AA
- Testability: the proposed multi-step wizard will need state management tests at each step

**Artifacts produced:** Testability notes (3 items), usability test plan for 6 participants.

**Usability test results:** 5/6 participants completed checkout in under 2 minutes. One participant confused by the address auto-complete behavior. Design updated.

### P3 Plan & Commit — quality strategy

Quality strategy defined based on P3 success metrics:
- **Functional:** all payment methods (card, ACH, wallet) must pass end-to-end
- **Performance:** checkout latency < 2s at P99 under expected load (1000 concurrent checkouts)
- **Security:** PCI DSS Level 1 compliance required; penetration testing mandatory
- **Reliability:** 99.95% uptime for payment processing; circuit breaker for payment gateway failures

**Test effort estimate:** 2 QA-sprints for automation setup; ongoing regression in CI.

### SDLC Phase B — acceptance criteria review

QA reviews acceptance criteria for testability:

| Story | Acceptance criterion | QA feedback |
|-------|---------------------|-------------|
| PAY-001: Card payment | "User can pay with Visa, Mastercard, Amex" | Add: specify test card numbers for each; add declined card scenario |
| PAY-002: ACH payment | "User can pay via bank transfer" | Add: specify bank verification flow timing; add insufficient funds scenario |
| PAY-003: Payment receipt | "User receives receipt after payment" | Add: specify receipt format; add email delivery verification; add receipt for failed payments |

**BDD scenarios written:**

```gherkin
Feature: Card payment
  Scenario: Successful payment with Visa
    Given the user has items totaling $49.99 in cart
    When they enter valid Visa card details and submit
    Then the payment is processed successfully
    And they see a confirmation with transaction ID

  Scenario: Declined card
    Given the user has items in cart
    When they enter a declined card number and submit
    Then they see an error message with decline reason
    And no charge is created
```

### SDLC Phase C — test architecture

Test architecture decisions:
- **Unit tests:** Jest for business logic; mock payment gateway SDK
- **Integration tests:** Testcontainers for database; WireMock for payment gateway stubs
- **Contract tests:** Pact for payment gateway API contract (consumer-driven)
- **E2E tests:** Playwright for critical checkout journey (3 scenarios: card success, card decline, ACH success)
- **Performance tests:** k6 for load testing checkout endpoint
- **Security tests:** OWASP ZAP in CI; manual penetration test pre-launch

### SDLC Phase D — test implementation (shift-left)

TDD for payment processing logic:
- 47 unit tests covering card validation, amount calculation, retry logic, idempotency
- 12 integration tests covering database transactions, gateway communication, webhook handling
- 3 contract tests (Pact) verifying payment gateway API compatibility
- Static analysis: ESLint, TypeScript strict mode, SonarQube quality gate

**CI pipeline quality gates:** all tests must pass; coverage > 80% on new code; SonarQube quality gate pass; no critical/high security findings.

### SDLC Phase E — verification

- **System tests:** Full checkout flow against staging environment with test payment gateway
- **Performance test:** k6 load test — 1000 concurrent checkouts, P99 latency 1.4s (target: < 2s) — passed
- **Security test:** OWASP ZAP scan — 0 high findings, 2 medium findings (fixed before release)
- **Exploratory testing:** QA explores edge cases — discovers that double-clicking "Pay" creates duplicate charges; filed PAY-BUG-001, fixed in Phase D rework
- **Acceptance testing:** BDD scenarios all green; PO reviews and accepts
- **RTM:** All 7 requirements traced to test cases; all test cases passed

### P4 Launch — production validation

- **Canary deployment:** 5% of traffic routed to new payment flow; monitoring for error rates, latency, conversion rate
- **Smoke tests:** 3 critical checkout scenarios automated in production (synthetic monitoring)
- **Results after 24h:** 0 errors, P99 latency 1.6s, conversion rate +2.1% vs control

### P5 Grow — outcome validation

**Week 4 metrics:**

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Checkout completion rate | 85% | 87% | Exceeded |
| Payment processing latency (P99) | < 2s | 1.5s | Met |
| Payment failure rate | < 1% | 0.4% | Met |
| Escaped defects (production) | 0 critical | 0 critical, 1 low | Met |

**Escaped defect:** Low-severity formatting issue in receipt PDF for amounts > $10,000 (comma placement). Regression test added.

**Quality feedback to SDLC Phase A:** "Add currency formatting unit tests for large amounts" — new story created in iteration backlog.

---

## Related reading

| Doc | Why |
|-----|-----|
| [`APPROACHES.md`](APPROACHES.md) | Test levels, types, techniques, strategies, ISTQB alignment |
| [`AUTOMATION-LANDSCAPE.md`](AUTOMATION-LANDSCAPE.md) | Framework taxonomy, selection guidance, cloud infrastructure |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | How PDLC and SDLC relate without the testing lens |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD, CI/CD quality gates |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, stage gates, outcome metrics |
| [`TEST-PLAN.template.md`](../../../sdlc/templates/TEST-PLAN.template.md) | Copy-paste template for scope-level test plans |
| [`methodologies/v-model/`](../../../sdlc/methodologies/v-model/README.md) | V&V pairing; RTM; formal test gates |
| [`methodologies/bdd.md`](../../../sdlc/methodologies/bdd.md) | Behavior-driven development; Given-When-Then; living specs |
