# BDD (Behavior-Driven Development)

## What it is

**Behavior-Driven Development (BDD)** is a collaborative practice that bridges the gap between **business requirements** and **technical implementation** by expressing desired system behavior in **business-readable** scenarios. BDD was created by Dan North (2006) as an evolution of **Test-Driven Development (TDD)** that shifts focus from testing code units to specifying **behavior** from the user's perspective.

BDD scenarios follow the **Given-When-Then** format (derived from acceptance test templates) and serve as both **living documentation** and **automated acceptance tests**.

BDD is **not** a standalone SDLC methodology — it is a **collaborative practice** that complements any delivery framework (Scrum, Kanban, XP, phased) by improving how teams specify and verify behavior.

## Process diagram (handbook)

![BDD — discovery, formulation, automation](../docs/assets/methodology-bdd-loop.svg)

*Discovery (explore behavior) → Formulation (write scenarios) → Automation (make them executable). The three practices of BDD.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**Wikipedia — Behavior-driven development**](https://en.wikipedia.org/wiki/Behavior-driven_development) | **Stable overview** of BDD — history, Given-When-Then, tools, relationship to TDD. |
| [Dan North — Introducing BDD](https://dannorth.net/introducing-bdd/) | **Original** article by BDD's creator — motivation and initial formulation. |
| [Cucumber — BDD overview](https://cucumber.io/docs/bdd/) | **Practitioner** guide — how to do BDD with a popular tool; process and anti-patterns. |

---

## Three practices

| Practice | Purpose |
|----------|---------|
| **Discovery** | Structured conversation (often **Example Mapping**) between business, development, and testing to explore desired behavior before writing code. |
| **Formulation** | Write concrete scenarios in **Given-When-Then** format that capture the agreed behavior. These become the specification. |
| **Automation** | Make scenarios executable using BDD frameworks (Cucumber, SpecFlow, Behave, etc.) so they serve as living, verifiable documentation. |

---

## Given-When-Then format

```gherkin
Feature: User login
  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    Then the user is redirected to the dashboard
    And a welcome message is displayed

  Scenario: Failed login with invalid password
    Given the user is on the login page
    When the user enters an invalid password
    Then an error message is displayed
    And the user remains on the login page
```

---

## BDD vs TDD

| Dimension | BDD | TDD |
|-----------|-----|-----|
| Focus | **Behavior** from user perspective | **Code** correctness at unit level |
| Language | Business-readable (Given-When-Then) | Code (test frameworks) |
| Audience | Business + development + testing | Primarily developers |
| Scope | Acceptance / integration level | Unit level |
| Complements | Works **with** TDD, not instead of it | Works with BDD at a lower level |

---

## Mapping to this blueprint's SDLC

| BDD idea | Blueprint touchpoint |
|----------|----------------------|
| Discovery | Phase A–B: requirements, acceptance criteria — BDD structures these conversations. |
| Formulation | Phase B: specification — scenarios become the spec (see [`spec-driven-development.md`](spec-driven-development.md)). |
| Automation | Phase D–E: build and verify — executable scenarios in the test suite. |
| Living documentation | Cross-phase: scenarios stay current as the system evolves; replaces stale docs. |

**Relationship to Spec-Driven Development:** BDD's Given-When-Then scenarios are a specific **implementation** of spec-driven development's principle that written intent leads implementation. See [`spec-driven-development.md`](spec-driven-development.md).

---

## Agentic SDLC: BDD + agents

| Topic | Guidance |
|-------|----------|
| **Scenario generation** | Agents can draft Given-When-Then scenarios from requirements. **Human** review ensures business accuracy and edge-case coverage. |
| **Step definition** | Agents can generate step definition code from scenarios. **Human** validates the binding between steps and system behavior. |
| **Living documentation** | Agent-maintained scenario summaries can serve as up-to-date feature documentation. |
| **Discovery** | The discovery conversation (Example Mapping) is **fundamentally human** — agents can prepare materials but cannot replace the collaborative exploration. |

---

## Further reading

- [Dan North — Introducing BDD](https://dannorth.net/introducing-bdd/) — **Original** article.
- [Cucumber](https://cucumber.io/) — **Popular** BDD tool ecosystem.
- Companion: [XP](xp.md) (TDD), [Spec-driven development](spec-driven-development.md), [Agile umbrella](agile.md)
