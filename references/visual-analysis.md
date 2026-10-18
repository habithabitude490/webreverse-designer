# Visual analysis — method

> Read at steps 2, 3, and 5 (structure, style, interactions).
> Prerequisite: `evidence-and-confidence.md` (Observed/Estimated/Hypothesis statuses).

## Principle
Describe only what is visible. Every visual claim cites its
source (screenshot + width, or file + line).

## 1. Preparation
1. Number the screenshots (S1, S2…) with page + width in px when known.
2. Note quality: compressed / cropped / annotated / full.
3. If a width is unknown, write "unknown width" — never guess it.

## 2. Structural inventory grid
For each page / screenshot, fill in:

- Header: logo, nav, CTA, sticky? (sticky = observed only with 2 scrolled
  screenshots or `position: sticky` in the provided CSS).
- Navigation: items, hierarchy, mobile burger, active state.
- Hero: title, subtitle, CTA(s), visual, background.
- Sections: count, order, headings, patterns (alternation, bands).
- Cards: grid, content (image/title/text/link), uniformity.
- Forms: fields, labels, buttons, visible error messages.
- CTAs: exact labels, position, style, repetition.
- Footer: columns, links, legal notices, social.
- Recurring components: buttons, badges, testimonials, FAQ, pricing…

Status per element: present / absent / uncertain + evidence.

## 3. Style grid
- Palette: eyedropper when possible (local tool), otherwise "estimated" + margin.
  Max 8 colors: background, text, primary, secondary, accent, success/error, neutrals.
- Typography: families (guessed = "appearance: geometric sans-serif,
  similar to…" — never assert a font without CSS evidence), relative
  sizes (H1 > H2 > body), weights, apparent line-heights.
- Hierarchy: reading order, size contrast, weight.
- Spacing: density (airy / compact), regular vertical rhythm?
- Grid: apparent columns, gutters, max content width?
  → Hypothesis by default, unless CSS provided.
- Borders / radii / shadows: estimated px values + Medium confidence.
- Iconography: style (outline / solid / emoji), consistency, sizes.

## 4. Interactions — strict rule
Document an interaction ONLY if:
- (a) observed: video, GIF, before/after series, visible hover state in screenshot; or
- (b) proven by code: JS listener, CSS state class, ARIA attribute.
Otherwise write "Not observed". Example phrasing:
- "Observed: underlined nav links on hover (screenshots S2/S3)." [High]
- "Proven by code: `menu.js:15` toggles `.open` on click." [High]
- "Not observed: mobile burger behavior (no screenshot / code)."

## 5. Anti-invention
- Do not infer animation from a static screenshot.
- Do not infer sticky from a single screenshot.
- Do not name a framework from visual style.
