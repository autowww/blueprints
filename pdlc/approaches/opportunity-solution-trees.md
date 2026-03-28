# Opportunity Solution Trees (OST)

## What it is

The **Opportunity Solution Tree** is a visual framework created by Teresa Torres (2016) that structures continuous product discovery by connecting four levels:

1. **Outcome** — the measurable result the team wants to achieve
2. **Opportunities** — unmet customer needs, pain points, or desires that could drive that outcome
3. **Solutions** — product ideas or features that address specific opportunities
4. **Experiments** — tests that validate whether a solution actually works

The OST makes discovery **visible**, **collaborative**, and **traceable** — the team can always see **why** they are building something (which opportunity it addresses) and **what evidence** supports it (which experiments validated it).

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [Teresa Torres — Opportunity Solution Trees](https://www.producttalk.org/2023/12/opportunity-solution-trees/) | **Canonical source** from the framework's creator — definition, visual examples, common mistakes, and how OSTs fit into continuous discovery. |
| [Teresa Torres — Continuous Discovery Habits](https://www.producttalk.org/2021/08/continuous-discovery-habits/) | **Book and framework** that embeds OSTs into a broader weekly discovery practice — interviews, assumption mapping, experiment design. |
| [Product School — OST Guide](https://productschool.com/blog/product-fundamentals/opportunity-solution-tree) | **Practitioner overview** with worked examples and tips for facilitating OST sessions with product teams. |

---

## Core structure

### The tree

```blueprint-diagram
key: linear
alt: Diagram
```

### Layer definitions

| Layer | Question it answers | Source of content | PDLC phase |
|-------|-------------------|-------------------|------------|
| **Outcome** | What measurable result do we want? | Product strategy, OKRs, P3 success metrics | P3 Strategize |
| **Opportunities** | What customer needs could drive that outcome? | User interviews, analytics, support data (P1 evidence) | P1 Discover Problem |
| **Solutions** | What could we build to address this opportunity? | Ideation, design thinking, competitive analysis | P2 Validate Solution |
| **Experiments** | How do we know this solution works? | Lean Startup experiments, usability tests, A/B tests | P2 Validate Solution |

### How the tree grows

1. **Start with the outcome** — a product or team OKR, business metric, or user behavior target. Not a feature request.
2. **Discover opportunities** — through user interviews, analytics, support data. Each opportunity is a **customer need**, not a solution in disguise. "Users can't find reports" is an opportunity. "Add a search bar" is a solution.
3. **Generate solutions** — for each opportunity, brainstorm multiple solutions. Resist the urge to commit to the first idea.
4. **Design experiments** — for each promising solution, design the **smallest test** that would validate or invalidate the key assumption. See [Lean Startup — Types of MVPs](lean-startup.md).
5. **Update continuously** — the tree is a living artifact. New interviews add opportunities. Experiment results validate or invalidate solutions. Failed experiments are kept (crossed out) as organizational memory.

---

## Mapping to PDLC phases

| PDLC phase | OST layer(s) active | Activity |
|------------|---------------------|----------|
| **P1 Discover Problem** | **Opportunities** | User interviews and data analysis populate the opportunity branches |
| **P2 Validate Solution** | **Solutions** + **Experiments** | Ideation generates solution branches; experiments validate them |
| **P3 Strategize** | **Outcome** | Strategic goals define the tree's root outcome |
| **SDLC A–F** | **Solutions** (validated) | Validated solutions with successful experiments become backlog items |
| **P5 Grow** | All layers | Usage data reveals new opportunities; A/B tests are experiments; iteration updates solutions |

### OST as the discovery backlog

In Dual-Track Agile teams, the OST serves as the **discovery backlog** — analogous to how the product backlog serves the delivery track:

| Delivery track | Discovery track (OST) |
|---------------|----------------------|
| Product backlog (stories) | Solution branches (ideas to validate) |
| Sprint/iteration goal | Experiment goal (what to learn this week) |
| Definition of Done | Validation criteria (what evidence is "enough") |
| Shipped increment | Validated or invalidated hypothesis |

---

## Rules of thumb

| Principle | Guidance |
|-----------|----------|
| **Outcomes, not outputs** | The tree root is a **measurable outcome** ("increase D7 retention by 15pp"), never a feature ("build a wizard"). |
| **Opportunities are needs, not solutions** | "Users struggle to configure integrations" is an opportunity. "Add a setup wizard" is a solution. Keep them separate. |
| **Multiple solutions per opportunity** | Generate at least 3 solution ideas per opportunity before committing. Resist convergence pressure. |
| **Smallest viable experiment** | Test the **riskiest assumption** first with the **cheapest experiment**. Code is expensive; prototypes and interviews are cheap. |
| **Show your work** | Keep invalidated solutions visible (crossed out) on the tree. They are organizational learning, not failures. |
| **One outcome at a time** | A product trio should focus on one outcome (one tree) per quarter or strategic cycle. Multiple trees fragment attention. |

---

## Anti-patterns

| Anti-pattern | Fix |
|-------------|-----|
| **Feature tree** | Solutions masquerading as opportunities ("Add dark mode" at the opportunity level). Reframe as user needs ("Users experience eye strain in low-light environments"). |
| **Giant tree, no experiments** | Tree is beautifully mapped but no experiments are running. The tree is not the work — experiments are the work. Run at least one experiment per week. |
| **Solution-first thinking** | Team starts with a solution and retrofits an opportunity. Start with outcomes and interviews. |
| **Static tree** | Tree created once and never updated. The OST is a **living artifact** — update it after every interview, experiment, and analytics review. |
| **Solo PM tree** | PM builds the tree alone. The product trio (PM + Designer + Tech Lead) should co-own the tree. Different perspectives surface different opportunities and solutions. |

---

## Further reading

- [Dual-Track Agile](dual-track-agile.md) — OST as the discovery track's organizing structure
- [Lean Startup](lean-startup.md) — Experiment design methods for the experiment layer
- [Design Thinking](design-thinking.md) — Empathize and Define modes populate the opportunity layer
- [PDLC.md — P1 and P2](../PDLC.md) — Phase definitions that OST operationalizes
