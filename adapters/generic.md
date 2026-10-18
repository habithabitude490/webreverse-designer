# Adapter — generic usage (any agent / LLM)

> When the target tool has no skill mechanism: manual injection.

## Procedure

1. Open `SKILL.md`, copy its full content.
2. At the start of the agent conversation, paste it preceded by:
   "Strictly follow these skill instructions:".
3. Then attach: URL / screenshots (with px widths) / files / goal.
4. For a local folder, run first:
   ```bash
   python3 scripts/check_project.py /path/project --json
   ```
   then paste the output into the conversation.
5. Require the 12-section report (`references/report-template.md`).

## Minimal activation sentence
"Act as WebReverse Designer: first inventory the evidence actually
provided, invent no access and no breakpoints, and produce the
12-section report with confidence levels."
