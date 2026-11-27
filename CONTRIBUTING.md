# Contributing

Public repo: https://github.com/homayoun-safarpour/agent-loop-field-guide

## Local loop

These are the commands CI runs.

```bash
pip install pytest
pytest -q
python scripts/check_contract.py templates/sample_filled.md
```

## Pull requests

1. One change per pull request.
2. A named pytest lock if you add a README claim.
3. Open a PR against `main`. Do not leave work only on a long-lived branch.
