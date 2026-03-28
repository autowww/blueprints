# Product management — body of knowledge

## Document map

| Section | Contents |
|---------|----------|
| [1. Vision and strategy](#1-vision-and-strategy) | Problem space, opportunity identification, strategic positioning, vision articulation |
| [2. Roadmap management](#2-roadmap-management) | Planning horizons, outcome vs feature roadmaps, alignment cadence |
| [3. Prioritization frameworks](#3-prioritization-frameworks) | RICE, ICE, weighted scoring, opportunity cost, value vs effort |
| [4. Market analysis](#4-market-analysis) | TAM/SAM/SOM, segmentation, market dynamics, regulatory landscape |
| [5. Competitive intelligence](#5-competitive-intelligence) | Positioning maps, feature parity, differentiation, moats, battlecards |
| [6. Business model and pricing](#6-business-model-and-pricing) | Value capture, pricing strategies, unit economics, packaging |
| [7. Product-market fit](#7-product-market-fit) | Signal detection, retention curves, Sean Ellis test, cohort analysis |
| [8. OKRs and success metrics](#8-okrs-and-success-metrics) | North Star, leading/lagging indicators, product health scorecard |
| [9. Discovery cadence](#9-discovery-cadence) | Continuous discovery, dual-track, experiment design, decision velocity |
| [10. Stakeholder communication](#10-stakeholder-communication) | Executive updates, customer advisory, cross-functional alignment |
| [11. Relationship to adjacent disciplines](#11-relationship-to-adjacent-disciplines) | BA, Project Management, UX, Marketing, CS boundaries |

---

## 1. Vision and strategy

### Problem space ownership

Product management begins with the **problem space** — understanding customer pain points, unmet needs, and market opportunities before committing to solutions. The PM owns the answer to: *"Why does this product exist, and for whom?"*

| Activity | Purpose | Key outputs |
|----------|---------|-------------|
| Problem framing | Articulate the core problem in customer language | Problem statement, jobs-to-be-done analysis |
| Opportunity identification | Scan for gaps in the market, technology shifts, regulatory changes | Opportunity assessment, market signals inventory |
| Strategic positioning | Define how the product wins relative to alternatives | Positioning statement, value proposition canvas |
| Vision articulation | Communicate a compelling future state that aligns the team | Product vision document, elevator pitch |

### Vision levels

| Level | Scope | Horizon | Example |
|-------|-------|---------|---------|
| **Company vision** | Organization-wide purpose | 5–10 years | "Make financial planning accessible to everyone" |
| **Product vision** | How this product contributes | 2–3 years | "The fastest path from idea to funded plan" |
| **Product strategy** | How to achieve the vision | 1–2 years | "Win solo founders first, then expand to teams" |

### Strategy frameworks

| Framework | When to use | Core idea |
|-----------|-------------|-----------|
| **Jobs-to-be-done** (JTBD) | Understanding why customers hire/fire products | Customers "hire" products for progress in their lives |
| **Playing to Win** (Lafley & Martin) | Strategic choice cascades | Winning aspiration → Where to play → How to win → Capabilities → Management systems |
| **Wardley Mapping** | Understanding value chain evolution | Map components by visibility and evolution stage to identify strategic moves |
| **Blue Ocean Strategy** | Creating uncontested market space | Eliminate-Reduce-Raise-Create grid against industry norms |

---

## 2. Roadmap management

### Roadmap types

| Type | Structure | Best for | Risk |
|------|-----------|----------|------|
| **Outcome-driven** | Themes → outcomes → key results | Empowered teams; discovery-heavy products | Requires trust and measurement maturity |
| **NOW / NEXT / LATER** | Three horizon buckets without fixed dates | Early-stage or fast-moving products | Lacks commitment signals for stakeholders who need dates |
| **Timeline** | Features on a calendar | Contractual obligations; regulated launches | False precision; creates feature-factory pressure |
| **Hybrid** | Near-term committed (dates), mid-term planned (outcomes), far-term aspirational | Most product organizations at scale | Requires discipline to not treat aspirational items as commitments |

### Roadmap hygiene

- **Review cadence:** Revisit quarterly (strategy alignment) and per-iteration (scope adjustment).
- **Input sources:** Customer feedback, analytics (P5), sales/CS signals, competitive moves, technology shifts, regulatory changes.
- **Stakeholder alignment:** Share roadmap updates proactively; explain **why** items moved, not just **what** changed.
- **Anti-pattern — the feature graveyard:** Items that remain on the roadmap for 3+ quarters without progress should be explicitly killed or re-scoped. Stale items erode roadmap credibility.

### Roadmap and Forge integration

In Forge SDLC, roadmap items decompose into the planning hierarchy:

```
Roadmap Theme
  └── Product Spark (PoC / MVP / Phase)
        └── Forge Iteration(s)
              └── Ore → Ingot → Spark → Charge
```

The PM (Product hat) owns the roadmap-to-Product-Spark decomposition. Engineering hat owns Ingot-to-Spark decomposition.

---

## 3. Prioritization frameworks

| Framework | Factors | Scoring | Best for |
|-----------|---------|---------|----------|
| **RICE** | Reach, Impact, Confidence, Effort | (R × I × C) / E | Data-rich environments; comparing dissimilar items |
| **ICE** | Impact, Confidence, Ease | I × C × E | Quick gut-check prioritization; experiments |
| **Weighted scoring** | Custom criteria with weights | Σ (weight × score) | Multi-stakeholder environments; transparent trade-offs |
| **Opportunity cost** | Value of next-best alternative foregone | Comparative | When capacity is the binding constraint |
| **Value vs Effort** (2×2) | Business value, implementation effort | Quadrant placement | Visual prioritization in workshops |
| **Kano model** | Must-be, One-dimensional, Attractive, Indifferent, Reverse | Survey + classification | Understanding which features drive satisfaction vs dissatisfaction |
| **Cost of Delay** | Revenue/value impact of waiting | Quantified delay cost | When timing matters (regulatory deadlines, competitive windows) |

### Prioritization principles

1. **Outcomes over outputs.** Prioritize toward the outcome you want to move, not toward the feature list.
2. **Explicit trade-offs.** Every "yes" is an implicit "no" to something else — make the trade-off visible.
3. **Confidence-weighted.** High-impact, low-confidence items need discovery before commitment, not a high-priority slot.
4. **Reversibility matters.** Low-reversibility decisions deserve more rigor; high-reversibility ones can move faster.
5. **Re-prioritize on new evidence.** Prioritization is continuous; a quarterly roadmap review that never changes is a red flag.

---

## 4. Market analysis

### Market sizing

| Concept | Definition | Estimation approach |
|---------|------------|---------------------|
| **TAM** (Total Addressable Market) | Total demand if 100% share and no constraints | Top-down (industry reports) or bottom-up (unit economics × universe) |
| **SAM** (Serviceable Addressable Market) | Portion you could serve with current product/model | TAM filtered by geography, segment, channel, and pricing |
| **SOM** (Serviceable Obtainable Market) | Realistic near-term capture | SAM × estimated penetration rate given competitive dynamics |

### Market dynamics

| Factor | What to assess |
|--------|----------------|
| **Growth rate** | Is the market expanding, stable, or contracting? |
| **Concentration** | Few large players (oligopoly) or fragmented? |
| **Switching costs** | How locked-in are customers to alternatives? |
| **Buyer power** | Do buyers have leverage (many alternatives, low switching cost)? |
| **Regulatory environment** | Are regulations creating or destroying opportunity? |
| **Technology shifts** | Are platform changes (AI, mobile, cloud) reshaping the market? |

### Segmentation

Effective segmentation groups potential customers by **observable characteristics that predict behavior**:

| Segmentation type | Examples | When to use |
|-------------------|----------|-------------|
| **Firmographic** | Company size, industry, geography, revenue | B2B; targeting and account-based marketing |
| **Behavioral** | Usage patterns, feature adoption, purchase frequency | Product-led growth; lifecycle marketing |
| **Needs-based** | Jobs-to-be-done, pain intensity, willingness to pay | Strategy and positioning; ICP definition |
| **Technographic** | Tech stack, tools used, infrastructure maturity | Developer tools; integration-dependent products |

---

## 5. Competitive intelligence

### Competitive landscape mapping

| Dimension | What to capture |
|-----------|-----------------|
| **Direct competitors** | Solve the same problem for the same audience |
| **Indirect competitors** | Solve the same problem differently (spreadsheets, manual processes, different category) |
| **Potential competitors** | Adjacent players who could enter (platform expansion, acqui-hires) |

### Positioning map

Plot competitors on two axes that matter to your ICP (e.g. ease-of-use vs depth-of-functionality, price vs specialization). Identify **white space** — underserved quadrants.

### Competitive analysis elements

| Element | Purpose |
|---------|---------|
| Feature comparison matrix | Where you lead, trail, or match |
| Pricing comparison | How your pricing model compares (per-seat, usage, flat, freemium) |
| Strengths / weaknesses | Per competitor; sourced from reviews, win/loss interviews, product trials |
| Differentiation statement | The 1–2 things you do that no competitor matches |
| Moat assessment | Network effects, data advantages, switching costs, brand, regulatory capture |
| Win/loss patterns | Why deals are won or lost; themes by segment and competitor |

### Competitive intelligence cadence

| Frequency | Activity |
|-----------|----------|
| **Continuous** | Monitor competitor releases, pricing changes, funding, key hires |
| **Quarterly** | Update positioning map and feature comparison; share with GTM |
| **Per-launch** | Competitive battlecard for sales; FAQ for support |
| **Annual** | Full landscape reassessment; strategic implications for roadmap |

---

## 6. Business model and pricing

### Business model components

| Component | Key questions |
|-----------|---------------|
| **Value proposition** | What value do you create? For whom? |
| **Revenue model** | How do you capture value? (Subscription, usage, transaction, licensing, marketplace) |
| **Cost structure** | What are the major cost drivers? (Infrastructure, people, acquisition, support) |
| **Unit economics** | CAC, LTV, LTV/CAC ratio, payback period, gross margin |

### Pricing strategies

| Strategy | Description | When to use |
|----------|-------------|-------------|
| **Value-based** | Price reflects perceived value to customer | Differentiated products with measurable ROI |
| **Cost-plus** | Price = cost + margin | Commodity or infrastructure products |
| **Competitive** | Price benchmarked against alternatives | Crowded markets; feature parity |
| **Penetration** | Low price to gain share, increase later | New entrants; network-effect products |
| **Freemium** | Free tier + paid tiers | PLG products; high volume, low marginal cost |
| **Usage-based** | Pay for what you consume | Cloud infrastructure; API products |

### Packaging

Group features into tiers that match segments:

- **Free / trial:** Low barrier; captures leads; limited feature set.
- **Standard:** Core value; majority of customers.
- **Professional / Team:** Collaboration, integrations, volume.
- **Enterprise:** Security, compliance, SLA, custom.

---

## 7. Product-market fit

### What product-market fit means

A product has achieved PMF when the market **pulls** the product — organic growth, high retention, low churn, and customers who would be "very disappointed" if the product disappeared.

### PMF signals

| Signal | Measurement | PMF indicator |
|--------|-------------|---------------|
| **Sean Ellis test** | Survey: "How would you feel if you could no longer use this product?" | ≥40% answer "very disappointed" |
| **Retention curves** | Cohort retention over time | Curve flattens (doesn't go to zero) |
| **Organic growth** | % of new users from word-of-mouth, SEO, or viral loops | Positive and increasing |
| **NPS / CSAT** | Net Promoter Score; Customer Satisfaction Score | NPS > 40; CSAT > 80% |
| **Revenue retention** | Net revenue retention (NRR) | NRR > 100% (expansion > churn) |
| **Usage depth** | Feature adoption breadth; DAU/MAU ratio | Increasing engagement over time |

### Pre-PMF vs post-PMF product management

| Dimension | Pre-PMF | Post-PMF |
|-----------|---------|----------|
| **Primary goal** | Find a repeatable, valuable use case | Scale and optimize |
| **Roadmap style** | Hypothesis-driven; NOW/NEXT/LATER | Outcome-driven with commitments |
| **Prioritization** | Speed of learning over feature completeness | Balance growth, retention, monetization |
| **Metrics** | Engagement, retention, qualitative feedback | Revenue, unit economics, market share |
| **Risk** | Building the wrong thing | Losing focus; feature bloat |

---

## 8. OKRs and success metrics

### Objective and Key Result structure

| Component | What it is | Example |
|-----------|------------|---------|
| **Objective** | Qualitative, inspiring goal | "Make onboarding delightful for new teams" |
| **Key Result** | Quantitative, measurable outcome | "Increase 7-day activation rate from 35% to 55%" |

### Metric layers

| Layer | Definition | Examples |
|-------|------------|---------|
| **North Star** | Single metric that best captures value delivered | Weekly active teams who complete a workflow |
| **Leading indicators** | Predictive; change before the North Star moves | Signup-to-first-action time; onboarding completion % |
| **Lagging indicators** | Confirmed outcomes; harder to influence directly | Revenue; churn rate; NPS |
| **Health metrics** | Guardrails — must not degrade while pursuing OKRs | Performance (P95 latency); error rate; support ticket volume |

### Product health scorecard

Track a balanced set of metrics across dimensions:

| Dimension | Example metrics |
|-----------|-----------------|
| **Acquisition** | New signups, trial starts, pipeline generated |
| **Activation** | Onboarding completion, first value moment reached |
| **Engagement** | DAU/MAU, feature adoption breadth, session depth |
| **Retention** | Cohort retention, logo churn, revenue churn |
| **Revenue** | MRR/ARR, expansion revenue, NRR, ARPU |
| **Satisfaction** | NPS, CSAT, support ticket sentiment |

---

## 9. Discovery cadence

### Continuous discovery habits

Product discovery should be **continuous, not episodic**. Key practices (per Teresa Torres):

| Practice | Frequency | Purpose |
|----------|-----------|---------|
| **Customer interviews** | Weekly (at least) | Maintain empathy; surface new opportunities |
| **Opportunity mapping** | Per cycle | Connect customer needs to outcomes via Opportunity Solution Trees |
| **Assumption testing** | Per decision | Identify riskiest assumptions; design small experiments |
| **Story mapping** | Per initiative | Visualize the user journey; identify scope for slices |

### Dual-track integration

| Track | Focus | Cadence | Output |
|-------|-------|---------|--------|
| **Discovery** | Understand problems; validate solutions | Continuous; 1–2 cycles ahead of delivery | Validated opportunities, experiment results, prototypes |
| **Delivery** | Build and ship validated solutions | Iteration-based (Forge: 1–2 week cycles) | Shippable increments |

Discovery feeds delivery with **validated Ore** (Forge terminology). Delivery feeds discovery with **usage data and customer feedback**.

### Experiment design

| Element | Description |
|---------|-------------|
| **Hypothesis** | If [action], then [outcome], because [rationale] |
| **Riskiest assumption** | The belief that, if wrong, invalidates the hypothesis |
| **Test method** | Prototype test, fake door, concierge, A/B test, survey, spike |
| **Success criteria** | Quantitative threshold for proceeding |
| **Decision** | Persevere, pivot, or kill — documented in experiment log |

---

## 10. Stakeholder communication

### Communication cadence

| Audience | Frequency | Format | Content |
|----------|-----------|--------|---------|
| **Executive / board** | Monthly or quarterly | Slide deck; written brief | Strategy update, OKR progress, key risks, resource asks |
| **Cross-functional team** | Weekly or per-iteration | Stand-up; written update | Current priorities, blockers, upcoming decisions |
| **Engineering** | Daily / per-iteration | Planning, refinement ceremonies | Context behind priorities; trade-off rationale |
| **Sales / CS** | Per-launch; quarterly roadmap | Enablement docs; roadmap preview | What's coming, competitive positioning, customer-facing messaging |
| **Customers (advisory)** | Quarterly | Advisory board; beta programs | Feedback on direction; early access; co-creation |

### Communication principles

1. **Lead with why.** Explain the outcome the team is pursuing before listing what will be built.
2. **Show trade-offs.** When stakeholders ask "why not X?", share the prioritization rationale, not just "it's not on the roadmap."
3. **Update proactively.** Stakeholders should not be surprised by changes; communicate shifts before they ask.
4. **Separate commitment from aspiration.** Clearly label what is committed vs what is being explored.

---

## 11. Relationship to adjacent disciplines

| Discipline | Boundary |
|------------|----------|
| **Business Analysis** | PM defines the **problem space, market opportunity, and strategic direction**. BA defines the **detailed requirements, elicitation protocols, and solution validation**. PM asks "what and why"; BA asks "what exactly and how to prove it." In small teams, one person fills both roles. In larger organizations, they are distinct but tightly coupled — PM feeds BA with validated problems and priorities; BA feeds PM with specification quality and stakeholder analysis. |
| **Project Management (Governance)** | PM defines **what to build and why** (product priorities, roadmap, outcomes). Project Management governs **how to deliver it** (schedule, budget, scope, risk, resource allocation). Product decides priorities; Project ensures they ship within constraints. Confusion between these roles is a common anti-pattern — see [`PM-SDLC-PDLC-BRIDGE.md`](../../governance/pm/PM-SDLC-PDLC-BRIDGE.md) for the delineation. |
| **UX / UI Design** | PM and UX form the core of the "product trio" (with Engineering). PM owns the **value proposition and market positioning**; UX owns the **experience design and usability**. They collaborate most intensely during P1–P2 discovery and SDLC phases A–C. |
| **Marketing** | PM defines **ICP, positioning, and competitive narrative**; Marketing operationalizes **GTM, channels, campaigns, and growth loops**. PM owns "why this product wins"; Marketing owns "how the market knows." |
| **Customer Success** | PM uses CS signals (**churn patterns, health scores, support themes**) as inputs for P5 decisions. CS uses PM's **roadmap and vision** to set customer expectations and plan proactive outreach. |
| **Engineering** | PM defines **what and why**; Engineering defines **how and when**. The Product hat in Forge ensures engineering decisions stay aligned with product strategy; the Engineering hat ensures product decisions respect technical reality. |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`PRODMGMT-SDLC-PDLC-BRIDGE.md`](PRODMGMT-SDLC-PDLC-BRIDGE.md) | How product management maps to both lifecycles |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, stage gates |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD |
| [`BA-SDLC-PDLC-BRIDGE.md`](../ba/BA-SDLC-PDLC-BRIDGE.md) | How BA relates to both lifecycles (sibling discipline) |
| [`PM-SDLC-PDLC-BRIDGE.md`](../../governance/pm/PM-SDLC-PDLC-BRIDGE.md) | How Project Management relates (governance counterpart) |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | Cross-lifecycle bridge |
| [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) | Delivery role archetypes |

---

*Keep project-specific product management artifacts (vision, roadmap, OKRs, metrics) in `docs/product/`, not in this file.*
