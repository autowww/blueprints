#!/usr/bin/env python3
"""
Single source of truth: forge.config.yaml versona.* → expected Cursor rule filenames
and template paths under blueprints' forge/versona/.

Used by sync-forge-cursor-rules.sh, check-forge-cursor-alignment.sh, and install/diff wrappers.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path
from typing import Iterable

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

# Installed .cursor/rules name → path relative to forge/versona/ (with .template suffix)
VERSONA_TEMPLATE_REL: dict[str, str] = {
    "versona-se.mdc": "catalog/discipline/engineering/versona-se.mdc.template",
    "versona-architecture.mdc": "catalog/discipline/engineering/versona-architecture.mdc.template",
    "versona-devops.mdc": "catalog/discipline/engineering/versona-devops.mdc.template",
    "versona-testing.mdc": "catalog/discipline/engineering/versona-testing.mdc.template",
    "versona-frontend.mdc": "catalog/discipline/engineering/versona-frontend.mdc.template",
    "versona-mobile.mdc": "catalog/discipline/engineering/versona-mobile.mdc.template",
    "versona-iot.mdc": "catalog/discipline/engineering/versona-iot.mdc.template",
    "versona-bigdata.mdc": "catalog/discipline/data/versona-bigdata.mdc.template",
    "versona-datascience.mdc": "catalog/discipline/data/versona-datascience.mdc.template",
    "versona-product-management.mdc": "catalog/discipline/product/versona-product-management.mdc.template",
    "versona-ba.mdc": "catalog/discipline/product/versona-ba.mdc.template",
    "versona-ux.mdc": "catalog/discipline/product/versona-ux.mdc.template",
    "versona-marketing.mdc": "catalog/discipline/product/versona-marketing.mdc.template",
    "versona-cs.mdc": "catalog/discipline/product/versona-cs.mdc.template",
    "versona-pm.mdc": "catalog/discipline/governance/versona-pm.mdc.template",
    "versona-security.mdc": "catalog/discipline/cross-cutting/versona-security.mdc.template",
    "versona-compliance.mdc": "catalog/discipline/cross-cutting/versona-compliance.mdc.template",
}

# Optional Versona templates (CLI flags), basename → rel under versona/
OPTIONAL_VERSONA_TEMPLATE_REL: dict[str, str] = {
    "versona-all.mdc": "catalog/routing/versona-all.mdc.template",
    "versona-project-setup.mdc": "catalog/workflow/versona-project-setup.mdc.template",
    "versona-roadmap-gate.mdc": "catalog/workflow/versona-roadmap-gate.mdc.template",
    "versona-cursor-rules-sync.mdc": "catalog/workflow/versona-cursor-rules-sync.mdc.template",
    "versona-sampling.mdc": "catalog/meta/versona-sampling.mdc.template",
    "versona-generic.mdc": "versona-generic.mdc.template",
    "versona-family-engineering.mdc": "catalog/discipline/engineering/family/versona-family-engineering.mdc.template",
    "versona-family-data.mdc": "catalog/discipline/data/family/versona-family-data.mdc.template",
    "versona-family-product.mdc": "catalog/discipline/product/family/versona-family-product.mdc.template",
}

# Standard packaged Forge Cursor rules: filename → rel under blueprints root (already .mdc, not .template)
STANDARD_FORGE_CURSOR_RULES_REL: dict[str, str] = {
    "forge-daily.mdc": "sdlc/templates/forge/cursor-rules/forge-daily.mdc",
    "forge-planning.mdc": "sdlc/templates/forge/cursor-rules/forge-planning.mdc",
    "forge-versona.mdc": "sdlc/templates/forge/cursor-rules/forge-versona.mdc",
    "forge-setup.mdc": "sdlc/templates/forge/cursor-rules/forge-setup.mdc",
    "forge-product-manager.mdc": "sdlc/templates/forge/cursor-rules/forge-product-manager.mdc",
}

ENG_MAP = {
    "software_engineering": "versona-se.mdc",
    "software_architecture": "versona-architecture.mdc",
    "devops": "versona-devops.mdc",
    "testing": "versona-testing.mdc",
    "frontend": "versona-frontend.mdc",
    "mobile": "versona-mobile.mdc",
    "embedded_iot": "versona-iot.mdc",
}
PROD_MAP = {
    "product_management": "versona-product-management.mdc",
    "business_analysis": "versona-ba.mdc",
    "ux_design": "versona-ux.mdc",
    "marketing": "versona-marketing.mdc",
    "customer_success": "versona-cs.mdc",
}


def discover_blueprints_and_versona(repo_root: Path) -> tuple[Path, Path]:
    """Return (blueprints_root, versona_dir)."""
    repo_root = repo_root.resolve()
    bp = repo_root / "blueprints"
    v1 = bp / "sdlc" / "methodologies" / "forge" / "versona"
    if v1.is_dir():
        return bp, v1
    v2 = repo_root / "sdlc" / "methodologies" / "forge" / "versona"
    if v2.is_dir():
        return repo_root, v2
    raise FileNotFoundError(
        "Could not find forge/versona under "
        f"{repo_root / 'blueprints'} or {repo_root}. "
        "Use a consuming repo with blueprints/ submodule or run from blueprints repo root."
    )


def load_cfg(cfg_path: Path) -> dict:
    if yaml is None:
        print(
            "PyYAML is required: pip install pyyaml\n"
            "Or use the manual tables in CURSOR-RULES-ALIGNMENT.md",
            file=sys.stderr,
        )
        sys.exit(2)
    with cfg_path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def expected_versona_filenames(data: dict) -> list[str]:
    versona = data.get("versona") or {}
    families = versona.get("families") or {}
    cc = versona.get("cross_cutting") or {}
    eng = versona.get("engineering_disciplines") or {}
    prod = versona.get("product_disciplines") or {}

    expected: list[str] = []

    if families.get("engineering"):
        for key, fname in ENG_MAP.items():
            if eng.get(key):
                expected.append(fname)

    if families.get("data"):
        expected.extend(["versona-bigdata.mdc", "versona-datascience.mdc"])

    if families.get("product"):
        for key, fname in PROD_MAP.items():
            if prod.get(key):
                expected.append(fname)

    if families.get("governance"):
        expected.append("versona-pm.mdc")

    if cc.get("security"):
        expected.append("versona-security.mdc")
    if cc.get("compliance"):
        expected.append("versona-compliance.mdc")

    seen: set[str] = set()
    uniq: list[str] = []
    for x in expected:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    return uniq


def merge_install_options(args: argparse.Namespace) -> tuple[list[str], bool]:
    """
    Preset bundles optional Versona files + whether to copy standard Forge .mdc rules.
    --with-* flags add on top (additive). No --preset (or minimal) = YAML-driven Versonas only.
    """
    preset = getattr(args, "preset", None)
    if preset in (None, "minimal"):
        optional: list[str] = []
        wf = False
    elif preset == "recommended":
        optional = [
            "versona-all.mdc",
            "versona-project-setup.mdc",
            "versona-roadmap-gate.mdc",
            "versona-cursor-rules-sync.mdc",
        ]
        wf = True
    elif preset == "full":
        optional = [
            "versona-all.mdc",
            "versona-project-setup.mdc",
            "versona-roadmap-gate.mdc",
            "versona-cursor-rules-sync.mdc",
            "versona-family-engineering.mdc",
            "versona-family-data.mdc",
            "versona-family-product.mdc",
            "versona-generic.mdc",
        ]
        wf = True
    else:
        print(f"Error: unknown preset {preset!r}", file=sys.stderr)
        sys.exit(2)

    def add(name: str) -> None:
        if name not in optional:
            optional.append(name)

    if args.with_project_setup:
        add("versona-project-setup.mdc")
    if args.with_roadmap_gate:
        add("versona-roadmap-gate.mdc")
    if args.with_all_routing:
        add("versona-all.mdc")
    if args.with_family_product:
        add("versona-family-product.mdc")
    if args.with_family_engineering:
        add("versona-family-engineering.mdc")
    if args.with_family_data:
        add("versona-family-data.mdc")
    if args.with_sampling:
        add("versona-sampling.mdc")
    if args.with_generic:
        add("versona-generic.mdc")
    if args.with_cursor_rules_sync:
        add("versona-cursor-rules-sync.mdc")

    if args.with_standard_forge_rules:
        wf = True

    return optional, wf


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def cmd_check(args: argparse.Namespace) -> int:
    root = Path(args.repo_root).resolve()
    cfg = root / "forge" / "forge.config.yaml"
    rules = root / ".cursor" / "rules"
    if not cfg.is_file():
        print(f"Error: missing {cfg} (run forge-init.sh first)", file=sys.stderr)
        return 1

    data = load_cfg(cfg)
    uniq = expected_versona_filenames(data)

    print("=== Forge Versona ↔ Cursor rules ===")
    print(f"Config: {cfg}")
    print(f"Rules:  {rules}")
    print()

    missing: list[str] = []
    if not rules.is_dir():
        print(
            f"! .cursor/rules/ does not exist — expected {len(uniq)} Versona rule(s) when you add them."
        )
        missing = list(uniq)
    else:
        for name in uniq:
            p = rules / name
            if p.is_file():
                print(f"  ok  {name}")
            else:
                print(f"  MISSING  {name}")
                missing.append(name)

    print()
    if missing:
        print(
            f"Summary: {len(missing)} missing — run:\n"
            "  bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync\n"
            "See: blueprints/sdlc/methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md"
        )
        return 1
    print("All expected Versona rules present.")
    return 0


def collect_install_jobs(
    repo_root: Path,
    data: dict,
    *,
    optional_names: Iterable[str],
    with_standard_forge: bool,
) -> list[tuple[Path, Path, str]]:
    """
    Returns list of (src, dest, label) where dest is under .cursor/rules/name.
    """
    bp_root, versona_root = discover_blueprints_and_versona(repo_root)
    rules_dir = repo_root / ".cursor" / "rules"

    jobs: list[tuple[Path, Path, str]] = []

    for name in expected_versona_filenames(data):
        rel = VERSONA_TEMPLATE_REL.get(name)
        if not rel:
            print(f"Warning: no template mapping for {name}", file=sys.stderr)
            continue
        src = versona_root / rel
        if not src.is_file():
            print(f"Warning: missing template {src}", file=sys.stderr)
            continue
        jobs.append((src, rules_dir / name, "versona"))

    seen_opt: set[str] = set()
    for name in optional_names:
        if name in seen_opt:
            continue
        seen_opt.add(name)
        rel = OPTIONAL_VERSONA_TEMPLATE_REL.get(name)
        if not rel:
            print(f"Warning: unknown optional rule {name}", file=sys.stderr)
            continue
        src = versona_root / rel
        if not src.is_file():
            print(f"Warning: missing template {src}", file=sys.stderr)
            continue
        jobs.append((src, rules_dir / name, "versona_optional"))

    if with_standard_forge:
        for fname, rel in STANDARD_FORGE_CURSOR_RULES_REL.items():
            src = bp_root / rel
            if not src.is_file():
                print(f"Warning: missing {src}", file=sys.stderr)
                continue
            jobs.append((src, rules_dir / fname, "forge_standard"))

    return jobs


def cmd_install(args: argparse.Namespace) -> int:
    root = Path(args.repo_root).resolve()
    cfg = root / "forge" / "forge.config.yaml"
    if not cfg.is_file():
        print(f"Error: missing {cfg}", file=sys.stderr)
        return 1

    data = load_cfg(cfg)
    optional, wf = merge_install_options(args)

    jobs = collect_install_jobs(
        root,
        data,
        optional_names=optional,
        with_standard_forge=wf,
    )

    rules_dir = root / ".cursor" / "rules"
    if args.dry_run:
        print("=== sync-forge-cursor-rules install (dry-run) ===")
        print(f"Target: {rules_dir}")
        for src, dest, label in jobs:
            print(f"  [{label}] {src} -> {dest}")
        return 0

    rules_dir.mkdir(parents=True, exist_ok=True)
    copied = 0
    skipped = 0
    for src, dest, label in jobs:
        if dest.is_file() and not args.force:
            print(f"  skip (exists): {dest.name}")
            skipped += 1
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        print(f"  installed: {dest.name}  [{label}]")
        copied += 1

    print()
    print(f"Done. Installed {copied}, skipped {skipped} (use --force to overwrite).")
    print("Tune globs in each .mdc if you use file-scoped attachment.")
    return 0


def cmd_diff(args: argparse.Namespace) -> int:
    root = Path(args.repo_root).resolve()
    cfg = root / "forge" / "forge.config.yaml"
    if not cfg.is_file():
        print(f"Error: missing {cfg}", file=sys.stderr)
        return 1
    data = load_cfg(cfg)
    optional, wf = merge_install_options(args)

    jobs = collect_install_jobs(
        root,
        data,
        optional_names=optional,
        with_standard_forge=wf,
    )
    rules_dir = root / ".cursor" / "rules"

    print("=== Versona / Forge Cursor rules — diff vs blueprints templates ===")
    print(f"Rules dir: {rules_dir}")
    print()

    differing: list[str] = []
    missing_src: list[str] = []
    missing_dest: list[str] = []
    identical: list[str] = []

    for src, dest, label in jobs:
        if not src.is_file():
            missing_src.append(str(src))
            continue
        if not dest.is_file():
            missing_dest.append(dest.name)
            print(f"  MISSING  {dest.name}  (source: {src.name})  [{label}]")
            continue
        a, b = _sha256_file(src), _sha256_file(dest)
        if a == b:
            identical.append(dest.name)
            print(f"  same  {dest.name}  [{label}]")
        else:
            differing.append(dest.name)
            print(f"  DIFF  {dest.name}  [{label}]  (run install with --force to overwrite)")

    print()
    if missing_src:
        print("Missing source files (blueprints layout?):", len(missing_src))
    if differing or missing_dest:
        print(
            f"Summary: {len(differing)} differ, {len(missing_dest)} missing installed copy. "
            "Review local edits before --force."
        )
        return 1
    print("All present files match blueprint sources (for selected rules).")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    root = Path(args.repo_root).resolve()
    cfg = root / "forge" / "forge.config.yaml"
    if not cfg.is_file():
        print(f"Error: missing {cfg}", file=sys.stderr)
        return 1
    data = load_cfg(cfg)
    optional, wf = merge_install_options(args)
    jobs = collect_install_jobs(
        root,
        data,
        optional_names=optional,
        with_standard_forge=wf,
    )
    rules_dir = root / ".cursor" / "rules"

    print("=== Forge Cursor rules — status ===")
    preset = getattr(args, "preset", None)
    if preset:
        print(f"Preset: {preset}")
    print(f"Rules dir: {rules_dir}")
    print()

    missing: list[str] = []
    drift: list[str] = []
    ok_count = 0
    no_template: list[str] = []

    for src, dest, label in jobs:
        if not src.is_file():
            print(f"  ! no template  {dest.name}  [{label}]")
            no_template.append(dest.name)
            continue
        if not dest.is_file():
            print(f"  missing  {dest.name}  [{label}]")
            missing.append(dest.name)
            continue
        if _sha256_file(src) == _sha256_file(dest):
            print(f"  ok  {dest.name}  [{label}]")
            ok_count += 1
        else:
            print(f"  drift  {dest.name}  [{label}]")
            drift.append(dest.name)

    print()
    n_bad = len(missing) + len(drift) + len(no_template)
    setup_rel = "blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh"
    if preset in (None, "minimal"):
        suggest = f"bash {setup_rel} sync --force"
    else:
        suggest = f"bash {setup_rel} sync --preset {preset} --force"

    if n_bad:
        print(
            f"Summary: {ok_count} ok, {len(missing)} missing, {len(drift)} drift, "
            f"{len(no_template)} missing template in blueprints"
        )
        print(f"Next: {suggest}")
        return 1
    print(f"Summary: {ok_count} ok — all expected files present and match templates.")
    return 0


def _add_preset_and_optional_rule_flags(p: argparse.ArgumentParser) -> None:
    p.add_argument(
        "--preset",
        choices=["minimal", "recommended", "full"],
        default=None,
        help="Bundle: minimal (default, YAML Versonas only), recommended, or full",
    )
    p.add_argument("--with-project-setup", action="store_true")
    p.add_argument("--with-roadmap-gate", action="store_true")
    p.add_argument("--with-all-routing", action="store_true")
    p.add_argument("--with-family-product", action="store_true")
    p.add_argument("--with-family-engineering", action="store_true")
    p.add_argument("--with-family-data", action="store_true")
    p.add_argument("--with-sampling", action="store_true")
    p.add_argument("--with-generic", action="store_true")
    p.add_argument(
        "--with-cursor-rules-sync",
        action="store_true",
        help="Optional versona-cursor-rules-sync.mdc (also in recommended/full presets)",
    )
    p.add_argument(
        "--with-standard-forge-rules",
        action="store_true",
        help="Also copy forge-daily, forge-planning, forge-versona, forge-setup, forge-product-manager",
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Forge Versona Cursor rules: check, install, diff, status")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_check = sub.add_parser("check", help="Compare forge.config.yaml to .cursor/rules (like check-forge-cursor-alignment.sh)")
    p_check.add_argument("repo_root", nargs="?", default=".", help="Repository root (default: .)")
    p_check.set_defaults(func=cmd_check)

    p_inst = sub.add_parser("install", help="Copy Versona templates into .cursor/rules")
    p_inst.add_argument("repo_root", nargs="?", default=".", help="Repository root (default: .)")
    p_inst.add_argument("--dry-run", action="store_true")
    p_inst.add_argument("--force", action="store_true", help="Overwrite existing rule files")
    _add_preset_and_optional_rule_flags(p_inst)
    p_inst.set_defaults(func=cmd_install)

    p_diff = sub.add_parser("diff", help="SHA256 compare installed .mdc vs blueprint sources")
    p_diff.add_argument("repo_root", nargs="?", default=".", help="Repository root (default: .)")
    _add_preset_and_optional_rule_flags(p_diff)
    p_diff.set_defaults(func=cmd_diff)

    p_stat = sub.add_parser(
        "status",
        help="Per-file missing/drift/ok vs templates (exit 1 if any missing or drift)",
    )
    p_stat.add_argument("repo_root", nargs="?", default=".", help="Repository root (default: .)")
    _add_preset_and_optional_rule_flags(p_stat)
    p_stat.set_defaults(func=cmd_status)

    args = p.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
