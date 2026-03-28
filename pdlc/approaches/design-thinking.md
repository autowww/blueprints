# Design Thinking

## What it is

**Design Thinking** is a human-centered approach to innovation that uses methods from design practice to match people's needs with what is technologically feasible and commercially viable. It is **not** a step-by-step process but a set of **mindsets and methods** that can be applied at different PDLC stages.

The most widely used model is the **Double Diamond** (British Design Council, 2004), which describes two phases of divergent and convergent thinking:

- **Diamond 1 — Problem space:** Diverge (explore many problems) → Converge (define the right problem)
- **Diamond 2 — Solution space:** Diverge (explore many solutions) → Converge (validate the right solution)

Design Thinking addresses **desirability risk** — "Do people actually need and want this?" — which is the most common cause of product failure.

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [IDEO — Design Thinking](https://designthinking.ideo.com/) | **Origin framework** from IDEO — the firm that popularized Design Thinking. Defines the five modes (Empathize, Define, Ideate, Prototype, Test) and human-centered design principles. |
| [Stanford d.school](https://dschool.stanford.edu/) | **Academic anchor** for Design Thinking education — process guides, teaching materials, and the "bootcamp bootleg" (free methodology cards). |
| [British Design Council — Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond/) | **Double Diamond** model — the canonical visualization of diverge/converge across problem and solution spaces. |
| [Nielsen Norman Group — Design Thinking](https://www.nngroup.com/articles/design-thinking/) | **Practitioner summary** with evidence-based guidance on when Design Thinking works (and when it doesn't). |

---

## Core structure

### The Double Diamond

```blueprint-diagram
key: swimlane
alt: Diagram
```

### Five modes (IDEO / Stanford d.school)

| Mode | Diamond | Activity | Output |
|------|---------|----------|--------|
| **Empathize** | D1 — Diverge | Observe and engage with users; understand their experiences, needs, and motivations | Empathy maps, interview notes, observation logs |
| **Define** | D1 — Converge | Synthesize research into a clear problem statement (point of view) | Problem statement, "How Might We" questions, persona refinements |
| **Ideate** | D2 — Diverge | Generate a broad range of solution ideas; defer judgment; build on ideas | Idea clusters, sketches, concept cards, prioritization matrix |
| **Prototype** | D2 — Converge (early) | Build quick, cheap representations of ideas to test with users | Paper prototypes, wireframes, clickable mocks, concierge MVPs |
| **Test** | D2 — Converge (late) | Put prototypes in front of users; gather feedback; refine or pivot | Usability test results, validation evidence, iteration notes |

---

## Mapping to PDLC phases

Design Thinking maps most strongly to PDLC P1–P2 (pre-build discovery and validation):

| PDLC phase | Design Thinking mode(s) | Activities |
|------------|------------------------|------------|
| **P1 Discover Problem** | **Empathize** + **Define** | User research, empathy mapping, problem framing, "How Might We" synthesis |
| **P2 Validate Solution** | **Ideate** + **Prototype** + **Test** | Brainstorming, rapid prototyping, usability testing, concept validation |
| **P3 Strategize** | Outputs inform strategy | Validated problem statement and solution concept feed vision, OKRs, business case |
| **SDLC C Design** | **Prototype** (refined) | Higher-fidelity design artifacts inform engineering design phase |
| **P5 Grow** | **Empathize** + **Test** (continuous) | Post-launch user research and testing for iteration |

### When to use Design Thinking

| Situation | Fit |
|-----------|-----|
| **New product / new market** | Strong — high uncertainty about user needs demands empathy-first approach |
| **Complex problem, unclear solution** | Strong — diverge-converge helps explore before committing |
| **Feature improvement on mature product** | Moderate — Empathize mode verifies assumptions; faster iteration than full Double Diamond |
| **Technical / infrastructure work** | Weak — users are internal; needs are more knowable; skip to specification |
| **Bug fix / maintenance** | Skip — problem is already defined by the bug itself |

---

## Anti-patterns

| Anti-pattern | Fix |
|-------------|-----|
| **Design Thinking as a workshop, not a practice** | A one-day "Design Thinking workshop" is not product discovery. Embed the modes into weekly team practice. |
| **Skipping Empathize** | Jumping to solutions without understanding users is the #1 failure mode. Require evidence from real users, not stakeholder assumptions. |
| **Diverge without converge** | Infinite ideation without commitment. Set clear converge criteria: "By Friday we choose 3 ideas to prototype." |
| **Prototype fidelity too high** | Low-fi prototypes (paper, wireframes) are faster and cheaper for early testing. Save high-fi for validation, not exploration. |
| **Design Thinking without delivery** | Beautiful insights and prototypes that never become products. Bridge to SDLC by setting clear gates (PDLC G2) after Test mode. |

---

## Further reading

- [Lean Startup](lean-startup.md) — Complementary: adds business viability testing to Design Thinking's desirability focus
- [Opportunity Solution Trees](opportunity-solution-trees.md) — Visual structure for organizing the Ideate mode
- [PDLC.md — P1 and P2](../PDLC.md) — How these modes map to PDLC phases with exit criteria
- [PDLC-SDLC Bridge](../PDLC-SDLC-BRIDGE.md) — Full lifecycle context
