# Maintaining the human handbook (`docs/`)

This folder holds **HTML + assets** for people who prefer a browser view over raw Markdown.

## Source of truth

| Canonical (edit first) | Human handbook (update when canonical changes) |
|------------------------|-----------------------------------------------|
| [`../STRUCTURE.md`](../STRUCTURE.md) | [`index.html`](index.html) — IA, principles, document types, relationships |
| [`../README.md`](../README.md) | [`index.html`](index.html) — overview / adopt steps if they change |
| [`../POLICY.md`](../POLICY.md) | [`index.html`](index.html) — governance section |

## When `blueprints/docs` changes

1. Edit **`STRUCTURE.md`**, **`README.md`**, or **`POLICY.md`** as needed.  
2. **Propose or apply matching updates** to **`docs/index.html`** so the handbook stays accurate.  
3. Bump the **“last aligned”** date in [`index.html`](index.html) (footer) and in this file if you keep a changelog here.

## UI stack (handbook)

| Piece | Role |
|-------|------|
| **[Tailwind CSS](https://tailwindcss.com)** (CDN in `index.html`) | Layout, typography, responsive sidebar. |
| **`assets/docs-theme.css`** | Smooth scroll, table chrome, skip-link, sidebar scrollbar. |
| **Google Fonts** | Fraunces (headings) + Plus Jakarta Sans (body). |

## Viewing locally

Open `blueprints/docs/docs/index.html` in a browser (`file://` works). For strict relative-path testing, run `python -m http.server` from `docs/`.

---

*This file is for maintainers; it is not part of the frozen blueprint prose itself.*
