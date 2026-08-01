"""
Build lanyard.svg for Shrikant's GitHub profile.
Assembles the SVG with the base64 face image embedded.
"""
import os

OUT_DIR = r"s:\JavaScript Projects\Github readme"

with open(os.path.join(OUT_DIR, "_face_img_b64.txt"), "r") as f:
    FACE_B64 = f.read().strip()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 660" width="420" height="660" role="img" aria-label="Shrikant Tathe ID card lanyard">
<title>Shrikant Tathe — swinging ID badge</title>
<defs>
<style type="text/css"><![CDATA[
text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}}
@keyframes settle{{0%{{transform:rotate(0deg) translateY(-660px)}}18%{{transform:rotate(0deg) translateY(0)}}30%{{transform:rotate(13deg)}}46%{{transform:rotate(-9deg)}}62%{{transform:rotate(6deg)}}78%{{transform:rotate(-3.5deg)}}92%{{transform:rotate(1.5deg)}}100%{{transform:rotate(0deg)}}}}
@keyframes sway{{0%,100%{{transform:rotate(-3.2deg)}}50%{{transform:rotate(3.2deg)}}}}
@keyframes cardWobble{{0%,100%{{transform:rotate(1.6deg)}}50%{{transform:rotate(-1.6deg)}}}}
@keyframes shine{{0%{{transform:translateX(-340px) skewX(-18deg)}}55%,100%{{transform:translateX(420px) skewX(-18deg)}}}}
@keyframes twinkle{{0%,100%{{opacity:0;transform:scale(.4)}}50%{{opacity:1;transform:scale(1)}}}}
@keyframes heartBeat{{0%,100%{{transform:scale(1)}}12%{{transform:scale(1.25)}}24%{{transform:scale(1)}}36%{{transform:scale(1.15)}}48%{{transform:scale(1)}}}}
.settle{{transform-origin:210px 6px;animation:settle 3.4s cubic-bezier(.34,1.1,.5,1) forwards}}
.sway{{transform-origin:210px 6px;animation:sway 4.2s ease-in-out 3.4s infinite}}
.wob{{transform-origin:210px 300px;animation:cardWobble 4.2s ease-in-out 3.4s infinite}}
.shine{{animation:shine 4.5s ease-in-out 3.6s infinite}}
.tw{{transform-box:fill-box;transform-origin:center;animation:twinkle 2.8s ease-in-out infinite}}
.hb{{transform-box:fill-box;transform-origin:center;animation:heartBeat 2.4s ease-in-out infinite}}
]]></style>
<linearGradient id="strapg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#dc2626"/><stop offset="50%" stop-color="#ef4444"/><stop offset="100%" stop-color="#dc2626"/>
</linearGradient>
<linearGradient id="cardg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0d0d18"/><stop offset="100%" stop-color="#08060f"/>
</linearGradient>
<linearGradient id="cardborder" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%"><animate attributeName="stop-color" values="#ef4444;#a855f7;#c084fc;#ef4444" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#a855f7;#ef4444;#ef4444;#a855f7" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="metal" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#c8ccd6"/><stop offset="45%" stop-color="#8a90a0"/><stop offset="55%" stop-color="#6a7080"/><stop offset="100%" stop-color="#9aa0b0"/>
</linearGradient>
<linearGradient id="shineg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".14"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/>
</linearGradient>
<linearGradient id="nameg2" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#ef4444;#a855f7;#ef4444" dur="5s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#a855f7;#ef4444;#a855f7" dur="5s" repeatCount="indefinite"/></stop>
</linearGradient>
<radialGradient id="lglow"><stop offset="0%" stop-color="#a855f7" stop-opacity=".2"/><stop offset="100%" stop-color="#a855f7" stop-opacity="0"/></radialGradient>
<radialGradient id="avatarGlow"><stop offset="0%" stop-color="#ef4444" stop-opacity=".3"/><stop offset="100%" stop-color="#ef4444" stop-opacity="0"/></radialGradient>
<filter id="glow2"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="cardShadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity=".55"/></filter>
<clipPath id="cardclip"><rect x="82" y="298" width="256" height="330" rx="20"/></clipPath>
<clipPath id="avatarClip"><circle cx="210" cy="412" r="55"/></clipPath>
</defs>

<circle cx="210" cy="440" r="230" fill="url(#lglow)"><animate attributeName="r" values="230;250;230" dur="5s" repeatCount="indefinite"/></circle>

<g class="tw" style="animation-delay:.5s"><path d="M60 200l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#fca5a5"/></g>
<g class="tw" style="animation-delay:1.6s"><path d="M372 300l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#ef4444"/></g>
<g class="tw" style="animation-delay:2.7s"><path d="M52 480l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#c084fc"/></g>
<g class="hb" style="animation-delay:1s"><path d="M368 480 c-4-9-17-7-17 3 0 7 10 13 17 18 7-5 17-11 17-18 0-10-13-12-17-3z" fill="#ef4444" opacity=".8" filter="url(#glow2)"/></g>

<!-- pendulum: settle then sway -->
<g class="settle"><g class="sway">

  <!-- Strap -->
  <g>
    <path d="M191 -6 L229 -6 L226 236 L194 236 Z" fill="url(#strapg)"/>
    <line x1="196" y1="0" x2="198.5" y2="234" stroke="#fff" stroke-opacity=".55" stroke-width="1" stroke-dasharray="4 3"/>
    <line x1="224" y1="0" x2="221.5" y2="234" stroke="#fff" stroke-opacity=".55" stroke-width="1" stroke-dasharray="4 3"/>
    <text x="0" y="0" font-size="10.5" font-weight="bold" fill="#fff" opacity=".92" letter-spacing="2" transform="translate(214,18) rotate(90)">SHRIKANT.DEV &#x2615; CODE &#x2615; SHRIKANT.DEV</text>
  </g>

  <!-- Clasp + ring -->
  <rect x="188" y="232" width="44" height="26" rx="6" fill="url(#metal)" stroke="#4a4f5c" stroke-width="1"/>
  <rect x="199" y="238" width="22" height="7" rx="3.5" fill="#3c414e"/>
  <circle cx="210" cy="272" r="14" fill="none" stroke="url(#metal)" stroke-width="5.5"/>

  <!-- Card (secondary wobble) -->
  <g class="wob">
    <rect x="82" y="298" width="256" height="330" rx="20" fill="url(#cardg)" stroke="url(#cardborder)" stroke-width="2" filter="url(#cardShadow)"/>
    <!-- slot -->
    <rect x="180" y="310" width="60" height="10" rx="5" fill="#040c14" stroke="#3b1d50" stroke-width="1"/>

    <g clip-path="url(#cardclip)">
      <!-- header band -->
      <rect x="82" y="298" width="256" height="34" fill="#1a0e24" opacity=".9"/>
      <text x="98" y="320" font-size="9" fill="#8b949e" letter-spacing="1.5">DEVELOPER ID</text>
      <text x="322" y="320" text-anchor="end" font-size="9" fill="#ef4444" letter-spacing="1.5">ST-2024</text>

      <!-- avatar circle glow -->
      <circle cx="210" cy="412" r="62" fill="url(#avatarGlow)"/>
      <!-- avatar border -->
      <circle cx="210" cy="412" r="59" fill="none" stroke="url(#cardborder)" stroke-width="2.5"/>
      <!-- Avatar with face image -->
      <g clip-path="url(#avatarClip)">
        <rect x="155" y="357" width="110" height="110" fill="#120b18"/>
        <image x="155" y="357" width="110" height="110" href="data:image/png;base64,{FACE_B64}"/>
      </g>

      <!-- shine overlay -->
      <rect x="82" y="298" width="110" height="330" fill="url(#shineg)" class="shine"/>

      <!-- Name -->
      <text x="210" y="490" text-anchor="middle" font-size="17" font-weight="bold" fill="url(#nameg2)" filter="url(#glow2)">Shrikant Tathe</text>

      <!-- Role -->
      <rect x="118" y="497" width="184" height="20" rx="10" fill="#1a0e24"/>
      <text x="210" y="511" text-anchor="middle" font-size="10.5" fill="#c084fc" letter-spacing=".5">Full Stack Java Dev</text>

      <!-- divider -->
      <line x1="110" y1="525" x2="310" y2="525" stroke="#3b1d50" stroke-width="1"/>

      <!-- Info rows -->
      <text x="110" y="543" font-size="10" fill="#6b7280">&#x1F393;</text>
      <text x="126" y="543" font-size="10" fill="#9ca3af">DYPCOE, Pune</text>
      <text x="110" y="560" font-size="10" fill="#6b7280">&#x1F4C5;</text>
      <text x="126" y="560" font-size="10" fill="#9ca3af">2023 - 2027</text>
      <text x="110" y="577" font-size="10" fill="#6b7280">&#x1F4A1;</text>
      <text x="126" y="577" font-size="10" fill="#9ca3af">AI/ML In Progress</text>
      <text x="110" y="594" font-size="10" fill="#6b7280">&#x1F4EC;</text>
      <text x="126" y="594" font-size="10" fill="#9ca3af">Open to Internships</text>

      <!-- bottom bar -->
      <rect x="82" y="606" width="256" height="22" fill="#0e0914" opacity=".8"/>
      <text x="210" y="621" text-anchor="middle" font-size="9" fill="#ef4444" letter-spacing="2">github.com/Shrikant922</text>

      <!-- QR-like decorative dots/barcode -->
      <g transform="translate(290, 540)">
        <rect x="0" y="0" width="3" height="32" fill="#ef4444" opacity="0.8"/>
        <rect x="5" y="0" width="1" height="32" fill="#ef4444" opacity="0.6"/>
        <rect x="8" y="0" width="4" height="32" fill="#a855f7" opacity="0.9"/>
        <rect x="14" y="0" width="2" height="32" fill="#ef4444" opacity="0.7"/>
        <rect x="18" y="0" width="1" height="32" fill="#a855f7" opacity="0.5"/>
        <rect x="21" y="0" width="5" height="32" fill="#ef4444" opacity="0.8"/>
        <rect x="28" y="0" width="2" height="32" fill="#a855f7" opacity="0.9"/>
      </g>
    </g>
  </g>

</g></g>
</svg>'''

out_path = os.path.join(OUT_DIR, "lanyard.svg")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Lanyard SVG written to {out_path}")
print(f"File size: {os.path.getsize(out_path) / 1024:.0f} KB")
