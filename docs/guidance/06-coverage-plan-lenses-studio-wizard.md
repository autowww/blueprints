# Lenses, Studio, and Wizard public-doc depth plan

## Current state

The public guide spine is correct and clean. The next step is to make the pages feel like complete product guidance rather than minimal path markers.

## Priority 1 pages

## Lenses overview

Add:

- clearer relationship visual for Classic, Studio, and Wizard
- capability table by surface
- “which surface should I use for which job” matrix
- one example workspace story

Possible child pages:

- choosing Classic vs Studio
- workspace model

## Install and run

Add:

- environment matrix
- standalone clone vs submodule comparison table
- verification checklist
- quick health-check section
- “when install succeeds but Studio does not” branch summary

Possible child pages:

- standalone clone
- submodule install
- health checks

## Workspace setup

This page especially benefits from visuals.

Add:

- workspace root diagram
- common layouts table
- “good / bad root choice” examples
- scan-behavior explanation in user language
- troubleshooting branches for empty or wrong scans

Possible child pages:

- common layouts
- choosing the root
- scan problems

## Studio overview

Add:

- screen-region map
- workspace lens explanation visual
- “Classic vs Studio” task table
- first-value path from landing to useful work

Possible child pages:

- navigation model
- choosing Flow vs Artifacts

## Studio 101

Add:

- first session flow diagram
- screenshot or split-layout walkthrough
- small glossary of main navigation labels
- example: open a project or workspace view end to end
- expected screen-state checklist

## Studio 201

This page should become much richer.

Add:

- recurring jobs matrix
- Flow vs Artifacts decision guide
- example day-in-the-life workflows
- context preservation tips
- do / avoid table

Split into:

- working in Flow mode
- working in Artifacts mode
- moving between plans, projects, and knowledge

## Studio 301

Keep it advanced but user-facing.

Add:

- advanced scenario matrix
- limitations/fallback guidance
- “when to go back to Classic” guidance without internal implementation detail
- examples of efficient multi-surface work

Split into:

- advanced workflows
- limitations and fallback patterns

## Wizard overview

Add:

- stepper or journey visual for the whole Wizard
- “what the Wizard is good for / not good for” matrix
- inputs vs outputs table
- brief example of a workshop outcome

Possible child pages:

- session model
- step map
- outputs guide

## Wizard 101

Add:

- hub vs session split-layout visual
- twelve-step table with purpose, question, and output
- one worked example end to end
- saved-draft and resume guidance

Split into:

- creating a session
- navigating a session
- first worked example

## Wizard 201

This is the strongest split candidate.

Add:

- mission-mode comparison matrix
- role/intent recommendations
- examples for each mode
- “choose this mode when” decision tree

Split into:

- mission modes overview
- Start from idea
- Tighten existing direction
- Package for execution
- Recover alignment / re-plan

## Wizard 301

Add:

- artifact-bundle matrix
- Refine loop diagram
- review vs recheck distinction table
- export and handoff examples
- practical guidance for Cursor Launch Pack use

Split into:

- artifact bundles
- Refine and LLM-assisted usage
- review and recheck
- Cursor Launch Pack handoff

## Troubleshooting

Add:

- fast triage section
- symptom/cause/action matrix with more coverage
- wizard-specific problems grouped separately from general Studio issues
- evidence and logs checklist for escalation

Split if needed into:

- install/run issues
- workspace scan issues
- Studio navigation issues
- Wizard session issues

## Recommended visual map

- Lenses overview → relationship tree + surface/job matrix
- Install and run → linear flow + environment matrix
- Workspace setup → file-layout diagram + root-choice examples
- Studio overview → screen map + workspace-lens visual
- Studio 101 → split layout + session flow
- Studio 201 → decision matrix + swimlane
- Studio 301 → edge-case table + fallback decision tree
- Wizard overview → 12-step journey visual + outputs matrix
- Wizard 101 → hub/session split layout + step table
- Wizard 201 → mission-mode matrix or quadrant
- Wizard 301 → artifact bundle matrix + loop-cycle diagram
- Troubleshooting → triage flow + symptom matrix

## Depth order of execution

1. Wizard 201
2. Studio 201
3. Wizard overview
4. Wizard 101
5. Workspace setup
6. Studio overview
7. Wizard 301
8. Studio 101
9. Troubleshooting
10. Lenses overview
11. Install and run
12. Studio 301
