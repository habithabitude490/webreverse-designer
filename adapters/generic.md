# Adapter — generic coding agent (universal, no install)

> Target: **any coding agent or LLM** (Copilot, Continue, Aider, Cody,
> ChatGPT, Gemini, Mistral, local models…).
> No skill mechanism needed. Two options: **A (recommended)** = paste
> `AGENT-PROMPT.md` (self-contained). **B (full)** = paste `SKILL.md`.
> Skill name to keep everywhere: `webreverse-designer`.

## Option A — zero-install (recommended, 2 min)

1. Open `AGENT-PROMPT.md`, copy its **whole content**.
2. At the start of a new agent conversation, paste it preceded by:
   `Strictly follow these skill instructions:`.
3. Then send the **activation line** (adapt brackets):
   `Act as WebReverse Designer on the evidence below. First inventory
   what is actually provided, invent no access and no breakpoints,
   then produce the 12-section report with confidence tags.
   Evidence: [paste URL / attach screenshots with px widths /
   paste files or inventory output / state goal].`
4. Attach evidence in the same message or follow-ups:
   - URL alone ≠ content (status = "provided, unverified");
   - screenshots **with px widths** when known (else "unknown width");
   - local files: paste content OR run step 5 and paste the output.
5. Local folder + shell access (optional but recommended):
   ```bash
   python3 /path/to/webreverse-designer/scripts/check_project.py /path/to/project --json
   ```
   Paste the JSON output into the conversation so the agent can cite
   `file:line` traceably. The script only inventories (stdlib only),
   it never executes the analyzed code.

## Option B — full skill injection

1. Copy the full content of `SKILL.md` (master file, v1.2.0).
2. Prepend `Strictly follow these skill instructions:` and paste.
3. If the agent supports multi-file context, also attach:
   `references/evidence-and-confidence.md` (mandatory vocabulary),
   `references/report-template.md` (12-section skeleton),
   then `visual-analysis.md` / `responsive-analysis.md` /
   `accessibility-review.md` as needed (see the Resources table in SKILL.md).
4. Then send the same activation line + evidence as in Option A.

## Expected output (acceptance checklist)

- [ ] §2 evidence table with S1/F1/U1 IDs + reliability (P1–P5);
- [ ] 12 sections, none removed ("Not assessable" + missing evidence if gap);
- [ ] every finding tagged `[High|Medium|Low|Not assessable]
        [Observed|Estimated|Hypothesis|Unknown] — … Evidence: …`;
- [ ] no invented breakpoint, framework, or test result;
- [ ] §11 recommendations with Impact × Effort;
- [ ] §12 limits, uncertainties (as questions), next steps.
- Reference model: `examples/sample-report-demo-bakery.md`.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Agent rebuilds the site | Resend rule: "observe/inventory/describe/document only, never generate or clone"; Option A §3 already forbids it. |
| Agent invents breakpoints / stack | Require citation: `@media` file:line or exact px widths; else "Unknown". |
| Agent claims "I visited the URL" | Ask: "quote the HTTP status / fetch proof from this session"; without proof → "URL provided, content unverified". |
| No shell access | Skip step 5; paste file contents manually + state paths. |
| Long context overflow | Use Option A only (AGENT-PROMPT.md ≈ 110 lines) instead of full SKILL + references. |

## Minimal activation sentence (short version)

"Act as WebReverse Designer: first inventory the evidence actually
provided, invent no access and no breakpoints, and produce the
12-section report with confidence levels."
