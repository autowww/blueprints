# V-Model — roles (prescriptive)

The V-Model defines roles around **verification levels** and **traceability**. Teams are typically structured by engineering discipline with clear handoff points between development and test.

## 1. Systems engineer

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Requirements decomposition, system-level design, interface specifications |
| **Archetypes** | **Implementer** (architecture), **Quality advocate** (requirements quality) |
| **Key outputs** | System requirements spec, system design document, interface control documents |

Owns the top-left of the V; their outputs define what system testing will verify.

## 2. Test manager

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Test strategy, test plans per V-level, test resource coordination, test evidence packages |
| **Archetypes** | **Quality advocate** (primary), **Orchestrator** (test coordination) |
| **Key outputs** | Test plans (unit, integration, system, acceptance), traceability matrix, test reports |

**Prescriptive rule:** Test manager should be engaged **from requirements phase** to ensure testability is designed in from the start.

## 3. IV&V lead (independent verification & validation)

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Independent assessment that development and test processes are sound; common in safety-critical systems |
| **Archetypes** | **Quality advocate** (independent from Build) |
| **Key outputs** | IV&V reports, process audit findings, independent test results |

Not always a separate role; required by some regulatory standards (DO-178C, IEC 62304).

## 4. Development team

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Detailed design, implementation, unit testing per design specifications |
| **Archetypes** | **Implementer** (primary), **Quality advocate** (unit-level testing) |
| **Key outputs** | Code, unit tests, detailed design documents |

## 5. Project manager

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Schedule, resources, gate coordination, stakeholder communication |
| **Archetypes** | **Orchestrator** |
| **Key outputs** | Project plan, gate evidence packages, status reports |

## 6. Sponsor / customer

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Defining needs (top-left), accepting the system (top-right), funding decisions |
| **Archetypes** | **Sponsor proxy**, **Steer** |
| **Key outputs** | Acceptance criteria, acceptance test sign-off, go/no-go decisions |

## 7. Ceremony participation matrix

| Ceremony | Sys engineer | Test mgr | IV&V | Dev team | PM | Sponsor |
|----------|-------------|----------|------|----------|----|---------|
| Requirements review | R | R | O | O | R | R |
| Design review | R | R | O | R | O | O |
| Test plan review | O | R | R | O | R | O |
| Test readiness review | O | R | R | R | R | O |
| Test result review | R | R | R | O | R | O |
| Acceptance review | R | R | O | O | R | R |

## 8. Links

- [Ceremonies](ceremonies-prescriptive.md) · [Foundation](foundation-connection.md)
