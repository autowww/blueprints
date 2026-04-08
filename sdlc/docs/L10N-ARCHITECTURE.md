# Localization architecture (Forge workspace)

This document defines how **internationalization (i18n)** and **localization (l10n)** are implemented across standalone repositories: handbooks, product sites, Kitchen Sink chrome, Android, and CI. It complements **[`WORKSPACE-LOCALIZATION-SCOPE.md`](WORKSPACE-LOCALIZATION-SCOPE.md)** (supported locale list and policy).

**Status:** architecture and phased implementation. Generator and CI hooks described here may evolve; the **manifest schema** and **URL rules** below are stable contracts for tooling.

---

## 1. Goals

1. **Delta translation:** Only **changed source segments** (or changed Markdown files) enter the translation queue; unchanged content keeps existing translations (translation memory / segment locking).
2. **Incremental HTML build:** Regenerate **only** HTML for slugs (and locales) affected by new translations or English source changes, except when a **cold full build** is requested.
3. **Chrome vs body:** **Chrome** (nav, footer, skip links, template labels) uses small **locale bundles**; **body** uses long-form Markdown pipelines per locale.
4. **Excluded locales:** Never ship `ru*` or `be*` (see workspace scope doc).

---

## 2. URL and output layout

### 2.1 Handbook (blueprints.forgesdlc.com)

- **Default (English):** Flat slugs under `website/*.html` (current behavior).
- **Localized:** Optional second segment: `website/<locale>/…` for BCP-47 language tags (e.g. `de`, `fr`, `he`, `ar`). Example: `website/de/sdlc--index.html`.
- **Assets:** Shared under `website/assets/` (not duplicated per locale). HTML under `website/<locale>/` uses **relative** paths to assets computed per output file (e.g. `../assets/forge-theme.css` for one level of nesting).

### 2.2 Forge product site (forgesdlc.com)

- Same pattern: default English at `website/` root; optional `website/<locale>/` for localized builds.
- Nested routes (e.g. `blog/foo.html`) require **per-file** relative prefix to `website/assets/` (see generator `href_prefix_to_assets()`).

### 2.3 hreflang

When multiple locales exist for the same logical page, each page exposes `<link rel="alternate" hreflang="…" href="…">` for each locale version. The exact injection point is the site generator or a post-pass; **en** is typically `x-default` where appropriate.

---

## 3. Translation storage options

| Approach | Pros | Cons |
|----------|------|------|
| **Parallel Markdown trees** `l10n/<locale>/…` mirroring `blueprints/` | Git-friendly, review in PRs | Large repos; merge when English moves |
| **XLIFF / PO + TM** | Industry standard; good for delta/fuzzy | Extra export/import steps |
| **TMS (Phrase, Crowdin, …)** | Workflow, reviewers, TM | Cost; vendor lock-in |

**Recommendation:** Start with **parallel trees** or **XLIFF 2.0** exports from changed files only; add TMS when volume justifies it.

---

## 4. Published manifest (translation + build state)

**Purpose:** Drive **which** slugs need re-translation and **which** HTML outputs to rebuild.

**Location (convention):** `blueprints-website/l10n-state/published-manifest.json` (gitignored or committed per team policy). **forgesdlc** may use `forgesdlc/l10n-state/published-manifest.json` with the same schema for product pages.

### 4.1 Schema (version 1)

```json
{
  "schema_version": 1,
  "generated_at": "2026-04-06T12:00:00Z",
  "source_locale": "en",
  "pages": {
    "sdlc--documentation-structure.html": {
      "source_sha256": "…",
      "locales": {
        "de": { "content_sha256": "…", "built_at": "2026-04-05T10:00:00Z" },
        "fr": { "content_sha256": "…", "built_at": "2026-04-05T10:00:00Z" }
      }
    }
  }
}
```

- **Keys** of `pages` are **handbook flat slugs** (for bpw) or **site slug** strings like `blog/foo` / `index` (for forge), depending on the generator.
- **`source_sha256`:** hash of English source (Markdown or composed page input) at last successful publish.
- **`locales[tag].content_sha256`:** hash of translated **source** used to build that locale (or of resulting body if you standardize on one).
- **CI:** `diff` English → update `source_sha256` for touched slugs → enqueue translation for **delta** → on import, update locale hashes → **incremental build** only those slugs × locales.

### 4.2 Example file

See **`blueprints-website/generator/examples/l10n-manifest.example.json`** in the **blueprints-website** repository (sibling of the blueprints repo in the workspace).

---

## 5. CI: diff → changed slugs

The script **`l10n_diff_slugs.py`** (in `blueprints-website/generator/`) reports which **handbook slugs** are affected by Git changes under the `blueprints/` submodule. Use its JSON output to:

1. Feed a TMS “upload only these paths”.
2. Filter **`--only-slugs`** / **`--manifest`** for incremental **`build-handbook.py`** runs.

---

## 6. Generator flags (conventions)

### 6.1 `build-handbook.py` (blueprints-website)

| Flag | Purpose |
|------|---------|
| `--incremental` | With `--all`, **do not** delete all `website/*.html` before build |
| `--website-subdir DIR` | Write HTML under `website/DIR/` (e.g. `de`); assets stay in `website/assets/` |
| `--only-slugs a.html,b.html` | Build **only** listed flat filenames |
| `--manifest PATH` | JSON file with `{ "slugs": [ "..."] }` (subset of pages) |
| `--locale TAG` | BCP-47 tag passed to HTML `lang` and chrome bundle loader (future-facing) |

### 6.2 `build-site.py` (forgesdlc)

| Flag | Purpose |
|------|---------|
| `--incremental` | Build only slugs listed by `--only-slugs` / `--manifest` |
| `--website-subdir DIR` | Output under `website/DIR/` with per-file asset prefix |
| `--only-slugs` | Comma-separated slug list (`index`, `blog/foo`, …) |
| `--manifest PATH` | JSON `{ "slugs": [ ... ] }` |
| `--skip-tutorials` | Skip tutorial handbook phase when doing partial builds |

---

## 7. Kitchen Sink chrome bundles

Shared UI strings for handbook layouts live under **`forgesdlc-kitchensink/locale/`** as `chrome.<locale>.json`. Generators load the bundle for **`--locale`** and pass strings into **`assemble_handbook_page`** / **`handbook_page`**. Default **`en`** matches previous hardcoded English.

---

## 8. Android (Cynefin)

See project **`docs/CYNEFIN-L10N-ROLLOUT.md`**. UI uses `res/values` / `values-xx`; LLM response language remains separate from UI locale.

---

## 9. References

- [`WORKSPACE-LOCALIZATION-SCOPE.md`](WORKSPACE-LOCALIZATION-SCOPE.md) — which locales are in scope.
- Workspace root script **`sync-workspace-localization-scope.sh`** — syncs `WORKSPACE-LOCALIZATION-SCOPE.md` to each git repo.
