"""
Build banner.svg for Shrikant's GitHub profile.
Fixed font sizing, layout spacing, and z-index ordering to prevent any clipping.
"""
import os

OUT_DIR = r"s:\JavaScript Projects\Github readme"

with open(os.path.join(OUT_DIR, "_banner_img_b64.txt"), "r") as f:
    BANNER_B64 = f.read().strip()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="1280" height="740" role="img" aria-label="Shrikant Tathe - Full Stack Java Developer and AIML Enthusiast">
<title>Shrikant Tathe — Full Stack Java Dev &amp; AIML Enthusiast</title>
<defs>
<style type="text/css"><![CDATA[
text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes popIn{{0%{{opacity:0;transform:translateY(14px) scale(.7)}}70%{{opacity:1;transform:translateY(-3px) scale(1.06)}}100%{{opacity:1;transform:translateY(0) scale(1)}}}}
@keyframes letterPop{{0%{{opacity:0;transform:scale(0) translateY(10px)}}60%{{opacity:1;transform:scale(1.2) translateY(-2px)}}100%{{opacity:1;transform:scale(1) translateY(0)}}}}
@keyframes floaty{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-8px)}}}}
@keyframes heartBeat{{0%,100%{{transform:scale(1)}}12%{{transform:scale(1.25)}}24%{{transform:scale(1)}}36%{{transform:scale(1.18)}}48%{{transform:scale(1)}}}}
@keyframes neonFlicker{{0%{{opacity:0}}5%{{opacity:.7}}7%{{opacity:.1}}10%{{opacity:.9}}12%{{opacity:.3}}16%,100%{{opacity:1}}}}
@keyframes twinkle{{0%,100%{{opacity:0;transform:scale(.4)}}50%{{opacity:1;transform:scale(1)}}}}
@keyframes slideInCode{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:translateY(0)}}}}
.ltr{{opacity:0;animation:letterPop .4s cubic-bezier(.2,.8,.3,1.3) forwards;display:inline-block}}
.ii,.pill,.soc,.st,.cl,.neon{{opacity:0}}
.pill{{transition:transform .2s ease,filter .2s ease;transform-box:fill-box;transform-origin:center;cursor:pointer}}
.pill:hover{{transform:scale(1.08);filter:brightness(1.35)}}
.tw{{transform-box:fill-box;transform-origin:center;animation:twinkle 2.6s ease-in-out infinite}}
.hb{{transform-box:fill-box;transform-origin:center;animation:heartBeat 2.2s ease-in-out infinite}}
.fl{{animation:floaty 5s ease-in-out infinite}}
.sep{{stroke:#2a1530;stroke-width:1;opacity:.7}}
.codeln{{opacity:0;animation:slideInCode .4s ease forwards}}
]]></style>

<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#120b18"/><stop offset="55%" stop-color="#160e22"/><stop offset="100%" stop-color="#0e0914"/>
</linearGradient>
<linearGradient id="nameg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#ef4444;#c084fc;#8b5cf6;#ef4444" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="55%"><animate attributeName="stop-color" values="#dc2626;#a855f7;#ef4444;#dc2626" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#8b5cf6;#ef4444;#c084fc;#8b5cf6" dur="7s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="borderg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#ef4444" stop-opacity=".35"/>
  <stop offset="50%" stop-color="#a855f7" stop-opacity=".3"/>
  <stop offset="100%" stop-color="#8b5cf6" stop-opacity=".35"/>
</linearGradient>
<radialGradient id="orbR"><stop offset="0%" stop-color="#ef4444" stop-opacity=".10"/><stop offset="100%" stop-color="#ef4444" stop-opacity="0"/></radialGradient>
<radialGradient id="orbP"><stop offset="0%" stop-color="#a855f7" stop-opacity=".12"/><stop offset="100%" stop-color="#a855f7" stop-opacity="0"/></radialGradient>
<radialGradient id="orbO"><stop offset="0%" stop-color="#f97316" stop-opacity=".07"/><stop offset="100%" stop-color="#f97316" stop-opacity="0"/></radialGradient>
<radialGradient id="charGlow"><stop offset="0%" stop-color="#a855f7" stop-opacity=".18"/><stop offset="100%" stop-color="#a855f7" stop-opacity="0"/></radialGradient>
<filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="neonGlow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="dots" width="30" height="30" patternUnits="userSpaceOnUse"><circle cx="15" cy="15" r=".6" fill="rgba(168,85,247,.08)"/></pattern>

<clipPath id="cPrompt"><rect x="48" y="30" width="0" height="50"><animate attributeName="width" from="0" to="500" dur="1s" begin=".3s" fill="freeze"/></rect></clipPath>
<clipPath id="cHi"><rect x="48" y="70" width="0" height="55"><animate attributeName="width" from="0" to="220" dur=".5s" begin="1.2s" fill="freeze"/></rect></clipPath>

<!-- QUOTE BOX CLIP PATHS (Aligned to text coordinates) -->
<clipPath id="q1"><rect x="48" y="258" width="0" height="30"><animate attributeName="width" from="0" to="350" dur=".7s" begin="3.4s" fill="freeze"/></rect></clipPath>
<clipPath id="q2"><rect x="48" y="284" width="0" height="30"><animate attributeName="width" from="0" to="350" dur=".6s" begin="4.2s" fill="freeze"/></rect></clipPath>

<!-- Cycling roles -->
<clipPath id="r1"><rect x="48" y="200" width="0" height="40"><animate attributeName="width" values="0;0;360;360;0;0" keyTimes="0;.01;.07;.2;.24;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
<clipPath id="r2"><rect x="48" y="200" width="0" height="40"><animate attributeName="width" values="0;0;360;360;0;0" keyTimes="0;.26;.32;.45;.49;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
<clipPath id="r3"><rect x="48" y="200" width="0" height="40"><animate attributeName="width" values="0;0;360;360;0;0" keyTimes="0;.51;.57;.7;.74;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
<clipPath id="r4"><rect x="48" y="200" width="0" height="40"><animate attributeName="width" values="0;0;360;360;0;0" keyTimes="0;.76;.82;.95;.99;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>

<clipPath id="charReveal"><rect x="680" y="100" width="600" height="0">
  <animate attributeName="height" from="0" to="640" dur="1.8s" begin=".5s" fill="freeze"/>
</rect></clipPath>

<linearGradient id="scanEdge" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#ef4444" stop-opacity="0"/><stop offset="18%" stop-color="#ef4444"/>
  <stop offset="50%" stop-color="#c084fc"/><stop offset="82%" stop-color="#a855f7"/>
  <stop offset="100%" stop-color="#a855f7" stop-opacity="0"/>
</linearGradient>
<linearGradient id="scanTrail" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#ef4444" stop-opacity="0"/><stop offset="100%" stop-color="#ef4444" stop-opacity=".15"/>
</linearGradient>

<clipPath id="bannerBox"><rect x="1" y="1" width="1278" height="738" rx="22"/></clipPath>
</defs>

<!-- ================= BACKGROUND ================= -->
<rect width="1280" height="740" rx="22" fill="url(#bg)"/>
<rect width="1280" height="740" rx="22" fill="url(#dots)"/>
<circle cx="200" cy="200" r="280" fill="url(#orbR)"><animate attributeName="r" values="280;310;280" dur="6s" repeatCount="indefinite"/></circle>
<circle cx="1060" cy="520" r="300" fill="url(#orbP)"><animate attributeName="r" values="300;330;300" dur="7s" repeatCount="indefinite"/></circle>
<circle cx="700" cy="120" r="200" fill="url(#orbO)"><animate attributeName="r" values="200;225;200" dur="5.5s" repeatCount="indefinite"/></circle>
<rect x="1" y="1" width="1278" height="738" rx="22" fill="none" stroke="url(#borderg)" stroke-width="1.5"/>

<!-- ================= LEFT: CONTENT ================= -->
<!-- Terminal prompt -->
<text clip-path="url(#cPrompt)" x="48" y="55" font-size="14"><tspan fill="#4ade80" font-weight="bold">user@dev</tspan><tspan fill="#8b949e">:~$ </tspan><tspan fill="#e6edf3">catty </tspan><tspan fill="#ef4444">README.md</tspan></text>

<!-- Hi, I'm -->
<text clip-path="url(#cHi)" x="48" y="96" font-size="22" font-weight="bold" fill="#e6edf3">Hey there! &#x1F44B;</text>

<!-- Name: Shrikant Tathe (Sized perfectly at 34px so it NEVER collides with editor at x=440) -->
<text x="48" y="160" font-size="34" font-weight="bold" fill="url(#nameg)" filter="url(#glow)" style="font-family:'Segoe Script', 'Brush Script MT', 'Comic Sans MS', cursive">
  <tspan class="ltr" style="animation-delay:1.50s">S</tspan><tspan class="ltr" style="animation-delay:1.55s">h</tspan><tspan class="ltr" style="animation-delay:1.60s">r</tspan><tspan class="ltr" style="animation-delay:1.65s">i</tspan><tspan class="ltr" style="animation-delay:1.70s">k</tspan><tspan class="ltr" style="animation-delay:1.75s">a</tspan><tspan class="ltr" style="animation-delay:1.80s">n</tspan><tspan class="ltr" style="animation-delay:1.85s">t</tspan>
  <tspan class="ltr" style="animation-delay:1.90s"> </tspan>
  <tspan class="ltr" style="animation-delay:1.95s">T</tspan><tspan class="ltr" style="animation-delay:2.00s">a</tspan><tspan class="ltr" style="animation-delay:2.05s">t</tspan><tspan class="ltr" style="animation-delay:2.10s">h</tspan><tspan class="ltr" style="animation-delay:2.15s">e</tspan>
</text>
<g class="hb" style="animation-delay:3s"><path d="M305 136 c-5-11-21-9-21 4 0 9 12 16 21 22 9-6 21-13 21-22 0-13-16-15-21-4z" fill="#ef4444" opacity=".95"/></g>

<!-- Cycling roles -->
<text clip-path="url(#r1)" x="48" y="208" font-size="15" fill="#ef4444" filter="url(#glow)">&lt; Full Stack Java Developer /&gt;</text>
<text clip-path="url(#r2)" x="48" y="208" font-size="15" fill="#ef4444" filter="url(#glow)">&lt; AIML In Progress /&gt;</text>
<text clip-path="url(#r3)" x="48" y="208" font-size="15" fill="#ef4444" filter="url(#glow)">&lt; Spring Boot Architect /&gt;</text>
<text clip-path="url(#r4)" x="48" y="208" font-size="15" fill="#ef4444" filter="url(#glow)">&lt; Code. Coffee. Repeat. /&gt;</text>

<!-- Quote box -->
<g class="cl" style="animation:fadeIn .5s ease 3.2s forwards">
  <rect x="48" y="236" width="340" height="68" rx="8" fill="#1a0e24" stroke="#3b1d50" stroke-width="1"/>
  <rect x="48" y="240" width="3.5" height="60" rx="1.5" fill="#ef4444"/>
</g>
<text clip-path="url(#q1)" x="72" y="266" font-size="14" fill="#e6edf3">I use AI... responsibly.</text>
<text clip-path="url(#q2)" x="72" y="288" font-size="14"><tspan fill="#a855f7" font-weight="bold">Mostly.</tspan><tspan fill="#e6edf3"> &#x1F608;</tspan></text>
<g class="tw" style="animation-delay:.9s"><path d="M360 260l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#c084fc"/></g>

<!-- Tech Stack -->
<text class="ii" x="48" y="348" font-size="15" fill="#a855f7" font-weight="bold" style="animation:fadeIn .4s ease 4.6s forwards">&#x1F9E9; Tech Stack</text>
<!-- Row 1 -->
<g class="pill" style="animation:fadeIn .3s ease 4.8s forwards"><rect x="48" y="364" width="65" height="26" rx="13" fill="rgba(239,68,68,.13)" stroke="#ef4444" stroke-width="1"/><text x="80" y="381" text-anchor="middle" font-size="12" fill="#fca5a5" font-weight="bold">Java</text></g>
<g class="pill" style="animation:fadeIn .3s ease 4.9s forwards"><rect x="121" y="364" width="88" height="26" rx="13" fill="rgba(247,223,30,.10)" stroke="#f7df1e" stroke-width="1"/><text x="165" y="381" text-anchor="middle" font-size="12" fill="#fde047" font-weight="bold">JavaScript</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5s forwards"><rect x="217" y="364" width="76" height="26" rx="13" fill="rgba(53,114,165,.14)" stroke="#3572A5" stroke-width="1"/><text x="255" y="381" text-anchor="middle" font-size="12" fill="#93c5fd" font-weight="bold">Python</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.1s forwards"><rect x="301" y="364" width="70" height="26" rx="13" fill="rgba(97,218,251,.10)" stroke="#61dafb" stroke-width="1"/><text x="336" y="381" text-anchor="middle" font-size="12" fill="#67e8f9" font-weight="bold">React</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.15s forwards"><rect x="379" y="364" width="75" height="26" rx="13" fill="rgba(109,179,63,.13)" stroke="#6DB33F" stroke-width="1"/><text x="416" y="381" text-anchor="middle" font-size="12" fill="#86efac" font-weight="bold">Spring</text></g>
<!-- Row 2 -->
<g class="pill" style="animation:fadeIn .3s ease 5.2s forwards"><rect x="48" y="398" width="102" height="26" rx="13" fill="rgba(109,179,63,.13)" stroke="#6DB33F" stroke-width="1"/><text x="99" y="415" text-anchor="middle" font-size="12" fill="#86efac" font-weight="bold">Spring Boot</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.3s forwards"><rect x="158" y="398" width="78" height="26" rx="13" fill="rgba(168,85,247,.13)" stroke="#a855f7" stroke-width="1"/><text x="197" y="415" text-anchor="middle" font-size="12" fill="#c4b5fd" font-weight="bold">REST API</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.4s forwards"><rect x="244" y="398" width="70" height="26" rx="13" fill="rgba(245,158,11,.12)" stroke="#f59e0b" stroke-width="1"/><text x="279" y="415" text-anchor="middle" font-size="12" fill="#fcd34d" font-weight="bold">MySQL</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.5s forwards"><rect x="322" y="398" width="68" height="26" rx="13" fill="rgba(227,79,38,.13)" stroke="#e34f26" stroke-width="1"/><text x="356" y="415" text-anchor="middle" font-size="12" fill="#ff8a65" font-weight="bold">HTML</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.6s forwards"><rect x="398" y="398" width="60" height="26" rx="13" fill="rgba(168,85,247,.13)" stroke="#a855f7" stroke-width="1"/><text x="428" y="415" text-anchor="middle" font-size="12" fill="#c4b5fd" font-weight="bold">CSS</text></g>

<!-- About Me -->
<text class="ii" x="48" y="465" font-size="15" fill="#ef4444" font-weight="bold" style="animation:fadeIn .4s ease 5.8s forwards">&#x2615; About Me</text>
<text class="ii" x="48" y="490" font-size="13.5" style="animation:fadeIn .4s ease 6s forwards"><tspan fill="#4ade80">&gt;_ </tspan><tspan fill="#cdd3dd">Building full-stack apps &amp; learning AI/ML.</tspan></text>
<text class="ii" x="48" y="514" font-size="13.5" style="animation:fadeIn .4s ease 6.2s forwards"><tspan fill="#fde047">&#x1F393; </tspan><tspan fill="#cdd3dd">DYPCOE, Pune  |  Comp. Engg. (2023-27)</tspan></text>
<text class="ii" x="48" y="538" font-size="13.5" style="animation:fadeIn .4s ease 6.4s forwards"><tspan fill="#a855f7">&#x1F680; </tspan><tspan fill="#cdd3dd">Open to internships &amp; collaborations.</tspan></text>

<!-- Stats bar -->
<g class="st" style="animation:fadeIn .5s ease 6.6s forwards">
  <rect x="48" y="562" width="530" height="66" rx="12" fill="#1a0e24" stroke="#3b1d50" stroke-width="1"/>
  <line x1="180" y1="574" x2="180" y2="616" class="sep"/>
  <line x1="312" y1="574" x2="312" y2="616" class="sep"/>
  <line x1="444" y1="574" x2="444" y2="616" class="sep"/>
  <text x="114" y="588" text-anchor="middle" font-size="11.5" fill="#9aa4b2">&#x1F4E6; Repos</text>
  <text x="246" y="588" text-anchor="middle" font-size="11.5" fill="#9aa4b2">&#x1F4BB; Commits</text>
  <text x="378" y="588" text-anchor="middle" font-size="11.5" fill="#9aa4b2">&#x2B50; Stars</text>
  <text x="502" y="588" text-anchor="middle" font-size="11.5" fill="#9aa4b2">&#x1F465; Followers</text>
</g>
<text class="st" x="114" y="616" text-anchor="middle" font-size="18" font-weight="bold" fill="#ef4444" filter="url(#glow)" style="animation:fadeIn .4s ease 6.8s forwards">15+</text>
<text class="st" x="246" y="616" text-anchor="middle" font-size="18" font-weight="bold" fill="#a855f7" filter="url(#glow)" style="animation:fadeIn .4s ease 6.95s forwards">70+</text>
<text class="st" x="378" y="616" text-anchor="middle" font-size="18" font-weight="bold" fill="#fde047" filter="url(#glow)" style="animation:fadeIn .4s ease 7.1s forwards">10+</text>
<text class="st" x="502" y="616" text-anchor="middle" font-size="18" font-weight="bold" fill="#c084fc" filter="url(#glow)" style="animation:fadeIn .4s ease 7.25s forwards">5+</text>

<!-- Neon sign (Bottom Left) -->
<g class="neon" style="animation:neonFlicker 2.4s ease 7.5s forwards">
  <text x="48" y="662" font-size="11" fill="#ef4444" filter="url(#neonGlow)" letter-spacing=".5" opacity=".9">&#x26A1; Training arc: defeated by NullPointerException.</text>
</g>

<!-- ================= CENTER: CODE EDITOR ================= -->
<g style="animation:fadeIn .6s ease 1s both">
  <rect x="420" y="46" width="300" height="225" rx="10" fill="#0d0d0d" stroke="#2a1530" stroke-width="1"/>
  <!-- title bar -->
  <rect x="420" y="46" width="300" height="26" rx="10" fill="#1a1124"/>
  <rect x="420" y="60" width="300" height="12" fill="#1a1124"/>
  <circle cx="436" cy="59" r="4.5" fill="#ff5f56"/>
  <circle cx="450" cy="59" r="4.5" fill="#ffbd2e"/>
  <circle cx="464" cy="59" r="4.5" fill="#27c93f"/>
  <text x="545" y="63" font-size="10" fill="#8b949e">dreams.jsx</text>
</g>
<!-- Code lines typed in -->
<text class="codeln" x="436" y="92" font-size="12" style="animation-delay:1.4s"><tspan fill="#c084fc">function</tspan><tspan fill="#e6edf3"> </tspan><tspan fill="#ffa657">buildDreams</tspan><tspan fill="#e6edf3">() {{</tspan></text>
<text class="codeln" x="436" y="110" font-size="12" style="animation-delay:1.8s"><tspan fill="#e6edf3">  </tspan><tspan fill="#c084fc">return</tspan><tspan fill="#e6edf3"> (</tspan></text>
<text class="codeln" x="436" y="128" font-size="12" style="animation-delay:2.2s"><tspan fill="#e6edf3">    </tspan><tspan fill="#ef4444">&lt;div</tspan><tspan fill="#e6edf3"> </tspan><tspan fill="#a855f7">className</tspan><tspan fill="#e6edf3">=</tspan><tspan fill="#a5d6ff">"dreams"</tspan><tspan fill="#ef4444">&gt;</tspan></text>
<text class="codeln" x="436" y="146" font-size="12" style="animation-delay:2.6s"><tspan fill="#e6edf3">      </tspan><tspan fill="#ef4444">&lt;Code /&gt;</tspan></text>
<text class="codeln" x="436" y="164" font-size="12" style="animation-delay:3s"><tspan fill="#e6edf3">      </tspan><tspan fill="#ffa657">&lt;Coffee /&gt;</tspan></text>
<text class="codeln" x="436" y="182" font-size="12" style="animation-delay:3.4s"><tspan fill="#e6edf3">      </tspan><tspan fill="#4ade80">&lt;Repeat /&gt;</tspan></text>
<text class="codeln" x="436" y="200" font-size="12" style="animation-delay:3.8s"><tspan fill="#e6edf3">      </tspan><tspan fill="#fde047">&lt;Success /&gt;</tspan></text>
<text class="codeln" x="436" y="218" font-size="12" style="animation-delay:4.2s"><tspan fill="#e6edf3">    </tspan><tspan fill="#ef4444">&lt;/div&gt;</tspan><tspan fill="#e6edf3">);</tspan></text>
<text class="codeln" x="436" y="236" font-size="12" style="animation-delay:4.6s"><tspan fill="#e6edf3">}} </tspan><tspan fill="#8b949e">// export default</tspan></text>

<!-- ================= TOP RIGHT: NEON SIGN ================= -->
<g class="neon" style="animation:neonFlicker 2.4s ease 5s forwards">
  <rect x="745" y="46" width="220" height="80" rx="12" fill="none" stroke="#a855f7" stroke-width="2" filter="url(#neonGlow)" opacity=".7"/>
  <text x="855" y="78" text-anchor="middle" font-size="19" font-weight="bold" fill="#ef4444" filter="url(#neonGlow)">&lt;/&gt;</text>
  <text x="855" y="98" text-anchor="middle" font-size="11" font-weight="bold" fill="#a855f7" filter="url(#neonGlow)" letter-spacing="2">KEEP CODING</text>
  <text x="855" y="114" text-anchor="middle" font-size="11" font-weight="bold" fill="#c084fc" filter="url(#neonGlow)" letter-spacing="2">KEEP GROWING</text>
</g>

<!-- ================= RIGHT SIDE: CHARACTER ================= -->
<circle cx="1020" cy="420" r="280" fill="url(#charGlow)"><animate attributeName="r" values="280;300;280" dur="5s" repeatCount="indefinite"/></circle>

<g class="fl">
  <g clip-path="url(#charReveal)">
    <!-- Shifted slightly down so character head doesn't overlap neon sign -->
    <image x="720" y="145" width="510" height="550" href="data:image/png;base64,{BANNER_B64}"/>
  </g>
</g>

<!-- Scan line sweep across character -->
<g clip-path="url(#bannerBox)">
  <rect x="720" y="145" width="510" height="4" fill="url(#scanEdge)" opacity=".8">
    <animate attributeName="y" from="145" to="700" dur="1.8s" begin=".5s" fill="freeze"/>
    <animate attributeName="opacity" values=".8;.8;0" keyTimes="0;.95;1" dur="1.8s" begin=".5s" fill="freeze"/>
  </rect>
  <rect x="720" y="-10" width="510" height="3" fill="url(#scanEdge)" opacity="0">
    <animate attributeName="opacity" values="0;0;.5;.5;0" keyTimes="0;.01;.02;.95;1" dur="3.5s" begin="2.5s" repeatCount="indefinite"/>
    <animate attributeName="y" from="-10" to="700" dur="3.5s" begin="2.5s" repeatCount="indefinite"/>
  </rect>
  <rect x="720" y="-10" width="510" height="0" fill="url(#scanTrail)" opacity="0">
    <animate attributeName="opacity" values="0;0;.3;.3;0" keyTimes="0;.01;.05;.90;1" dur="3.5s" begin="2.5s" repeatCount="indefinite"/>
    <animate attributeName="y" from="-10" to="700" dur="3.5s" begin="2.5s" repeatCount="indefinite"/>
    <animate attributeName="height" values="0;80;80;0" keyTimes="0;.1;.9;1" dur="3.5s" begin="2.5s" repeatCount="indefinite"/>
  </rect>
</g>

<!-- ================= BOTTOM SOCIAL BAR ================= -->
<g class="soc" style="animation:fadeIn .4s ease 7.5s forwards">
  <g><circle cx="65" cy="714" r="10" fill="none" stroke="#ef4444" stroke-width="1"/><text x="65" y="718" text-anchor="middle" font-size="10" fill="#ef4444">&#x2709;</text></g>
  <text x="81" y="718" font-size="11" fill="#9aa4b2">shrikanttathe04@gmail.com</text>
  <g><circle cx="310" cy="714" r="10" fill="none" stroke="#a855f7" stroke-width="1"/><text x="310" y="718" text-anchor="middle" font-size="11" fill="#a855f7">&#x2B22;</text></g>
  <text x="326" y="718" font-size="11" fill="#9aa4b2">Shrikant922</text>
  <circle cx="470" cy="714" r="4" fill="#4ade80"><animate attributeName="opacity" values="1;.4;1" dur="2s" repeatCount="indefinite"/></circle>
  <text x="480" y="718" font-size="11" fill="#9aa4b2">open to collaborate</text>
  <text x="730" y="718" font-size="11" fill="#8b949e" font-style="italic">"Code is my art, Logic is my superpower." &#x2764;</text>
</g>
</svg>'''

out_path = os.path.join(OUT_DIR, "banner.svg")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg)

print("Banner updated successfully!")
