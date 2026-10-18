# Accessibility & usability — limits and grid

> Read before report section 8. Prerequisite: P1/P2/P3 evidence inventoried.
> Without keyboard/screen-reader testing: no definitive verdict.

## Warning (restate in every report)
Without keyboard, screen-reader, or instrumented measurements, no definitive
verdict (e.g. "WCAG compliant") is allowed. This review is a
**visual / static presumption**, bounded by the evidence.

## 1. What CAN be assessed from screenshots
- Apparent heading hierarchy (likely single H1? logical order?).
- Visible form labels (vs placeholders alone).
- Apparent readability: relative sizes, apparent contrast
  (always "apparent", never a numeric ratio without measurement).
- Apparent touch targets on mobile (large / small / cramped).
- Text over image without overlay (readability risk).

## 2. What CAN be assessed from provided code
- `lang`, `title`, landmarks (`header/nav/main/footer`), `h1–h6` levels.
- `<img>` `alt`, `label`/`aria-label`, roles, `aria-*`.
- Computable contrasts (if exact hex colors in the CSS).
- Visible focus (`:focus`), skip-link, static tab order.

## 3. What is FORBIDDEN without real testing
- Asserting WCAG compliance (A/AA/AAA) or a score.
- Asserting full screen-reader / keyboard-navigation compatibility.
- Computing a contrast ratio from a compressed screenshot.

## 4. Reporting grid
| Criterion | Status | Evidence | Confidence |
|---------|--------|--------|-----------|
| Single H1 and heading order | OK / Risk / Not verifiable | … | … |
| Form labels | … | … | … |
| Text alternatives | … | … | … |
| Apparent contrast | … | … | … |
| Touch targets | … | … | … |
| Focus / keyboard navigation | Not tested (default) | — | Not assessable |
| Screen reader | Not tested (default) | — | Not assessable |

## 5. Usability (bounded by evidence)
Journey readability, CTA clarity (action labels?), visible
feedback (states, errors), density, form length.
Each remark = observation + evidence + presumed user impact
("presumed", not "measured").
