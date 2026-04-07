# Blueprints public-doc depth plan

## Current state

The Blueprints public docs are now framed correctly for adoption and use. The next improvement is depth: more decision support, more examples, and more visual explanation.

## Priority 1 pages

## Home

Keep it concise. Do not turn the home page into a deep reference page.

Add:

- a compact “what changes in my repo” visual
- a small comparison table: Quickstarts vs Adopting vs Setup profile vs Forge Studio
- a “who should start where” card set

Do not add:

- deep methodology lists
- package taxonomies
- internal file maps

## Quickstarts hub

Add:

- quickstart selection matrix
- estimated time / outcome / who it is for table
- small visual showing how Quickstarts relates to Adopting, Setup profile, and Troubleshooting

## Adopting Blueprints

Current page is good as a chooser, but it needs stronger decision support.

Add:

- audience/path comparison matrix
- “what changes / what stays the same” table
- one decision tree visual
- examples of each ICP path
- risk / trade-off table

Split into optional child pages:

- solo / small team
- team lead / EM
- organization / platform

## First hour in your repository

Add:

- repo-layout visual
- step/verify matrix with expected files and outcomes
- common mistakes table
- short explanation of why the layout is structured this way

Optional child pages:

- repo layout explained
- Forge initialization explained
- Cursor rules explained

## Project setup profile

This is the best candidate for a deeper restructure.

Add:

- grouped phases instead of one long checklist
- progress table with required vs optional
- file-tree visual for the target repo shape
- examples of minimum, recommended, and full setups
- “copy this to SETUP.md” guidance with a checklist variant

Split into subtopics:

- core repo setup
- Forge alignment
- product docs and templates
- editor / agent alignment
- optional companion tooling

## Updating the Blueprints submodule

Add:

- routine flow diagram
- pre-update / update / validate / rollback matrix
- “what could break” table
- post-update communication checklist

Split into:

- routine update
- validate and test
- rollback and conflict recovery

## Team rollout patterns

This page is currently too thin for the importance of the topic.

Add:

- rollout timeline or phased roadmap
- stakeholder swimlane
- pilot / expand / standardize pattern
- resistance/risk table
- ownership matrix
- success measures

Split into:

- single-team rollout
- multi-team rollout
- org/platform rollout
- governance cadence

## Forge Studio quickstart

Keep it operationally light, but deepen the reader experience.

Add:

- what Forge Studio helps with compared with handbook-only reading
- setup flow visual
- “what you will see” screen map
- quick paths: just Studio vs Studio + Wizard
- verify-success table

Do not add maintainer build mechanics.

## Troubleshooting / FAQ

Add:

- symptom index
- categorized fixes by area: layout, submodule, Forge, Cursor, Studio companion
- quick triage decision tree
- “evidence to gather before asking for help” checklist

## Recommended visual map

- Home → board-columns or relationship tree
- Quickstarts hub → matrix + lightweight flow
- Adopting → decision tree + audience/path matrix
- First hour → linear flow + file-tree visual
- Setup profile → roadmap + target repo layout diagram
- Updating the submodule → decision flow + rollback table
- Team rollout → timeline + swimlane
- Forge Studio quickstart → split layout + linear flow
- Troubleshooting → decision flow + symptom matrix

## Depth order of execution

1. Adopting Blueprints
2. Project setup profile
3. Team rollout patterns
4. First hour in your repository
5. Updating the submodule
6. Troubleshooting / FAQ
7. Forge Studio quickstart
8. Home and Quickstarts hub polish
