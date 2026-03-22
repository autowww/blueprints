#!/usr/bin/env python3
"""Inject the shared portal-nav.js <script> tag into all handbook HTML files.

Run from the blueprints root:
    python3 docs/inject-portal-nav.py

Idempotent: skips files that already contain the portal-nav.js reference.
"""
from __future__ import annotations

import os
from pathlib import Path

BLUEPRINTS_ROOT = Path(__file__).resolve().parent.parent
PORTAL_NAV_FILENAME = "portal-nav.js"

HANDBOOK_DIRS = [
    BLUEPRINTS_ROOT / "sdlc" / "docs",
    BLUEPRINTS_ROOT / "pdlc" / "docs",
    BLUEPRINTS_ROOT / "product" / "docs",
    BLUEPRINTS_ROOT / "disciplines" / "governance" / "pm" / "docs",
    BLUEPRINTS_ROOT / "disciplines" / "product" / "ba" / "docs",
]

SCRIPT_MARKER = "portal-nav.js"


def compute_data_root(html_path: Path) -> str:
    """Compute the relative path from html_path's directory to BLUEPRINTS_ROOT."""
    rel = os.path.relpath(BLUEPRINTS_ROOT, html_path.parent)
    return rel


def compute_script_src(html_path: Path) -> str:
    """Compute the relative path from html_path's directory to docs/assets/portal-nav.js."""
    target = BLUEPRINTS_ROOT / "docs" / "assets" / PORTAL_NAV_FILENAME
    rel = os.path.relpath(target, html_path.parent)
    return rel


def inject(html_path: Path) -> bool:
    """Insert <script> before </body>. Returns True if the file was modified."""
    text = html_path.read_text(encoding="utf-8")

    if SCRIPT_MARKER in text:
        return False

    src = compute_script_src(html_path)
    data_root = compute_data_root(html_path)
    tag = f'  <script src="{src}" data-root="{data_root}"></script>\n'

    idx = text.rfind("</body>")
    if idx == -1:
        return False

    new_text = text[:idx] + tag + text[idx:]
    html_path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    modified = 0
    skipped = 0
    for d in HANDBOOK_DIRS:
        if not d.is_dir():
            print(f"  skip (not found): {d.relative_to(BLUEPRINTS_ROOT)}")
            continue
        for html in sorted(d.rglob("*.html")):
            if inject(html):
                print(f"  injected: {html.relative_to(BLUEPRINTS_ROOT)}")
                modified += 1
            else:
                skipped += 1
    print(f"\nDone. Modified: {modified}, already present: {skipped}.")


if __name__ == "__main__":
    main()
