# Marketing ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **Marketing** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **Marketing** — "How do we **acquire, engage, and retain** users in a measurable, compliant way?"

Marketing is **PDLC-heavy**: positioning and GTM crystallize in **P3**, launch comms and channel readiness peak in **P4**, and growth, retention, and monetization experiments dominate **P5**. SDLC supplies the **implementation substrate** — analytics instrumentation in **Build**, SEO and landing surfaces in **Frontend**, and reliable **experiment / flag / pipeline** infrastructure often co-owned with **DevOps**.

**Canonical sources:** [`MARKETING.md`](MARKETING.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md) · [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; how Marketing relates to PDLC and SDLC |
| [Comparison table](#comparison-table) | Marketing vs SDLC vs PDLC — scope, ownership, metrics, risks |
| [When one is missing](#when-one-is-missing) | Consequences when Marketing, SDLC, or PDLC are practiced in isolation |
| [Marketing across the lifecycle](#marketing-across-the-lifecycle) | Activities and outputs mapped to PDLC P1–P6 and SDLC A–F |
| [Role mapping](#role-mapping) | Who owns Marketing work at each phase; SDLC roles and archetypes |
| [Artifact flow](#artifact-flow) | Handoffs between Marketing, SDLC, and PDLC |
| [Calibration](#calibration) | When to invest more or less in marketing depth by initiative and context |
| [Anti-patterns](#anti-patterns) | Common failures when Marketing is siloed or decoupled from product reality |
| [Worked example](#worked-example) | End-to-end scenario — launching a B2B SaaS feature |
| [Related reading](#related-reading) | Authoritative docs in this package and sibling lifecycles |

---

## Comparison table

| Dimension | Marketing | SDLC | PDLC |
|-----------|-----------|------|------|
| **Core question** | How do we acquire, engage, and retain users? | How do we build this correctly? | Should we build this; does it create the right outcomes? |
| **Scope** | STP, positioning, channels, content, GTM, lifecycle campaigns, analytics & attribution, pricing/packaging narrative, DevRel where relevant | Requirements → design → implementation → verification → release (**A** Discover through **F** Release) | Problem discovery → validation → strategy → launch → growth → sunset (**P1**–**P6**) |
| **Primary owner** | Marketing / growth / product marketing — often partners **PM** and **GTM**; DevRel may own technical top-of-funnel | Delivery team; **Owner** and **Implementer** per [`SDLC.md`](../../../sdlc/SDLC.md) | Product manager / product trio; GTM where relevant |
| **Timeline** | Always-on channels plus campaign spikes; long-running SEO and brand equity | Sprint, iteration, or release train cadence | Product lifetime (months to years) |
| **Success metric** | CAC, LTV, funnel conversion, retention cohorts, pipeline (SLG), product-qualified leads (PLG), share of voice, incrementality where measured | Velocity, defect escape rate, CI/CD gate pass rate, quality attributes in DoD | Adoption, retention, revenue, NPS, outcome KPIs |
| **Key artifacts** | ICP, messaging hierarchy, campaign briefs, editorial calendar, martech specs (events, UTMs), launch checklist, pricing pages | Specs, designs, code, tests, release notes | Research synthesis, experiments, strategy, launch and growth metrics |
| **Risk focus** | Wasted spend, misleading claims, privacy violations, brand–product mismatch, channel dependency | Technical risk — correctness, performance, security | Market and outcome risk — desirability, viability, fit |
| **Failure mode** | Traffic without activation; hype without retention; compliant analytics theater without decisions | Late or low-quality delivery; tracking broken in production | Right product with invisible launch; or launch noise without strategy |

---

## When one is missing

| Scenario | What happens |
|----------|-------------|
| **Marketing without PDLC** | Campaigns optimize vanity metrics for a product that lacks fit — high CAC, weak retention, churn blamed on “bad leads.” |
| **Marketing without SDLC** | Strategy decks and UTMs exist, but **events, SEO, and experiment hooks** ship late or wrong — attribution and learning loops break. |
| **PDLC without Marketing** | Strong discovery and build, but weak **positioning, launch rhythm, and distribution** — adoption lags despite product quality. |
| **SDLC without Marketing input** | Engineering ships technically correct pages and events that **do not match naming, consent, or SEO** needs — rework and data distrust. |
| **PDLC + SDLC, weak Marketing** | Product-market fit may exist but **growth is accidental**; expansion and category narrative are under-invested. |
| **All three practiced** | Strategy chooses the right bets; delivery implements measurable, compliant experiences; marketing **amplifies real value** and feeds learning back to P1–P2 and P5. |

---

## Marketing across the lifecycle

| Phase | Marketing role | Key activities | Outputs |
|-------|----------------|----------------|---------|
| **P1 Discover** | **Market listener** | Category and competitor scans, search demand signals, community listening, early message tests | Hypothesis briefs, search insight summaries, ICP draft inputs |
| **P2 Validate** | **Experiment partner** | Landing page smoke tests, waitlist campaigns, pricing sensitivity probes (ethical, non-deceptive) | Channel feasibility readout, early funnel baselines |
| **P3 Plan & Commit** | **Positioning owner** | STP, messaging hierarchy, GTM motion (PLG vs SLG), packaging narrative, martech & measurement plan | Positioning doc, ICP, launch themes, analytics / UTM standard |
| **A Discover** | **Requirements partner** | Surface SEO, tracking, and consent constraints as discovery inputs | Marketing NFRs — e.g. crawlability, event taxonomy needs |
| **B Specify** | **Spec reviewer** | Event names, attribution fields, landing URLs, email triggers, CMS requirements | Marketing acceptance criteria in specs / tickets |
| **C Design** | **Experience aligner** | Landing and onboarding **copy, CTA, and proof** aligned with UX flows | Creative specs, content-model needs |
| **D Build** | **Instrumentation partner** | Implement tags, server-side events, structured data, email templates, marketing site changes | Working pixels/events, CMS content, transactional templates |
| **E Verify** | **QA stakeholder** | Validate tracking in staging, link checks, consent behavior, SEO regressions | Sign-off checklist, defect tickets for analytics/SEO |
| **F Release** | **Launch executor** | Coordinated comms — email, paid, social, partners; sales enablement | Campaign live, monitoring dashboard, retrospective slot |
| **P4 Launch** | **GTM lead** | Launch narrative, PR/analyst, paid/organic burst, community, success/support briefing | Launch report, share of voice, pipeline or signup attribution |
| **P5 Grow** | **Growth operator** | Lifecycle email, retention offers, referral programs, SEO expansion, experiment backlog with Product | Cohort analyses, experiment outcomes, CAC/LTV views |
| **P6 Sunset** | **Comms partner** | Sunset messaging, migration offers, archive SEO (redirect strategy), stakeholder comms | Sunset comms plan, redirect map, knowledge-base updates |

---

## Role mapping

Who carries Marketing accountability at each lifecycle step, alongside PDLC and SDLC. In small teams, **PM** or a **founder** may own positioning and campaigns; in larger orgs, **product marketing**, **growth**, and **demand gen** split the work. SDLC uses **Owner** and **Implementer**; archetypes follow [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md).

| Phase(s) | Marketing stance | PDLC accountability (typical) | SDLC accountability | Archetype |
|----------|------------------|------------------------------|---------------------|-----------|
| **P1–P2** | **Research + experiment** | PM, research, discovery trio | — (upstream of formal SDLC) | Demand & value |
| **P3** | **Positioning + GTM strategy** | PM, strategy, sales leadership | Owner (priorities, scope); Implementer consulted on feasibility | Steer & govern; Demand & value |
| **A–B** | **Spec + NFR partner** | — | Owner (acceptance); Implementer (technical specs, event taxonomy) | Build & integrate |
| **C–D** | **Build partner** | — | Implementer (frontend, APIs for email/billing, tag infra) | Build & integrate |
| **E** | **QA + validation** | — | Implementer fixes; Assure & ship interprets release gates | Assure & ship |
| **F** | **Launch comms** | GTM, PM | Implementer executes release; Owner go/no-go | Assure & ship; Demand & value |
| **P4** | **Launch lead** | PM, GTM | Overlaps **F** — production + comms alignment | Demand & value |
| **P5** | **Growth + retention** | PM, analytics | Iteration **A**–**F** for product + growth bets | Flow & improvement |
| **P6** | **Sunset comms** | PM, legal | Implementer redirects, data export messaging | Steer & govern |

---

## Artifact flow

### PDLC / SDLC → Marketing (inputs)

| Source | Marketing usage |
|--------|-----------------|
| Research synthesis (**P1**–**P2**) | Personas, pains, and language for messaging |
| Strategy and roadmap (**P3**) | Launch themes, tier changes, competitive framing |
| UX flows and copy (**B**–**C**) | Honest claims, onboarding emails, help content |
| Release scope and timing (**F**) | Campaign calendar, embargo dates, feature flag plan |
| Analytics from product (**P5**, warehouse) | Cohort quality by channel, activation funnel, retention drivers |

### Marketing → SDLC (outputs)

| Marketing artifact | SDLC usage |
|--------------------|------------|
| Event taxonomy & naming (**B**–**D**) | Implement analytics, flags, and QA assertions |
| SEO brief (**B**–**C**) | URL structure, meta, structured data, performance budgets for marketing pages |
| Consent / tag specification (**B**–**D**) | Implement CMP behavior, load order, server-side forwarding |
| Experiment spec (**B**–**E**) | Hypothesis, metrics, sample size — implemented via flags and tracking |

### Marketing → PDLC (feedback)

| Marketing signal | PDLC usage |
|------------------|------------|
| Funnel and cohort performance | Prioritize **P5** experiments; revisit **P3** positioning if ICP misfires |
| Search and social listening | New problem statements for **P1** |
| Win/loss and pipeline themes (SLG) | Inform **P2** validation and **P3** packaging |
| Creative and message tests | Evidence for value prop and roadmap emphasis |

### Closed-loop summary

| Direction | Essence |
|-----------|---------|
| **Into Marketing** | Product truth, UX reality, and release timing become **credible GTM and measurable funnels**. |
| **Out to SDLC** | Positioning and growth needs become **events, pages, consent, and experiment infrastructure**. |
| **Out to PDLC** | Channel and funnel data answer **whether strategy survives contact with the market**. |

---

## Calibration

### By initiative type

| Situation | Marketing investment | Reasoning |
|-----------|---------------------|-----------|
| **New category / brand** | **High** — positioning, narrative, PR, and long-horizon SEO/content | Demand must be **created**, not captured |
| **Feature in mature product** | **Medium** — launch comms, lifecycle touches, sales enablement, incremental SEO | Leverage existing audience; focus on **activation** more than awareness |
| **PLG product** | **High** on **product-facing** growth — onboarding, lifecycle email, in-product prompts | CAC efficiency depends on **product + marketing loop** |
| **Enterprise SLG** | **High** on **pipeline** — ABM, events, SDR air cover, case studies | Sales cycles need **proof and multi-threaded** stories |
| **Regulated or privacy-sensitive** | **High** on **compliance-aware** martech and messaging review | Missteps create legal and brand risk |
| **Internal platform** | **Low** on external ads; **targeted** on adoption within the org | “Marketing” may be **enablement and documentation** |

### By organizational context

| Context | Emphasis |
|---------|----------|
| **Startup** | Founder-led narrative; few channels done well; ruthless analytics hygiene |
| **Scale-up** | Specialize roles (PMM, growth, content); invest in warehouse + experimentation |
| **Enterprise** | Alignment with sales stages; longer content and event cycles; stricter approval |

### Signals you may be over- or under-investing

| Signal | Interpretation |
|--------|----------------|
| **Under-invested** | Product launches with no reachable audience; last-click reports drive bad cuts; retention collapses after paid bursts |
| **Well calibrated** | Stable or improving CAC payback; messaging matches NPS themes; experiments tie to **P5** outcomes |
| **Over-engineered (for context)** | Full attribution stack before baseline events; agency sprawl without ICP clarity |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Launch without instrumentation** | Big bang comms while events and conversions are untested | Define taxonomy in **B**; QA in **E**; soft launch to validate |
| **Vanity metric optimization** | Chasing impressions or clicks that do not correlate with revenue or retention | Tie campaigns to **activation and cohort** KPIs |
| **Marketing–product disconnect** | Ads promise capabilities the product does not deliver | Joint positioning sessions; **UX + PMM** review creative |
| **Dark patterns** | Obscured billing, fake urgency, hidden opt-outs | Align with UX ethics and **compliance**; protect brand |
| **Last-click tyranny** | Budget cuts to upper-funnel channels that assist conversions | Use experiments, MMM, or geo holdouts where feasible; document assists |

---

## Worked example

**Scenario:** A B2B SaaS team ships a **new analytics API** for enterprise customers. Product and engineering are ready for **P4**; sales expects pipeline within the quarter.

| Step | Lifecycle | What happens |
|------|-----------|--------------|
| 1 | **P3** | Product marketing finalizes **ICP** (mid-market data teams), **positioning** vs build-it-yourself and batch vendors, and **pricing** narrative (seat + usage). Messaging hierarchy aligns with BA capability language and UX onboarding. |
| 2 | **B** | PMM adds **event taxonomy** (`api_key_created`, `first_successful_query`) and **UTM standard** for the launch campaign. Security reviews data sent to ad platforms. |
| 3 | **C–D** | Frontend ships **docs landing**, **structured data**, and **comparison** page; backend enables **server-side conversion** events to the ad network. Email templates wired for trial upgrade. |
| 4 | **E** | QA runs **staging** tag checks, consent flows, and broken-link scans; SEO spot-check for canonicals and noindex rules. |
| 5 | **F** | Coordinated **launch**: changelog, customer email, webinar, paid search on high-intent queries, and **sales one-pager**. Feature flag aligns public docs visibility with GA. |
| 6 | **P4** | Measure **activation** (first successful query in 7 days) by **channel**; sales feedback loop on objections. |
| 7 | **P5** | Run **onboarding experiments** (SDK snippets, sample notebooks); expand **SEO** to tutorial cluster; **case study** with design partner. |

**Outcome:** Pipeline and product usage rise together because **GTM claims**, **docs**, and **instrumentation** matched the **SDLC** release, and **P5** learning focuses on **activation**, not raw lead count.

| Without strong PDLC | Without disciplined SDLC | Without Marketing |
|--------------------|------------------------|-------------------|
| API ships but **ICP** unclear — message scatters, win rate low | Events wrong — **false conclusions**; SEO pages late | Great product **invisible**; sales lacks proof and air cover |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`MARKETING.md`](MARKETING.md) | Full body of knowledge — principles, channels, growth, analytics, GTM |
| [`channels/README.md`](channels/README.md) | Channel guide index |
| [`growth/README.md`](growth/README.md) | Growth engineering guide index |
| [`README.md`](README.md) | Package overview and cross-links |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6 |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | Product–delivery alignment |
| [`UX-SDLC-PDLC-BRIDGE.md`](../ux-design/UX-SDLC-PDLC-BRIDGE.md) | Shared onboarding and activation concerns |
| [`DEVOPS-SDLC-PDLC-BRIDGE.md`](../../engineering/devops/DEVOPS-SDLC-PDLC-BRIDGE.md) | Flags, pipelines, reliability for experiments |

---

*Keep project-specific marketing plans in `docs/product/marketing/` and GTM documents in `docs/product/`, not in this file.*
