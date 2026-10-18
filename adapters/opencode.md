# Adapter — OpenCode (CLI / desktop / web)

> Valid for OpenCode V2 (`SKILL.md`-format skills supported).
> If your setup offers no skill discovery, use `adapters/generic.md`.

## Installation (global — all projects)

OpenCode discovers skills in `~/.config/opencode/skills/`.
It also reads `~/.claude/skills/` and `~/.agents/skills/` as
compatibility sources — an existing Claude Code installation is
therefore usable as-is, no duplication required.

```bash
# 1. Copy the skill (folder name = skill ID)
mkdir -p ~/.config/opencode/skills
cp -r /path/to/webreverse-designer ~/.config/opencode/skills/webreverse-designer

# 2. Verify the tree
ls ~/.config/opencode/skills/webreverse-designer/SKILL.md \
   ~/.config/opencode/skills/webreverse-designer/scripts/check_project.py

# 3. Activation test (read-only inventory)
python3 ~/.config/opencode/skills/webreverse-designer/scripts/check_project.py --version
```

Project scope: copy the same folder into `.opencode/skills/webreverse-designer/`
of your project. OpenCode searches from the current directory up to the
project root (`.claude/skills/` and `.agents/skills/` are also read there).

## Usage

- Auto-activation: the skill is advertised when a request matches its
  `description` (analyze / audit / document an existing site).
- Explicit activation: mention it in the prompt as
  `@webreverse-designer` followed by the request.
- The frontmatter `name`/`description` drive discovery; the folder name
  determines the skill ID (`webreverse-designer`). Do not rename it.

## Notes

- Precedence: for the same ID, project `.opencode/skills/` overrides the
  global `~/.config/opencode/skills/` copy.
- Extra sources (local folders or an HTTP catalog) can be registered with
  the `skills` array in any `opencode.json(c)`.
- The script is read-only: no `sudo`, no `chmod`, no API key.
- Live analysis: when the OpenCode session exposes browser/network tools,
  the skill may capture live evidence (P6/P7) — see
  `references/evidence-and-confidence.md`.
