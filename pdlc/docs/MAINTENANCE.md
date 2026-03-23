# Maintaining the PDLC handbook

Per-area **`blueprints/pdlc/docs/*.html`** chapter files and nav assets are **no longer maintained in Git**. The browser handbook is generated from blueprint Markdown by CI into **`blueprints/website/`**.

## Source of truth

| Canonical (edit first) | Published handbook |
|------------------------|--------------------|
| [`../PDLC.md`](../PDLC.md) | Generated `pdlc--*.html` pages under **`blueprints/website/`** |
| [`../PDLC-SDLC-BRIDGE.md`](../PDLC-SDLC-BRIDGE.md) | Same build |
| [`../approaches/*.md`](../approaches/README.md) | Same build |
| [`../README.md`](../README.md) | Same build |
| [`../POLICY.md`](../POLICY.md) | Same build |

## Build

From **`blueprints/`**:

```bash
python3 generator/build-handbook.py pdlc
```

Or use **`--all`**. Filenames use the `pdlc--` prefix (flat `website/` directory).

## When `blueprints/pdlc` changes

1. Edit the Markdown sources above.  
2. Run **`generator/build-handbook.py`** (or rely on CI) so **`website/pdlc--*.html`** stays accurate.  
3. Global handbook architecture and CI are described in [`../../docs/MAINTENANCE.md`](../../docs/MAINTENANCE.md).

---

*This file is for maintainers; it is not part of the frozen process text itself.*
