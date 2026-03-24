#!/usr/bin/env bash
# Compare forge/forge.config.yaml versona.* flags to .cursor/rules/ versona-*.mdc presence.
# Usage: run from repository root. Requires Python 3 + PyYAML.
set -euo pipefail

ROOT="${1:-.}"
CFG="${ROOT}/forge/forge.config.yaml"
RULES="${ROOT}/.cursor/rules"

die() { echo "Error: $*" >&2; exit 1; }

[[ -f "$CFG" ]] || die "missing $CFG (run forge-init.sh first or pass repo root as \$1)"

python3 <<'PY' "$CFG" "$RULES"
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "PyYAML is required: pip install pyyaml\n"
        "Or use the manual tables in CURSOR-RULES-ALIGNMENT.md",
        file=sys.stderr,
    )
    sys.exit(2)

cfg_path = Path(sys.argv[1])
rules_dir = Path(sys.argv[2])

with cfg_path.open(encoding="utf-8") as f:
    data = yaml.safe_load(f) or {}

versona = data.get("versona") or {}
families = (versona.get("families") or {})
cc = (versona.get("cross_cutting") or {})
eng = (versona.get("engineering_disciplines") or {})
prod = (versona.get("product_disciplines") or {})

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

# de-dupe preserve order
seen = set()
uniq = []
for x in expected:
    if x not in seen:
        seen.add(x)
        uniq.append(x)

print("=== Forge Versona ↔ Cursor rules ===")
print(f"Config: {cfg_path}")
print(f"Rules:  {rules_dir}")
print()

missing = []
if not rules_dir.is_dir():
    print(f"! .cursor/rules/ does not exist — expected {len(uniq)} Versona rule(s) when you add them.")
    for name in uniq:
        missing.append(name)
else:
    for name in uniq:
        p = rules_dir / name
        if p.is_file():
            print(f"  ok  {name}")
        else:
            print(f"  MISSING  {name}")
            missing.append(name)

print()
if missing:
    print(f"Summary: {len(missing)} missing (copy from blueprints/.../versona/*.mdc.template).")
    print("See: blueprints/sdlc/methodologies/forge/setup/CURSOR-RULES-ALIGNMENT.md")
    sys.exit(1)
print("All expected Versona rules present.")
PY
