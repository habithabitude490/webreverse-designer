# Changelog — WebReverse Designer

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and versioning follows [SemVer](https://semver.org/).

## [Unreleased]

## [1.5.0] — 2026-10-18
### Added
- **Live analysis support**: when the environment provides browser/network
  tools, verified live capture is allowed — new evidence types P6 (in-session
  capture with viewport px) and P7 (fetched source), live responsive mode
  (multi-width captures) in `references/responsive-analysis.md`,
  updated `SKILL.md` (inputs, method step 1, inviolable rules, limitations).
- `adapters/opencode.md`: OpenCode V2 installation card (global
  `~/.config/opencode/skills/`, project `.opencode/skills/`,
  `.claude/skills` compatibility, `@webreverse-designer` activation).
- `check_project.py`: ignored symlinks are counted and reported as a
  warning. 2 regression tests added (12 total).
### Fixed
- `check_project.py`: CSS class false positives — `url(logo.png)` and
  `@import "base.css"` no longer yield `png`/`css` pseudo-classes
  (negative lookbehind `(?<![\w\-/])`); PEP8 blank lines.
### Changed
- README: publication status updated, OpenCode card added, live-analysis
  limits, test count, version examples refreshed.
- `INSTALL-CLAUDE-CODE.txt`: version references bumped to 1.5.0.

## [1.4.0] — 2026-10-18
### Added
- `INSTALL-CLAUDE-CODE.txt`: copy-paste English prompt for an AI with
  shell access to install + verify the skill in Claude Code
  (`~/.claude/skills/webreverse-designer`), ASCII, zero manual commands.
### Fixed
- `check_project.py --version` no longer requires a folder argument
  (`path` is now optional; missing path prints usage + exit 1).
  Regression test added (`test_version_flag_needs_no_path`).

## [1.3.0] — 2026-10-18
### Added
- `SETUP.txt`: self-contained universal setup prompt in plain ASCII text —
  paste into ANY coding agent/LLM, no install needed.
- `SETUP-ANY-AGENT.md`: Markdown version of the same prompt with usage guide.
### Changed
- `adapters/generic.md`: expanded into a full generic-coding-agent adapter
  (Option A zero-install via `AGENT-PROMPT.md`, Option B full `SKILL.md`
  injection, acceptance checklist, troubleshooting).

## [1.2.0] — 2026-10-18
### Added
- `AGENT-PROMPT.md`: self-contained universal prompt for any coding agent
  (works without skill support: paste-and-go).
### Changed
- **Full English translation**: README, all 5 references, all 4 adapters,
  script messages/docstrings, test strings, examples, CHANGELOG, CONTRIBUTING.
- Demo files renamed: `rapport-exemple-boulangerie-demo.md` →
  `sample-report-demo-bakery.md`; fictional content translated to English.
- Evidence labels standardized to English: screenshots S1/S2/S3
  (was C1/C2/C3), "Inventory"/"WARNING" script output.

## [1.1.0] — 2026-10-18
### Fixed
- Skill structure: tightened `SKILL.md` (short frontmatter, 8-point method,
  resource routing table), read-headers (`when to read / prerequisites`)
  on all 5 references, `examples/README.md`, dead-code removal
  (`TEXT_EXTENSIONS`), agent-usage docstrings on
  `extract_signals` / `scan_file` / `scan_project`.

## [1.0.0] — 2026-10-18
### Added
- `SKILL.md`: identity, activation, 7-step method, security rules.
- `references/`: evidence/confidence, visual analysis, responsive,
  accessibility, report template (12 sections).
- `scripts/check_project.py` (stdlib only): HTML/CSS/JS inventory,
  `.git`/`node_modules`/`dist`/`build`/venv exclusions, text + JSON output.
- `tests/`: 8 `unittest` tests, `demo-project` fixtures (fictional case).
- `examples/`: full report on fictional case + demo mini-project.
- `adapters/`: Claude Code, Cursor, Claude.ai / web, generic usage guides.
- `README.md`, `LICENSE` (MIT), `CONTRIBUTING.md`, `.gitignore`.
