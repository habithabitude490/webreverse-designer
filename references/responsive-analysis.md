# Responsive analysis — method

> Read at step 4, as soon as ≥ 1 screenshot or a CSS with `@media` is provided.
> Prerequisite: `evidence-and-confidence.md`. Without 2 widths: not assessable section.

## Principle
Responsive can only be assessed by comparing ≥ 2 real widths.
1 width = mandatory "Not assessable" section.

## 1. Reference widths (indicative, not normative)
- Mobile: ~360–414px — Large mobile / small tablet: ~480–768px
- Tablet / small desktop: ~768–1024px — Desktop: ~1280–1440px+

These bands classify received screenshots, NEVER assert
the site's breakpoints. Real breakpoints come only from code
(media queries) or screenshots with known exact widths.

## 2. Comparative protocol
For each component (header/nav, hero, card grid, form, footer):
1. Describe its state at each available width.
2. Note adaptations: burger switch, stacking, shrinking,
   hiding, overflow, overlap.
3. Qualify: fluid / breakpoint rupture / degraded / unreadable.
4. Cite evidence: "S1 1440px vs S3 390px".

## 3. Special cases
- Screenshot without width: usable as a "hint" (Medium confidence max),
  never to assert a breakpoint.
- Single width: write "Responsive not assessable — provide
  mobile + desktop screenshots" at the top + list missing evidence.
- Provided CSS: record exact `@media` (file:line) and present
  them as "breakpoints declared in the provided code", not as
  "verified behavior" unless matching screenshots exist.

## 4. Standard phrasing
- "Observed: horizontal nav at 1440px (S1) → burger at 390px (S3)." [High]
- "Estimated: stacked hero on mobile, title ≈ 28px vs ≈ 56px desktop." [Medium]
- "Unknown: 768–1024px range (no screenshot)."
- FORBIDDEN: "breakpoint at 768px" without a cited media query or exact width.
