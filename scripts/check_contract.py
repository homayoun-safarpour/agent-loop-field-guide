#!/usr/bin/env python3
"""Verify a Loop Contract markdown file has the five required decision sections, each filled.

A heading counts only as its own line, outside HTML comments and fenced code blocks.
A section counts only when it holds an answer: text that is not blank, not inside an
HTML comment, not a bare label ending in a colon, and not a table row with an empty cell.

Exit codes:
  0 - all five headings present, each with content under it
  2 - one or more headings missing, or a section is empty
  1 - usage / IO error, or the file is not UTF-8
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

COMMENT = re.compile(r"<!--.*?(?:-->|\Z)", re.DOTALL)
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
HEADING = re.compile(r"^ {0,3}(#{1,6})(?:\s|$)")
LABEL = re.compile(r"^\*\*[^*]+\*\*[^*]*:\s*$|^\*\*[^*]+:\*\*\s*$")
TABLE_SEPARATOR = re.compile(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?$")


def _blank_comments(text: str) -> str:
    """Remove HTML comments (an unclosed one runs to the end) but keep line numbers."""
    return COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def sections(text: str) -> dict[str, list[str]]:
    """Map each heading line (outside comments and fences) to the content lines under it."""
    lines = _blank_comments(text).splitlines()
    found: dict[str, list[str]] = {}
    current: list[str] | None = None
    fence: str | None = None
    for i, raw in enumerate(lines):
        line = raw.rstrip()
        mark = FENCE.match(line)
        if fence is not None:
            close = line.strip()
            if close and set(close) == {fence[0]} and len(close) >= len(fence):
                fence = None
            elif current is not None and line.strip():
                current.append(line)
            continue
        if mark:
            fence = mark.group(1)
            continue
        heading = HEADING.match(line)
        if heading:
            if len(heading.group(1)) <= 2:  # a subheading stays inside its section
                current = found.setdefault(line.strip(), [])
            continue
        if current is None or not line.strip() or LABEL.match(line.strip()):
            continue
        if line.lstrip().startswith("|"):
            if TABLE_SEPARATOR.match(line.strip()):
                continue
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if TABLE_SEPARATOR.match(nxt):
                continue  # header row
            if any(not c for c in _cells(line)):
                current.append("")  # a row with an empty cell marks the section as unfilled
                continue
        current.append(line)
    return found


def check(path: Path) -> tuple[list[str], list[str]]:
    found = sections(path.read_text(encoding="utf-8-sig"))
    missing = [h for h in REQUIRED if h not in found]
    empty = [h for h in REQUIRED if h in found and (not found[h] or "" in found[h])]
    return missing, empty


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/check_contract.py <LOOP_CONTRACT.md>", file=sys.stderr)
        return 1
    path = Path(argv[1])
    if not path.is_file():
        print(f"not a file: {path}", file=sys.stderr)
        return 1
    try:
        missing, empty = check(path)
    except UnicodeDecodeError:
        print(f"not UTF-8: {path}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"cannot read: {path}: {exc.strerror}", file=sys.stderr)
        return 1
    if missing:
        print("FAIL: missing headings:")
        for h in missing:
            print(f"  - {h}")
    if empty:
        print("FAIL: empty sections:")
        for h in empty:
            print(f"  - {h}")
    if missing or empty:
        return 2
    print(f"PASS: {path} has all five Loop Contract headings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
