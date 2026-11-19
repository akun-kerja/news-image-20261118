#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news front page (1024x1024 PNG).

Stories verified 19 Nov 2026 from multiple independent news summaries
of 18 Nov 2026 (Open Chronicle, Horizon, Reuters, NPR, Daily News):
 1. APEC Shenzhen: Xi meets Putin; Trump-Xi-Putin trilateral on Thursday
 2. Gulf: Iran drones hit Kuwait & Bahrain; US strikes Qeshm missile site
 3. Ukraine: Kerch Bridge partly collapses after drone/missile attack
 4. USA: Peltola wins Alaska Senate seat; Democrats 56-44
 5. Nvidia: revenue doubles to $115.8bn; board rejects Huang return
 6. Health/weather: US loses measles-free status; Cyclone Akvan nears India
All text is drawn with DejaVu fonts; no photos or copied artwork.
Run: python3 build_image.py  -> writes entry.png (<=1 MiB, 1024x1024)
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W = H = 1024
BG = (253, 252, 248)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (16, 42, 90)
TEAL = (0, 105, 105)
GOLD = (176, 124, 0)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_panel(d, x, y, w, h, tag, tag_color, headline, body, icon):
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=(255, 255, 255),
                        outline=(200, 200, 195), width=2)
    d.rounded_rectangle([x, y, x + w, y + 44], radius=14, fill=tag_color)
    d.rectangle([x, y + 30, x + w, y + 44], fill=tag_color)
    d.text((x + 16, y + 9), tag, font=font(SANS, 22), fill=(255, 255, 255))
    # simple pictogram circle on the right of the headline
    cx, cy = x + w - 32, y + 68
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], outline=tag_color, width=3)
    d.text((cx - 9, cy - 11), icon, font=font(SANS, 18), fill=tag_color)
    hl = wrap(d, headline, font(SANS, 25), w - 84)
    yy = y + 56
    for line in hl[:2]:
        d.text((x + 16, yy), line, font=font(SANS, 25), fill=INK)
        yy += 31
    bl = wrap(d, body, font(SANS_R, 19), w - 32)
    yy += 4
    for line in bl[:2]:
        d.text((x + 16, yy), line, font=font(SANS_R, 19), fill=(60, 60, 60))
        yy += 25


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Masthead
    d.text((512, 18), "WORLD NEWS", font=font(SERIF, 72), fill=NAVY, anchor="ma")
    d.text((512, 102), "WEDNESDAY, 18 NOVEMBER 2026",
           font=font(SANS, 34), fill=RED, anchor="ma")
    d.line([40, 152, 984, 152], fill=NAVY, width=4)
    d.text((512, 162), "Six stories that defined the day",
           font=font(SERIF_R, 26), fill=(70, 70, 70), anchor="ma")
    # Lead story: APEC
    x, y, w, h = 40, 208, 944, 200
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=(255, 255, 255),
                        outline=(200, 200, 195), width=2)
    d.rounded_rectangle([x, y, x + w, y + 46], radius=14, fill=NAVY)
    d.rectangle([x, y + 32, x + w, y + 46], fill=NAVY)
    d.text((x + 16, y + 9), "LEAD  •  APEC, SHENZHEN", font=font(SANS, 23),
           fill=(255, 255, 255))
    # globe pictogram
    d.ellipse([x + w - 140, y + 60, x + w - 40, y + 160], outline=NAVY, width=5)
    d.ellipse([x + w - 115, y + 85, x + w - 65, y + 135], outline=TEAL, width=4)
    d.line([x + w - 140, y + 110, x + w - 40, y + 110], fill=TEAL, width=3)
    hl = ["Xi meets Putin in Shenzhen;",
          "Trump joins them on Thursday"]
    yy = y + 56
    for line in hl:
        d.text((x + 16, yy), line, font=font(SERIF, 33), fill=INK)
        yy += 42
    body = ("The leaders of China and Russia open APEC talks a day before "
            "an unprecedented three-way summit with the US president.")
    for line in wrap(d, body, font(SANS_R, 22), w - 200)[:2]:
        d.text((x + 16, yy), line, font=font(SANS_R, 22), fill=(60, 60, 60))
        yy += 28
    # Grid: 2 columns x 3 rows
    panels = [
        ("GULF", RED, "Iran drones strike Kuwait & Bahrain",
         "Drones hit Kuwait and Bahrain; the US strikes a missile "
         "site on Qeshm Island.", "\u2601"),
        ("UKRAINE", TEAL, "Kerch Bridge partly collapses",
         "Ukrainian drones and missiles hit the bridge to Crimea; "
         "one arch falls.", "\u2693"),
        ("USA", NAVY, "Peltola wins Alaska Senate seat",
         "Democrat Mary Peltola unseats Dan Sullivan. Democrats "
         "take a 56\u201344 majority.", "\u2713"),
        ("TECH", GOLD, "Nvidia doubles to $115.8bn",
         "Record revenue, but the board rejects ex-chief Jensen "
         "Huang's return.", "\u25a3"),
        ("HEALTH", RED, "US loses measles-free status",
         "After 26 years, 5,400+ cases and 10 deaths. Ebola in "
         "DR Congo tops 11,000.", "+"),
        ("WEATHER", TEAL, "Cyclone Akvan nears India",
         "A severe storm heads for India's east coast; evacuations "
         "begin in Odisha.", "\u2248"),
    ]
    pw, ph, gap = 464, 176, 14
    for i, (tag, col, head, body, icon) in enumerate(panels):
        px = 40 + (i % 2) * (pw + gap)
        py = 424 + (i // 2) * (ph + gap)
        draw_panel(d, px, py, pw, ph, tag, col, head, body, icon)
    d.line([40, 992, 984, 992], fill=(200, 200, 195), width=2)
    d.text((512, 1000), "18 NOVEMBER 2026  •  APEC  •  GULF  •  UKRAINE  •  USA  •  TECH  •  HEALTH",
           font=font(SANS_R, 15), fill=(120, 120, 120), anchor="ma")
    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
