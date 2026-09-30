"""Named claim: blank Loop Contract template exposes the five decisions."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "templates" / "LOOP_CONTRACT.md"
SCRIPT = ROOT / "scripts" / "check_contract.py"


def test_blank_contract_passes_check_script():
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), str(CONTRACT)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_truncated_contract_exits_2(tmp_path: Path):
    bad = tmp_path / "bad.md"
    bad.write_text("# incomplete\n\n## 1. Done\n\nok\n", encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), str(bad)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 2


FILLED = ROOT / "templates" / "sample_filled.md"

EMPTY_CELLS = """# Contract

## 1. Done

pytest -q exits 0

## 2. Verifier

ruff check

## 3. Stop layers

| Layer | Your rule |
| --- | --- |
| Goal / done check | |
| Max turns or ticks | |
| Budget (tokens / $ / wall clock) | |
| No-progress rule | |

## 4. State file

LOOP_STATE.md

## 5. Irreversible

force push
"""


def run_check(path: Path, *flags: str):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *flags, str(path)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_empty_cells_pass_default_and_fail_strict(tmp_path: Path):
    f = tmp_path / "empty.md"
    f.write_text(EMPTY_CELLS, encoding="utf-8")
    assert run_check(f).returncode == 0
    strict = run_check(f, "--strict")
    assert strict.returncode == 2
    assert "## 3. Stop layers" in strict.stdout


def test_strict_passes_filled_sample():
    assert run_check(FILLED, "--strict").returncode == 0


def test_strict_fails_blank_template():
    assert run_check(CONTRACT, "--strict").returncode == 2
