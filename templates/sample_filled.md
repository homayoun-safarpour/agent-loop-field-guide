# Loop Contract - filled sample (agent-loop-engine)

Reference fill for a goal-based engineering backlog. Copy `LOOP_CONTRACT.md` blank for new work.

## 1. Done

**Objective signal that means finished:**

```
All backlog items in LOOP_STATE.md checked; pytest -q and ruff check src tests both exit 0 on the last tick.
```

## 2. Verifier

**What checks the work that did not produce it:**

```
Quality gates before every decision:
  tests = python -m pytest -q
  lint  = python -m ruff check src tests
The decision policy never advances while a gate is red.
```

## 3. Stop layers

| Layer | Your rule |
| --- | --- |
| Goal / done check | No open checkboxes left in LOOP_STATE.md |
| Max turns or ticks | One bounded action per tick |
| Budget (tokens / $ / wall clock) | No LLM in the decision path; operator budget is external |
| No-progress rule | Head item stale >2 days loses priority to cheapest open item |

## 4. State file

**Path to durable backlog / progress on disk:**

```
LOOP_STATE.md
```

**Journal / audit trail:**

```
journal/JOURNAL.md
git history for code changes
```

## 5. Irreversible

**Actions that require a human yes before the loop may proceed:**

```
Force-push, deleting releases, publishing secrets, unpaid cloud spend.
The decision engine prints the next order; it does not execute irreversible actions.
```

## Loop type (pick one primary)

- [ ] Turn-based
- [x] Goal-based (backlog + gates define done)
- [ ] Time-based
- [ ] Proactive

## Operator

Who executes the bounded action after the decision?

- [x] Mix (describe): Human or coding agent executes the printed order; CI re-runs gates.

## Notes

```
See docs/FIELD_GUIDE.md. Runnable companion: https://github.com/homayoun-safarpour/agent-loop-engine
```
