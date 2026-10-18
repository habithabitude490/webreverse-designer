# Adapter — Cursor

> Cursor uses its own rules / commands. There is no guaranteed universal
> "skill" format: import the content as project rules.

## Installation (Linux Mint)

```bash
# 1. Copy the skill into the project (or globally)
mkdir -p .cursor/rules
cp /path/to/webreverse-designer/SKILL.md .cursor/rules/webreverse-designer.mdc
# Add at the top of the .mdc file:
# ---
# description: Web design analysis and documentation (reverse design)
# globs: ["**/*.html", "**/*.css"]
# alwaysApply: false
# ---

# 2. References: copy references/ alongside if needed
cp -r /path/to/webreverse-designer/references .cursor/rules/webreverse-refs/

# 3. Script: use it from the integrated terminal
python3 /path/to/webreverse-designer/scripts/check_project.py ./ --json
```

## Activation test
Open Chat / Composer and ask:
"Following .cursor/rules/webreverse-designer.mdc, analyze the design
of the tests/fixtures/demo-project folder."
