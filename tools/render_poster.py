#!/usr/bin/env python3
"""Render the entry poster for make.fun competition news-image-20261124.

Draws a one-page newspaper front page that sums up the world news of
Tuesday 24 November 2026, using only stories reported that day (wire
reports via AP/AFP, SCMP's world page, Qatar Tribune, The Manila Times
and Horizon's 24 Nov 2026 digest). Offline asset builder: it is NOT run
by the grader. The grader runs main.ts, which copies the entry.png this
script produces. Output: ../entry.png (1024x1024, PNG, under 1 MiB).
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (20, 18, 14)
RED = (179, 32, 42)
GREY = (92, 86, 76)
BAND = (20, 18, 14)
WHITE = (250, 248, 243)

FONT_DIR = "/usr/share/fonts/truetype/noto/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


SERIF_BLACK = "NotoSerif-Black.ttf"
SERIF_BOLD = "NotoSerif-Bold.ttf"
SANS_BLACK = "NotoSans-Black.ttf"
SANS_BOLD = "NotoSans-Bold.ttf"
SANS = "NotoSans-Regular.ttf"


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_block(draw, x, y, w, kicker, headline, blurb, head_size=27, blurb_size=18):
    """One news block: red kicker, serif headline, sans blurb. Returns height used."""
    draw.text((x, y), kicker, font=font(SANS_BLACK, 18), fill=RED)
    y += 27
    hf = font(SERIF_BOLD, head_size)
    for line in wrap(draw, headline, hf, w):
        draw.text((x, y), line, font=hf, fill=INK)
        y += int(head_size * 1.15)
    y += 3
    bf = font(SANS, blurb_size)
    for line in wrap(draw, blurb, bf, w):
        draw.text((x, y), line, font=bf, fill=(52, 48, 40))
        y += int(blurb_size * 1.3)
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 40
    CW = W - 2 * M

    # --- top hairline + dateline strip -----------------------------------
    d.line([(M, 26), (W - M, 26)], fill=INK, width=3)
    d.text((M, 34), "ONE DAY · ONE IMAGE · THE WHOLE WORLD", font=font(SANS_BOLD, 19), fill=GREY)
    right = "EST. 2026"
    d.text((W - M - d.textlength(right, font=font(SANS_BOLD, 19)), 34), right,
           font=font(SANS_BOLD, 19), fill=GREY)

    # --- masthead ---------------------------------------------------------
    mast = "THE WORLD IN ONE PAGE"
    mf = font(SERIF_BLACK, 71)
    d.text(((W - d.textlength(mast, font=mf)) / 2, 58), mast, font=mf, fill=INK)

    # --- red date band ----------------------------------------------------
    d.rectangle([M, 148, W - M, 204], fill=RED)
    date_line = "TUESDAY · 24 NOVEMBER 2026"
    df = font(SANS_BLACK, 38)
    d.text(((W - d.textlength(date_line, font=df)) / 2, 157), date_line, font=df, fill=WHITE)

    # --- lead story -------------------------------------------------------
    y = 222
    d.text((M, y), "TOP STORY — UKRAINE · LIBYA · RUSSIA", font=font(SANS_BLACK, 21), fill=RED)
    y += 30
    hf = font(SERIF_BLACK, 46)
    for line in ["Ukraine Sea Drones Sink Russian", "Warship at a Libyan Base"]:
        d.text((M, y), line, font=hf, fill=INK)
        y += 52
    y += 4
    bf = font(SANS, 22)
    lead = ("Kyiv said its naval drones sank a Russian warship at a Libyan base. "
            "Moscow warned of a \u201cdangerous trend\u201d, Tripoli demanded answers, "
            "and the UN sought a probe.")
    for line in wrap(d, lead, bf, CW):
        d.text((M, y), line, font=bf, fill=(52, 48, 40))
        y += 28
    y += 8
    d.line([(M, y), (W - M, y)], fill=INK, width=2)
    y += 16

    # --- two-column grid --------------------------------------------------
    col_w = (CW - 40) // 2
    x1, x2 = M, M + col_w + 40
    grid_top = y
    blocks_left = [
        ("MYANMAR · THE HAGUE",
         "14 Nations Back ICJ Genocide Ruling",
         "Britain sanctioned Myanmar's leaders after the World Court's "
         "genocide ruling on the Rohingya."),
        ("UKRAINE WAR",
         "Kyiv Region Strikes Kill at Least 14",
         "Russian strikes hit homes across the Kyiv region overnight, "
         "Ukrainian officials said. (AFP)"),
        ("UNITED NATIONS · TECHNOLOGY",
         "UN Chief: Global AI Rules Within a Year",
         "Ant\u00f3nio Guterres urged states to agree a multilateral "
         "framework for managing AI risks."),
    ]
    blocks_right = [
        ("UNITED STATES",
         "US States Sue Musk Firms Over Grok Images",
         "States accuse Musk's companies of letting the Grok chatbot "
         "produce sexualised images."),
        ("MIDDLE EAST · ISRAEL",
         "Eisenkot Has Until Dec 6 to Form a Government",
         "Israel's opposition leader races to build a coalition to "
         "replace Benjamin Netanyahu."),
        ("ASIA",
         "Nepal Quake; Indonesia Fire Kills 24",
         "A 5.6-magnitude quake struck Nepal near China; a factory "
         "fire in Indonesia killed 24."),
    ]
    row_h = 144
    for i in range(3):
        draw_block(d, x1, grid_top + i * row_h, col_w, *blocks_left[i])
        draw_block(d, x2, grid_top + i * row_h, col_w, *blocks_right[i])
    # column divider
    mid = M + col_w + 20
    d.line([(mid, grid_top + 2), (mid, grid_top + 3 * row_h - 22)], fill=(196, 188, 168), width=2)
    y = grid_top + 3 * row_h - 4

    # --- markets band -----------------------------------------------------
    d.rectangle([M, y, W - M, y + 52], fill=BAND)
    markets = "MARKETS  ·  S&P 500 +4.7%  ·  NASDAQ +6.5%  ·  NIKKEI +3.9%  ·  DAX +2.2%  ·  BRENT $86.70"
    size = 23
    while size > 12 and d.textlength(markets, font=font(SANS_BOLD, size)) > CW - 32:
        size -= 1
    mkf = font(SANS_BOLD, size)
    d.text(((W - d.textlength(markets, font=mkf)) / 2, y + 14), markets, font=mkf, fill=WHITE)
    y += 66

    # --- in brief ---------------------------------------------------------
    brief = ("IN BRIEF — China opens its Tiangong station to a first foreign astronaut, "
             "Pakistan's Zeeshan Ali · Denmark bans school phones to grade 10 · "
             "Injured Gaza children arrive in the UK for care")
    brf = font(SANS, 19)
    for line in wrap(d, brief, brf, CW):
        d.text((M, y), line, font=brf, fill=(52, 48, 40))
        y += 25
    y += 6
    d.line([(M, y), (W - M, y)], fill=INK, width=3)
    foot = "Every story on this page was reported on Tuesday 24 November 2026."
    ff = font(SANS_BOLD, 18)
    d.text(((W - d.textlength(foot, font=ff)) / 2, y + 8), foot, font=ff, fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
