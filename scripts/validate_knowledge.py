#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CARD_DIRS = ["mechanics", "skills", "classes", "crafting", "endgame", "farming", "economy", "builds", "items"]
REQUIRED = ["id", "module", "status", "confidence", "applies_to", "last_verified", "tags", "sources"]
ALLOWED_STATUS = {"OFFICIAL", "DATA_VERIFIED", "COMMUNITY_VERIFIED", "INFERENCE", "DISPUTED", "NEEDS_RETEST", "OBSOLETE"}

errors = []
seen_ids = set()
for dirname in CARD_DIRS:
    base = ROOT / dirname
    if not base.exists():
        continue
    for path in base.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        parts = text.split("---\n", 2)
        if len(parts) < 3:
            errors.append(f"{path.relative_to(ROOT)}: malformed frontmatter")
            continue
        fm = parts[1]
        values = {}
        for line in fm.splitlines():
            m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
            if m:
                values[m.group(1)] = m.group(2).strip().strip('"')
        for key in REQUIRED:
            if key not in values:
                errors.append(f"{path.relative_to(ROOT)}: missing {key}")
        kid = values.get("id")
        if kid:
            if kid in seen_ids:
                errors.append(f"{path.relative_to(ROOT)}: duplicate id {kid}")
            seen_ids.add(kid)
        status = values.get("status")
        if status and status not in ALLOWED_STATUS:
            errors.append(f"{path.relative_to(ROOT)}: invalid status {status}")

if errors:
    print("Knowledge validation FAILED")
    for err in errors:
        print("-", err)
    sys.exit(1)

print(f"Knowledge validation OK: {len(seen_ids)} cards")
