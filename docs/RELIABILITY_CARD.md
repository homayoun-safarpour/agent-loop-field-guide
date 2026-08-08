# Reliability card — agent-loop-field-guide

| Field | Value |
| --- | --- |
| **Job** | Force five loop decisions onto disk before automation |
| **Primary signal** | Filled `LOOP_CONTRACT.md` + `scripts/check_contract.py` exit 0/2 |
| **Claim** | Chat-only "done" is not a verifier; empty contract cells mean you are still prompting |
| **Not claimed** | Runtime tick engine (use agent-loop-engine) |

## Field alignment

Same production habit as repair-before-advance loops: write the gate policy before spending tokens.
