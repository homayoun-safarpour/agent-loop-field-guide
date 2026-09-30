# loop-contract

**You are about to run an agent loop. If "done" only lives in the model's head, the loop will waste money or ship broken work.**

[![CI](https://github.com/homayoun-safarpour/agent-loop-field-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/homayoun-safarpour/agent-loop-field-guide/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/license-MIT-green)

Fill a five-decision Loop Contract before you automate an agent loop. Field guide + templates + heading checker.

```bash
git clone https://github.com/homayoun-safarpour/agent-loop-field-guide
cd agent-loop-field-guide
python scripts/check_contract.py examples/incomplete_contract.md
```

```text
FAIL: missing headings:
  - ## 2. Verifier
  - ## 3. Stop layers
  - ## 4. State file
  - ## 5. Irreversible
```

That command exits 2. There is no pip install. The checker is stdlib.

The blank template (`templates/LOOP_CONTRACT.md`) exits 0 because the headings exist. Empty cells still mean you are prompting.

## Use this when

| Situation | Use this guide? |
| --- | --- |
| You are about to schedule `/loop`, cron, or an autonomous coding agent | Yes - fill the contract first |
| You need a five-decision checklist (done, verifier, stop layers, state, irreversible) | Yes |
| You want a runnable decision policy in Python | No - use [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine) |
| You want another agent framework | No |

This repo is a field guide plus templates, not a runtime.

## Quickstart

Interview pack: [docs/INTERVIEW.md](docs/INTERVIEW.md).

Claim boundaries: [docs/RELIABILITY_CARD.md](docs/RELIABILITY_CARD.md).

Copy the blank contract into your project before you automate:

```bash
# Unix
cp templates/LOOP_CONTRACT.md ../YOUR_PROJECT/LOOP_CONTRACT.md
# Windows PowerShell
Copy-Item templates/LOOP_CONTRACT.md ..\YOUR_PROJECT\LOOP_CONTRACT.md
python scripts/check_contract.py templates/LOOP_CONTRACT.md
```

```text
PASS: templates/LOOP_CONTRACT.md has all five Loop Contract headings
```

Read the full synthesis: [docs/FIELD_GUIDE.md](docs/FIELD_GUIDE.md)

## What is in the box

| Path | Purpose |
| --- | --- |
| [docs/FIELD_GUIDE.md](docs/FIELD_GUIDE.md) | Consensus from Anthropic, Willison, loop-engineering, Ralph/harness lineage |
| [templates/LOOP_CONTRACT.md](templates/LOOP_CONTRACT.md) | Blank five-decision contract |
| [templates/sample_filled.md](templates/sample_filled.md) | Filled example tied to agent-loop-engine |
| [scripts/check_contract.py](scripts/check_contract.py) | Verifies required headings exist (exit 0/2); `--strict` also fails on empty sections |
| [examples/incomplete_contract.md](examples/incomplete_contract.md) | Stranger fail path (exit 2) |

## The five decisions (preview)

1. **Done** - objective signal (command, exit code, score)
2. **Verifier** - check that did not produce the work
3. **Stop layers** - goal + max turns + budget and/or no-progress
4. **State file** - durable path on disk
5. **Irreversible** - human yes before delete / force-push / spend

## Related instruments

- [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine) - markdown state, quality gates, one tick, journal
- [judge-drift-sentinel](https://github.com/homayoun-safarpour/judge-drift-sentinel) - judge vs system drift gate
- [trace-gate](https://github.com/homayoun-safarpour/trace-gate) - trajectory regression gate
- [judge-field-guide](https://github.com/homayoun-safarpour/judge-field-guide) - link-checked map of the LLM-judge ecosystem
- [ai-eng-skill-range](https://github.com/homayoun-safarpour/ai-eng-skill-range) - graded katas for the same hire skills

## Field alignment

Fill the contract before `/loop` or cron. Claim boundaries: [docs/RELIABILITY_CARD.md](docs/RELIABILITY_CARD.md).

## Author

Homayoun Safarpour. [LinkedIn](https://www.linkedin.com/in/homayoun-safarpour/)

## License

MIT
