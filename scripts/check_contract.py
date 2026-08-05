#!/usr/bin/env python3
"""Verify a Loop Contract markdown file has the five required decision headings.

Exit codes:
  0 - required headings present
  2 - missing one or more required headings
  1 - usage / IO error
"""

from __future__ import annotations

import sys
from pathlib import Path

REQUIRED = [
    "## 1. Done",
    "## 2. Verifier",
    "## 3. Stop layers",
    "## 4. State file",
    "## 5. Irreversible",
]


def check(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [h for h in REQUIRED if h not in text]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/check_contract.py <LOOP_CONTRACT.md>", file=sys.stderr)
        return 1
    path = Path(argv[1])
    if not path.is_file():
        print(f"not a file: {path}", file=sys.stderr)
        return 1
    missing = check(path)
    if missing:
        print("FAIL: missing headings:")
        for h in missing:
            print(f"  - {h}")
        return 2
    print(f"PASS: {path} has all five Loop Contract headings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
