# Documentation design principles

Standards for Markdown sources and generated documentation across the blueprint framework.

## 0. Multi-surface documentation architecture

Blueprint `.md` files are the **single source of truth** in this repository. They may feed several surfaces; each surface has a distinct lens:

| Surface | Lens | Audience | Repo |
|---------|------|----------|------|
| **GitHub / clone** | Full corpus; engineering reference | Contributors, readers browsing the repo | `blueprints` |
| **blueprints.forgesdlc.com** | **Curated product handbook** — user-oriented technical content only | Engineers, architects, team leads adopting the framework | Built from `blueprints` via **blueprints-website** |
| **GitHub Wiki** (optional) | Pure engineering quick reference | Developers using blueprints day-to-day | `blueprints` |
| **forgesdlc.com** | Forge SDLC methodology product | CTOs, managers, methodology coaches | `forgesdlc` |

**Important:** **blueprints.forgesdlc.com is not a mirror** of every Markdown file in the repository. It publishes only what is **explicitly allowed** by publication metadata (see §2). Maintainer, internal, and build-oriented docs remain in the repo and on GitHub; they are **excluded** from the public handbook unless explicitly opted in and appropriate for end readers.

No full-page copies between surfaces — only **cross-references** with short summaries around a link.

## 1. Public handbook vs repository mirror

| Where | What it contains |
|-------|------------------|
| **Repository (GitHub)** | Full framework text: methodology, templates, policies, maintainer notes, ADRs, architecture notes, and work-in-progress — **complete** |
| **blueprints.forgesdlc.com** | **Subset**: technical, **user-oriented** pages — setup, adoption, correct usage, workflows, examples, recipes, upgrades, troubleshooting — **only if** `public_publish` is true (see §2) |
| **Maintainer / internal** | May stay in-repo under `docs/`, package READMEs, or area trees; must be marked **maintainer** or **internal** in metadata and **excluded** from the public build (`public_publish: false` or omitted from manifest allowlists) |

The old rule “every Markdown file gets an HTML page on the public site” is **obsolete**. The correct statements are:

- Every tracked framework `.md` remains **authoritative source** for the repo and for workflows that consume raw Markdown.
- Only **opt-in** pages appear on **blueprints.forgesdlc.com** (manifest + per-file `public_publish: true`).

## 2. Publication metadata (frontmatter + manifest)

Public publishing is **explicit opt-in**, not default-all.

### 2.1 Per-file YAML frontmatter

When present, frontmatter is **authoritative** for that file’s publication flags. The **canonical field list**, CI rules, and manifest flags are documented in **blueprints-website** at [`generator/PUBLIC-HANDBOOK-METADATA.md`](https://github.com/autowww/blueprints-website/blob/main/generator/PUBLIC-HANDBOOK-METADATA.md) (handbook repo, not this corpus).

Summary for authors:

```yaml
---
audience: public              # public | operator | maintainer | internal
public_publish: true          # must be true for public handbook emission when manifest requires explicit opt-in
handbook_area: blueprints      # blueprints | lenses | studio | wizard
learning_level: reference      # overview | 101 | 201 | 301 | troubleshooting | reference
nav_group: SDLC                # optional; logical IA bucket (human label, not a path)
nav_title: Adopt Forge in your repo   # optional; human outcome-oriented title for nav and page title
tier: 201                      # optional; depth hint (101 / 201 / 301)
product_area: blueprints       # optional; Lenses/Studio/Wizard still use this for legacy tooling
---
```

| Field | Purpose |
|-------|---------|
| `audience` | Who the page is **for**. `maintainer` / `internal` never emit to the public handbook. |
| `public_publish` | **`true`** only if the page may appear on blueprints.forgesdlc.com (plus manifest allowlist). |
| `handbook_area` | Product surface for handbook policy (`blueprints` vs **lenses** / **studio** / **wizard**). |
| `learning_level` | Depth / intent (`overview` … `reference`). |
| `nav_group` | Grouping for navigation design (not a file path). |
| `nav_title` | Optional override for sidebar and `<title>`; must be **human outcome-oriented**, not a filename or path. |

### 2.2 Manifest (strict allowlist)

The **blueprints-website** repo contains [`generator/handbook-publish-manifest.yaml`](https://github.com/autowww/blueprints-website/blob/main/generator/handbook-publish-manifest.yaml): paths relative to the `blueprints/` submodule.

When **`strict_public_allowlist`** is **true**, a file publishes only if it matches **`public_allowlist_globs`** (or legacy **`include_globs`** if the allowlist is empty) and does **not** match **`exclude_globs`**, and frontmatter does not set `public_publish: false`. When **`require_explicit_public_publish`** is **true**, each published page must also set **`public_publish: true`**. Maintainer-only or repo-shaped pages belong in **`exclude_globs`** (or in GitHub-only trees such as `docs/`).

The **forge-lenses** subsection still lists explicit filenames under `docs/handbook-public/`, each with **`public_publish: true`** in frontmatter.

## 3. Audience, tier, and publication matrix

- **Tier** (101 / 201 / 301) describes **depth**.
- **Audience** describes **who** may rely on the page.
- **public_publish** describes **whether** the page may appear on the public handbook.

Together they replace “tier alone decides everything.” Example: a **301** page for **maintainers** belongs in the repo but typically has `public_publish: false` on the public site.

## 4. Forbidden on the public handbook

The following **must not** appear as **public** content on blueprints.forgesdlc.com (use `public_publish: false` or keep out of manifest allowlists):

- ADRs and product-internal architecture decisions
- Package layouts, file maps, module maps, source-path inventories
- Implementation plans, roadmap/WBS for maintainers
- Docs-generator internals, raw “how this repo is built” pipelines
- Raw Markdown file inventories as **page content**
- Content whose primary purpose is describing repository structure for contributors

**Exception:** Discipline methodology may teach concepts such as “ADR practice” or “architecture views” as **user-facing** methodology when framed for adopters, not as internal product ADRs or repo maps.

## 5. Stricter rules: Lenses, Forge Studio, Blueprints Wizard

For `product_area` **lenses**, **studio**, or **wizard**, public pages are **stricter**. Public docs may include only:

- Purpose and scope
- Prerequisites
- Getting started
- 101 / 201 / 301 tutorials (aligned with tier)
- Task recipes
- Troubleshooting
- **Minimal** operator settings needed to use the feature safely

Anything else (internals, API route dumps, trust-model ADRs, package architecture) stays **maintainer** / **internal** and **off** the public handbook.

## 6. Human outcome-oriented navigation and titles

- **Navigation labels** and **page titles** must describe **outcomes** (“Adopt the SDLC blueprint”), not **implementation** (`sdlc/README.md`, `POLICY.md`).
- Do not use raw paths, filenames, or `.md` names as **visible** link or nav text.
- URLs may still use technical slugs until a renaming phase; **labels** must stay human.

The handbook builder may use `nav_title` from frontmatter for sidebar entries and HTML titles.

## 7. 101 / 201 / 301 tiering

| Tier | Name | Characteristics |
|------|------|----------------|
| **101** | Introduction | Self-contained. “What is this? When do I use it?” |
| **201** | Practical | How-to guides, integration patterns; references 101 without re-explaining. |
| **301** | Advanced | Extension points, deeper analysis; assumes 201. |

Guidelines:

- Prefer declaring `tier` in frontmatter for new and heavily edited pages.
- 101 content must stand alone; 301 may assume prior tiers.

## 8. Cross-referencing policy

| From → To | Policy |
|-----------|--------|
| GitHub Wiki → forgesdlc.com | Mention sparingly when pairing blueprints with ForgeSDLC |
| Public handbook → forgesdlc.com | Link freely for methodology context |
| Public handbook → GitHub | Link for canonical source and deeper reference |
| forgesdlc.com → public handbook | Link when technical depth is needed |

## 9. Human-friendly presentation

Raw Markdown is the source of truth; generated HTML must be **useful on first read**:

| Element | When to use |
|---------|-------------|
| **Tables** | Comparisons, role matrices, RACI charts |
| **Blueprint diagram fences (`blueprint-diagram`)** | Process flows, lifecycle mappings (static SVG templates on the handbook) |
| **Code examples** | CLI, configuration snippets |
| **Numbered steps** | Procedures, adoption guides |

Summary tables should link to detail pages where applicable.

## 10. Diagram-first authoring

Use **` ```blueprint-diagram `** / **` ```blueprint-diagram-expand `** fenced blocks. Maintainer-only details for templates and catalogs belong in **toolchain** docs, not in frozen framework text.

## 11. CSS framework and fonts

Handbook HTML uses Bootstrap 5.3 (CDN), Proxima Nova Black / Open Sans / Courier New — see the **blueprints-website** generator and Kitchensink theme.

## 12. Page layout pattern

Sidebar + main content + ToC + prev/next + canonical source banner — implemented by **forge-autodoc** and **blueprints-website**.

## 13. Portal navigation

Injected via `generator/inject-portal-nav.js` in the consumer repo; portal labels are **human** (see §6).

## 14. Markdown is the source of truth

- Edit Markdown first; regenerate HTML with **`generator/build-handbook.py`** in **blueprints-website**.
- Do not edit generated HTML directly.
- Canonical source links point at GitHub `.md` where appropriate.

## 15. Template rendering

Files ending in `.template.md` render with a **Template** banner when published.

## 16. Human-readable link text

Links **must** use descriptive text — never raw paths or URLs as the visible name.

| Bad | Good |
|-----|------|
| `` [`blueprints/sdlc/`](../sdlc/README.md) `` | `[SDLC handbook](...)` with descriptive text |
| Link text showing `.md` filename | Use the document’s purpose as link text |

## 17. Link targets and builder behavior

Cross-references use relative `.md` paths in source; **blueprints-website** rewrites them to flat HTML slugs for publishable targets. Unpublished targets should not be linked from public pages (or should link to GitHub instead).

## 18. Build workflow (blueprints-website)

```bash
python3 generator/build-handbook.py --all
python3 generator/inject-portal-nav.py
```

Publication decisions are implemented by **`handbook-publish-manifest.yaml`**, **`handbook_metadata.py`**, and **`build-handbook.py`**. See [`MAINTENANCE.md`](MAINTENANCE.md) and [`PUBLIC-HANDBOOK-MIGRATION.md`](PUBLIC-HANDBOOK-MIGRATION.md).

## Rationale (summary)

| Rule | Why |
|------|-----|
| Curated public handbook | Users need a **product** experience, not a dump of every internal note. |
| Stricter Lenses / Studio / Wizard | Shipping surfaces change quickly; avoid leaking internals and reduce support debt. |
| Exclude ADRs, maps, build internals | Keeps public docs **durable** and **safe** to share. |
| Maintainer docs in-repo, off public | Contributors need truth next to code; readers need clarity. |
| Human nav titles | Wayfinding beats implementation detail. |
| Explicit `public_publish` | Prevents accidental publication when adding files. |
| Tier + audience | Makes policy **machine-checkable** and reviewable. |
