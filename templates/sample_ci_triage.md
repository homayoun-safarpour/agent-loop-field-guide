# Loop Contract - filled sample (CI / PR triage)

Public-safe example for a recurring CI failure and PR-comment triage loop.
No secrets, no private research, no personal data.

## 1. Done

**Objective signal that means finished** (command, exit code, score threshold):

```
gh run list --workflow CI --limit 1 shows conclusion=success on main,
and the previously failing job name no longer appears in the last red run.
Locally: pytest -q exits 0 for the package named in LOOP_STATE.md.
```

## 2. Verifier

**What checks the work that did not produce it:**

```
GitHub Actions CI log for the named workflow (not the agent that proposed the fix).
Local re-run: pytest -q (and ruff check if the failure was lint).
Optional: a second human glance at the PR diff before merge.
```

## 3. Stop layers

| Layer | Your rule |
| --- | --- |
| Goal / done check | Latest CI on main is green for the named workflow |
| Max turns or ticks | Max 8 ticks per incident |
| Budget (tokens / $ / wall clock) | No paid APIs required; wall clock < 90 minutes |
| No-progress rule | Stop after 2 ticks with the same error signature |

## 4. State file

**Path to durable backlog / progress on disk:**

```
LOOP_STATE.md
```

**Journal / audit trail (if any):**

```
journal/JOURNAL.md
gh run URL of the failing job pasted into the state file each tick
```

## 5. Irreversible

**Actions that require a human yes before the loop may proceed:**

```
git push --force, approving production deploy workflows,
rotating credentials, closing someone else's PR without ask.
```

## Loop type (pick one primary)

- [ ] Turn-based
- [x] Goal-based (backlog + gates define done)
- [ ] Time-based
- [ ] Proactive

## Operator

Who executes the bounded action after the decision?

- [x] Mix (describe): Coding agent proposes the fix; human merges after CI green.

## Notes

```
Companion engine: https://github.com/homayoun-safarpour/agent-loop-engine
Blank template: templates/LOOP_CONTRACT.md
```
