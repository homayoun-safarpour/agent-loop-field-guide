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

def test_missing_file_exits_1_with_stderr(tmp_path: Path):
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), str(tmp_path / "no_such_contract.md")],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 1
    assert "not a file" in proc.stderr
