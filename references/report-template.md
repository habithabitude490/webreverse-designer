# Report template

> Read at step 8, to produce the final report (12 sections, none removed).
> Prerequisite: all resources above + completed evidence inventory.

> Copy this template for each analysis. Do not remove any of the 12 sections.
> If a section is not assessable, write it with the missing evidence.
> Confidence vocabulary: see `evidence-and-confidence.md`.

# Design analysis report — [Site / page name]

- Date: [YYYY-MM-DD]
- Analyst: WebReverse Designer (AI) + [human name if reviewed]
- Scope: [agreed pages / screens]
- User goal: [why this analysis]

---

## 1. Executive summary
[5–10 lines max: site nature, dominant structure, style in 3 adjectives,
strengths (2–3), main risks (2–3), reliability framing sentence.]

## 2. Scope and examined evidence
### 2.1 Inventoried evidence
| # | Type | Detail | Width / version | Reliability |
|---|------|--------|-------------------|-----------|
| S1 | Screenshot | … | 1440px | P2 |
| F1 | File | `index.html` (XXX lines) | — | P1 |
| U1 | URL | `https://…` (provided, [visited / not visited]) | — | P5 |
### 2.2 Inventory tool
[`scripts/check_project.py` output if a local folder was analyzed, else "N/A"]
### 2.3 What was NOT examined
[Live DOM, interactions, exact breakpoints, backend code… as applicable]

## 3. Page architecture
[Page by page: block order, role of each block, present/absent/uncertain table.]
| Element | Page A | Page B | Evidence |
|---------|--------|--------|--------|
| Header / Nav | … | … | … |
| Hero | … | … | … |
| … | | | |

## 4. Recurring components and patterns
[Component card: name, occurrences, variants, anatomy, observed states.]
- **Primary button**: … (evidence …)
- **Article card**: …
- **Contact form**: …

## 5. Estimated design system
[The word "estimated" is in the title and every unmeasured value carries ≈ + margin.]
- Palette (table: usage / value / observed-or-estimated status / evidence)
- Typography (apparent families, relative scale, weights)
- Spacing / grid (explicit hypotheses)
- Radii / shadows / borders (≈ px values)
- Iconography
- Proposed tokens (`name: value /* status */` format)

## 6. Responsive design
[If a single width: "Not assessable — …" + missing evidence. Otherwise comparative table per component and width. No invented breakpoint.]

## 7. Observed interactions
[Only observed or code-proven. Otherwise "Not observed" + what to provide.]
| Interaction | Trigger | Effect | Evidence | Confidence |
|-------------|-------------|-------|--------|-----------|
| … | … | … | … | … |

## 8. Accessibility and usability
[`accessibility-review.md` grid filled + "without real testing, no definitive verdict" reminder.]

## 9. Verifiable technologies and code structure
[If code provided: entry points, tree, declared dependencies, classes/components. If no code: "Not assessable — no file provided. Any technology hypothesis is excluded." Do not execute the code.]

## 10. Findings by confidence level
### High — [list, `[High] [Observed] — … Evidence: …` format]
### Medium — […]
### Low — […]
### Not assessable — [unanswered questions + evidence that would settle them]

## 11. Priority recommendations (impact × effort)
| # | Recommendation | Impact | Effort | Evidence / rationale | Risk if ignored |
|---|----------------|--------|--------|----------------|------------------|
| R1 | … | H/M/L | H/M/L | … | … |
[Order by high Impact + low Effort first. No site regeneration here.]

## 12. Limits, uncertainties, and next steps
- Limits: [access, missing evidence, compression, scope]
- Uncertainties: [3–5 max, phrased as questions]
- Next steps: [screenshots to provide (exact widths), files to provide, tests to run, re-analysis]
