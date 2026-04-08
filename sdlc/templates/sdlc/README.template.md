---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# SDLC — {{PROJECT_NAME}}

**Copy note:** Links below assume this file lives at **`sdlc/README.md`** (repo root). They are wrong if you open the template from `blueprints/sdlc/templates/sdlc/` — run `init-sdlc-workspace.sh` or adjust paths mentally.

**This folder is mutable.** Use it for anything **project-specific** about how we apply the SDLC: pointers, notes, decisions, or links—**not** for editing the frozen blueprint.

**Engineering tracking** (git-centric identity, work units, ceremonies) is documented as three Markdown files here — a **foundation**, a **methodologies** chapter (Scrum, Kanban, phased, XP), and **challenges** kept separate. They are **not** part of the frozen `blueprints/sdlc/` text. The SDLC handbook has a dedicated **[Methodologies & tracking](../blueprints/sdlc/docs/methodologies.html)** chapter (hierarchy + lenses) and links from the [handbook home](../blueprints/sdlc/docs/index.html). If you use [`docs/INDEX.md`](../docs/INDEX.md), add an **Engineering tracking** subsection (e.g. [`#engineering-tracking`](../docs/INDEX.md#engineering-tracking)). Bootstrap the same file set from [`SDLc-WORKSPACE.md`](../blueprints/sdlc/SDLc-WORKSPACE.md).

| What | Where |
|------|--------|
| **Frozen SDLC baseline** (do not change unless policy says so) | [`blueprints/sdlc/README`](../blueprints/sdlc/README.md) · [`POLICY.md`](../blueprints/sdlc/POLICY.md) |
| **Frozen product-functional IA** (if adopted) | [`blueprints/product/README`](../blueprints/product/README.md) · [`STRUCTURE.md`](../blueprints/product/STRUCTURE.md) |
| **Human handbook (SDLC, HTML)** | [`docs/index.html`](../blueprints/sdlc/docs/index.html) · [`MAINTENANCE.md`](../blueprints/sdlc/docs/MAINTENANCE.md) |
| **Human handbook (product functional, HTML)** (if adopted) | [`docs/index.html`](../blueprints/product/docs/index.html) |
| **Process text** | [`SDLC.md`](../blueprints/sdlc/SDLC.md) · [`DOCUMENTATION-STRUCTURE.md`](../blueprints/sdlc/DOCUMENTATION-STRUCTURE.md) |
| **Optional templates (SDLC)** | [`templates/`](../blueprints/sdlc/templates/README.md) |
| **Product functional templates** (if adopted) | [`templates/`](../blueprints/product/templates/README.md) |
| **Living product functional docs** | [`docs/product/`](../docs/product/INDEX.md) |
| **Project profile & stack** | [`docs/PROJECT.md`](../docs/PROJECT.md) |
| **Requirements, WBS, milestones, risks** | [`docs/requirements/`](../docs/requirements/INDEX.md) |
| **Roadmap (this repo)** | [`docs/ROADMAP.md`](../docs/ROADMAP.md) |
| **Documentation index** | [`docs/INDEX.md`](../docs/INDEX.md) |
| **Engineering tracking** | [`TRACKING-FOUNDATION.md`](TRACKING-FOUNDATION.md) · [`TRACKING-METHODOLOGIES.md`](TRACKING-METHODOLOGIES.md) · [`TRACKING-CHALLENGES.md`](TRACKING-CHALLENGES.md) |
| **CI/CD & quality gates** | [`docs/development/CI-CD.md`](../docs/development/CI-CD.md) |
| **Test plans** | [`docs/testing/README.md`](../docs/testing/README.md) |

Add files here (e.g. `NOTES.md`, `CHECKLIST.md`) when you need **project-only** SDLC guidance without modifying the blueprint.

---

*This folder is the working surface; **`blueprints/sdlc/`** is the canonical reusable SDLC template; **`blueprints/product/`** (if used) is the canonical product-functional IA; **`docs/product/`** holds project prose.*
