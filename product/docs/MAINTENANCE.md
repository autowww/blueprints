# Maintaining the product blueprint handbook

Per-area **`blueprints/product/docs/*.html`** handbooks are **no longer maintained in Git**. The browser handbook is generated from blueprint Markdown by CI.

## Source of truth

| Canonical (edit first) | Published handbook |
|------------------------|--------------------|
| [`../STRUCTURE.md`](../STRUCTURE.md) | Generated HTML under **`blueprints/website/`** (e.g. `product--*.html`) |
| [`../README.md`](../README.md) | Same build |
| [`../POLICY.md`](../POLICY.md) | Same build |

## Build

From **`blueprints/`**:

```bash
python3 generator/build-handbook.py product
```

Or use **`--all`** to regenerate every area. Output is a **flat** `website/` directory (area-prefixed filenames).

## When `blueprints/product` changes

1. Edit **`STRUCTURE.md`**, **`README.md`**, or **`POLICY.md`** as needed.  
2. Run the generator (or wait for CI) so **`website/product--*.html`** matches.  
3. For repo-wide build and deployment details, see [Maintaining the documentation (repo-wide)](https://github.com/autowww/blueprints/blob/main/docs/MAINTENANCE.md).

---

*This file is for maintainers; it is not part of the frozen blueprint prose itself.*
