# Adapter — Claude Code (CLI)

> Valid for Claude Code with `SKILL.md`-format skill support.
> If your version offers no skill import, use
> `adapters/generic.md`.

## Installation (Linux Mint)

```bash
# 1. Clone / copy the skill
git clone <REPO-URL> ~/skills 2>/dev/null || mkdir -p ~/skills
cp -r /path/to/webreverse-designer ~/.claude/skills/webreverse-designer

# 2. Verify the tree
ls ~/.claude/skills/webreverse-designer/SKILL.md \
   ~/.claude/skills/webreverse-designer/scripts/check_project.py

# 3. Permissions (script is read-only already — no chmod +x needed)
python3 ~/.claude/skills/webreverse-designer/scripts/check_project.py --version

# 4. Activation test: in Claude Code, ask
#    "Analyze the design of tests/fixtures/demo-project with WebReverse Designer"
```

## Notes
- Folder name = skill name (`webreverse-designer`). Do not rename it.
- Mechanism not guaranteed across versions: if import fails,
  paste the `SKILL.md` content as a conversation prefix (see `generic.md`).
