# Evidence and confidence levels

> Read first, before any finding. Prerequisites: none.
> Normative: mandatory confidence vocabulary for the report.

This document is normative. Every report must classify each piece of
evidence and each finding using these categories. Using any other
confidence vocabulary is forbidden.

## 1. Accepted evidence types

| Code | Type | Example | Strength |
|------|------|---------|-------|
| P1 | Readable local file | `index.html:42`, `styles.css:10` | Strong |
| P2 | Annotated screenshot + known width | "desktop screenshot 1440px, hero visible" | Strong (visual only) |
| P3 | Screenshot without width / cropped | "mobile screenshot, unknown width" | Medium |
| P4 | Unverified user statement | "user says the menu is sticky" | Weak |
| P5 | Bare URL (no session access) | `https://example.com` provided, not visited | Nil for content |

Rule: a bare URL proves nothing about content. Until the session has
actually fetched the page (and it is allowed: no bypassing),
the status is "URL provided, content unverified".

## 2. Finding levels

- **Observed**: directly visible in P1/P2/P3. Cite the exact evidence.
  E.g.: "Observed: green rectangular CTA button under the hero (desktop screenshot 1440px)."
- **Estimated**: approximate measurement from visual evidence.
  Always include a margin ("≈", "on the order of", range).
  E.g.: "Estimated: navy blue ≈ #1B2A4A (±10%, eyedropper on compressed screenshot)."
- **Hypothesis**: reasonable deduction not verifiable as-is.
  E.g.: "Hypothesis: 12-column grid (suggested alignments, code not provided)."
- **Unknown / Not observable**: write explicitly rather than leaving a gap.
  E.g.: "Unknown: behavior below 360px (no mobile screenshot provided)."

## 3. Confidence levels

| Level | When to use |
|--------|-------------|
| **High** | P1 or P2, cited evidence, reproducible. |
| **Medium** | P3 or visual estimate with margin, or partial P1 (truncated file). |
| **Low** | P4 or logical but unverified hypothesis. |
| **Not assessable** | P5 only, or total absence of evidence. Write "Not assessable" + missing evidence. |

## 4. Forbidden / mandatory phrasing

- Forbidden: "the site uses React", "breakpoint at 768px", "WCAG AA accessible"
  without matching P1/P2 evidence.
- Mandatory: every report section contains at least one limitation mention.
- Mandatory: report section 10 ("Findings by confidence level")
  groups all findings sorted High → Not assessable.

## 5. Minimum traceability

Each finding follows the format:
`[Confidence: High|Medium|Low|Not assessable] [Status: Observed|Estimated|Hypothesis|Unknown] — statement. Evidence: …`

Example:
`[High] [Observed] — The header contains a left logo + 5 links + 1 CTA. Evidence: desktop screenshot 1440px + index.html:12-28.`
