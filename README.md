# agent-loop-field-guide

**You are about to run an agent loop. If "done" only lives in the model's head and progress only lives in chat, the loop will waste money or ship broken work. Fill this contract first.**

[![CI](https://github.com/homayoun-safarpour/agent-loop-field-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/homayoun-safarpour/agent-loop-field-guide/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/license-MIT-green)

Copy the blank Loop Contract into your project **before** you automate. This repo is a field guide plus templates, not a runtime. For a deterministic tick engine (state, gates, one action, journal), use [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine).

## Use this when

| Situation | Use this guide? |
| --- | --- |
| You are about to schedule `/loop`, cron, or an autonomous coding agent | Yes - fill the contract first |
| You need a five-decision checklist (done, verifier, stop layers, state, irreversible) | Yes |
| You want a runnable decision policy in Python | No - use [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine) |
| You want another agent framework | No |

## Quickstart (under 5 minutes)

```bash
git clone https://github.com/homayoun-safarpour/agent-loop-field-guide
cd agent-loop-field-guide
cp templates/LOOP_CONTRACT.md ../YOUR_PROJECT/LOOP_CONTRACT.md
# fill every section - empty cells mean you are still prompting
python scripts/check_contract.py templates/LOOP_CONTRACT.md
```

Read the full synthesis: [docs/FIELD_GUIDE.md](docs/FIELD_GUIDE.md)

## What is in the box

| Path | Purpose |
| --- | --- |
| [docs/FIELD_GUIDE.md](docs/FIELD_GUIDE.md) | Consensus from Anthropic, Willison, loop-engineering, Ralph/harness lineage |
| [templates/LOOP_CONTRACT.md](templates/LOOP_CONTRACT.md) | Blank five-decision contract |
| [templates/sample_filled.md](templates/sample_filled.md) | Filled example tied to agent-loop-engine |
| [scripts/check_contract.py](scripts/check_contract.py) | Verifies required headings exist (exit 0/2) |

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

## Field alignment

Fill the contract before `/loop` or cron. Claim boundaries: [docs/RELIABILITY_CARD.md](docs/RELIABILITY_CARD.md).

## Author

Homayoun Safarpour · [LinkedIn](https://www.linkedin.com/in/homayoun-safarpour/)

## License

MIT
