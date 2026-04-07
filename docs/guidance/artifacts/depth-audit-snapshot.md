# Public handbook depth audit (snapshot)

Generated per [Prompt 1](../07-cursor-prompts-sequence.md). Maintainer-only; not published.

**Scope:** Blueprints SDLC onboarding pages (`handbook_area: blueprints`, `nav_group: onboarding` where applicable) and forge-lenses `handbook-public/*.md`.

**Quality bar:** [01-doc-depth-charter.md](../01-doc-depth-charter.md).

## Summary

| Area | Strong pages (orientation + execution) | Common gaps |
|------|----------------------------------------|-------------|
| Blueprints onboarding | Adopting (ICP tables), First hour (verify table), Submodule update | Team rollout thin; SETUP long linear list; FAQ symptom index could be richer |
| Lenses / Studio / Wizard | Install steps, overview framing | Studio/Wizard 201 need decision support and examples; troubleshooting dense but uneven |

## Page-by-page (abbreviated)

| Page | Primary reader job | Strengths | Gaps | Visual / structured recommendation | Split? | Priority |
|------|-------------------|-----------|------|-------------------------------------|--------|----------|
| SDLC README (handbook home) | Find the right door | Clear deliverable table | “What changes in my repo” could be one row richer | Small capability vs outcome matrix | No | Polish |
| Quickstarts hub | Pick a fast path | Two-row quickstart table | Selection matrix vs Adopting / SETUP | Quickstart selection matrix | No | Medium |
| Adopting Blueprints | Choose ICP path | Three path tables with verify | Decision tree for path choice; risk/trade-off row | Decision matrix + “what stays the same” table | Optional child paths later | High |
| First hour | Bootstrap repo | Step + verify table | Repo layout “why” mini-section; mistakes table | Step/verify already strong; add mistakes table | Optional deep dives | High |
| Project setup profile | Full checklist | Ordered steps | Phased grouping; progress table required vs optional | Phase table + repo-shape summary | Yes (tracks) | High |
| Updating submodule | Bump safely | Commands | Pre/post matrix; rollback emphasis | Update lifecycle table | Yes (routine vs recovery) | Medium |
| Team rollout | Scale adoption | Basic pattern list | Timeline, stakeholders, risks | Phase + ownership table | Yes (scale bands) | High |
| Forge Studio quickstart | Run Lenses | Clear URLs | Screen map; handbook-only vs Studio value | Compare table | No | Medium |
| Troubleshooting | Unblock | Themed sections | Symptom-first index; triage order | Symptom → fix table | No | Medium |
| Lenses overview | Pick surface | — | Relationship matrix Classic/Studio/Wizard | Surface/job matrix | Optional | Medium |
| Install and run | Get app running | — | Env matrix; health checks | Prerequisites matrix | Optional | Medium |
| Workspace setup | Correct root | — | Good/bad root examples table | Layout diagram (SVG) | Optional | High |
| Studio 101–301 | Use Studio | — | Flow vs Artifacts guide; examples | Decision tables | 201 split if long | High |
| Wizard 101–301 | Run sessions | — | 12-step table; mission modes | Step matrix; mode pages | 201 split | High |
| Lenses troubleshooting | Recover | — | Group Studio vs Wizard issues | Triage table | Optional | Medium |

Use [target-outlines.md](target-outlines.md) for the approved target shape per page.
