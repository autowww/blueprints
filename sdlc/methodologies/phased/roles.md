# Phased delivery — roles (prescriptive)

## 1. Sponsor / senior responsible owner (SRO)

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Outcomes, funding, escalation resolution; **accepts** stage gate decisions at steering level |
| **Archetypes** | **Sponsor proxy**, **Steer** |
| **Key outputs** | Charter approval, stage **go**, exception approvals for major change |

## 2. Project / program manager (PM)

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Integrated schedule, budget, RAID, stakeholder comms; **does not** own technical truth |
| **Archetypes** | **Orchestrator** |
| **Key outputs** | Status reports, gate packs, dependency management |

## 3. Business analyst (BA)

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Requirements traceability, stakeholder elicitation, UAT coordination (often) |
| **Archetypes** | **Orchestrator**, **Implementer** (documentation) |
| **Key outputs** | SRS, use cases, acceptance criteria packs |

## 4. Tech lead / architect

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Technical integrity, NFRs, build approach; **signs** technical gate criteria where used |
| **Archetypes** | **Quality advocate**, **Implementer** |
| **Key outputs** | Design baselines, ADRs, non-functional test strategy |

## 5. Delivery team (build/test/ops)

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Work package execution per baseline; raise variances early |
| **Archetypes** | **Implementer** (primary), **Quality advocate** (testing) |

## 6. Ceremony participation matrix

| Ceremony | Sponsor | PM | BA | Tech lead | Team |
|----------|---------|----|----|-----------|------|
| Gate review | R (decision) | R (facilitate pack) | R | R | O |
| Weekly status | O | R | O | O | O |
| Design review | O | R | R | R | R |
| Test readiness | O | R | O | R | R |
| UAT | O | R | R | O | O |
| PIR / lessons | O | R | R | R | R |

## 7. Links

- [Ceremonies](ceremonies-prescriptive.md) · [Foundation](foundation-connection.md)
