# Adapter — Claude.ai / web interface (Projects)

> Claude.ai does not allow installing a system skill. Use the
> **Projects** feature: instructions + attached documents.

## Installation

1. Create a Project, e.g. "WebReverse Designer".
2. In the Project's custom instructions, paste the full
   `SKILL.md`.
3. As Project attachments (knowledge), add the 5 files from
   `references/` + one example from `examples/`.
4. Start a conversation in that Project and attach your screenshots /
   files to analyze.

## Specific limits
- No `check_project.py` execution on Claude.ai: run it
  locally (Linux Mint) and paste its text/JSON output into the chat.
- Always state screenshot widths (px) in your messages.
