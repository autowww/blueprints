# External reference URLs (PDLC approach guides)

Curated list of **https** targets cited in [`blueprints/pdlc/approaches/`](README.md) and in [`PDLC-SDLC-BRIDGE.md`](../PDLC-SDLC-BRIDGE.md). When you change a URL in Markdown, update the matching approach guide's "Authoritative sources" section.

Each row includes an **executive summary**: what the link is and **why this blueprint points to it**, so readers can decide whether to open it.

## Product management & discovery

| Topic | URL | Executive summary (why it's linked here) |
|-------|-----|----------------------------------------|
| Marty Cagan — SVPG (Inspired / Empowered) | https://www.svpg.com/inspired-how-to-create-tech-products-customers-love/ | **Foundational text** on modern product management: product trio, discovery, empowered teams. Philosophical anchor for PDLC thinking about outcomes over outputs. |
| Marty Cagan — Dual-Track Agile | https://www.svpg.com/dual-track-agile/ | **Origin framing** for running discovery and delivery in parallel — defines why the product trio co-owns discovery alongside engineering delivery. |
| SVPG — Product Discovery | https://www.svpg.com/product-discovery/ | **Collection** of articles on discovery practices — risk assessment, opportunity assessment, prototyping — from the SVPG team. |
| Teresa Torres — Continuous Discovery Habits | https://www.producttalk.org/2021/08/continuous-discovery-habits/ | **Practical framework** for weekly discovery: opportunity solution trees, interview cadence, assumption mapping. Operationalizes PDLC P1–P2 as ongoing practice. |
| Teresa Torres — Opportunity Solution Trees | https://www.producttalk.org/2023/12/opportunity-solution-trees/ | **Canonical source** for the OST framework — visual structure connecting outcomes → opportunities → solutions → experiments. |
| Product Talk (blog) | https://www.producttalk.org/ | **Blog and community** from Teresa Torres — ongoing articles on discovery, experimentation, and product trio practices. |
| Melissa Perri — Escaping the Build Trap | https://melissaperri.com/book | **Diagnosis and cure** for organizations that ship features without validating outcomes — directly addresses the "SDLC without PDLC" anti-pattern. |
| Mind the Product | https://www.mindtheproduct.com/ | **Community hub** for product management: conferences, articles, and frameworks — neutral background for PDLC vocabulary. |
| Product School — Resources | https://productschool.com/blog | **Practitioner content** on product management — OSTs, discovery, metrics, team structures. |

## Lean Startup & experimentation

| Topic | URL | Executive summary (why it's linked here) |
|-------|-----|----------------------------------------|
| Eric Ries — The Lean Startup | http://theleanstartup.com/ | **Canonical text** defining Build-Measure-Learn, MVP, validated learning, pivot/persevere. The reference for hypothesis-driven product development. |
| Steve Blank — Customer Development | https://steveblank.com/category/customer-development/ | **Precursor framework** to Lean Startup: Customer Discovery → Validation → Creation → Building. Business-model-validation layer. |
| Ash Maurya — Running Lean / Lean Stack | https://leanstack.com/running-lean-book | **Practitioner playbook** for applying Lean Startup — Lean Canvas, experiment design, metrics that matter. |
| Jeff Gothelf — Lean UX | https://www.jeffgothelf.com/lean-ux-book/ | **UX + Lean Startup integration** — hypotheses, experiments, outcomes in Agile teams. Bridges design practice with delivery. |
| Jeff Patton — Dual Track Development | https://www.jpattonassociates.com/dual-track-development/ | **Practical guidance** on separating learning work from building work — visual models for dual-track implementation. |

## Design Thinking

| Topic | URL | Executive summary (why it's linked here) |
|-------|-----|----------------------------------------|
| IDEO — Design Thinking | https://designthinking.ideo.com/ | **Origin framework** — Empathize, Define, Ideate, Prototype, Test. Defines human-centered design principles used in PDLC P1–P2. |
| Stanford d.school | https://dschool.stanford.edu/ | **Academic anchor** for Design Thinking education — process guides, teaching materials, and the "bootcamp bootleg" toolkit. |
| British Design Council — Double Diamond | https://www.designcouncil.org.uk/our-resources/the-double-diamond/ | **Double Diamond model** — canonical visualization of diverge/converge across problem and solution spaces. |
| Nielsen Norman Group — Design Thinking | https://www.nngroup.com/articles/design-thinking/ | **Evidence-based** practitioner summary of when Design Thinking works and its limitations. |

## Agile product delivery (vendor context)

| Topic | URL | Executive summary (why it's linked here) |
|-------|-----|----------------------------------------|
| Atlassian — Product development | https://www.atlassian.com/agile/product-management/product-development | **Practitioner overview** of product development in an Agile context — complements Forge’s PDLC ↔ SDLC bridge for software teams. |

## Stage-Gate & governance

| Topic | URL | Executive summary (why it's linked here) |
|-------|-----|----------------------------------------|
| Stage-Gate International | https://www.stage-gate.com/ | **Official** Stage-Gate body of knowledge — Robert Cooper's framework, 5th-generation updates, research. Authority for gate criteria and stage definitions. |
| Stage-Gate — Discovery-to-launch process | https://www.stage-gate.com/about/stage-gate-innovation-performance-framework/discovery-to-launch-process/ | **Discovery-to-launch** framing from Stage-Gate International — aligns with gated NPD vocabulary used alongside Forge P1–P6. |
| 5th-Generation Stage-Gate Model | https://www.stage-gate.com/about/5th-generation-stage-gate-model/ | **Current evolution**: iterative stages, Agile integration, lean gates, adaptive governance. Addresses historical rigidity criticism. |
| PDMA — Product Development and Management Association | https://community.pdma.org/ | **Practitioner community** for product development — research, benchmarking, and Stage-Gate updates from Robert Cooper. |

## Product lifecycle & growth

| Topic | URL | Executive summary (why it's linked here) |
|-------|-----|----------------------------------------|
| ProductPlan — Product development cycle | https://www.productplan.com/glossary/product-development-cycle/ | **Definition overview** of the product development cycle — helps teams compare generic phase language to Forge P1–P6 without claiming one global standard. |
| ProductPlan — Product Lifecycle | https://productplan.com/glossary/product-lifecycle/ | **Clear overview** of lifecycle stages (Introduction, Growth, Maturity, Decline) with strategic implications. Starting reference for PLM. |
| ProductPlan — End-of-Life | https://productplan.com/learn/how-to-end-of-life-product/ | **Practical checklist** for product retirement — communications, migration, support wind-down. Informs P6 sunset planning. |
| Product Marketing Alliance — Sunsetting | https://productmarketingalliance.com/how-to-sunset-product-complete-guide-examples/ | **Complete guide** with real examples of product sunset strategies — phased approach, stakeholder management. |
| Reforge — Growth Series | https://www.reforge.com/growth-series | **Growth frameworks** for post-launch: acquisition, activation, retention, revenue, referral. Deepens P5 Grow. |
| DORA — State of DevOps | https://dora.dev/ | **Delivery metrics** research (DORA four key metrics) — the SDLC side of the metrics comparison in the bridge document. |

## Quick verification (maintainers)

From a shell, expect HTTP **200** (some sites return **301** then 200 when following redirects):

```bash
urls=(
  https://www.svpg.com/inspired-how-to-create-tech-products-customers-love/
  https://www.producttalk.org/2021/08/continuous-discovery-habits/
  http://theleanstartup.com/
  https://designthinking.ideo.com/
  https://www.stage-gate.com/
  https://www.stage-gate.com/about/stage-gate-innovation-performance-framework/discovery-to-launch-process/
  https://productplan.com/glossary/product-lifecycle/
  https://www.productplan.com/glossary/product-development-cycle/
  https://www.atlassian.com/agile/product-management/product-development
  https://dora.dev/
  https://www.designcouncil.org.uk/our-resources/the-double-diamond/
)
for u in "${urls[@]}"; do
  printf '%s ' "$(curl -sS -o /dev/null -w '%{http_code}' -L --max-time 15 "$u")"
  echo "$u"
done
```

Expand the array with any new links before merging doc changes.
