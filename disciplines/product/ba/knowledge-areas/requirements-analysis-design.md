# Requirements Analysis & Design Definition

Transforms elicited information into **structured requirements** and **design definitions** that the delivery team can implement. This knowledge area is where BA work produces its most tangible outputs — the specifications, models, and design options that drive SDLC phases B and C.

**BABOK alignment:** Knowledge Area 7 (Requirements Analysis and Design Definition).

**Lifecycle mapping:** Primarily **SDLC B–C** (Specify, Design) with inputs from **PDLC P2** (solution validation). The most SDLC-heavy knowledge area.

---

## 1. Tasks

### 1.1 Specify and model requirements

Express requirements in structured formats that reduce ambiguity and enable verification.

| Input | Output |
|-------|--------|
| Confirmed elicitation results, business objectives | Specified requirements (text, models, diagrams) |

**Specification formats:**

| Format | When to Use | Example |
|--------|-------------|---------|
| **User stories** | Agile delivery; incremental features | "As a tenant admin, I can search audit logs by user, so that I can investigate security incidents." |
| **Use cases** | Complex interactions; multiple actors and flows | Detailed steps, preconditions, postconditions, alternate/exception flows |
| **Business rules** | Complex logic; regulatory constraints | "Retention period must be ≥ 90 days for SOC 2-compliant tenants." |
| **Data models** | Data-intensive features; integration | Entity-relationship diagrams, data dictionaries |
| **Process models** | Workflow features; multi-step operations | BPMN diagrams, activity diagrams, swimlane charts |
| **State diagrams** | Lifecycle-driven entities; status workflows | State machine diagrams showing valid transitions |
| **Interface specifications** | API contracts; system integration | OpenAPI specs, message schemas, protocol definitions |
| **Acceptance criteria** | Any methodology; verifiable conditions | Given/When/Then (Gherkin); checklist format |
| **Prototypes** | UX-driven features; complex interactions | Wireframes, clickable prototypes, design mockups |

### 1.2 Verify requirements

Check that requirements are well-formed — complete, consistent, unambiguous, feasible, and testable.

| Input | Output |
|-------|--------|
| Specified requirements | Verified requirements (quality-checked) |

**Verification checklist:**

| Quality | Question | Red Flag |
|---------|----------|----------|
| **Complete** | Does it cover all known scenarios and edge cases? | "TBD", missing error handling, gaps in state transitions |
| **Consistent** | Does it conflict with other requirements? | Two requirements that contradict each other |
| **Unambiguous** | Is there only one way to interpret it? | Vague terms like "fast", "user-friendly", "as needed" |
| **Feasible** | Can the team build this within constraints? | Requirement exceeds technical capability or budget |
| **Testable** | Can you write a test that proves it is implemented? | "System should be intuitive" (not testable) |
| **Traceable** | Can it be linked to a business objective? | Orphan requirement with no business justification |
| **Necessary** | Does it serve a validated business need? | Gold-plating; "nice to have" disguised as "must have" |

### 1.3 Validate requirements

Confirm that the requirements, if implemented, will deliver the intended business value.

| Input | Output |
|-------|--------|
| Verified requirements, business objectives, stakeholder expectations | Validated requirements (value-confirmed) |

**Validation vs verification:**
- **Verification** asks: "Are we specifying this correctly?" (internal quality)
- **Validation** asks: "Are we specifying the right thing?" (external value)

**Validation techniques:**
- Stakeholder reviews and walkthroughs
- Prototype-based validation (does the prototype satisfy the requirement's intent?)
- Traceability analysis (does every requirement trace to a business objective?)
- Test scenario review (do test cases cover the intended user outcomes?)

### 1.4 Define requirements architecture

Organize requirements into a coherent structure that reveals relationships, dependencies, and gaps.

| Input | Output |
|-------|--------|
| Verified and validated requirements | Requirements architecture (organized, categorized, dependency-mapped) |

**Architecture considerations:**
- Group requirements by domain, feature, or user journey
- Identify dependencies between requirement groups
- Identify cross-cutting requirements (security, performance, accessibility)
- Map to the project's requirements structure (milestone → epic → story → task per [`STRUCTURE-PROPOSAL.md`](../../../../docs/requirements/STRUCTURE-PROPOSAL.md))

### 1.5 Define design options

Propose solution approaches that satisfy the requirements and evaluate their trade-offs.

| Input | Output |
|-------|--------|
| Requirements, constraints, organizational context | Design options with trade-off analysis |

**Design option elements:**
- Description of the approach
- How it satisfies each requirement
- Assumptions and constraints
- Estimated effort, cost, and timeline
- Risks and mitigation strategies
- Recommendation with rationale

**SDLC connection:** Design options feed into **SDLC Phase C (Design)** and may trigger **ADRs** (Architecture Decision Records) in `docs/adr/`.

### 1.6 Analyze potential value

Estimate the expected benefits of proposed solutions before committing to build.

| Input | Output |
|-------|--------|
| Design options, business objectives, current state baseline | Value assessment (expected benefits, costs, ROI, payback period) |

**PDLC connection:** Value analysis feeds into **PDLC P3 (Plan & Commit)** — it provides the quantitative backbone for the business case and stage gate (G3) decision.

---

## 2. Techniques commonly used

| Technique | Usage in This Knowledge Area |
|-----------|------------------------------|
| Use case modeling | Specify complex interactions (§1.1) |
| User story writing | Specify incremental features for agile delivery (§1.1) |
| Data modeling | Specify data requirements (entities, relationships, constraints) (§1.1) |
| Process modeling (BPMN) | Specify workflow requirements (§1.1) |
| State modeling | Specify lifecycle-driven behavior (§1.1) |
| Business rules analysis | Specify decision logic and constraints (§1.1) |
| Interface analysis | Specify system integration requirements (§1.1) |
| Prototyping | Validate solution concepts with stakeholders (§1.3) |
| Acceptance criteria definition | Define verifiable conditions (Given/When/Then) (§1.1) |
| Reviews and walkthroughs | Verify and validate requirements (§1.2, §1.3) |
| Decision analysis | Evaluate design options (§1.5) |
| Non-functional requirements analysis | Specify quality attributes (§1.1) |
| Estimation | Size requirements for planning (§1.6) |
| MoSCoW prioritization | Scope design options (§1.5) |

Full technique catalog: [`techniques/README.md`](../techniques/README.md).

---

## 3. Relationship to PDLC and SDLC

| RADD Task | PDLC Mapping | SDLC Mapping |
|-----------|--------------|--------------|
| Specify and model requirements | P2: solution validation uses lightweight specifications | B (Specify): formal specification for delivery |
| Verify requirements | — | B: quality check before development starts |
| Validate requirements | P2: prototype-based validation with users | B–C: stakeholder review of specifications |
| Define requirements architecture | P3: scope structure for initiative | A–B: requirements organized into milestone/epic/story |
| Define design options | P2: feasibility assessment, solution concepts | C (Design): architectural options, ADRs |
| Analyze potential value | P2–P3: business case quantification | — (delivery assumes value is validated) |

### Connection to spec-driven development

This knowledge area produces the core inputs for **spec-driven development** ([`spec-driven-development.md`](../../../../sdlc/methodologies/spec-driven-development.md)):
- Requirements specifications become **spec documents**
- Acceptance criteria become **verifiable intent**
- Design options inform **architectural decisions**

The spec-driven approach adds the delivery mechanism (how specifications drive implementation); RADD adds the analytical rigor (how specifications are created and validated).
