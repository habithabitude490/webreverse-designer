# WebReverse Designer

Open-source AI skill (MIT) specialized in **analyzing and documenting
the design of existing websites**. It observes, inventories, and documents —
it **never rebuilds or generates any site**.

- Inputs: public URL (live capture when the agent provides browser/network
  tools), screenshots, HTML/CSS/JS files, user context.
- Output: **structured 12-section Markdown report** with confidence
  levels, limits, and prioritized recommendations (impact × effort).
- Requirements: Python 3, **standard library only**, Linux Mint
  (portable elsewhere).

## Tree

```
webreverse-designer/
├── SKILL.md                  # skill identity + method (master file)
├── INSTALL-CLAUDE-CODE.txt   # copy-paste prompt: an AI installs the skill in Claude Code
├── AGENT-PROMPT.md           # universal prompt for any coding agent
├── SETUP.txt                 # same prompt, plain ASCII text (AI ingestion)
├── SETUP-ANY-AGENT.md        # same prompt, Markdown version with guide
├── README.md                 # this file
├── LICENSE                   # MIT
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
├── references/
│   ├── evidence-and-confidence.md
│   ├── visual-analysis.md
│   ├── responsive-analysis.md
│   ├── accessibility-review.md
│   └── report-template.md
├── scripts/
│   └── check_project.py      # static inventory (stdlib, never executes)
├── tests/
│   ├── test_check_project.py # 12 unittest tests
│   └── fixtures/demo-project # fictional mini-site (5 files)
├── examples/
│   ├── README.md                 # examples guide
│   ├── sample-report-demo-bakery.md
│   └── demo-project/         # fictional mini-site for manual trials
└── adapters/
    ├── claude-code.md  ├── cursor.md  ├── claude-ai.md
    ├── opencode.md     └── generic.md
```

## Installation — Linux Mint

### 1. Download
```bash
# Option A: clone
git clone https://github.com/habithabitude490/webreverse-designer.git
cd webreverse-designer
# Option B: local archive already present
ls SKILL.md   # must exist, run from the skill folder
```

### 2. Verify the tree
```bash
cd webreverse-designer
find . -type f | sort
python3 --version   # 3.8+ required (tested: 3.12 on Mint 22.3)
```

### 3. Install the skill into the target tool
> There is **no universal mechanism**: pick ONE card.
| Tool | Card |
|-------|-------|
| Claude Code | `adapters/claude-code.md` |
| OpenCode | `adapters/opencode.md` |
| Cursor | `adapters/cursor.md` |
| Claude.ai / web | `adapters/claude-ai.md` |
| Other / unknown | `adapters/generic.md` |

No installer needed? Two zero-install options (same prompt):
- `SETUP.txt` — plain ASCII text: paste into ANY agent/LLM, works everywhere.
- `AGENT-PROMPT.md` — Markdown version with usage notes.
- Claude Code install via an AI? `INSTALL-CLAUDE-CODE.txt` — paste into an
  AI with shell access; it copies + verifies the skill for you.

### 4. Activation test
```bash
python3 scripts/check_project.py tests/fixtures/demo-project
python3 -m unittest discover -s tests -v   # 12 tests expected: OK
```

### 5. Test on a local project
```bash
python3 scripts/check_project.py /path/to/your/project --json | head -n 40
```

### Permissions
Read-only is enough. No `sudo`, no packages, no API keys.

## Usage

1. **Inventory the evidence** (URL? screenshots + px widths? files?).
2. Run `check_project.py` if a local folder is provided.
3. Ask the agent: "Act as WebReverse Designer and analyze …"
   (or follow `adapters/generic.md` / paste `AGENT-PROMPT.md`).
4. Receive the **12-section report**: summary, evidence, architecture,
   components, estimated design system, responsive, interactions, a11y, code,
   findings by confidence, impact×effort recommendations, limits.

## Examples
- `examples/sample-report-demo-bakery.md`: full report (fictional case).
- Replay the inventory: `python3 scripts/check_project.py examples/demo-project`.

## Limits (summary)
- Bare URL ≠ guaranteed access. With browser/network tools: live capture
  allowed and cited (P6/P7); without them: screenshots required.
  Never simulate.
- 1 single width → responsive **not assessable**; breakpoints never invented.
- Interactions only if **observed** or **proven by code**.
- Accessibility: visual/static presumptions, **no WCAG verdict**
  without real tests. See `references/accessibility-review.md`.
- No bypassing (auth, paywall, CAPTCHA, anti-bot), no secrets,
  no execution of analyzed code, no copying of proprietary code.

## Troubleshooting
| Symptom | Likely cause | Fix |
|----------|----------------|----------|
| `folder not found (code 1)` | wrong path | absolute path, quotes if spaces |
| "Empty" project | exclusions or wrong folder | `--json` → check `skipped_dirs` |
| `[imperfect encoding]` | non-UTF-8 file | normal: replaced chars, partial analysis |
| Skill not recognized by tool | wrong format/target | re-read the exact `adapters/` card |
| Failing tests | Python < 3.8 or moved files | `python3 --version`, rerun from skill root |

## Dependencies
**None.** Python 3 standard library only
(`argparse`, `json`, `os`, `re`, `sys`, `dataclasses`, `unittest`, …).
Rationale: trivial install, easy audit, zero supply-chain risk.

## Open-source sharing
- License: MIT (`LICENSE`). Example: fictional case, no third-party rights.
- Never commit: secrets (`.env`, keys), `node_modules/`, `dist/`.
- Published: [github.com/habithabitude490/webreverse-designer](https://github.com/habithabitude490/webreverse-designer) — releases tagged `vX.Y.Z`.
- Publishing an update:
  ```bash
  git add -A && git commit -m "feat: WebReverse Designer 1.5.0"
  git push origin main
  git tag v1.5.0 && git push origin v1.5.0
  gh release create v1.5.0 --title "v1.5.0" --notes "…"
  ```
- Contributions: see `CONTRIBUTING.md`.

## Security
See the "Inviolable rules" section of `SKILL.md`.
In short: cited evidence, observed/estimated/hypothesis/unknown distinguished,
no destructive actions, copyright respected.
