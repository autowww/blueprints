#!/usr/bin/env python3
"""
Stage blueprint *.md files for GitHub Wiki: copy tree, fix links wiki cannot resolve.
Run from repo root via sync-wiki.sh (sets BLUEPRINTS_ROOT, WIKI_STAGE).
"""
from __future__ import annotations

import os
import re
import pathlib

ROOT = pathlib.Path(os.environ["BLUEPRINTS_ROOT"]).resolve()
OUT = pathlib.Path(os.environ["WIKI_STAGE"]).resolve()
REPO_BLOB = "https://github.com/autowww/blueprints/blob/main"

SKIP_TOP = frozenset({"wiki-source", ".git"})
# Template stubs are noisy in the wiki; keep real READMEs under templates/
SKIP_NAME_SUFFIX = ".template.md"


def iter_sources() -> list[tuple[pathlib.Path, str]]:
    found: list[tuple[pathlib.Path, str]] = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if rel.parts[0] in SKIP_TOP:
            continue
        if rel.name.endswith(SKIP_NAME_SUFFIX):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        found.append((rel, text))
    return found


def transform(rel: pathlib.Path, text: str) -> str:
    s = str(rel).replace("\\", "/")

    def blob_sdlc_docs(m: re.Match[str]) -> str:
        return f"]({REPO_BLOB}/sdlc/docs/{m.group(1)})"

    # Handbook HTML: wiki has no sibling file — link to GitHub code browser
    if s.startswith("sdlc/"):
        text = re.sub(r"\]\(docs/([^)]+\.html)\)", blob_sdlc_docs, text)
        text = text.replace("blueprints/agents/", "../agents/")
        text = text.replace("blueprints/sdlc/docs/", f"{REPO_BLOB}/sdlc/docs/")

    if s.startswith("sdlc/methodologies/"):
        text = re.sub(r"\]\(\.\./docs/([^)]+\.html)\)", blob_sdlc_docs, text)
        # e.g. methodologies/ceremonies/README.md → ../../docs/…
        text = re.sub(r"\]\(\.\./\.\./docs/([^)]+\.html)\)", blob_sdlc_docs, text)

    if s.startswith("agents/"):
        text = re.sub(r"\]\(\.\./sdlc/docs/([^)]+\.html)\)", blob_sdlc_docs, text)

    return text


def write_sidebar(rel_paths: list[pathlib.Path]) -> None:
    by_top: dict[str, list[pathlib.Path]] = {}
    for rel in rel_paths:
        top = rel.parts[0]
        by_top.setdefault(top, []).append(rel)

    lines = [
        "### [Home](Home)",
        "",
        "_Mirrored from [`autowww/blueprints`](https://github.com/autowww/blueprints) — run `wiki-source/sync-wiki.sh` to refresh._",
        "",
    ]
    order = ("sdlc", "docs", "agents")
    for top in list(order) + sorted(k for k in by_top if k not in order):
        if top not in by_top:
            continue
        title = top.upper() if top.islower() else top
        lines.append(f"### {title}")
        for rel in sorted(by_top[top]):
            # Wiki page path: path without .md (slashes allowed)
            page = str(rel.with_suffix("")).replace("\\", "/")
            label = rel.name.removesuffix(".md")
            if label == "README":
                label = f"{rel.parent.name}/README" if rel.parent != pathlib.Path(".") else "README"
            lines.append(f"- [{label}]({page})")
        lines.append("")

    (OUT / "_Sidebar.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    if OUT.exists():
        for child in OUT.iterdir():
            if child.is_file():
                child.unlink()
            else:
                import shutil

                shutil.rmtree(child)
    OUT.mkdir(parents=True, exist_ok=True)

    rel_paths: list[pathlib.Path] = []
    for rel, text in iter_sources():
        out_path = OUT / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(transform(rel, text), encoding="utf-8")
        rel_paths.append(rel)

    write_sidebar(rel_paths)
    print(f"Staged {len(rel_paths)} markdown files + _Sidebar.md under {OUT}")


if __name__ == "__main__":
    main()
