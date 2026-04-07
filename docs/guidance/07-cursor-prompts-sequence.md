# Cursor prompt sequence for increasing depth and quality

Run these prompts in order. Do not skip the audit and outline phases.

## Where the guidance files live

- **Canonical (git):** `blueprints/docs/guidance/` in the [blueprints](https://github.com/autowww/blueprints) repository — numbered `01-` … `08-` files plus [`README.md`](README.md).
- **Workspace Cursor path:** `docs/guidance/` at the multi-repo root is a **symlink** to that directory (when the workspace layout matches this repository).
- **forge-lenses clone:** see [`forge-lenses/docs/public-doc-depth-guidance.md`](../../../forge-lenses/docs/public-doc-depth-guidance.md) for a pointer to the same bundle.

**Alternate filenames (if you prefer unnumbered files):** the bundle matches Prompt 3’s names as follows:

| Numbered file | Prompt 3 name |
|---------------|-----------------|
| `01-doc-depth-charter.md` | `public-doc-depth-charter.md` |
| `02-page-archetypes-and-coverage.md` | `page-archetypes-and-coverage.md` |
| `03-visual-language-and-ks-usage.md` | `visual-language-and-ks-usage.md` |
| `04-topic-splitting-rules.md` | `topic-splitting-rules.md` |
| `08-review-checklist.md` | `public-doc-review-checklist.md` |

## Prompt 1 — audit current depth and visual gaps

```text
Audit the current public documentation for depth, coverage, and reading experience.

Focus only on the public handbook pages, not maintainer docs.

Evaluate each page for:
- reader outcome clarity
- completeness of topic coverage
- presence or absence of a mental model
- presence or absence of examples
- presence or absence of troubleshooting / edge cases
- use of structured content (tables, matrices, checklists)
- whether a visual would help
- whether the topic should split into subtopics

Use these handbook areas:
- Blueprints home and SDLC onboarding pages
- Lenses / Studio / Wizard public guides

Return a table with columns:
- page
- primary reader job
- current strengths
- current gaps
- visual(s) recommended
- split needed? yes/no
- priority

Use the guidance files in docs/guidance/ as the source of truth for quality rules.
Do not rewrite files yet.
```

## Prompt 2 — generate target outlines per page

```text
Using the depth audit and the guidance files in docs/guidance/, produce target outlines for the public pages.

For each page, return:
- final page purpose in one sentence
- target archetype (overview, quickstart, 101, 201, 301, adoption, troubleshooting, reference-lite)
- required sections
- required structured elements
- required visual
- should split? if yes, parent page + child page list

Do this for:
- Blueprints home
- Quickstarts hub
- Adopting Blueprints
- First hour in your repository
- Project setup profile
- Updating the Blueprints submodule
- Team rollout patterns
- Forge Studio quickstart
- Lenses overview
- Install and run
- Workspace setup
- Studio overview
- Studio 101
- Studio 201
- Studio 301
- Wizard overview
- Wizard 101
- Wizard 201
- Wizard 301
- Troubleshooting

Do not edit the source yet. Produce a clean plan first.
```

## Prompt 3 — add reusable authoring guidance files

**Status:** Superseded when the numbered bundle is already committed under `blueprints/docs/guidance/` (or linked from `docs/guidance/`). Do **not** recreate those documents from scratch.

Use Prompt 3 only to:

- align filenames with the table above (optional copies or symlinks), or
- merge small edits after human review (diff-only).

```text
Create or update maintainer-only guidance markdown files under docs/guidance/ using the approved plan.

Needed files:
- docs/guidance/public-doc-depth-charter.md
- docs/guidance/page-archetypes-and-coverage.md
- docs/guidance/visual-language-and-ks-usage.md
- docs/guidance/topic-splitting-rules.md
- docs/guidance/public-doc-review-checklist.md

Write them so future page authors can use them without reading the full repository history.

Rules:
- maintainer-only, not part of the public handbook
- short enough to be usable
- specific enough to guide real edits
```

## Prompt 4 — deepen Blueprints pages first

```text
Deepen the Blueprints public pages using docs/guidance/ as the quality bar.

Priority order:
1. Adopting Blueprints
2. Project setup profile
3. Team rollout patterns
4. First hour in your repository
5. Updating the Blueprints submodule
6. Troubleshooting / FAQ
7. Forge Studio quickstart
8. Quickstarts hub and home-page polish

For each page:
- keep the public boundary
- add richer explanations, examples, and verification guidance
- add the recommended visual and structured elements
- split the page into subtopics where the plan says to split
- keep navigation clean and outcome-oriented

Do not reintroduce maintainer internals.

Return:
- files changed
- new subpages created
- visuals/tables added
- redirects or nav changes needed
```

## Prompt 5 — deepen Lenses / Studio / Wizard pages

```text
Deepen the public Lenses / Studio / Wizard handbook using docs/guidance/ as the quality bar.

Priority order:
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

For each page:
- add a clearer mental model
- add one primary visual
- add more structured content: tables, matrices, examples, checklists
- add worked examples where missing
- split into subpages where the plan recommends it
- keep the content user-facing, not maintainer-facing

Special instruction:
- Wizard 201 should become a comparison parent page plus child pages per mission mode if the source structure supports it.
- Studio 201 should add a clear Flow vs Artifacts decision guide and recurring-work examples.
```

## Prompt 6 — add Kitchen Sink visuals deliberately

```text
Add visuals to the public handbook pages using the Forge design system / Kitchen Sink patterns already available in the site.

Use the visual-language guidance file and choose visuals by reader job, not by decoration.

Tasks:
- identify where each page needs a diagram, matrix, or split layout
- add the minimal right visual per page
- prefer diagrams for flow, branching, role boundaries, hierarchy, or timelines
- prefer tables/matrices for comparison, options, prerequisites, and verification
- use split layout for UI walkthroughs where screenshots or previews help
- keep the page readable; do not over-decorate

Return a page-by-page map of:
- visual added
- why it helps the reader
- source files changed
```

## Prompt 7 — create subtopics and rewire navigation

```text
Create focused child pages for the topics marked for splitting, then update public navigation and previous/next links.

Split by reader job, not by internal repo layout.

High-priority splits:
- Adopting Blueprints → audience-specific paths
- Project setup profile → grouped setup tracks
- Updating the Blueprints submodule → routine update / validate / rollback
- Team rollout patterns → single-team / multi-team / org-platform / governance cadence
- Wizard 201 → one child page per mission mode
- Wizard 301 → artifact bundles / Refine / review and recheck / Cursor Launch Pack
- Workspace setup → common layouts / root choice / scan problems

Requirements:
- parent page remains a good chooser page
- child pages are more focused, not duplicated walls of prose
- previous/next and related links keep the learning path obvious
```

## Prompt 8 — enrich with examples and scenario blocks

```text
Add worked examples and scenario blocks to the public pages that still feel abstract.

Use realistic but generic examples.

Minimum examples to add:
- one Blueprints adoption example for each ICP path
- one first-hour repo example
- one Studio first-session example
- one Studio recurring-work example
- one Wizard first-session example
- one example per Wizard mission mode
- one update/rollback example for Blueprints submodule updates
- one team-rollout example

Each example should include:
- starting situation
- action taken
- expected result
- what to check
```

## Prompt 9 — run a final depth QA pass

```text
Run a final QA pass on the public documentation after the depth improvements.

Check every public page for:
- clear reader outcome
- strong mental model
- sufficient execution detail
- decision support where needed
- troubleshooting or recovery guidance where needed
- at least one primary visual on medium/long pages
- at least two structured elements per substantive page
- examples where the topic benefits from them
- no maintainer-internal leakage
- clean navigation after any topic splits

Return:
- pass/fail by page
- remaining weak pages
- pages still too thin
- visuals that still need work
- broken links or nav issues
- exact files to revisit
```
