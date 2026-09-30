#!/usr/bin/env python3
"""Verify a Loop Contract markdown file has the five required decision headings.

Default mode checks headings only. With --strict, each required section must
also contain text other than comments, bold labels, code fences and empty
table cells.

Exit codes:
  0 - checks passed
  2 - missing headings, or (with --strict) empty sections
  1 - usage / IO error
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = [
    "## 1. Done",
    "## 2. Verifier",
    "## 3. Stop layers",
    "## 4. State file",
    "## 5. Irreversible",
]

COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
FENCE = "`" * 3


def check(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [h for h in REQUIRED if h not in text]


def section_body(text: str, heading: str) -> str:
    start = text.index(heading) + len(heading)
    nxt = re.search(r"^## ", text[start:], re.MULTILINE)
    return text[start : start + nxt.start()] if nxt else text[start:]


def has_content(body: str) -> bool:
    in_table = False
    for raw in COMMENT.sub("", body).splitlines():
        line = raw.strip()
        if not line or line.startswith(FENCE) or line.startswith("**"):
            continue
        if line.startswith("|"):
            if not in_table:
                in_table = True
                continue
            if set(line) <= set("|-: "):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if any(cells[1:]):
                return True
            continue
        return True
    return False


def check_empty(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [h for h in REQUIRED if not has_content(section_body(text, h))]


def main(argv: list[str]) -> int:
    args = argv[1:]
    strict = "--strict" in args
    paths = [a for a in args if a != "--strict"]
    if len(paths) != 1:
        print(
            "usage: python scripts/check_contract.py [--strict] <LOOP_CONTRACT.md>",
            file=sys.stderr,
        )
        return 1
    path = Path(paths[0])
    if not path.is_file():
        print(f"not a file: {path}", file=sys.stderr)
        return 1
    missing = check(path)
    if missing:
        print("FAIL: missing headings:")
        for h in missing:
            print(f"  - {h}")
        return 2
    if strict:
        empty = check_empty(path)
        if empty:
            print("FAIL: empty sections:")
            for h in empty:
                print(f"  - {h}")
            return 2
    print(f"PASS: {path} has all five Loop Contract headings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
