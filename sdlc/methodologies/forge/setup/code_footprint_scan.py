#!/usr/bin/env python3
"""Readonly code-footprint scan for Forge / Blueprints-consuming repositories."""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_PROFILE = "tight"
DEFAULT_MAX_FILES = 100
TOKEN_CHARS = 4

BAND_ORDER = ("comfortable", "tight", "risky", "poor")

SOURCE_SUFFIXES = {
    ".c",
    ".cc",
    ".cpp",
    ".cs",
    ".css",
    ".go",
    ".h",
    ".hpp",
    ".html",
    ".java",
    ".jinja",
    ".j2",
    ".js",
    ".jsx",
    ".json",
    ".kt",
    ".kts",
    ".less",
    ".mjs",
    ".md",
    ".mdc",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".sass",
    ".scss",
    ".sh",
    ".toml",
    ".ts",
    ".tsx",
    ".vue",
    ".yaml",
    ".yml",
}

GENERATED_SUFFIXES = {
    ".lock",
    ".map",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".pdf",
    ".zip",
    ".gz",
}

DEFAULT_EXCLUDED_DIRS = {
    ".cache",
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "htmlcov",
    "node_modules",
    "out",
    "site",
    "static-export",
    "vendor",
    "venv",
    "website",
    "showcase",
}

DEFAULT_EXCLUDED_PATH_GLOBS = (
    "blueprints",
    "blueprints/*",
    "kitchensink",
    "kitchensink/*",
    "*/assets/vendor/*",
    "*/cdn/*",
    "*/generated/*",
    "*/tutorials/**/*.html",
    "*/tutorials/**/*.css",
    "*/tutorials/**/*.js",
    "*/website/*",
    "*/showcase/*",
    "*/dist/*",
    "*/build/*",
    "*/blueprints/*",
    "*/kitchensink/*",
)

LANGUAGE_BY_SUFFIX = {
    ".css": "css",
    ".go": "go",
    ".html": "html",
    ".java": "java",
    ".js": "javascript",
    ".jsx": "javascript",
    ".json": "json",
    ".kt": "kotlin",
    ".kts": "kotlin",
    ".less": "css",
    ".md": "markdown",
    ".mdc": "markdown",
    ".mjs": "javascript",
    ".py": "python",
    ".rb": "ruby",
    ".rs": "rust",
    ".sass": "css",
    ".scss": "css",
    ".sh": "shell",
    ".toml": "toml",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".vue": "vue",
    ".yaml": "yaml",
    ".yml": "yaml",
}


@dataclass(frozen=True)
class FootprintProfile:
    """Band ceilings and which bands appear in scan output."""

    name: str
    report_from_band: str
    comfortable_max_lines: int = 400
    comfortable_max_bytes: int = 24 * 1024
    comfortable_max_tokens: int = 3000
    tight_max_lines: int = 700
    tight_max_bytes: int = 48 * 1024
    tight_max_tokens: int = 6000
    risky_max_lines: int = 1500
    risky_max_bytes: int = 96 * 1024
    risky_max_tokens: int = 12000


PROFILES: dict[str, FootprintProfile] = {
    "comfortable": FootprintProfile(
        name="comfortable",
        report_from_band="tight",
    ),
    "tight": FootprintProfile(
        name="tight",
        report_from_band="risky",
    ),
    "strict": FootprintProfile(
        name="strict",
        report_from_band="tight",
    ),
}


@dataclass(frozen=True)
class Finding:
    path: str
    language: str
    lines: int
    bytes: int
    approx_tokens: int
    band: str
    profile: str
    reason: str
    suggestion: str


def _matches_any(path: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def _is_binary(path: Path) -> bool:
    try:
        with path.open("rb") as handle:
            chunk = handle.read(4096)
    except OSError:
        return True
    return b"\0" in chunk


def _should_skip_file(
    rel_posix: str,
    path: Path,
    *,
    include_patterns: list[str],
    exclude_patterns: list[str],
) -> bool:
    name = path.name
    suffix = path.suffix.lower()
    if _matches_any(rel_posix, exclude_patterns):
        return True
    if name.endswith((".min.js", ".min.css")):
        return True
    if suffix in GENERATED_SUFFIXES:
        return True
    if include_patterns:
        return not _matches_any(rel_posix, include_patterns)
    return suffix not in SOURCE_SUFFIXES


def _band(lines: int, size: int, tokens: int, profile: FootprintProfile) -> str:
    if (
        lines > profile.risky_max_lines
        or size > profile.risky_max_bytes
        or tokens > profile.risky_max_tokens
    ):
        return "poor"
    if (
        lines > profile.tight_max_lines
        or size > profile.tight_max_bytes
        or tokens > profile.tight_max_tokens
    ):
        return "risky"
    if (
        lines > profile.comfortable_max_lines
        or size > profile.comfortable_max_bytes
        or tokens > profile.comfortable_max_tokens
    ):
        return "tight"
    return "comfortable"


def _band_rank(band: str) -> int:
    try:
        return BAND_ORDER.index(band)
    except ValueError:
        return len(BAND_ORDER)


def _should_report(band: str, profile: FootprintProfile) -> bool:
    return _band_rank(band) >= _band_rank(profile.report_from_band)


def _reason(lines: int, size: int, tokens: int, band: str, profile: FootprintProfile) -> str:
    signals: list[str] = []
    if lines > profile.tight_max_lines:
        signals.append(f"{lines} LoC (tight target ≤{profile.tight_max_lines})")
    elif lines > profile.comfortable_max_lines:
        signals.append(f"{lines} LoC (comfortable ≤{profile.comfortable_max_lines})")
    if tokens > profile.tight_max_tokens:
        signals.append(f"~{tokens} tokens (tight ≤~{profile.tight_max_tokens})")
    elif tokens > profile.comfortable_max_tokens:
        signals.append(f"~{tokens} tokens (comfortable ≤~{profile.comfortable_max_tokens})")
    if size > profile.tight_max_bytes:
        signals.append(f"{size} bytes")
    if not signals:
        signals.append(f"band={band}")
    return ", ".join(signals)


def _suggestion(language: str, band: str) -> str:
    if band == "tight":
        return (
            "At default target ceiling — avoid growth; split before adding substantial behavior."
        )
    if band == "comfortable":
        return "Within comfortable band for one-pass LLM review."
    if language in {"markdown", "yaml", "json", "toml"}:
        return "Consider splitting catalog/config sections only if lookup and ownership stay clear."
    return (
        "Plan a semantic split: entrypoint, config, domain services, IO/adapters, "
        "rendering/reporting, tests/fixtures, or shared types. Add README.md or INDEX.md "
        "for any new folder."
    )


def _scan_file(root: Path, path: Path, *, profile: FootprintProfile) -> Finding | None:
    try:
        size = path.stat().st_size
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    lines = text.count("\n") + (0 if text.endswith("\n") or not text else 1)
    tokens = max(1, len(text) // TOKEN_CHARS)
    band = _band(lines, size, tokens, profile)
    if not _should_report(band, profile):
        return None
    suffix = path.suffix.lower()
    language = LANGUAGE_BY_SUFFIX.get(suffix, suffix.lstrip(".") or "text")
    rel = path.relative_to(root).as_posix()
    return Finding(
        path=rel,
        language=language,
        lines=lines,
        bytes=size,
        approx_tokens=tokens,
        band=band,
        profile=profile.name,
        reason=_reason(lines, size, tokens, band, profile),
        suggestion=_suggestion(language, band),
    )


def scan(
    root: Path,
    *,
    profile: FootprintProfile,
    max_files: int,
    include_patterns: list[str],
    exclude_patterns: list[str],
) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    excluded_patterns = [*DEFAULT_EXCLUDED_PATH_GLOBS, *exclude_patterns]

    for current_str, dirnames, filenames in os.walk(root):
        current = Path(current_str)
        rel_dir = "." if current == root else current.relative_to(root).as_posix()
        dirnames[:] = [
            dirname
            for dirname in dirnames
            if dirname not in DEFAULT_EXCLUDED_DIRS
            and not _matches_any(
                f"{rel_dir}/{dirname}" if rel_dir != "." else dirname,
                excluded_patterns,
            )
        ]
        for filename in filenames:
            path = current / filename
            rel_posix = path.relative_to(root).as_posix()
            if _should_skip_file(
                rel_posix,
                path,
                include_patterns=include_patterns,
                exclude_patterns=excluded_patterns,
            ):
                continue
            if _is_binary(path):
                continue
            finding = _scan_file(root, path, profile=profile)
            if finding:
                findings.append(finding)

    findings.sort(
        key=lambda item: (
            -_band_rank(item.band),
            -item.lines,
            item.path,
        )
    )
    return findings[:max_files]


def print_text(findings: list[Finding], root: Path, profile: FootprintProfile) -> None:
    print("=== Code footprint scan ===")
    print(f"Root: {root.resolve()}")
    print(f"Profile: {profile.name} (reports bands: {', '.join(BAND_ORDER[_band_rank(profile.report_from_band):])})")
    print(f"Default target band: tight (≤~{profile.tight_max_lines} LoC, ≤~{profile.tight_max_tokens} tokens)")
    print(f"Findings: {len(findings)}")
    if not findings:
        print("No files in reported bands for this profile.")
        return
    print()
    for item in findings:
        print(f"- {item.path}")
        print(
            f"  band={item.band} language={item.language} "
            f"lines={item.lines} bytes={item.bytes} approx_tokens={item.approx_tokens}"
        )
        print(f"  reason: {item.reason}")
        print(f"  suggestion: {item.suggestion}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Readonly scan for source files vs LLM footprint bands (default profile: tight)."
    )
    parser.add_argument("root", nargs="?", default=".", help="Repository root or directory to scan")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--max-files", type=int, default=DEFAULT_MAX_FILES)
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILES.keys()),
        default=DEFAULT_PROFILE,
        help=f"Scan profile (default: {DEFAULT_PROFILE} — report risky+poor)",
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Glob to include (can be repeated). Defaults to known source/control suffixes.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Additional repo-relative glob to exclude (can be repeated).",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = Path(args.root)
    if not root.is_dir():
        print(f"Error: scan root is not a directory: {root}", file=sys.stderr)
        return 2
    profile = PROFILES[args.profile]
    findings = scan(
        root,
        profile=profile,
        max_files=args.max_files,
        include_patterns=args.include,
        exclude_patterns=args.exclude,
    )
    if args.format == "json":
        print(json.dumps([asdict(item) for item in findings], indent=2))
    else:
        print_text(findings, root, profile)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
