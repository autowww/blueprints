# Maintaining the documentation portal

This folder (`docs/`) is the **overarching documentation portal** for the blueprint framework. It provides a single HTML entry point (`index.html`) and the shared cross-area navigation bar used by all handbook pages.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Portal landing page — framework overview, area cards, adoption guide. |
| `assets/portal-nav.js` | Self-contained JavaScript that injects a fixed top navigation bar into any page. |
| `MAINTENANCE.md` | This file. |

## Shared top bar (`portal-nav.js`)

Every handbook HTML page includes one `<script>` tag before `</body>`:

```html
<script src="../../docs/assets/portal-nav.js" data-root="../.."></script>
```

The `data-root` attribute is the relative path from the current page to the **blueprints root** directory. The script uses it to compute links to each area's handbook.

### Adding a new area

1. Create the area's HTML handbook (e.g. `<area>/docs/index.html`).
2. Open `docs/assets/portal-nav.js` and add an entry to the `AREAS` array.
3. Add a card to `docs/index.html`.
4. Run `docs/inject-portal-nav.py` to add the `<script>` tag to the new handbook's HTML files.

### Updating the top bar

Edit `portal-nav.js` once — all pages that include it pick up the change automatically.

## Injecting the top bar into new pages

Use the helper script:

```bash
python3 docs/inject-portal-nav.py
```

It scans all `.html` files under handbook directories, inserts the `<script>` tag before `</body>` if not already present, and computes the correct `data-root` value. Safe to re-run (idempotent).

## Portal landing page

When blueprint areas change significantly, update `docs/index.html`:
- Area cards (add/remove/rename).
- Relationship diagram.
- "Last updated" date in the footer.
