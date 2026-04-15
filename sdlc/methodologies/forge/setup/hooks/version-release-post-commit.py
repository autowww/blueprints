#!/usr/bin/env python3
"""
Post-commit helper: stamp Keep a Changelog [Unreleased], optionally auto-bump
PATCH in package.json, and finalize [Unreleased] when MAJOR or MINOR increases.

Invoked from .git/hooks/post-commit with repo root = cwd (git sets this).
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from fnmatch import fnmatch
from pathlib import Path
from typing import Any


SKIP_FILE = "FORGE_HOOK_SKIP"
SKIP_MARKERS = ("[skip-changelog]", "[skip-version]")


def _run_git(repo: Path, *args: str, check: bool = True) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        text=True,
        check=check,
    )
    return (r.stdout or "").strip()


def _git_head_files(repo: Path) -> list[str]:
    """Paths changed in HEAD (first parent only)."""
    out = _run_git(repo, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD")
    if not out:
        return []
    return out.splitlines()


def _is_merge_commit(repo: Path) -> bool:
    parents = _run_git(repo, "rev-list", "--parents", "-n", "1", "HEAD").split()
    # format: commit parent1 parent2...
    return len(parents) > 2


def _commit_message(repo: Path) -> str:
    return _run_git(repo, "log", "-1", "--format=%B")


def _commit_subject(repo: Path) -> str:
    return _run_git(repo, "log", "-1", "--format=%s")


def _load_manifest(repo: Path) -> dict[str, Any] | None:
    p = repo / ".forge" / "version-release.json"
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _paths_match(files: list[str], patterns: list[str]) -> bool:
    for f in files:
        for pat in patterns:
            if any(ch in pat for ch in "*?["):
                if fnmatch(f, pat):
                    return True
            elif f == pat or f.startswith(pat):
                return True
    return False


def _semver_tuple(v: str) -> tuple[int, int, int] | None:
    v = v.strip()
    if v.startswith("v"):
        v = v[1:]
    core = v.split("-", 1)[0].split("+", 1)[0]
    parts = core.split(".")
    if len(parts) < 3:
        return None
    try:
        return (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError:
        return None


def _version_change_kind(old_v: str | None, new_v: str | None) -> str | None:
    """major_minor | patch_only | None (same or not comparable)."""
    if not old_v or not new_v:
        return None
    to, tn = _semver_tuple(old_v), _semver_tuple(new_v)
    if to is None or tn is None:
        return None
    if tn < to:
        return None
    if tn[0] > to[0] or tn[1] > to[1]:
        return "major_minor"
    if tn[2] > to[2]:
        return "patch_only"
    return None


def _bump_patch_version(v: str) -> str | None:
    """Return X.Y.(Z+1) for plain numeric semver; None if prerelease or non-semver."""
    s = v.strip()
    if s.lower().startswith("v"):
        s = s[1:]
    if "-" in s or "+" in s:
        return None
    t = _semver_tuple(v)
    if t is None:
        return None
    return f"{t[0]}.{t[1]}.{t[2] + 1}"


def _npm_version_line_changed_in_diff(repo: Path, rel: str) -> bool:
    """True if HEAD commit touched the package.json version field vs HEAD~1."""
    r = subprocess.run(
        ["git", "diff", "HEAD~1", "HEAD", "--", rel],
        cwd=repo,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return False
    diff = r.stdout or ""
    if not diff.strip():
        return False
    for line in diff.splitlines():
        if not line.startswith(("+", "-")) or line.startswith(("+++", "---")):
            continue
        if '"version"' in line or "'version'" in line:
            return True
    return False


def _write_npm_version(repo: Path, rel: str, new_ver: str) -> None:
    p = repo / rel
    raw = p.read_text(encoding="utf-8")

    def repl(m: re.Match[str]) -> str:
        return f"{m.group(1)}{new_ver}{m.group(3)}"

    new_raw, n = re.subn(
        r'("version"\s*:\s*")([^"\n]+)(")',
        repl,
        raw,
        count=1,
    )
    if n != 1:
        raise ValueError(f"Could not replace single version field in {rel}")
    p.write_text(new_raw, encoding="utf-8")


def _read_npm_version(repo: Path, rel: str) -> str | None:
    p = repo / rel
    if not p.is_file():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    v = data.get("version")
    return v if isinstance(v, str) else None


def _read_file_at_rev(repo: Path, rev: str, rel: str) -> str | None:
    r = subprocess.run(
        ["git", "show", f"{rev}:{rel}"],
        cwd=repo,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return None
    return r.stdout


def _npm_version_from_blob(blob: str | None) -> str | None:
    if not blob:
        return None
    try:
        data = json.loads(blob)
    except json.JSONDecodeError:
        return None
    v = data.get("version")
    return v if isinstance(v, str) else None


def _first_npm_version_file(version_files: list[dict[str, Any]]) -> str | None:
    for spec in version_files:
        rel = spec.get("path")
        kind = spec.get("kind")
        if isinstance(rel, str) and rel and kind == "npm":
            return rel
    return None


def _head_vs_parent_npm_versions(
    repo: Path, rel: str
) -> tuple[str | None, str | None]:
    """(old_version, new_version) from HEAD~1 and HEAD trees."""
    p = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD~1"],
        cwd=repo,
        capture_output=True,
    )
    if p.returncode != 0:
        return None, None
    new_v = _read_npm_version(repo, rel)
    old_v = _npm_version_from_blob(_read_file_at_rev(repo, "HEAD~1", rel))
    return old_v, new_v


def _section_from_subject(subject: str, default: str) -> str:
    s = subject.lower()
    if s.startswith("feat") or s.startswith("feature"):
        return "Added"
    if s.startswith("fix") or s.startswith("hotfix"):
        return "Fixed"
    return default


def _stamp_unreleased(
    text: str,
    subject: str,
    section: str,
) -> str | None:
    """Append one bullet under [Unreleased] if not already present for this subject line."""
    rx = re.compile(r"^## \[Unreleased\]\s*\n(.*?)(?=^## \[)", re.M | re.S)
    m = rx.search(text)
    if not m:
        return None
    inner = m.group(1)
    bullet = f"- {subject.strip()}"
    if bullet in inner:
        return None

    sec_heading = f"### {section}\n"
    if sec_heading in inner:
        before, after = inner.split(sec_heading, 1)
        lines_after = after.splitlines(keepends=True)
        insert_at = 0
        while insert_at < len(lines_after):
            line = lines_after[insert_at]
            if line.startswith("### "):
                break
            insert_at += 1
        new_lines = lines_after[:insert_at] + [f"{bullet}\n"] + lines_after[insert_at:]
        new_inner = before + sec_heading + "".join(new_lines)
    else:
        new_inner = inner.rstrip() + f"\n\n{sec_heading}\n{bullet}\n"

    new_block = f"## [Unreleased]\n{new_inner}"
    return text[: m.start()] + new_block + text[m.end() :]


def _finalize_unreleased(text: str, new_ver: str, date_str: str) -> str | None:
    rx = re.compile(r"^## \[Unreleased\]\s*\n(.*?)(?=^## \[)", re.M | re.S)
    m = rx.search(text)
    if not m:
        return None
    body = m.group(1).rstrip() + "\n"
    replacement = f"## [Unreleased]\n\n## [{new_ver}] — {date_str}\n{body}"
    return text[: m.start()] + replacement + text[m.end() :]


def _write_skip(repo: Path) -> None:
    p = repo / ".git" / SKIP_FILE
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("1\n", encoding="utf-8")


def _consume_skip(repo: Path) -> bool:
    p = repo / ".git" / SKIP_FILE
    if p.is_file():
        try:
            p.unlink()
        except OSError:
            pass
        return True
    return False


def post_commit(repo: Path) -> int:
    if os.environ.get("CI"):
        return 0
    if _consume_skip(repo):
        return 0
    if _is_merge_commit(repo):
        return 0

    msg = _commit_message(repo)
    if any(x in msg for x in SKIP_MARKERS):
        return 0

    manifest = _load_manifest(repo)
    if not manifest:
        return 0

    changelog_rel = manifest.get("changelog")
    if not isinstance(changelog_rel, str) or not changelog_rel:
        return 0

    prefixes = manifest.get("watch_path_prefixes") or manifest.get("watch_paths")
    if not isinstance(prefixes, list):
        prefixes = []
    prefixes = [p for p in prefixes if isinstance(p, str)]

    version_files = manifest.get("version_files")
    if not isinstance(version_files, list):
        version_files = []

    changed = _git_head_files(repo)
    default_section = manifest.get("default_section")
    if not isinstance(default_section, str) or default_section not in (
        "Added",
        "Changed",
        "Fixed",
        "Removed",
        "Deprecated",
        "Security",
    ):
        default_section = "Changed"

    ch_path = repo / changelog_rel
    if not ch_path.is_file():
        return 0

    text = ch_path.read_text(encoding="utf-8")
    orig_ch = text
    new_text = text

    auto_patch = manifest.get("auto_patch")
    if auto_patch is None:
        auto_patch = True
    if not isinstance(auto_patch, bool):
        auto_patch = True

    rel_npm = _first_npm_version_file(version_files)
    old_v, new_v = (None, None)
    if rel_npm:
        old_v, new_v = _head_vs_parent_npm_versions(repo, rel_npm)

    # Stamp first so the current commit subject rolls into the same release
    # when a human raises MAJOR/MINOR (finalize runs next).
    if prefixes and _paths_match(changed, prefixes):
        subject = _commit_subject(repo)
        sec = _section_from_subject(subject, default_section)
        stamped = _stamp_unreleased(new_text, subject, sec)
        if stamped is not None:
            new_text = stamped

    # Finalize [Unreleased] only when humans raise MAJOR or MINOR vs parent.
    if rel_npm and old_v and new_v:
        kind = _version_change_kind(old_v, new_v)
        if kind == "major_minor" and not re.search(
            rf"^## \[{re.escape(new_v)}\]", new_text, re.M
        ):
            date_str = datetime.now(timezone.utc).date().isoformat()
            fin = _finalize_unreleased(new_text, new_v, date_str)
            if fin is not None:
                new_text = fin

    patch_bumped = False
    if (
        auto_patch
        and rel_npm
        and (repo / rel_npm).is_file()
        and prefixes
        and _paths_match(changed, prefixes)
        and old_v is not None
        and not _npm_version_line_changed_in_diff(repo, rel_npm)
    ):
        cur = _read_npm_version(repo, rel_npm)
        nxt = _bump_patch_version(cur) if cur else None
        if nxt and cur != nxt:
            _write_npm_version(repo, rel_npm, nxt)
            patch_bumped = True

    ch_changed = new_text != orig_ch
    if not ch_changed and not patch_bumped:
        return 0

    if ch_changed:
        ch_path.write_text(new_text, encoding="utf-8")

    _write_skip(repo)
    to_add = [changelog_rel] if ch_changed else []
    if patch_bumped:
        to_add.append(rel_npm)
    subprocess.run(["git", "add", *to_add], cwd=repo, check=True)
    subprocess.run(
        ["git", "commit", "--amend", "--no-edit", "--no-verify"],
        cwd=repo,
        check=True,
    )
    return 0


def main(argv: list[str]) -> int:
    repo = Path.cwd()
    if len(argv) > 1 and argv[1] == "--repo":
        repo = Path(argv[2]).resolve()
    if not (repo / ".git").exists():
        return 0
    return post_commit(repo)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
