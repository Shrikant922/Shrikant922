"""
Build banner-light.svg: light-mode recolor of banner.svg.
Reads the dark banner and does color replacements for light theme.
"""
import os, re

OUT_DIR = r"s:\JavaScript Projects\Github readme"

with open(os.path.join(OUT_DIR, "banner.svg"), "r", encoding="utf-8") as f:
    svg = f.read()

# Color replacements for light mode
replacements = [
    # Background: dark -> light lavender/rose
    ('#120b18', '#faf5ff'),
    ('#160e22', '#fef2f2'),
    ('#0e0914', '#f5f3ff'),
    # Card/panel bg: dark -> light
    ('#1a0e24', '#f3e8ff'),
    ('#0d0d0d', '#fefce8'),
    ('#1a1124', '#ede9fe'),
    # Border/separator colors
    ('#3b1d50', '#d8b4fe'),
    ('#2a1530', '#e9d5ff'),
    ('#3b2a5c', '#c4b5fd'),
    # Text: light on dark -> dark on light
    ('#e6edf3', '#1e1b4b'),
    ('#cdd3dd', '#374151'),
    ('#8b949e', '#6b7280'),
    ('#9aa4b2', '#4b5563'),
    # Dots pattern: reduce visibility
    ('rgba(168,85,247,.08)', 'rgba(168,85,247,.04)'),
    # Orb opacities: reduce
    ('stop-opacity=".10"', 'stop-opacity=".05"'),
    ('stop-opacity=".12"', 'stop-opacity=".06"'),
    ('stop-opacity=".07"', 'stop-opacity=".03"'),
    ('stop-opacity=".18"', 'stop-opacity=".08"'),
    # Border glow opacity: reduce
    ('stop-opacity=".35"', 'stop-opacity=".20"'),
    ('stop-opacity=".3"', 'stop-opacity=".18"'),
]

for old, new in replacements:
    svg = svg.replace(old, new)

# Update the title
svg = svg.replace(
    'aria-label="Shrikant Tathe - Full Stack Java Developer and AIML Enthusiast"',
    'aria-label="Shrikant Tathe - Full Stack Java Developer and AIML Enthusiast (Light)"'
)

# Write light banner
out_path = os.path.join(OUT_DIR, "banner-light.svg")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Light banner written to {out_path}")
print(f"File size: {os.path.getsize(out_path) / 1024:.0f} KB")
