---
name: ai-tells
applies-to: writing, copy, content, blog, post, marketing, email, AI writing, AI-sounding, humanize, sounds robotic, AI tells, remove AI-isms
---

# AI-Tells Lens

Catch and remove the patterns that make writing read as machine-generated. Run the draft against
the catalog below; for each hit, quote the offending text and propose a human rewrite. This lens
flags tells — pair it with `editorial` for general clarity/structure.

> Pattern taxonomy adapted from conorbronsdon/avoid-ai-writing (MIT).

## Two-pass discipline

1. **First pass** — scan all six categories, flag every hit with the quoted span.
2. **Rewrite** — produce the cleaned version.
3. **Second pass** — re-scan the rewrite; AI tells survive edits and breed new ones. Don't declare
   done until a clean pass finds nothing new.

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

Report findings worst-first (P0 placeholders/self-reference → P1 vocabulary/template phrases →
P2 rhythm/structure), then the rewritten text, then the second-pass result. For a SHARPEN/FORGE
run, fold these as prohibitions/requirements into the emitted prompt instead of rewriting.
