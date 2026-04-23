# Public handbook migration (blueprints.forgesdlc.com)

This matrix tracks the shift from an implicit “mirror of Markdown” to a **curated product handbook** with explicit publication rules. Authoritative policy: [`DESIGN-PRINCIPLES.md`](DESIGN-PRINCIPLES.md).

| Phase | Scope | Actions | Exit criteria |
|-------|--------|---------|----------------|
| **P0** | Blueprints docs | Land DESIGN-PRINCIPLES, MAINTENANCE, POLICY cross-links, this file | Governance merged |
| **P1** | blueprints-website | `handbook-publish-manifest.yaml` bulk opt-in per framework area; generator filters by manifest + `public_publish` | Parity with prior public output until corpus is tightened |
| **P2** | blueprints-website | YAML frontmatter parsed; `nav_title` for labels | New pages can opt in/out without manifest-only edits |
| **P3** | blueprints-website | Sidebar and titles prefer `nav_title` | Spot-check navigation |
| **P4** | blueprints + forge-lenses | Remove or set `public_publish: false` on maintainer-heavy pages; split mixed content | Public site matches allowlists |
| **P5** | blueprints-website CI | `validate_handbook_public_metadata.py` (required keys when `public_publish: true`) | Green CI on `main` |

## Generator locations (blueprints-website)

| File | Role |
|------|------|
| `generator/handbook-publish-manifest.yaml` | Bulk include/exclude globs (paths relative to `blueprints/` submodule) |
| `generator/handbook_metadata.py` | Frontmatter parse, publish decision helpers |
| `generator/build-handbook.py` | Emits only publishable blueprint-area pages |
| `generator/tooling_handbooks.py` | Stages forge-lenses `docs/handbook-public/` through the same rules |
