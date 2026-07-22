"""One-off generator for the answer-delta proof asset:
    docs/assets/proof-prompt-delta.png  — the workhorse still image (skims into HN/LinkedIn/dev.to)
    docs/assets/proof-prompt-delta.gif  — animates the reveal (social / dev.to asset)

Design: the PROMPT DELTA. One-line request in → the complete prompt promptsmith hands back, with
every added line tagged in the margin with the decision the one-liner left unstated. The point is
that the length is recovered senior judgment, not padding — so each annotation names the specific
thing a rushed one-liner forgets.

Content is faithful to docs/assets/proof-answer-delta.md (the fleshed prompt, Panel 3). Honesty
floor intact: the OPEN QUESTION line shows the tool flagging what it cannot know instead of guessing.

Not part of the package; run once, the image + gif are the committed artifacts."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = r"C:\Windows\Fonts\CascadiaMono.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\consolab.ttf"
FS = 16
font = ImageFont.truetype(FONT_PATH, FS)
font_b = ImageFont.truetype(FONT_BOLD_PATH, FS)
font_sm = ImageFont.truetype(FONT_PATH, 14)
font_title = ImageFont.truetype(FONT_BOLD_PATH, 19)

# GitHub-dark palette (matches make-sharpen-gif.py)
BG = (13, 17, 23)
PANEL = (22, 27, 34)
FG = (201, 209, 217)
DIM = (110, 118, 129)
GREEN = (63, 185, 80)
BLUE = (88, 166, 255)
ORANGE = (219, 154, 60)
GREEN_TAG_BG = (18, 38, 24)
BLUE_TAG_BG = (18, 31, 48)
LINE_H = 22

# ---------------------------------------------------------------- content
INPUT_CMD = "/promptsmith:sharpen write a function to retry a failed API call"

# rows of the OUTPUT prompt: (kind, text, annotation)
#   kind: head (section label, blue) | body (FG) | blank
ROWS = [
    ("head", "ROLE: a backend engineer who treats a retry as a", None),
    ("body", "      correctness decision, not a loop.", None),
    ("head", "OBJECTIVE: retry ONLY when retrying is safe and can succeed.", None),
    ("blank", "", None),
    ("head", "REQUIREMENTS:", None),
    ("body", "- Retry only retryable failures: timeouts, 429, 5xx.", "you never said which failures are safe to retry"),
    ("body", "  Never 4xx (except 429) - they only waste the budget.", None),
    ("body", "- Exponential backoff WITH jitter.", "the thundering-herd storm you'd forget"),
    ("body", "- A total deadline, not just a max attempt count.", "attempts aren't time - one slow call runs past a count"),
    ("body", "- Honor a Retry-After header on 429/503.", None),
    ("blank", "", None),
    ("head", "PROHIBITIONS (must NOT do):", None),
    ("body", "- NEVER retry a non-idempotent POST unless the caller", "the one line that stops a double charge"),
    ("body", "  supplies an idempotency key.", None),
    ("body", "- Do NOT swallow the final error; surface what failed.", None),
    ("blank", "", None),
    ("head", "OPEN QUESTION (answer before building):", None),
    ("body", "- Is this call idempotent / does it carry a key?", "honesty floor: flags what it can't know - won't guess"),
    ("body", "  The retry is only safe if yes. I will not guess.", None),
]

ANNOT_X = 620


def annot_color(text):
    return GREEN if text.startswith("honesty floor") else ORANGE


def paint_block(d, ox, oy, n_rows=None, annots_on=None):
    """Render the OUTPUT prompt rows starting at (ox, oy).
    n_rows: reveal only the first n rows (for the GIF). None = all.
    annots_on: set of row indices whose margin note is drawn. None = all."""
    limit = len(ROWS) if n_rows is None else n_rows
    for i, (kind, text, annot) in enumerate(ROWS):
        if i >= limit:
            break
        y = oy + i * LINE_H
        if kind == "head":
            d.text((ox, y), text, font=font, fill=BLUE)
        elif kind == "body":
            d.text((ox, y), text, font=font, fill=FG)
        # margin annotation
        if annot and (annots_on is None or i in annots_on):
            c = annot_color(annot)
            d.text((ANNOT_X, y), "<-", font=font, fill=c)
            d.text((ANNOT_X + font.getlength("<- "), y), annot, font=font_sm, fill=c)


# ================================================================ STATIC PNG
def build_png():
    PADX = 28
    W = 1240
    top = 96
    input_h = 78
    body_start = top + input_h
    H = body_start + len(ROWS) * LINE_H + 92

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # title
    d.text((PADX, 22), "One line in. The prompt a senior would have written, out.",
           font=font_title, fill=FG)
    d.text((PADX, 52), "Same request. Every added line is a decision the one-liner left unstated - not padding.",
           font=font_sm, fill=DIM)

    # INPUT
    y = top
    tag = "YOU TYPE"
    d.rounded_rectangle([PADX, y, PADX + font_sm.getlength(tag) + 18, y + 22], radius=6, fill=BLUE_TAG_BG)
    d.text((PADX + 9, y + 3), tag, font=font_sm, fill=BLUE)
    pre = "/promptsmith:sharpen "
    d.text((PADX, y + 32), pre, font=font_b, fill=GREEN)
    d.text((PADX + font.getlength(pre), y + 32), INPUT_CMD[len(pre):], font=font, fill=FG)

    # OUTPUT tag
    tag2 = "YOU GET BACK - a complete, review-ready prompt"
    d.rounded_rectangle([PADX, body_start - 30, PADX + font_sm.getlength(tag2) + 18, body_start - 8],
                        radius=6, fill=GREEN_TAG_BG)
    d.text((PADX + 9, body_start - 27), tag2, font=font_sm, fill=GREEN)

    paint_block(d, PADX, body_start)

    # caption
    cap_y = H - 58
    d.text((PADX, cap_y), "Same one-liner. The invisible scaffolding a senior adds - named, so you don't have to",
           font=font_sm, fill=DIM)
    d.text((PADX, cap_y + 20), "remember to, every time. It never invents the answer to \"is this idempotent?\" - it flags it.",
           font=font_sm, fill=DIM)
    d.text((W - PADX - font_b.getlength("promptsmith"), cap_y + 10), "promptsmith", font=font_b, fill=BLUE)

    out = r"C:\dev\promptsmith\docs\assets\proof-prompt-delta.png"
    img.save(out)
    print("PNG:", out, img.size)


# ================================================================ ANIMATED GIF
GW, GH = 1240, 620
GPAD = 24


def gbase():
    img = Image.new("RGB", (GW, GH), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, GW - 1, 34], fill=PANEL)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([GPAD + i * 22, 12, GPAD + 12 + i * 22, 24], fill=c)
    d.text((GW / 2, 17), "PowerShell", font=font, fill=DIM, anchor="mm")
    return img, d


def gframe(typed=None, cursor=False, intro=False, n_rows=0, annots_on=None, caption=False):
    img, d = gbase()
    y = 34 + GPAD
    pre = "PS C:\\dev> "
    d.text((GPAD, y), pre, font=font, fill=GREEN)
    if typed is not None:
        d.text((GPAD + font.getlength(pre), y), typed, font=font, fill=FG)
        if cursor:
            cx = GPAD + font.getlength(pre) + font.getlength(typed)
            d.rectangle([cx, y, cx + 9, y + 16], fill=FG)
    y += LINE_H
    if intro:
        y += 6
        d.text((GPAD, y), "-> the prompt promptsmith hands back:", font=font, fill=DIM)
        y += LINE_H + 4
        paint_block(d, GPAD, y, n_rows=n_rows, annots_on=annots_on)
    if caption:
        cy = GH - 46
        d.text((GPAD, cy), "Same one-liner. The scaffolding a senior adds, made explicit -",
               font=font_sm, fill=GREEN)
        d.text((GPAD, cy + 18), "and it flags what it can't know instead of guessing.",
               font=font_sm, fill=GREEN)
    return img


def build_gif():
    frames, durs = [], []

    def add(img, ms):
        frames.append(img)
        durs.append(ms)

    # Phase 1 — type the one-liner
    typed = ""
    for ch in INPUT_CMD:
        typed += ch
        add(gframe(typed=typed, cursor=True), 20)
    add(gframe(typed=typed, cursor=True), 650)

    # Phase 2 — reveal the fleshed prompt, line by line
    for n in range(1, len(ROWS) + 1):
        add(gframe(typed=typed, intro=True, n_rows=n), 55)
    add(gframe(typed=typed, intro=True, n_rows=len(ROWS)), 800)

    # Phase 3 — pop the margin annotations in, one at a time
    annot_idxs = [i for i, r in enumerate(ROWS) if r[2]]
    on = set()
    for idx in annot_idxs:
        on = set(on) | {idx}
        add(gframe(typed=typed, intro=True, n_rows=len(ROWS), annots_on=set(on)), 90)
        add(gframe(typed=typed, intro=True, n_rows=len(ROWS), annots_on=set(on)), 620)

    # Phase 4 — caption, long hold
    add(gframe(typed=typed, intro=True, n_rows=len(ROWS), annots_on=set(annot_idxs), caption=True), 3200)

    out = r"C:\dev\promptsmith\docs\assets\proof-prompt-delta.gif"
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=durs, loop=0, optimize=True)
    print("GIF:", out, "frames:", len(frames))


if __name__ == "__main__":
    build_png()
    build_gif()
