# V-Model

## What it is

The **V-Model** (Verification and Validation Model) extends the **Waterfall** model by explicitly pairing each **development phase** on the left side of the "V" with a corresponding **testing phase** on the right side. Requirements map to acceptance tests, high-level design maps to system tests, detailed design maps to integration tests, and implementation maps to unit tests. The bottom of the V is **coding**; verification flows upward on the right.

It is **standard** in **regulated industries** (automotive via ISO 26262, medical devices via IEC 62304, aerospace via DO-178C, defense) where **traceability** between requirements and test evidence is mandatory. It is **not** a lightweight iterative framework — it emphasizes **upfront planning** and **formal verification**.

## Process diagram (handbook)

![V-Model — left side (development) and right side (testing)](../docs/assets/methodology-v-model.svg)

*Left side descends from requirements to code; right side ascends from unit tests to acceptance. Horizontal arrows show traceability between corresponding levels.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**Wikipedia — V-model (software development)**](https://en.wikipedia.org/wiki/V-model_(software_development)) | **Stable overview** of the V-Model — phases, traceability, and comparison with Waterfall and Agile. |
| [Wikipedia — Verification and validation](https://en.wikipedia.org/wiki/Verification_and_validation) | **Foundational concepts** — "Are we building the product right?" (verification) vs "Are we building the right product?" (validation). |
| [ISO 26262 (catalogue)](https://www.iso.org/standard/68383.html) | **Automotive** functional safety standard that mandates V-Model-style development — catalogue entry (full text licensed). |
| [IEC 62304 (catalogue)](https://www.iso.org/standard/71604.html) | **Medical device** software lifecycle standard — V-Model-aligned process requirements (catalogue entry). |

**Note:** The V-Model is a **conceptual framework**, not a single standard. Different industries adapt it; the core idea of pairing development and test levels is universal.

---

## Core structure (summary)

### Left side (development / decomposition)

| Level | Activities |
|-------|-----------|
| **Requirements analysis** | Stakeholder needs, system requirements, acceptance criteria. |
| **System design** | Architecture, subsystem boundaries, interfaces. |
| **Detailed design** | Module-level design, algorithms, data structures. |
| **Implementation** | Coding, unit construction. |

### Right side (testing / integration)

| Level | Activities | Traces to |
|-------|-----------|-----------|
| **Unit testing** | Test individual modules against detailed design. | Detailed design |
| **Integration testing** | Test module interactions against system design. | System design |
| **System testing** | Test complete system against system requirements. | Requirements |
| **Acceptance testing** | Validate with users/stakeholders against business needs. | Stakeholder needs |

### Key characteristics

| Characteristic | Description |
|----------------|-------------|
| **Traceability** | Every requirement maps to a test; every test traces back to a requirement. |
| **Early test planning** | Test plans are written during the corresponding development phase, not after coding. |
| **Formal verification** | Each right-side phase verifies outputs of the corresponding left-side phase. |
| **Sequential with feedback** | Primarily sequential, but issues found during testing feed back to the corresponding development level. |

---

## Mapping to this blueprint's SDLC

[`SDLC.md`](../SDLC.md) uses **Phases A–F** (discover → release). The V-Model maps as a structured pass with paired verification:

| V-Model idea | Blueprint touchpoint |
|---------------|----------------------|
| Requirements analysis (left) | Phase A–B: discovery, requirements in `docs/requirements/`. |
| System/detailed design (left) | Phase B–C: architecture, design in `docs/architecture/`, ADRs. |
| Implementation (bottom) | Phase D: build, code, CI configuration. |
| Unit/integration testing (right) | Phase D–E: verify, tests in test suites, CI quality gates. |
| System/acceptance testing (right) | Phase E: verify against requirements, traceability matrices. |
| Traceability | `docs/requirements/traceability/` — requirements ↔ tests ↔ design. |

---

## Agentic SDLC: V-Model + agents + tracking

| Topic | Guidance |
|-------|----------|
| **Test planning** | Agents can draft test plans from requirements; **human** review ensures coverage and domain correctness. |
| **Traceability** | Agents can generate traceability matrices and flag gaps; **human** validates the mapping is meaningful, not just mechanical. |
| **Verification evidence** | Agent-generated test results still need **human** sign-off in regulated contexts. Automated evidence ≠ automated approval. |
| **Early test design** | Agents excel at generating test skeletons during design phases; ensures test thinking happens early. |

---

## V-Model vs other methodologies

| Comparison | Relationship |
|------------|-------------|
| **V-Model → Phased** | V-Model **is** a phased approach with explicit test pairing. Phased delivery may or may not include formal V-level traceability. |
| **V-Model → Agile** | Agile compresses V-levels into each iteration. You can apply V-Model **thinking** (pair each spec level with a test level) inside Sprints without the sequential overhead. |
| **V-Model → Spiral** | Spiral adds risk-driven iteration; V-Model adds formal test pairing. A safety-critical spiral project might use V-Model structure within each spiral's Q3. |

---

## Ceremonies

**Methodology-neutral intent types** (Align, Commit, Sync, …) live in [`ceremonies/ceremony-foundation.md`](ceremonies/ceremony-foundation.md). **V-Model events mapped to those intents:** [`ceremonies/v-model.md`](ceremonies/v-model.md).

---

## Prescriptive deep dive (teams)

Package **[`v-model/README.md`](v-model/README.md)** — foundation fit, roles (systems engineer, test manager, IV&V), ceremonies (design reviews, test readiness, acceptance), process maps with traceability.

---

## Further reading

- [Wikipedia — V-model (software development)](https://en.wikipedia.org/wiki/V-model_(software_development)) — **Overview** of phases and traceability.  
- [Wikipedia — Verification and validation](https://en.wikipedia.org/wiki/Verification_and_validation) — **Foundational** V&V concepts.  
- Companion: [Phased delivery](phased-delivery.md), [Spiral](spiral.md), [Agentic SDLC](agentic-sdlc.md)
