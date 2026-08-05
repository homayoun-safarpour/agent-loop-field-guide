# Field guide: designing agent loops that stop for the right reasons

**Long work fails when the only memory is a chat window and the only stop condition is "the model feels done." This guide turns five high-signal sources into a short contract you fill before you automate.**

This repository is the checklist and attribution. A runnable decision policy lives in [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine).

## Sources (read these; we paraphrase, we do not copy)

| # | Source | What it contributes |
| --- | --- | --- |
| 1 | [Anthropic - Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Workflows vs agents; evaluator-optimizer; keep designs simple; invest in tool interfaces (ACI) |
| 2 | [Anthropic - Loop engineering](https://claude.com/blog/getting-started-with-loops) | Turn / goal / time / proactive loops; verifiable stop criteria; skills as repeatable checks |
| 3 | [Simon Willison - Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) | Agent = tools in a loop toward a goal; sandbox; tests amplify agent value |
| 4 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | High-star open patterns for loop readiness, audit, and durable orchestration culture |
| 5 | [Ralph pattern](https://ghuntley.com/ralph/) / [ralph-copilot](https://github.com/giocaizzi/ralph-copilot) + [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | Filesystem + git as memory; fresh context; harness around the model; reviewer separate from maker |

Honest boundary: those projects are larger than this guide. We extract **shared rules that survive across them**, then point at a small, testable implementation.

## What the best sources agree on

1. **Start simple.** Add multi-step loops only when a metric says the simpler path fails (Anthropic).
2. **Done must be machine-checkable.** Tests, scores, exit codes - not "the model decided it was finished" (Anthropic loops + Willison).
3. **Verifier is not the maker.** A separate check, second agent, or deterministic gate reviews the result.
4. **Durable state lives on disk.** Markdown / JSON / git beat chat logs for multi-session work (Ralph + harness culture).
5. **Stop in layers.** Goal met, max turns, budget, and no-progress - together, not one alone.
6. **Tool interfaces matter.** Absolute paths, clear args, scripts for deterministic steps (Anthropic tool appendix).
7. **Humans before irreversible actions.** Delete, force-push, spend, or production write needs an explicit checkpoint.

## Loop types (when to use which)

From Anthropic's loop engineering framing, compressed into operator language:

| Loop | You hand off | Use when | Stop signal |
| --- | --- | --- | --- |
| Turn-based | The verification check | Exploring or deciding | Human accepts the turn, or a skill/gate fails |
| Goal-based | The definition of done | You can write a pass/fail criterion | Goal met or turn/budget cap |
| Time-based | The trigger | Recurring work, external systems | Interval cancelled or queue empty |
| Proactive | The prompt + schedule | Well-defined streams (triage, CI fix) | Per-task goal + routine off switch |

Use the smallest loop that matches the work. A cron that re-prompts without a verifier is not a production loop.

## The five-decision Loop Contract

Before you automate, write these five decisions down.

- Blank: [`templates/LOOP_CONTRACT.md`](../templates/LOOP_CONTRACT.md)
- Filled sample: [`templates/sample_filled.md`](../templates/sample_filled.md)

| # | Decision | Question you must answer |
| --- | --- | --- |
| 1 | **Done** | What objective signal means finished? (command, exit code, score threshold) |
| 2 | **Verifier** | What checks the work that did **not** produce it? |
| 3 | **Stop layers** | Goal check + max turns/ticks + budget and/or no-progress rule |
| 4 | **State file** | Where does progress live on disk so a crash can resume? |
| 5 | **Irreversible** | What requires a human yes before the loop may proceed? |

If any cell is empty, you are still prompting, not looping.

Validate headings locally:

```bash
python scripts/check_contract.py templates/LOOP_CONTRACT.md
```

Exit `0` = required sections present. Exit `2` = missing headings.

## Filesystem and git as memory

Chat context rot is real. Patterns that keep winning put durable artifacts in the repo:

- A human-editable backlog (for example `LOOP_STATE.md`)
- An append-only journal of decisions
- Git commits as the audit trail for code changes
- Fresh context per iteration when the previous window is polluted (Ralph-style)

## How this maps to agent-loop-engine

```
Loop Contract                 agent-loop-engine
-------------                 -----------------
Done                          your gates (pytest, ruff, sibling CLIs)
Verifier                      gates run before advance; repair beats progress
Stop layers                   one action per tick; red gate blocks new work
State file                    LOOP_STATE.md (checkbox backlog)
Irreversible                  engine never executes; operator / CI does
```

Sibling instruments that plug in as gates (exit `0` / `2`):

- [judge-drift-sentinel](https://github.com/homayoun-safarpour/judge-drift-sentinel) - system change vs judge drift
- [trace-gate](https://github.com/homayoun-safarpour/trace-gate) - trajectory regression against a frozen baseline

## Anti-patterns

| Anti-pattern | Why it fails | Prefer |
| --- | --- | --- |
| Model is the only judge of done | Confirms its own work | Independent gate or second reviewer |
| Unbounded loop | Cost and damage grow without a stop | Turn/budget/no-progress caps |
| Relative paths in tools | Break after cwd changes | Absolute paths (Anthropic ACI lesson) |
| Memory only in chat | Cannot resume cleanly | State file + journal + git |
| New features on red tests | Compounds breakage | Repair-before-advance |
| LLM re-derives a fixed script | Burns tokens on deterministic work | Ship a script; call it from the loop |

## Two-minute path

```bash
git clone https://github.com/homayoun-safarpour/agent-loop-field-guide
cd agent-loop-field-guide
cp templates/LOOP_CONTRACT.md /tmp/LOOP_CONTRACT.md
# edit /tmp/LOOP_CONTRACT.md for your project
python scripts/check_contract.py templates/LOOP_CONTRACT.md
# optional: run a real tick engine
# https://github.com/homayoun-safarpour/agent-loop-engine
```

## Attribution

Ideas above are synthesized from the linked Anthropic posts, Willison's essay, the loop-engineering project, and the Ralph / harness-engineering lineage. Wording here is original. Upstream projects keep their own licenses; link them, do not vendor their trees into this guide.
