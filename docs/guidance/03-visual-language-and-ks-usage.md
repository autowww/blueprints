# Visual language and Kitchen Sink usage guide

Use the Forge design system and Kitchen Sink visuals deliberately. Choose the visual that reduces cognitive load for the reader.

## Core rule

Every medium or long public page should include:

- one primary visual
- one summary table or matrix
- one concrete example block or scenario

## Which visual to use when

## Process and flow topics

Use when the reader needs to understand sequence, handoff, or progression.

Recommended visual types:

- `linear-flow` for happy-path setup or tutorial flow
- `swimlane` for multi-role handoffs
- `decision-flow` when the path branches
- `loop-cycle` for recurring operating loops
- `checklist` for readiness or completion review

Good fits:

- First hour in your repository
- Install and run
- Studio 101
- Wizard 101
- Troubleshooting triage

## Structural and relationship topics

Use when the reader needs to understand containment, ownership, or relationship between things.

Recommended visual types:

- `tree` for hierarchy of guides or concepts
- `board-columns` for grouped capabilities or phases
- `org-chart` for role/responsibility pages
- `network` for linked products or adjacent systems

Good fits:

- Blueprints overview
- Lenses overview
- “How Blueprints, Studio, and Wizard relate” pages
- Team rollout pages

## Timeline and planning topics

Use when the reader must understand order over time, adoption waves, or phased rollout.

Recommended visual types:

- `timeline`
- `roadmap`
- `gantt`

Good fits:

- Team rollout patterns
- Updating the submodule
- adoption path pages with staged rollouts

## Comparison and decision topics

Use when the reader must choose between options.

Recommended visual types:

- comparison table
- quadrant
- bullet chart only if genuine performance/goal comparison exists
- do/avoid matrix
- mission mode matrix

Good fits:

- Adopting Blueprints
- Wizard mission modes
- Studio workflow mode comparisons
- when to use Blueprints vs Studio vs Wizard

## Metrics or evidence topics

Use only when there is real data to show.

Recommended visual types:

- static or API charts from the Kitchen Sink data chart contract
- heatmap for dense activity/status summaries
- KPI tiles for overview pages with meaningful values

Do not invent fake metrics merely to decorate the page.

Good fits:

- adoption progress dashboard pages if you have real data
- compliance / coverage pages
- repo or content coverage reporting

## UI walkthrough topics

Use when the reader must understand a screen or interaction flow.

Recommended visual types:

- split layout: screenshot or preview left, explanation right
- annotated screenshot with numbered callouts
- state diagram if UI states matter
- workspace lens visual for cognitive mode switching

Good fits:

- Studio overview
- Studio 101/201
- Wizard overview
- Wizard 101 hub vs session explanation

## Recommended Kitchen Sink components by documentation job

### Cards / bento grids

Use for:

- capability summaries
- “start here” options
- role-based entry points
- grouped next steps

Avoid using cards when a simple table is clearer.

### Tables

Use for:

- comparisons
- prerequisites
- step/verify summaries
- glossary entries
- option and trade-off lists

Prefer tables when the reader needs exactness.

### Callouts

Use sparingly for:

- warnings
- success states
- important caveats
- “not covered here” boundaries

Do not turn half the page into callouts.

### Split layout

Use when you have a live example, screenshot, or interactive embed worth keeping visible while the reader reads explanatory text.

Best for:

- Studio navigation walkthroughs
- Wizard stepper walkthroughs
- setup pages with file tree or UI preview

### Topic preview cards

Use to let the reader inspect a related page without losing context.

Best for:

- overview pages with several child topics
- “choose your path” pages
- product relationship pages

## Minimum visual contract by page type

### Overview pages

Must include:

- one mental-model visual
- one capability or role matrix

### Quickstarts / 101s

Must include:

- one flow visual
- one step/verify table

### 201 / 301 pages

Must include:

- one decision or comparison visual
- one option / trade-off matrix

### Troubleshooting pages

Must include:

- one triage flow visual or symptom matrix
- one symptom/cause/action table

## Visual anti-patterns

Do not:

- add diagrams that simply restate a heading
- add charts with no meaningful data
- use more than one decorative background element in a dense handbook page
- turn every paragraph into a card
- use a matrix when the page only needs a checklist

## Suggested diagram mapping for current docs

### Blueprints

- Adopting Blueprints → decision tree + audience/path matrix
- First hour → linear flow + verify checklist table
- Project setup profile → roadmap / grouped checklist + file-tree visual
- Updating the submodule → decision flow + rollback table
- Team rollout patterns → phased timeline + stakeholder swimlane
- Forge Studio quickstart → linear flow + split layout with `/studio/` screen preview

### Lenses / Studio / Wizard

- Lenses overview → relationship tree or board-columns for Classic / Studio / Wizard
- Install and run → linear flow + environment matrix
- Workspace setup → tree or file-layout diagram + common layouts table
- Studio overview → workspace lens visual + screen-region callout map
- Studio 101 → first-session flow + step/result table
- Studio 201 → mode comparison matrix + recurring-work swimlane
- Studio 301 → decision matrix + limitations table
- Wizard overview → stepper or journey diagram + outputs table
- Wizard 101 → hub/session split layout + 12-step matrix
- Wizard 201 → mission-mode quadrant or comparison table
- Wizard 301 → artifact-bundle matrix + review/recheck loop diagram
- Troubleshooting → symptom triage flow + fix matrix
