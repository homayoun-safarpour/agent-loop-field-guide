"""Named claims: the checker passes only a contract whose five sections are real and filled."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "templates" / "LOOP_CONTRACT.md"
SCRIPT = ROOT / "scripts" / "check_contract.py"

HEADINGS = [
    "## 1. Done",
    "## 2. Verifier",
    "## 3. Stop layers",
    "## 4. State file",
    "## 5. Irreversible",
]


def run(path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        capture_output=True,
        text=True,
        check=False,
    )


def filled(heading_prefix: str = "") -> str:
    return "".join(f"{heading_prefix}{h}\n\nanswer for {h}\n\n" for h in HEADINGS)


def test_blank_template_fails_with_empty_sections():
    proc = run(CONTRACT)
    assert proc.returncode == 2, proc.stdout + proc.stderr
    assert "FAIL: empty sections:" in proc.stdout
    for h in HEADINGS:
        assert h in proc.stdout
    assert "PASS" not in proc.stdout


def test_filled_samples_pass():
    for name in ("sample_filled.md", "sample_ci_triage.md"):
        proc = run(ROOT / "templates" / name)
        assert proc.returncode == 0, name + proc.stdout + proc.stderr
        assert proc.stdout.startswith("PASS: ")


def test_headings_inside_html_comment_do_not_count(tmp_path: Path):
    bad = tmp_path / "commented.md"
    bad.write_text("# Contract\n\n<!--\n" + filled() + "-->\n", encoding="utf-8")
    proc = run(bad)
    assert proc.returncode == 2, proc.stdout
    assert "FAIL: missing headings:" in proc.stdout
    assert "## 1. Done" in proc.stdout


def test_headings_mentioned_in_one_prose_line_do_not_count(tmp_path: Path):
    bad = tmp_path / "prose.md"
    bad.write_text(
        "We skipped the template sections ## 1. Done ## 2. Verifier ## 3. Stop layers "
        "## 4. State file ## 5. Irreversible as not needed.\n",
        encoding="utf-8",
    )
    proc = run(bad)
    assert proc.returncode == 2, proc.stdout
    assert "## 5. Irreversible" in proc.stdout


def test_headings_inside_fenced_code_block_do_not_count(tmp_path: Path):
    for fence in ("```", "~~~"):
        bad = tmp_path / "fenced.md"
        bad.write_text(f"# Contract\n\n{fence}markdown\n" + filled() + f"{fence}\n", encoding="utf-8")
        proc = run(bad)
        assert proc.returncode == 2, fence + proc.stdout
        assert "FAIL: missing headings:" in proc.stdout


def test_section_with_only_comment_label_or_empty_cells_is_empty(tmp_path: Path):
    bad = tmp_path / "hollow.md"
    bad.write_text(
        "## 1. Done\n\n**Objective signal that means finished:**\n\n```\n<!-- e.g. pytest -q -->\n```\n\n"
        "## 2. Verifier\n\npytest -q\n\n"
        "## 3. Stop layers\n\n| Layer | Your rule |\n| --- | --- |\n| Max turns | 8 |\n| Budget | |\n\n"
        "## 4. State file\n\nLOOP_STATE.md\n\n"
        "## 5. Irreversible\n\n<!-- force-push -->\n",
        encoding="utf-8",
    )
    proc = run(bad)
    assert proc.returncode == 2, proc.stdout
    assert "FAIL: missing headings:" not in proc.stdout
    empty = proc.stdout.split("FAIL: empty sections:", 1)[1]
    assert "## 1. Done" in empty and "## 3. Stop layers" in empty and "## 5. Irreversible" in empty
    assert "## 2. Verifier" not in empty and "## 4. State file" not in empty


def test_subheading_stays_inside_its_section(tmp_path: Path):
    good = tmp_path / "sub.md"
    good.write_text(filled().replace("answer for ## 1. Done", "### Command\n\npytest -q"), encoding="utf-8")
    proc = run(good)
    assert proc.returncode == 0, proc.stdout


def test_filled_contract_with_utf8_bom_passes(tmp_path: Path):
    good = tmp_path / "bom.md"
    good.write_text(filled(), encoding="utf-8-sig")
    proc = run(good)
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_utf16_file_exits_1_with_not_utf8_message(tmp_path: Path):
    bad = tmp_path / "utf16.md"
    bad.write_text(filled(), encoding="utf-16")
    proc = run(bad)
    assert proc.returncode == 1
    assert "not UTF-8:" in proc.stderr
    assert "Traceback" not in proc.stderr
    assert "PASS" not in proc.stdout


def test_truncated_contract_exits_2(tmp_path: Path):
    bad = tmp_path / "bad.md"
    bad.write_text("# incomplete\n\n## 1. Done\n\nok\n", encoding="utf-8")
    proc = run(bad)
    assert proc.returncode == 2


def test_missing_file_exits_1_with_stderr(tmp_path: Path):
    proc = run(tmp_path / "no_such_contract.md")
    assert proc.returncode == 1
    assert "not a file" in proc.stderr
