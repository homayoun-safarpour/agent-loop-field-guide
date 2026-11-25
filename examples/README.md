# Examples

This repo is a field guide (templates + checker), not a runtime.

| Path | What it shows |
| --- | --- |
| [../templates/sample_filled.md](../templates/sample_filled.md) | Filled five-decision contract tied to agent-loop-engine |
| [../templates/LOOP_CONTRACT.md](../templates/LOOP_CONTRACT.md) | Blank contract to copy into your project |

```bash
python scripts/check_contract.py templates/sample_filled.md
```

Exit `0` means the five required sections are present and each holds an answer. Exit `2` lists missing headings or empty sections, so the blank template exits `2`.
