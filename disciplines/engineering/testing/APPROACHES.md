---
slug: discipline-testing
tier: 201
lens: discipline
nav_section: Disciplines
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Testing approaches (blueprint)

**Purpose:** Product-agnostic reference for **testing vocabulary**, **test strategies**, and **test design techniques**. Uses ISTQB Foundation (v4.0.1) terminology as the shared language while covering modern practices (shift-left, contract testing, AI-augmented testing) that extend beyond the ISTQB syllabus.

**Audience:** Teams adopting [`blueprints/sdlc/`](../../../sdlc/README.md); project-specific test plans and stack choices stay in **`docs/testing/`**.

| Related doc | Role |
|-------------|------|
| [`README.md`](README.md) | Testing knowledge-base hub. |
| [`AUTOMATION-LANDSCAPE.md`](AUTOMATION-LANDSCAPE.md) | Which **tools** implement these approaches. |
| [`SDLC.md`](../../../sdlc/SDLC.md) §7 | CI/CD, quality gates, test plans — lifecycle spine. |
| [`TEST-PLAN.template.md`](../../../sdlc/templates/TEST-PLAN.template.md) | Scope-level test plan template. |
| [`methodologies/v-model/`](../../../sdlc/methodologies/v-model/README.md) | V&V pairing; RTM; formal test gates. |
| [`methodologies/devops/`](../../../sdlc/methodologies/devops/README.md) | Automated test pyramid; CI/CD pipeline flows. |
| [`methodologies/bdd.md`](../../../sdlc/methodologies/bdd.md) | Given-When-Then; living specifications. |

---

## 1. Test levels

Test levels define the **granularity** at which software is tested. Each level targets defects at a different layer of integration.

| Level | What it verifies | Typical owner | Automation | SDLC phase |
|-------|-----------------|---------------|------------|------------|
| **Unit** | Individual functions, methods, or classes in isolation. | Developer | Almost always automated (JUnit, pytest, Jest, XCTest). | D Build |
| **Integration** | Interactions between modules, services, or system components. | Developer / QA | Automated; may need test doubles for external dependencies. | D Build / E Verify |
| **System** | The complete integrated system against specified requirements. | QA / test team | Automated (E2E frameworks) + manual exploratory. | E Verify |
| **Acceptance** | Whether the system satisfies user needs and business requirements. | Owner / stakeholder / QA | May include automated regression + manual UAT. | E Verify / F Release |

**V-Model pairing:** each design level on the left side of the V produces specifications that the corresponding test level on the right side verifies — see [`v-model/foundation-connection.md`](../../../sdlc/methodologies/v-model/foundation-connection.md).

---

## 2. Test types

Test types describe **what quality characteristic** is being tested, independent of test level.

| Type | Purpose | When to apply |
|------|---------|---------------|
| **Functional** | Does the system do what it should? Verifies behavior against requirements. | All levels; primary focus of most test plans. |
| **Non-functional** | Performance, usability, reliability, security, accessibility, compatibility. | System and acceptance levels; plan early (Phase B Specify). |
| **Structural (white-box)** | Exercises internal code paths (statement, branch, condition coverage). | Primarily unit and integration; coverage targets in CI gates. |
| **Change-related** | Confirmation testing (defect fixes) and regression testing (unchanged behavior). | After every change; automated regression suites are the backbone of CI. |

---

## 3. The modern test pyramid

The classic test pyramid (unit → integration → E2E) has evolved to reflect modern architectures and tooling. The modern version adds static analysis at the base and contract/API tests as a distinct layer.

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

| Layer | Characteristics | Examples |
|-------|----------------|----------|
| **Static analysis** | Fastest feedback; no execution needed; catches syntax, type, style, and security issues at author time. | ESLint, ktlint, Android Lint, SonarQube, Detekt, mypy, Clippy. |
| **Unit / component** | Fast; isolated; mock external dependencies; high volume. | JUnit, pytest, Jest, XCTest, go test. |
| **API / contract** | Validates inter-service communication without full system; catches breaking interface changes. | Pact, Spring Cloud Contract, REST Assured, Postman/Newman. |
| **E2E / UI** | Validates user-visible behavior through the real UI; slow but high confidence. | Playwright, Cypress, Selenium, Espresso, Appium. |

**Guideline:** invest most in the lower layers (fast, cheap, stable) and keep the E2E layer thin — only critical user journeys and smoke tests.

---

## 4. Test design techniques

Techniques for **deriving test cases** systematically rather than ad-hoc. ISTQB groups them into black-box, white-box, and experience-based.

### 4.1 Black-box (specification-based)

| Technique | When to use |
|-----------|-------------|
| **Equivalence partitioning** | Divide inputs into classes where all values in a class should behave identically; test one representative per class. |
| **Boundary value analysis** | Focus on edges of equivalence classes (min, max, off-by-one); common source of defects. |
| **Decision table** | Complex business rules with multiple conditions and actions; each column is a test case. |
| **State transition** | System behavior depends on state (e.g. order lifecycle, auth flows); test valid and invalid transitions. |
| **Use case / scenario** | End-to-end user journeys; validates that the system supports the intended workflow. |

### 4.2 White-box (structure-based)

| Technique | When to use |
|-----------|-------------|
| **Statement coverage** | Ensure every code statement is executed at least once; minimum viable coverage. |
| **Branch coverage** | Ensure every decision branch (if/else, switch) is taken; catches paths missed by statement coverage. |
| **Condition / MC/DC** | Multiple condition decision coverage; required by safety standards (DO-178C, IEC 62304). |

### 4.3 Experience-based

| Technique | When to use |
|-----------|-------------|
| **Exploratory testing** | Simultaneous learning, test design, and execution; effective for new features, usability, and edge cases that formal techniques miss. |
| **Error guessing** | Experienced testers anticipate likely defects based on past patterns. |
| **Checklist-based** | Reusable checklists for common concerns (accessibility, localization, security). |

---

## 5. Testing strategies

### 5.1 Shift-left testing

Move testing activities **earlier** in the lifecycle to catch defects when they are cheapest to fix. Research shows bugs caught in requirements cost 10–100x less than those found in production.

| Practice | SDLC phase | What it means |
|----------|------------|---------------|
| **Requirements testing** | B Specify | QA reviews acceptance criteria for testability, completeness, and ambiguity before development starts. |
| **Static analysis in IDE** | D Build | Linters and type checkers run as the developer types — fastest possible feedback. |
| **TDD (Test-Driven Development)** | D Build | Write a failing test → implement to pass → refactor. Ensures every unit of code has a test from birth. |
| **BDD (Behavior-Driven Development)** | B Specify / D Build | Write Given-When-Then scenarios as executable specifications before implementation — see [`bdd.md`](../../../sdlc/methodologies/bdd.md). |
| **Code review as testing** | D Build | Peer review catches design issues, logic errors, and security problems before merge. |
| **CI quality gates** | D Build / E Verify | Automated pipeline enforces build + lint + test + scan on every push — see [`SDLC.md`](../../../sdlc/SDLC.md) §7. |

### 5.2 Shift-right testing

Complement shift-left by testing **in production** to catch issues that pre-production environments cannot surface.

| Practice | What it means |
|----------|---------------|
| **Canary releases** | Deploy to a small percentage of users; monitor for errors before full rollout. |
| **Feature flags** | Enable/disable features at runtime; test in production without full deployment. |
| **Synthetic monitoring** | Automated probes that continuously verify critical user journeys in production. |
| **Chaos engineering** | Deliberately inject failures (network latency, service outages) to verify resilience. |
| **Observability** | Structured logging, distributed tracing, and metrics to detect and diagnose issues quickly. |

### 5.3 Test-Driven Development (TDD)

```
  ┌─────────┐     ┌─────────┐     ┌──────────┐
  │  Red    │────→│  Green  │────→│ Refactor │──→ (repeat)
  │ (write  │     │ (make   │     │ (improve │
  │  failing│     │  it     │     │  design) │
  │  test)  │     │  pass)  │     └──────────┘
  └─────────┘     └─────────┘
```

TDD ensures that tests exist **before** implementation, not as an afterthought. It produces well-tested, loosely coupled code. XP elevates TDD to a core practice — see [`xp.md`](../../../sdlc/methodologies/xp.md).

### 5.4 Behavior-Driven Development (BDD)

BDD extends TDD by expressing tests in **business language** (Gherkin syntax):

```gherkin
Feature: User login
  Scenario: Valid credentials
    Given the user is on the login page
    When they enter valid credentials
    Then they should see the dashboard
```

BDD scenarios serve as **living specifications** and **automated acceptance tests** simultaneously. Cucumber, SpecFlow, and similar runners execute Gherkin features against step definitions. AURORA-IA elevates behavioral contracts (Gherkin) to the core of its AI-native lifecycle — see [`../../../../sdlc/AI-NATIVE-METHODOLOGIES.md`](../../../../sdlc/AI-NATIVE-METHODOLOGIES.md).

Full methodology guide: [`bdd.md`](../../../sdlc/methodologies/bdd.md).

### 5.5 Contract testing

Validates **inter-service agreements** without requiring the full system to be running. Critical for microservices and API-first architectures.

```
  ┌──────────┐  contract  ┌──────────┐
  │ Consumer │───────────→│ Provider │
  │ (writes  │            │ (verifies│
  │  expected│            │  contract│
  │  behavior│            │  against │
  │  as Pact)│            │  its API)│
  └──────────┘            └──────────┘
```

| Variant | Description |
|---------|-------------|
| **Consumer-driven** | Consumer defines expected interactions (Pact); provider verifies it can satisfy them. |
| **Provider-driven** | Provider publishes its API schema (OpenAPI); consumers validate compatibility. |
| **Bi-directional** | Both sides publish expectations; a broker checks compatibility. |

### 5.6 Visual / snapshot testing

Detects **unintended visual regressions** by comparing screenshots or DOM snapshots against baselines.

| Approach | Tools | Trade-offs |
|----------|-------|------------|
| **Pixel comparison** | Applitools, Percy, Playwright visual comparisons | High fidelity; can be sensitive to rendering differences across environments. |
| **DOM snapshot** | Jest snapshots, Storybook | Fast; less prone to rendering noise; misses visual-only issues. |
| **Component snapshot** | Storybook + Chromatic | Isolates components; good for design systems and UI libraries. |

### 5.7 AI-augmented testing

The testing industry has entered what practitioners call the **agentic epoch** — AI agents that autonomously explore, generate, and maintain tests.

| Capability | What it means | Current maturity |
|------------|---------------|-----------------|
| **Autonomous exploration** | AI agents navigate applications, identify interactive elements, and build test coverage without scripted instructions. | Production-ready in leading tools (Mabl, testRigor, Playwright Agents). |
| **Natural-language test generation** | Describe tests in plain English; AI produces executable test code. | Practical for daily use; quality varies by framework. |
| **Self-healing selectors** | Tests automatically adapt when UI elements change (locator strategies, DOM structure). | Reduces 30–40% maintenance tax from brittle selectors. |
| **AI-generated unit tests** | Coding agents (Cursor, Claude Code, Copilot) generate unit/integration tests from code or specs. | Effective for boilerplate; human review essential for edge cases and intent. |
| **Drift detection** | Spec ↔ code ↔ test coherence checks (AURORA-IA drift index). | Emerging; conceptual frameworks exist, tooling is early. |

**Connection to agentic SDLC:** see [`agentic-sdlc.md`](../../../sdlc/methodologies/agentic-sdlc.md) and [`AI-NATIVE-METHODOLOGIES.md`](../../../../sdlc/AI-NATIVE-METHODOLOGIES.md) for governance models around AI test generation (progressive autonomy, quality gates, human review).

---

## 6. ISTQB certification landscape

ISTQB provides a standardized body of knowledge for software testing. The certifications below are the most relevant for teams using this blueprint.

| Certification | Focus | Relevance |
|---------------|-------|-----------|
| **CTFL v4.0.1** (Foundation Level) | Test fundamentals, levels, types, techniques, management, tool support. Updated for Agile/DevOps; "whole team" quality approach. | Core — provides shared vocabulary used throughout this document. |
| **CTAL-TA v4.0** (Advanced Test Analyst) | Advanced test design techniques; risk-based testing; defect management. | For dedicated test analysts and QA leads. |
| **CTAL-TAE v2.0** (Advanced Test Automation Engineering) | Architecture of test automation frameworks; maintainability; reporting. | For test automation engineers building framework infrastructure. |
| **CT-TAS** (Test Automation Strategy) | Strategic planning for test automation adoption; ROI; organizational readiness. | For managers and architects deciding automation investment. |
| **CT-GenAI** (Testing with Generative AI) | Using LLMs across the testing lifecycle — test design, generation, review, analysis. | New; aligns with agentic SDLC and AI-native methodologies. |
| **CT-AI** (AI Testing) | Testing AI-based systems (bias, explainability, data quality); distinct from using AI for testing. | Relevant when your product includes AI/ML features. |

**Position in this blueprint:** ISTQB vocabulary (test levels, types, techniques) is used as the **shared language** throughout this package. Certification is optional — the goal is common understanding, not exam prep.

---

## 7. Mapping to SDLC phases and ceremony intents

| Phase | Testing activities | Ceremony intents | Key approaches |
|-------|--------------------|-----------------|----------------|
| **A Discover** | Identify quality risks; consider testability of proposed features. | C1 Align | Risk-based test planning; quality attribute workshops. |
| **B Specify** | Review acceptance criteria for testability; write behavioral contracts (Gherkin); plan test levels and scope. | C1 Align, C6 Assure (readiness) | BDD; requirements testing; shift-left. |
| **C Design** | Draft test plans for non-trivial scope; select automation framework; define V-level pairing (if V-Model). | C1 Align, C6 Assure | Test design techniques (§4); contract test design; V-Model RTM. |
| **D Build** | Write unit tests (TDD); implement integration tests; configure static analysis; add tests to CI gates. | C2 Commit, C3 Sync, C6 Assure | TDD; static analysis; CI quality gates; AI-generated tests. |
| **E Verify** | Execute system and acceptance tests; run regression suites; perform exploratory testing; review traceability. | C3 Sync, C4 Review, C6 Assure | E2E automation; exploratory testing; visual testing; contract verification. |
| **F Release** | Final acceptance; smoke tests in staging/production; monitor canary deployment. | C4 Review, C6 Assure | Acceptance testing; shift-right (canary, synthetic monitoring). |

---

## 8. Authoritative sources & further reading

| Topic | URL | Executive summary |
|-------|-----|-------------------|
| ISTQB CTFL Syllabus v4.0.1 | https://istqb.org/certifications/certified-tester-foundation-level | Foundation Level syllabus — test fundamentals, levels, types, techniques, management. |
| ISTQB Test Automation syllabi | https://istqb.org/certifications/test-automation | CT-TAS (strategy) and CTAL-TAE (engineering) syllabi for automation. |
| ISTQB CT-GenAI | https://istqb.org/certifications/testing-with-generative-ai | Testing with Generative AI certification — LLMs in the testing lifecycle. |
| Martin Fowler — Test Pyramid | https://martinfowler.com/articles/practical-test-pyramid.html | Definitive explanation of the test pyramid and when to use each layer. |
| Martin Fowler — TDD | https://martinfowler.com/bliki/TestDrivenDevelopment.html | Short expert summary of TDD principles and motivation. |
| Dan North — Introducing BDD | https://dannorth.net/introducing-bdd/ | Original BDD article by its creator — motivation and formulation. |
| Pact — Contract testing | https://docs.pact.io/ | Consumer-driven contract testing; getting started, concepts, best practices. |
| Google Testing Blog | https://testing.googleblog.com/ | Practitioner articles on test strategy, flaky tests, test culture. |
| DORA — DevOps Research | https://dora.dev/ | Research-backed DevOps metrics; testing's impact on deployment performance. |
| Wikipedia — Software testing | https://en.wikipedia.org/wiki/Software_testing | Stable overview of testing concepts, history, and terminology. |
| OWASP Testing Guide | https://owasp.org/www-project-web-security-testing-guide/ | Security testing methodology; complements functional and non-functional testing. |

---

*Hub:* [`README.md`](README.md) · *Tools:* [`AUTOMATION-LANDSCAPE.md`](AUTOMATION-LANDSCAPE.md) · *Bridge:* [`TESTING-SDLC-PDLC-BRIDGE.md`](TESTING-SDLC-PDLC-BRIDGE.md) · *Lifecycle:* [`SDLC.md`](../../../sdlc/SDLC.md) §7 · *Test plan template:* [`TEST-PLAN.template.md`](../../../sdlc/templates/TEST-PLAN.template.md)