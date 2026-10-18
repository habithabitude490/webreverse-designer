# Changelog — WebReverse Designer

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and versioning follows [SemVer](https://semver.org/).

## [Unreleased]
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
