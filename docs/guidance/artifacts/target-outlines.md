# Target outlines (Prompt 2)

Approver edits this file before bulk content work. Maintainer-only.

Legend: archetypes from [02-page-archetypes-and-coverage.md](../02-page-archetypes-and-coverage.md).

## Blueprints (SDLC onboarding)

### SDLC blueprint README (`sdlc/README.md`) — handbook area index

- **Purpose:** Orient readers to the reusable SDLC package and the fastest links for adoption vs deep methodology.
- **Archetype:** Overview (compressed).
- **Sections:** Deliverable table (keep); add one row “Onboarding journey” linking adopting → quickstarts → SETUP; keep “what does not belong” short.
- **Structured:** Capability/outcome table (extend existing); optional “who starts where” bullets.
- **Visual:** Not required in-repo Markdown (handbook HTML may already diagram); avoid exceeding [onboarding hub limits](../../../blueprints-website/generator/validate_public_handbook_surface.py) for `sdlc/README.md`.
- **Split:** No.

### Quickstarts hub (`sdlc/quickstarts/README.md`)

- **Purpose:** Route readers to First hour vs Forge Studio with time/audience hints.
- **Archetype:** Overview.
- **Structured:** Selection matrix (time, outcome, prerequisite repo state); link to Adopting vs SETUP.
- **Visual:** Lightweight flow: Adopt → Quickstart → SETUP (prose or table, not Mermaid).
- **Split:** No.

### Adopting Blueprints (`sdlc/adopting-blueprints.md`)

- **Purpose:** Help readers pick path A/B/C and know what changes in the repo.
- **Archetype:** Adoption (chooser).
- **Structured:** Path comparison matrix; “what changes / what stays frozen”; optional risk/trade-off row per path.
- **Visual:** Numbered decision flow in prose (ICP questions → path).
- **Split:** Optional future children per path; parent remains chooser.

### First hour (`sdlc/quickstarts/first-hour.md`)

- **Purpose:** One sitting to submodule + `sdlc/` + Forge + Cursor (+ optional Studio).
- **Archetype:** Quickstart.
- **Structured:** Step/verify table (exists); add “common mistakes” short table.
- **Visual:** Same-page linear sequence (headings already).
- **Split:** Optional deep links to layout/Forge/Cursor explainers.

### Project setup profile (`sdlc/SETUP.md`)

- **Purpose:** Full ordered setup for teams standardizing end-to-end.
- **Archetype:** Reference-lite + tutorial chain.
- **Structured:** Group steps into phases (bootstrap / Forge / Cursor / optional product) with a “required vs optional” column.
- **Visual:** Phase table first; avoid raw file-map dumps.
- **Split:** Future: separate pages per track if length grows; keep one checklist until then.

### Updating the Blueprints submodule (`sdlc/updating-blueprints-submodule.md`)

- **Purpose:** Safe pointer bumps with validation.
- **Archetype:** Reference-lite / troubleshooting-adjacent.
- **Structured:** Pre-bump / bump / validate / communicate matrix; rollback/recovery bullets.
- **Visual:** Ordered checklist (prose).
- **Split:** Optional child for conflict recovery later.

### Team rollout patterns (`sdlc/team-rollout.md`)

- **Purpose:** How to expand Blueprints+Forge usage beyond one anchor repo.
- **Archetype:** Adoption / rollout.
- **Structured:** Phased timeline table; pilot → expand → standardize; risks and mitigations; ownership row.
- **Split:** Optional children by org size when content grows.

### Forge Studio quickstart (`sdlc/quickstarts/forge-studio.md`)

- **Purpose:** Run forge-lenses locally and open `/studio/`.
- **Archetype:** Quickstart.
- **Structured:** Verify table (exists); add “handbook-only vs Studio” comparison row.
- **Visual:** Not required as diagram; URL list suffices.

### Troubleshooting (`sdlc/troubleshooting-faq.md`)

- **Purpose:** Symptom-first recovery for consumers.
- **Archetype:** Troubleshooting.
- **Structured:** Symptom index table; “evidence to gather” checklist; keep sections themed.
- **Split:** No.

## Lenses / Studio / Wizard (`forge-lenses/docs/handbook-public/`)

### Lenses overview (`01-lenses-overview.md`)

- **Archetype:** Overview. **Structured:** Surface × job matrix. **Split:** Optional.

### Install and run (`02-install-and-run.md`)

- **Archetype:** Quickstart. **Structured:** Standalone vs submodule table; env matrix.

### Workspace setup (`03-workspace-setup.md`)

- **Archetype:** Tutorial 201. **Structured:** Layout table; good/bad root examples.

### Studio overview / 101 / 201 / 301 (`04`–`07`)

- **Archetype:** Overview + 101–301 ladder. **Structured:** Flow vs Artifacts matrix on 201; limitations table on 301.

### Wizard overview / 101 / 201 / 301 (`08`–`11`)

- **Archetype:** Overview + tutorials. **Structured:** Twelve-step table on 101; mission mode matrix on 201; artifact bundles on 301.

### Troubleshooting (`12-troubleshooting.md`)

- **Archetype:** Troubleshooting. **Structured:** Symptom/cause/action expansion.

---

**Handbook build note:** [`validate_public_handbook_surface.py`](../../../../blueprints-website/generator/validate_public_handbook_surface.py) limits H2/table counts on onboarding **hub** pages (`README.md`, `sdlc/README.md`, `sdlc/quickstarts/README.md`, `sdlc/adopting-blueprints.md`). Keep expansions within those caps or shift detail to non-hub pages.
