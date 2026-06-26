---
name: visual-design
applies-to: UI, visual style, theme, brand, typography, color, spacing, look and feel, aesthetic, tone
---

# Visual Design Lens

A senior visual/brand designer's eye. Especially for "make it feel ___" requests — force
the vague feeling into concrete visual decisions.

**Establish the intended aesthetic first.** Before judging, identify the target style family from
the request, the existing tokens, or the named adjectives. If it's genuinely unclear, flag it as
an open question — don't default to your own taste. The checks below split into two kinds, and the
split matters: **hard rules** are perception facts true in every aesthetic; **style-relative**
items are only "wrong" relative to a chosen family. Never penalize a design for not being a
different style (a brutalist or maximalist layout is not failing by breaking minimal conventions).

## Hard rules — always enforced, every aesthetic

These are cognitive/perceptual facts, independent of style. A failure here is a real defect.

- **Readability.** Body line length in the 45–75ch range; text legible at its size; no walls of text.
- **Contrast / legibility.** Text and essential UI meet contrast needs against their background,
  whatever the palette (this overlaps the `accessibility` lens — both apply).
- **Type hierarchy exists.** A clear scale (display / heading / body / caption); the eye can rank
  importance without reading.
- **Spacing is systematic.** A consistent spacing scale with rhythm and alignment — not arbitrary
  per-element pixel values.
- **Visual weight directs attention.** The eye lands where it should; the primary element wins;
  nothing important competes with noise.
- **Color is intentional and consistent.** Semantic colors (success/error/etc.) used consistently;
  palette has intent, not accumulation.

## Style-relative — judge *within* the chosen family, never cross-penalize

Each family has its own internally-consistent answers to these. Evaluate whether the design is
coherent and well-executed *for its family*, not whether it matches a default taste.

- **Palette mood** — muted vs. saturated vs. high-contrast.
- **Decoration level** — minimal/restrained vs. expressive/maximal.
- **Type personality** — neutral grotesk vs. editorial serif vs. display/character.
- **Corner radius & shape** — sharp vs. soft vs. organic.
- **Motion** — still vs. subtle vs. animated/expressive (if animated, does it support meaning?).
- **Density** — airy whitespace vs. dense/information-rich.

Common style families (not exhaustive): **modern-minimal, editorial, brutal, playful,
premium-luxury, tech-cyberpunk, warm-content, brand-driven.** Each sets its own defaults for the
items above — e.g. minimal favors airy + muted + restrained; brutal favors dense + high-contrast +
sharp; both can be excellent.

## Translating the request

- **Name the adjectives.** Calm? Authoritative? Playful? Premium? Pin the 2–3 target words.
- **Translate feeling → mechanics**, *within the family*: calm = generous whitespace, muted
  palette, low-contrast motion; authoritative = strong type hierarchy, restrained color,
  structure over decoration.
- **Restraint, family-appropriate.** What can be removed without breaking the intended aesthetic?
  Decoration that doesn't earn its place *by the family's own standard*.
- **Consistency with brand.** Does it match existing brand tokens, or drift?
