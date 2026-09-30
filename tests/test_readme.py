from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8-sig")
SCRIPT = ROOT / "scripts" / "check_contract.py"
INCOMPLETE = ROOT / "examples" / "incomplete_contract.md"


def test_readme_spoken_h1_is_loop_contract():
    assert README.lstrip().startswith("# loop-contract\n")
    assert "agent-loop-field-guide" in README


def test_readme_first_screen_matches_top100_craft():
    pip_at = README.find("pip install")
    interview_at = README.find("Interview pack")
    assert 0 <= pip_at < interview_at
    head = "\n".join(README.splitlines()[:22])
    assert "# loop-contract" in head
    assert "git clone https://github.com/homayoun-safarpour/agent-loop-field-guide" in head
    assert "examples/incomplete_contract.md" in head
    assert "python scripts/check_contract.py" in head
    assert "FAIL: missing headings:" in head
    assert "## 5. Irreversible" in head
    assert "Interview pack" not in head
    assert "\u2014" not in head
    assert "PASS:" not in head


def test_readme_stranger_incomplete_contract_exits_2():
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), str(INCOMPLETE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 2
    assert "FAIL: missing headings:" in proc.stdout
    assert "## 2. Verifier" in proc.stdout
