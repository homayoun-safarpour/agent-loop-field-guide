# Interview talking points : agent-loop-field-guide

Five CLI-backed points for a technical screen (no resume recap).

- **`cp templates/LOOP_CONTRACT.md ../YOUR_PROJECT/LOOP_CONTRACT.md`** : copy the blank contract before cron, `/loop`, or any autonomous coding agent; empty cells mean you are still prompting, not operating.
- **`python scripts/check_contract.py templates/sample_filled.md`** : verifies the five decision sections (`Done`, `Verifier`, `Stop layers`, `State file`, `Irreversible`); exit **0** when each heading is there with an answer under it. The blank template exits **2** with five empty sections.
- **Remove a heading and re-run `check_contract.py`** : exit **2** lists missing headings and empty sections; the checker does not judge whether your answers are good, only that each section is filled.
- **`templates/sample_filled.md`** : worked example of filled cells; compare your project copy against it before you trust “done” in chat.
- **Pair with `loop-engine tick` from [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine)** : this repo is templates plus synthesis; the engine runs gates and journal ticks once the contract names your verifier commands.
