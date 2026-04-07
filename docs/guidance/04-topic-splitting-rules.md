# Topic splitting rules

Split topics to improve focus, not to manufacture more pages.

## Split triggers

Create subtopics when a page has one or more of these problems:

- two or more distinct jobs to be done
- one section is significantly more important than the rest
- the page needs multiple major visuals to stay readable
- the audience changes mid-page
- operational instructions interrupt concept explanation
- troubleshooting becomes a large secondary section
- examples are too numerous to keep inline

## Good split patterns

## Pattern 1: Overview + child tutorials

Use when a topic has a broad mental model plus several workflows.

Parent page:

- what it is
- how it fits
- when to use which child page
- capability map

Child pages:

- specific workflow or tutorial

Example:

- Studio overview
- Studio 101
- Studio 201
- Studio 301

## Pattern 2: Decision page + path pages

Use when the main job is choosing the right path.

Parent page:

- decision factors
- comparison matrix
- recommended path by audience

Child pages:

- each path in detail

Example:

- Adopting Blueprints
- Solo / small team
- Team lead / EM
- Org / platform rollout

## Pattern 3: Core workflow + branches

Use when the page has one main flow plus meaningful variations.

Parent page:

- common path
- summary of branches

Child pages:

- branch A
- branch B
- recovery / rollback path

Example:

- Updating the Blueprints submodule
- routine update
- update with conflicts
- rollback / pinning

## Pattern 4: Concept page + worked examples

Use when examples dominate the page.

Parent page:

- core concept
- how to choose an example

Child pages:

- example 1
- example 2
- example 3

Example:

- Wizard mission modes
- Start from idea example
- Tighten existing direction example
- Package for execution example
- Recovery / alignment example

## Pattern 5: Main guide + troubleshooting companion

Use when fixes become large enough to distract from the main guide.

Main guide:

- success path only

Companion page:

- symptom-first troubleshooting

Example:

- Install and run
- Troubleshooting

## Split thresholds

Strongly consider splitting when a page exceeds any two of these:

- more than 7 substantial headings
- more than 3 tables or matrices
- more than 1 primary visual
- more than 1200–1500 words of substantive content
- more than 2 distinct audiences
- more than 2 workflows

## Current high-priority split candidates

## Blueprints

### Adopting Blueprints

Keep the current summary page, then add focused child pages:

- adoption paths at a glance
- solo / small-team adoption
- team lead / EM adoption
- org / platform adoption

### First hour in your repository

Keep a concise quickstart, but split supporting depth into:

- repository layout explained
- Forge initialization explained
- Cursor rules and presets explained
- optional Forge Studio companion setup

### Project setup profile

Split into:

- core repository setup
- Forge alignment
- product docs and templates
- editor / agent alignment
- optional companion tools

### Updating the Blueprints submodule

Split into:

- routine update flow
- validate the update
- recover from conflicts / rollback
- team communication after the bump

### Team rollout patterns

Split into:

- single-team rollout
- multi-team rollout
- platform / org rollout
- governance cadence and ownership

## Lenses / Studio / Wizard

### Lenses overview

Keep overview, but add optional child pages:

- Classic vs Studio
- workspace model
- choosing the right surface

### Install and run

Split depth into:

- environment and prerequisites
- standalone clone flow
- submodule flow
- verification and first health checks

### Workspace setup

Split into:

- common workspace layouts
- choosing the root correctly
- registry and labeling only if needed
- common scan problems

### Studio overview

Keep overview, but add richer child depth via:

- screen map / navigation model
- choosing Flow vs Artifacts
- relationship to Classic

### Studio 201

Split if it grows into:

- daily navigation patterns
- keeping context across pages
- switching lenses deliberately

### Studio 301

Split if advanced usage expands into:

- advanced workflows
- limitations and fallback patterns

### Wizard overview

Keep overview, but add:

- session model
- twelve-step map
- outputs and what they are for

### Wizard 101

Likely split into:

- creating a session
- understanding the twelve steps
- first worked example

### Wizard 201

Best split candidate:

- one page per mission mode, with comparison parent page

### Wizard 301

Split into:

- artifact bundles
- Refine / LLM-assisted usage
- review and recheck
- Cursor Launch Pack

## File naming guidance

Use names that reflect reader jobs, not internal implementation.

Prefer:

- `studio-navigation-model.md`
- `wizard-mission-modes.md`
- `update-blueprints-routine-flow.md`

Avoid:

- `wizard-internals-stepper.md`
- `workspace-registry-v2.md`
- `implementation-details.md`
