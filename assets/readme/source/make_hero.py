#!/usr/bin/env python3
"""OverSpec's README title: the icon redrawn from its 16-by-16 pixel grid, the name, the app's tagline and stripe
rule, and the kinds of game one library holds, as the Show menu's chips. Colours are the app's (Cinema theme)."""
import sys

BG, SURFACE, RAISED, TEXT, MUTED, ACCENT = "#080c16", "#141d30", "#23324c", "#f2f5fb", "#a7b3c5", "#96f4df"
MINT = "#74f1de"
STRIPES = ["#e8413c", "#f5d33f", "#3fc56b", "#3fc8e8"]
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

# The icon, measured from release/icon/overspec.png in cells of its pixel grid (65 of its 1024 pixels each): a stepped
# outer octagon whose lower right is cut straight where the stripes end, a smooth octagonal hole, and the four stripes
# running where column + row is 20.18 to 23.57. Its rounded square spans cells 0.15 to 14.8.
OUTER = [(5, 2), (10, 2), (10, 3), (11, 3), (11, 4), (12, 4), (12, 5), (13, 5), (13, 10.57), (10.57, 13), (5, 13),
         (5, 12), (4, 12), (4, 11), (3, 11), (3, 10), (2, 10), (2, 5), (3, 5), (3, 4), (4, 4), (4, 3), (5, 3)]
HOLE = [(5.92, 4.5), (9.13, 4.5), (10.4, 5.77), (10.4, 9.23), (9.13, 10.5), (5.92, 10.5), (4.65, 9.23), (4.65, 5.77)]
SQUARE = (0.15, 14.8)


def loop(points):
    return "M" + " L".join("%g,%g" % p for p in points) + "Z"


def icon(x, y, size):
    """The app icon: a navy rounded square, the mint ring, and the four stripes across its lower right."""
    lo, hi = SQUARE
    scale = size / (hi - lo)
    ring = loop(OUTER) + loop(HOLE)
    edges = [20.18 + i * (23.57 - 20.18) / 4 for i in range(5)]
    bands = "".join('<polygon fill="%s" points="%g,0 0,%g 0,%g %g,0"/>' % (c, a, a, b, b)
                    for c, a, b in zip(STRIPES, edges, edges[1:]))
    return f'''<g transform="translate({x} {y})">
    <defs>
      <linearGradient id="iconBg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e1e4b"/><stop offset="1" stop-color="#030a1e"/></linearGradient>
    </defs>
    <rect width="{size}" height="{size}" rx="{size * 0.21:g}" fill="url(#iconBg)"/>
    <g transform="scale({scale:g}) translate({-lo} {-lo})">
      <defs><clipPath id="ring"><path d="{ring}" clip-rule="evenodd"/></clipPath></defs>
      <path d="{ring}" fill="{MINT}" fill-rule="evenodd"/>
      <g clip-path="url(#ring)">{bands}</g>
    </g>
  </g>'''


def chip(x, y, label, width, chosen=False):
    fill, ink = (ACCENT, BG) if chosen else (RAISED, TEXT)
    return (f'<rect x="{x}" y="{y}" width="{width}" height="46" rx="10" fill="{fill}"/>'
            f'<text x="{x + width / 2:g}" y="{y + 30}" text-anchor="middle" font-size="21" fill="{ink}">{label}</text>')


def main(out):
    rule = "".join(f'<rect x="{230 + i * 36}" y="190" width="36" height="6" fill="{c}"/>' for i, c in enumerate(STRIPES))
    chips = [(774, 92, "Spectrum", 158, True), (944, 92, "Spectrum Next", 192, False),
             (774, 150, "Spec256", 130, False), (916, 150, "ZX-Poly", 118, False), (1046, 150, "Timex", 90, False),
             (774, 208, "NexClash .nxc", 178, False), (964, 208, "ULAplus", 116, False)]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="390" viewBox="0 0 1200 390" role="img" aria-labelledby="title desc">
  <title id="title">OverSpec</title>
  <desc id="desc">OverSpec, your Spectrum universe: classic ZX Spectrum games, enhanced colour editions and Spectrum Next games in one library, for Windows, Linux and Mac.</desc>
  <rect width="1200" height="390" rx="28" fill="{BG}"/>
  {icon(64, 60, 140)}
  <g font-family="{SANS}">
    <text x="228" y="150" font-size="86" font-weight="500" fill="{TEXT}" letter-spacing="-1">OverSpec</text>
    <text x="232" y="180" font-size="18" fill="{MUTED}" letter-spacing="2">YOUR SPECTRUM UNIVERSE</text>
    {rule}
    <text x="774" y="74" font-size="18" fill="{ACCENT}" letter-spacing="2.4">ONE LIBRARY</text>
    {"".join(chip(*c) for c in chips)}
    <text x="64" y="304" font-size="29" fill="{TEXT}">Classic Spectrum games, colour editions and Spectrum Next games,</text>
    <text x="64" y="342" font-size="29" fill="{TEXT}">picked from one library and played from the sofa.</text>
  </g>
  <text x="1136" y="342" text-anchor="end" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="18" fill="{MUTED}">Windows · Linux · Mac</text>
</svg>
'''
    open(out, "w", encoding="utf-8", newline="\n").write(svg)


if __name__ == "__main__":
    main(sys.argv[1])
