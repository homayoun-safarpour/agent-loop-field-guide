# Interview notes — agent-loop-field-guide

## Three questions

1. Why fill a Loop Contract before scheduling an agent loop?
2. Which of the five decisions is missing when teams only write a clever system prompt?
3. How does this guide relate to `agent-loop-engine` without being a second framework?

## Two-minute demo

```bash
git clone https://github.com/homayoun-safarpour/agent-loop-field-guide
cd agent-loop-field-guide
cp templates/LOOP_CONTRACT.md /tmp/demo_contract.md
python scripts/check_contract.py templates/LOOP_CONTRACT.md
# open docs/FIELD_GUIDE.md → "What the best sources agree on"
```

## Limitations

- Templates and a heading checker only; no runtime loop.
- Source synthesis is paraphrased attribution, not a substitute for reading Anthropic / Willison / loop-engineering primary docs.
- Exit code `2` means missing headings, not that the filled answers are good engineering judgments.
