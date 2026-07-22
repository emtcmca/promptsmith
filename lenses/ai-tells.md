---
name: ai-tells
applies-to: writing, copy, content, blog, post, marketing, email, AI writing, AI-sounding, humanize, sounds robotic, AI tells, remove AI-isms
---

# AI-Tells Lens

Catch and remove the patterns that make writing read as machine-generated. Run the draft against
the catalog below; for each hit, quote the offending text and propose a human rewrite. This lens
flags tells — pair it with `editorial` for general clarity/structure.

> Pattern taxonomy adapted from conorbronsdon/avoid-ai-writing (MIT).

## Never strip these (read before flagging anything)

This lens strips aggressively. That is correct for generic machine prose and **wrong** for the
four cases below. A word on the tier lists is a candidate, not a verdict — check it against these
carve-outs first. Over-stripping is a real defect of this lens, not a side effect to tolerate.

- **Quoted and attributed material.** Never rewrite inside a direct quotation, a testimonial, an
  excerpt, or anything attributed to a named person or document. Altering a quote to sound less
  AI-ish falsifies it. Flag nothing inside quote marks; if the surrounding prose introduces it
  badly, fix *that*.
- **Statutory, legal, regulatory, and contractual text.** Governing documents, statutes, policy
  language, and compliance copy use `vital`, `material`, `shall`, `ensure`, and similar terms as
  **terms of art with settled meaning**. Rewriting them changes what the document does. Leave
  them verbatim and say why you skipped them.
- **Domain terminology.** A word on a tier list can be the correct technical term in context —
  `harness` (test harness), `robust` (statistics), `key` (cryptography), `vital` (clinical
  vitals), `elevate` (medical). Judge by whether a domain reader would expect the word, not by
  whether it appears on the list.
- **A deliberate authorial voice.** If the author has an evident stylistic signature — recurring
  fragments, a motif of punctuation, an idiosyncratic sign-off, a consistent rhythm — **that is
  not an AI tell.** Enhance, don't override; suggest, don't replace. Where a change would alter
  voice rather than remove a tell, **flag it as a suggestion and leave the text alone.** This is
  the `editorial` lens's voice-preservation guardrail, restated here because `ai-tells` is
  routinely run alone (`--lens ai-tells`) and must carry its own counterweight rather than
  depending on `editorial` happening to co-fire.

When you skip a candidate under any carve-out above, **say so in the findings** — "left `vital`
at line 4 (statutory term)". A silent skip is indistinguishable from a miss.

## Two-pass discipline

1. **First pass** — scan all six categories, flag every hit with the quoted span.
2. **Draft the replacements** — for each hit, work out the plain-language replacement.
3. **Second pass** — re-scan those replacements in context; AI tells survive edits and breed new
   ones, so a fix that introduces a fresh tell is not a fix. Don't declare done until a clean pass
   finds nothing new.

**What gets emitted depends on the invoking route — this lens never decides that for itself.**

- **LENS without `--fix` (the default):** findings only, each with its proposed replacement
  quoted inline. Run steps 2–3 as *internal* work to validate the replacements you propose.
  **Do not emit a rewritten artifact** — the command's default contract is critique, not rewrite,
  and a lens may not override it.
- **LENS with `--fix`:** emit the corrected artifact as the deliverable, followed by the
  second-pass result in both directions (see `commands/lens.md` Step 6).
- **SHARPEN / FORGE:** fold the findings in as prohibitions/requirements in the emitted prompt.
  Nothing is rewritten.

## Tiered vocabulary

- **Tier 1 — always flag.** leverage, delve, robust, seamless, cutting-edge, game-changing,
  foster, underscore, realm, tapestry, testament, landscape, navigate (figurative), elevate,
  unlock, harness, pivotal, crucial, vital, embark, beacon. Replace with plain words.
- **Tier 2 — flag when clustered** (2+ in a paragraph). showcase, utilize, facilitate,
  comprehensive, holistic, nuanced, multifaceted, intricate, myriad, plethora.
- **Tier 3 — flag at high density** (repeated across the piece). meaningful, impactful, valuable,
  effective, essential, key, ensure, enhance.

## The catalog (6 categories)

**1. Content tells**
- Significance inflation — "plays a vital role," "stands as a testament," "a pivotal moment."
- Vague attribution — "experts say," "studies show," "it is widely believed" with no source.
- Formulaic balance — a tacked-on "challenges/limitations" or "however, it's important" hedge.
- Superficial "-ing" padding — "highlighting the importance of," "emphasizing the need to."

**2. Language tells**
- Tier-1/2/3 vocabulary above.
- Copula avoidance — "serves as," "acts as," "functions as" where "is" works.
- Synonym cycling — renaming the same thing three ways to avoid repetition (often less clear).
- Template phrases — "in today's fast-paced world," "it's important to note," "when it comes to,"
  "at the end of the day."

**3. Structure tells**
- Em-dash overuse — more than ~1 per paragraph reads as AI rhythm.
- Uniform rhythm — sentences and paragraphs all the same length; no short punchy lines.
- Rhetorical-question openers — "Ever wondered why…?" "What if I told you…?"
- Inline-header lists — every bullet is "**Bold lead-in:** explanation," repeated mechanically.
- "Not only X but also Y" / "X isn't just Y — it's Z" constructions.

**4. Communication tells**
- Chatbot artifacts — "Certainly!," "Great question!," "I'd be happy to."
- "Let's explore / let's dive in / let's unpack."
- Sycophancy — "You're absolutely right," "That's a fantastic point."
- Generic conclusions — "In conclusion, … remains a crucial aspect of."

**5. Structural detection**
- Boilerplate repetition — "the integration of," "the world of," "in the realm of" recurring.
- Hedge-stacking — "may potentially possibly help in some cases."
- Hashtag / emoji-bullet stuffing in prose that shouldn't have it.

**6. Tool fingerprints**
- Unfilled placeholders — `[Your Name]`, `[Company]`, `[Insert X here]` left in.
- Leftover markup — stray citation tokens, markdown pasted into plain-text channels, UTM cruft.
- AI self-reference — "As an AI," "As a language model," "I cannot browse."

## Output

Report findings worst-first: P0 placeholders/self-reference → P1 vocabulary/template phrases →
P2 rhythm/structure. Quote the offending span on every finding and give its replacement.

Then follow the invoking route, per "What gets emitted" above — findings only by default, the
corrected artifact plus the second-pass result under `--fix`, and folded-in requirements on a
SHARPEN/FORGE run. When you skip a candidate under a carve-out, say so in the findings.
