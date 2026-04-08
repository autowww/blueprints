---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# DevOps — roles (prescriptive)

DevOps emphasizes **shared accountability** between development and operations. Roles are defined by **capability**, not by organizational walls.

## 1. SRE (Site Reliability Engineer)

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Production reliability; SLO definition and enforcement; error budget management; automation to reduce toil |
| **Archetypes** | **Assure & ship** (primary), **Build & integrate** (reliability engineering) |
| **Key outputs** | SLO definitions, error budget policies, reliability automation, incident response procedures |

**Prescriptive rule:** SRE is not "Ops renamed." SRE applies **software engineering** to operations problems. If more than 50% of time is toil, invest in automation.

## 2. Platform engineer

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Internal developer platform; CI/CD infrastructure; developer experience; self-service capabilities |
| **Archetypes** | **Build & integrate** (primary), **Assure & ship** (platform reliability) |
| **Key outputs** | CI/CD pipelines, deployment tooling, environment provisioning, developer documentation |

Platform engineers build **products for developers** — the platform should make doing the right thing easy.

## 3. Release engineer

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Release process design; deployment automation; rollback procedures; release coordination |
| **Archetypes** | **Assure & ship** (primary), **Orchestrator** (release coordination) |
| **Key outputs** | Release pipelines, deployment runbooks, rollback procedures, release notes |

May be a dedicated role or a capability distributed across the team.

## 4. Development team (with DevOps accountability)

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Feature development **and** operational readiness; on-call participation; incident response |
| **Archetypes** | **Build & integrate** (primary), **Assure & ship** (shared) |
| **Key outputs** | Production-ready code, monitoring instrumentation, runbooks for their services |

**Prescriptive rule:** "You build it, you run it." Developers participate in on-call rotation and incident response for services they own.

## 5. On-call engineer (rotated)

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | First response to production alerts; initial diagnosis; escalation when needed |
| **Archetypes** | **Assure & ship** (incident response) |
| **Key outputs** | Incident response, initial mitigation, handoff to resolving team |

Rotation among team members; not a permanent role. On-call load should be sustainable (see error budgets).

## 6. Ceremony participation matrix

| Ceremony | SRE | Platform eng | Release eng | Dev team | On-call |
|----------|-----|-------------|-------------|----------|---------|
| Deployment review | R | O | R | R | O |
| Incident response | R | O | O | R (owning team) | R |
| Post-mortem | R | O | O | R | R |
| SLO review | R | O | O | R | O |
| Pipeline retro | O | R | R | R | O |
| On-call handoff | O | — | — | R | R |

## 7. Anti-patterns (by role)

| Anti-pattern | Why it hurts | Fix |
|--------------|--------------|-----|
| **SRE as ticket-taker** for ops requests | Reduces to traditional ops; no reliability engineering | SRE sets SLOs and error budgets; teams self-serve within guardrails |
| **Platform team builds but nobody uses** | Wasted investment; teams work around the platform | Treat platform as a product; measure adoption and developer satisfaction |
| **Developers exempt from on-call** | No production ownership; "throw it over the wall" | Shared on-call with SRE support; sustainable rotation |
| **Release engineer as sole gatekeeper** | Bottleneck; delays deployments | Automate release process; self-service deployments within guardrails |

## 8. Links

- [Ceremonies](ceremonies-prescriptive.md) · [Foundation](foundation-connection.md)
