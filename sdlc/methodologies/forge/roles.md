# Forge — roles (prescriptive)

Forge keeps standard role names and uses the blueprint's **Owner / Implementer** model. It adds a **hat-switching protocol** for teams where one person holds multiple perspectives and **Bellows** as challenge functions (not roles).

## 0. Forge team vs sub-accountabilities

A Forge team consists of people who **own**, **implement**, **challenge**, and **govern** work. In small teams these accountabilities overlap. Forge makes the overlap explicit through **hats** rather than pretending one person is not making trade-offs between perspectives.

## 0.1 Map to this blueprint (foundation)

| Foundation element | Product hat | Engineering hat | Challenge hat | Governance hat |
|--------------------|-------------|-----------------|---------------|----------------|
| **Phases A–F** | Strong in **A–B** (discover/specify) | Strong in **C–E** (design/build/verify) | Cross-cutting (all phases) | Strong in **E–F** (verify/release) |
| **Tracking spine** | Owns **value ordering** and **acceptance** | **Links work** to Ingots/Sparks; meets **DoD** | Reviews for blind spots | Ensures **traceability** and **evidence** |
| **Ceremony intents C1–C6** | **C1/C2** in refinement & planning | **C2–C4** execution and review | **C1/C4** challenge at decision points | **C6** Assay Gate steward |
| **Archetypes** | Sponsor proxy, Orchestrator | Implementer, Quality advocate | Quality advocate (cross-cutting) | Orchestrator, Quality advocate |

## 0.2 Bellows: challenge functions, not roles

Bellows are **not** team roles. They are discipline-specific challenge agents (AI or human) that pressure-test work from particular perspectives. A Bellows challenge does not own delivery; it strengthens thinking.

| Bellows family | Disciplines covered | When most active |
|----------------|--------------------|--------------------|
| **Engineering** | SE, Architecture, DevOps, Testing, Frontend, Mobile, Embedded/IoT | Design, build, verify |
| **Data** | Big Data, Data Science | Specify, design, verify |
| **Product** | BA, UX, Marketing, Customer Success | Discover, specify, review |
| **Governance** | PM | Planning, review, release |
| **Cross-cutting** | Security, Compliance | All phases (shift-left emphasis) |

Each Bellows references its discipline's knowledge base and bridge document in [`../../disciplines/`](../../../disciplines/README.md).

## 1. The four hats

### Product hat

| Aspect | Prescriptive guidance |
|--------|----------------------|
| **Accountable for** | Maximizing value from the team's work; Ore intake quality; Ingot acceptance |
| **Key question** | *Is this the right thing to build?* |
| **Typical archetype** | Sponsor proxy, Orchestrator |
| **Outputs** | Ore items with context, ordered Ingots, acceptance decisions, Product Spark definitions |

### Engineering hat

| Aspect | Prescriptive guidance |
|--------|----------------------|
| **Accountable for** | Technical quality, implementation correctness, sustainable architecture |
| **Key question** | *Is this built well?* |
| **Typical archetype** | Implementer, Quality advocate |
| **Outputs** | Completed Sparks meeting DoD, PRs, technical ADRs, test coverage |

### Challenge hat

| Aspect | Prescriptive guidance |
|--------|----------------------|
| **Accountable for** | Surfacing blind spots, risks, and alternatives before costly commitments |
| **Key question** | *What are we missing?* |
| **Typical archetype** | Quality advocate (cross-cutting) |
| **Outputs** | Bellows challenge results, risk flags, alternative proposals, evidence requests |

### Governance hat

| Aspect | Prescriptive guidance |
|--------|----------------------|
| **Accountable for** | Release evidence, process discipline, decision traceability |
| **Key question** | *Can we prove this is ready?* |
| **Typical archetype** | Orchestrator, Quality advocate |
| **Outputs** | Assay Gate checklists, Ember Log stewardship, release decisions, compliance evidence |

## 2. Hat-switching protocol

In smaller teams (especially solo practitioners), one person holds multiple hats. Forge makes this explicit:

1. **Declare the hat.** Before a decision, state which perspective you are prioritizing. In conversation or commits, prefix with the hat: `[Product]`, `[Engineering]`, `[Challenge]`, `[Governance]`.
2. **Separate the concerns.** Do not mix "should we build this?" (Product) with "how should we build this?" (Engineering) without marking the transition.
3. **Use Bellows for hats you are not wearing.** When deep in Engineering, invoke a Bellows agent for the Product or Challenge perspective you might neglect.
4. **Log hat-switching decisions.** When a hat-switch changes direction (e.g., Engineering hat overrules Product hat on feasibility), capture the trade-off in the Ember Log.

## 3. Scaling model

| Scale | Team size | Hat distribution | Bellows configuration |
|-------|-----------|------------------|-----------------------|
| **Solo** | 1 | One person, all hats, explicit switching | AI Bellows for all uncovered perspectives |
| **Small team** | 2–5 | Hats shared; designate primary per person | AI Bellows + peer challenge |
| **Team** | 5–12 | Dedicated hat holders possible; Bellows disciplines assigned | Mix of AI and specialist human Bellows |
| **Multi-team** | 12+ | Full role separation; cross-team Bellows | Dedicated challenge roles + AI augmentation |

**Scaling rule:** add formality only when the cost of a mistake exceeds the cost of the ceremony.

## 4. Event participation matrix

Legend: **R** = required · **O** = optional · **—** = not expected

| Ceremony | Product hat | Engineering hat | Challenge hat | Governance hat |
|----------|-------------|-----------------|---------------|----------------|
| **Refinement** (Ore → Ingot) | R | R | O (Bellows) | O |
| **Planning** (Ingot → Sparks) | R | R | O (Bellows) | O |
| **Daily sync** (Charge) | O | R | — | — |
| **Review** (evidence) | R | R | R (Bellows) | R |
| **Assay Gate** (release) | R | R | O | R |
| **Retro** (learning) | R | R | O | R |

## 5. Interface with standard roles

| Standard role | Forge hat mapping |
|---------------|-------------------|
| **Product Owner / PM** | Product hat (primary); Governance hat (release acceptance) |
| **Engineering Lead / Architect** | Engineering hat (primary); Challenge hat (technical review) |
| **Scrum Master / Delivery Lead** | Governance hat (primary); facilitates ceremonies |
| **Developers / Engineers** | Engineering hat (primary) |
| **QA** | Challenge hat (testing Bellows); Governance hat (Assay Gate evidence) |
| **BA / Analyst** | Product hat (Ore intake, Ingot refinement); Challenge hat (BA Bellows) |

## 6. Anti-patterns (by hat)

| Anti-pattern | Why it hurts | Fix |
|--------------|--------------|-----|
| Never declaring hat switches | Conflated decisions; no audit trail | Explicit `[Hat]` prefix; Ember Log |
| Challenge hat dominates every decision | Analysis paralysis; Bellows as bureaucracy | Time-box Bellows; use at decision points only |
| Governance hat skipped for speed | Undocumented decisions; release surprises | Assay Gate is non-negotiable; adjust scope instead |
| Solo developer ignores all but Engineering | Product/challenge blind spots compound | Schedule Bellows invocations; daily hat rotation |

## 7. Agentic SDLC (same accountabilities)

AI agents (including Bellows) **do not** replace human accountability for Ore acceptance, Spark quality, release decisions, or Ember Log integrity. Agent output is treated like any other contribution: traceable, reviewed, covered by DoD. See [agentic-sdlc.md](../agentic-sdlc.md).

## 8. Links

- [Foundation connection](foundation-connection.md) · [Ceremonies](ceremonies-prescriptive.md) · [roles-archetypes.md](../roles-archetypes.md)
- [Bellows contract](bellows/BELLOWS-CONTRACT.md) · [Disciplines hub](../../../disciplines/README.md)
