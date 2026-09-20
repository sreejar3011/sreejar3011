import os

def create_badge(filename, title, tag, theme_colors, icon_svg):
    primary, secondary, glow, accent_light = theme_colors
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 130 130" width="130" height="130">
  <defs>
    <linearGradient id="bg-grad-{filename}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141923" />
      <stop offset="50%" stop-color="#0E131C" />
      <stop offset="100%" stop-color="#080B10" />
    </linearGradient>
    <linearGradient id="border-grad-{filename}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{primary}" />
      <stop offset="50%" stop-color="{secondary}" />
      <stop offset="100%" stop-color="{primary}" />
    </linearGradient>
    <linearGradient id="icon-grad-{filename}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{accent_light}" />
      <stop offset="100%" stop-color="{primary}" />
    </linearGradient>
    <linearGradient id="shimmer-{filename}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(255,255,255,0)" />
      <stop offset="50%" stop-color="rgba(255,255,255,0.25)" />
      <stop offset="100%" stop-color="rgba(255,255,255,0)" />
    </linearGradient>
    <filter id="glow-{filename}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <clipPath id="hex-clip-{filename}">
      <path d="M 61,12 Q 65,10 69,12 L 109,33 Q 113,35 113,40 L 113,90 Q 113,95 109,97 L 69,118 Q 65,120 61,118 L 21,97 Q 17,95 17,90 L 17,40 Q 17,35 21,33 Z" />
    </clipPath>
    <style>
      @keyframes float-icon {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-2.5px); }}
      }}
      @keyframes pulse-ring {{
        0%, 100% {{ opacity: 0.6; stroke-width: 2px; }}
        50% {{ opacity: 1; stroke-width: 2.8px; filter: drop-shadow(0 0 6px {glow}); }}
      }}
      @keyframes sweep {{
        0% {{ transform: translateX(-140px) rotate(35deg); }}
        25%, 100% {{ transform: translateX(180px) rotate(35deg); }}
      }}
      .badge-container {{
        transform-origin: center;
      }}
      .animated-ring {{
        animation: pulse-ring 3.5s ease-in-out infinite;
      }}
      .animated-icon {{
        animation: float-icon 4s ease-in-out infinite;
        transform-origin: 65px 62px;
      }}
      .shimmer-bar {{
        animation: sweep 6s ease-in-out infinite;
      }}
    </style>
  </defs>

  <!-- Ambient Glow -->
  <path d="M 61,12 Q 65,10 69,12 L 109,33 Q 113,35 113,40 L 113,90 Q 113,95 109,97 L 69,118 Q 65,120 61,118 L 21,97 Q 17,95 17,90 L 17,40 Q 17,35 21,33 Z"
        fill="{primary}" opacity="0.12" filter="blur(8px)" />

  <!-- Badge Body -->
  <g class="badge-container">
    <!-- Main Hexagon Background -->
    <path d="M 61,12 Q 65,10 69,12 L 109,33 Q 113,35 113,40 L 113,90 Q 113,95 109,97 L 69,118 Q 65,120 61,118 L 21,97 Q 17,95 17,90 L 17,40 Q 17,35 21,33 Z"
          fill="url(#bg-grad-{filename})" />
    
    <!-- Inner Subtle Pattern Grid -->
    <g opacity="0.1" stroke="#FFFFFF" stroke-width="0.5">
      <line x1="30" y1="40" x2="100" y2="40" />
      <line x1="25" y1="65" x2="105" y2="65" />
      <line x1="30" y1="90" x2="100" y2="90" />
      <line x1="65" y1="20" x2="65" y2="110" />
    </g>

    <!-- Shimmer Highlight Effect -->
    <g clip-path="url(#hex-clip-{filename})">
      <rect class="shimmer-bar" x="-60" y="-30" width="45" height="200" fill="url(#shimmer-{filename})" opacity="0.6" />
    </g>

    <!-- Outer Animated Border -->
    <path class="animated-ring"
          d="M 61,12 Q 65,10 69,12 L 109,33 Q 113,35 113,40 L 113,90 Q 113,95 109,97 L 69,118 Q 65,120 61,118 L 21,97 Q 17,95 17,90 L 17,40 Q 17,35 21,33 Z"
          fill="none" stroke="url(#border-grad-{filename})" stroke-width="2" />

    <!-- AWS Header Ribbon -->
    <path d="M 46,23 L 84,23" stroke="{primary}" stroke-width="1.5" stroke-linecap="round" opacity="0.8" />
    <text x="65" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="7.5" font-weight="900" fill="#F0F4F8" letter-spacing="1.8" text-anchor="middle">AWS</text>

    <!-- Central Floating Icon -->
    <g class="animated-icon">
      {icon_svg}
    </g>

    <!-- Lower Badge Tag Ribbon -->
    <rect x="36" y="94" width="58" height="13" rx="6.5" fill="#141B26" stroke="{primary}" stroke-width="1" opacity="0.9" />
    <text x="65" y="103.5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="6" font-weight="700" fill="{accent_light}" letter-spacing="0.8" text-anchor="middle">{tag}</text>
  </g>
</svg>'''
    
    with open(f"badges/{filename}.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated badges/{filename}.svg")


# 1. AWS Technical Accredited (Cloud Architecture / Cubes)
icon_tech = '''
      <!-- Architecture Cloud & Isometric Cube -->
      <g transform="translate(65, 59)">
        <!-- Hexagon Core / Cube -->
        <path d="M 0,-18 L 16,-9 L 16,9 L 0,18 L -16,9 L -16,-9 Z" fill="#1A2234" stroke="#FF9900" stroke-width="1.5" />
        <path d="M 0,-18 L 0,18" stroke="#FF9900" stroke-width="1.2" opacity="0.6" />
        <path d="M 0,0 L 16,-9" stroke="#FF9900" stroke-width="1.2" opacity="0.6" />
        <path d="M 0,0 L -16,-9" stroke="#FF9900" stroke-width="1.2" opacity="0.6" />
        <!-- Node Dots -->
        <circle cx="0" cy="-18" r="2" fill="#FFC72C" />
        <circle cx="16" cy="-9" r="2" fill="#FFC72C" />
        <circle cx="16" cy="9" r="2" fill="#FFC72C" />
        <circle cx="0" cy="18" r="2" fill="#FFC72C" />
        <circle cx="-16" cy="9" r="2" fill="#FFC72C" />
        <circle cx="-16" cy="-9" r="2" fill="#FFC72C" />
        <circle cx="0" cy="0" r="3" fill="#FF9900" />
      </g>
'''

# 2. AWS Cloud Economics Essentials (Finance / Growth / Metrics)
icon_econ = '''
      <!-- Cloud Economics / Financial Metrics Chart -->
      <g transform="translate(65, 59)">
        <path d="M -18,14 L -18,-12 Q -18,-14 -16,-14 L 16,-14 Q 18,-14 18,-12 L 18,14 Z" fill="#10251E" stroke="#00D084" stroke-width="1.2" opacity="0.5" />
        <!-- Ascending Bar Chart -->
        <rect x="-14" y="4" width="5" height="9" rx="1.5" fill="#00D084" opacity="0.6" />
        <rect x="-6" y="-2" width="5" height="15" rx="1.5" fill="#00D084" opacity="0.8" />
        <rect x="2" y="-8" width="5" height="21" rx="1.5" fill="#00D084" />
        <rect x="10" y="-13" width="5" height="26" rx="1.5" fill="#38EF7D" />
        <!-- Uptrend Arrow -->
        <path d="M -15,5 L -4,-1 L 4,-8 L 13,-14" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" />
        <path d="M 8,-14 L 14,-14 L 14,-8" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
      </g>
'''

# 3. AWS Generative AI Technical (Neural Spark / Intelligence Matrix)
icon_genai = '''
      <!-- Generative AI Spark & Brain Matrix -->
      <g transform="translate(65, 59)">
        <!-- 4-point Main Sparkle -->
        <path d="M 0,-19 Q 0,-2 17,0 Q 0,2 0,19 Q 0,2 -17,0 Q 0,-2 0,-19 Z" fill="url(#icon-grad-aws-generative-ai)" />
        <!-- Micro Sparkles -->
        <path d="M 12,-11 Q 12,-4 18,-3 Q 12,-2 12,5 Q 12,-2 6,-3 Q 12,-4 12,-11 Z" fill="#F472B6" />
        <path d="M -12,8 Q -12,3 -7,2 Q -12,1 -12,-4 Q -12,1 -17,2 Q -12,3 -12,8 Z" fill="#C084FC" />
        <!-- Center Light Dot -->
        <circle cx="0" cy="0" r="2.5" fill="#FFFFFF" />
      </g>
'''

# 4. AWS Agentic AI Essentials (Autonomous Multi-Agent Loop)
icon_agentic = '''
      <!-- Autonomous Agent Nodes & Feedback Loops -->
      <g transform="translate(65, 59)">
        <!-- Orbit Loop -->
        <circle cx="0" cy="0" r="16" fill="none" stroke="#06B6D4" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.7" />
        <!-- Agent Bot Hex Core -->
        <rect x="-9" y="-9" width="18" height="18" rx="5" fill="#0E2433" stroke="#22D3EE" stroke-width="1.5" />
        <!-- Bot Eyes / Sensor -->
        <circle cx="-3.5" cy="-2" r="1.8" fill="#22D3EE" />
        <circle cx="3.5" cy="-2" r="1.8" fill="#22D3EE" />
        <path d="M -3.5,3.5 Q 0,5.5 3.5,3.5" fill="none" stroke="#22D3EE" stroke-width="1.2" stroke-linecap="round" />
        <!-- Satellite Agent Nodes -->
        <circle cx="-13" cy="-10" r="3" fill="#3B82F6" stroke="#FFFFFF" stroke-width="0.8" />
        <circle cx="15" cy="-5" r="3.2" fill="#8B5CF6" stroke="#FFFFFF" stroke-width="0.8" />
        <circle cx="0" cy="16" r="2.8" fill="#06B6D4" stroke="#FFFFFF" stroke-width="0.8" />
      </g>
'''

# 5. AWS Security Essentials (Security Shield & Keylock)
icon_security = '''
      <!-- Cyber Shield & Lock -->
      <g transform="translate(65, 59)">
        <!-- Outer Shield -->
        <path d="M 0,-17 L 15,-10 Q 15,6 0,18 Q -15,6 -15,-10 Z" fill="#2A141A" stroke="#EF4444" stroke-width="1.5" />
        <!-- Inner Glow Shield -->
        <path d="M 0,-13 L 11,-8 Q 11,4 0,14 Q -11,4 -11,-8 Z" fill="#3B1219" opacity="0.6" />
        <!-- Lock Shackle -->
        <path d="M -4,-2 L -4,-6 Q -4,-10 0,-10 Q 4,-10 4,-6 L 4,-2" fill="none" stroke="#F59E0B" stroke-width="1.6" stroke-linecap="round" />
        <!-- Lock Body -->
        <rect x="-7" y="-2" width="14" height="11" rx="2.5" fill="#F59E0B" />
        <!-- Keyhole -->
        <circle cx="0" cy="2.5" r="1.5" fill="#1C1917" />
        <rect x="-0.8" y="2.5" width="1.6" height="3" fill="#1C1917" />
      </g>
'''

# 6. AWS Migration Essentials (Orbital Cloud Sync & Data Relocation)
icon_migration = '''
      <!-- Migration Arrows & Cloud Transfer -->
      <g transform="translate(65, 58)">
        <!-- Cloud outline -->
        <path d="M -12,2 Q -15,2 -16,0 Q -18,-3 -15,-6 Q -15,-11 -10,-12 Q -6,-15 0,-13 Q 5,-15 10,-11 Q 15,-10 14,-5 Q 17,-3 16,0 Q 15,2 12,2 Z"
              fill="#172554" stroke="#3B82F6" stroke-width="1.2" opacity="0.7" />
        <!-- Circular Migration Sync Arrows -->
        <path d="M -12,8 A 12 12 0 0 1 12,8" fill="none" stroke="#60A5FA" stroke-width="1.8" stroke-linecap="round" />
        <path d="M 9,5 L 13,8 L 9,11" fill="none" stroke="#60A5FA" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
        <path d="M 12,12 A 12 12 0 0 1 -12,12" fill="none" stroke="#F59E0B" stroke-width="1.8" stroke-linecap="round" />
        <path d="M -9,9 L -13,12 L -9,15" fill="none" stroke="#F59E0B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
      </g>
'''

# 7. AWS DevOps Essentials (Infinity Loop & CI/CD Pipeline)
icon_devops = '''
      <!-- DevOps Infinity Loop -->
      <g transform="translate(65, 59)">
        <!-- Infinity Path -->
        <path d="M -8,0 C -16,-11 -20,11 -8,0 C 4,-11 8,11 20,0 C 8,-11 4,11 -8,0 Z"
              fill="none" stroke="#F97316" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" />
        <!-- Secondary Pipeline Track -->
        <path d="M -8,0 C -16,-11 -20,11 -8,0 C 4,-11 8,11 20,0 C 8,-11 4,11 -8,0 Z"
              fill="none" stroke="#FDE047" stroke-width="1" stroke-dasharray="3 3" />
        <!-- Pipeline Checkpoints -->
        <circle cx="-13" cy="-4" r="2" fill="#FFFFFF" />
        <circle cx="13" cy="4" r="2" fill="#FFFFFF" />
      </g>
'''

# 8. AWS Cloud Operations Essentials (Telemetry & System Dashboard)
icon_cloudops = '''
      <!-- Cloud Operations Telemetry Gauge & Activity Pulse -->
      <g transform="translate(65, 59)">
        <!-- Gauge Outer Arch -->
        <path d="M -15,8 A 17 17 0 1 1 15,8" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" />
        <path d="M -15,8 A 17 17 0 0 1 6,-14" fill="none" stroke="#A855F7" stroke-width="2.4" stroke-linecap="round" />
        <!-- Pulse Waveform in Center -->
        <path d="M -14,2 L -7,2 L -3,-6 L 1,9 L 5,-2 L 9,3 L 14,3" fill="none" stroke="#38BDF8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
        <!-- Center Status Dot -->
        <circle cx="0" cy="12" r="2" fill="#22C55E" />
      </g>
'''

# 9. AWS Migration Foundations (Architectural Pillars & Cloud Base)
icon_foundations = '''
      <!-- Foundations Pillars & Cloud Platform -->
      <g transform="translate(65, 59)">
        <!-- Cloud Header Platform -->
        <rect x="-16" y="-15" width="32" height="6" rx="2" fill="#0284C7" />
        <!-- 3 Pillars -->
        <rect x="-14" y="-7" width="6" height="18" rx="1.5" fill="#1E293B" stroke="#38BDF8" stroke-width="1.2" />
        <rect x="-3" y="-7" width="6" height="18" rx="1.5" fill="#1E293B" stroke="#38BDF8" stroke-width="1.2" />
        <rect x="8" y="-7" width="6" height="18" rx="1.5" fill="#1E293B" stroke="#38BDF8" stroke-width="1.2" />
        <!-- Foundation Base -->
        <rect x="-18" y="12" width="36" height="4" rx="1.5" fill="#38BDF8" />
      </g>
'''

badges = [
    ("aws-technical-accredited", "AWS Technical Accredited", "PARTNER", ("#FF9900", "#FF5500", "rgba(255, 153, 0, 0.6)", "#FFD280"), icon_tech),
    ("aws-cloud-economics", "Cloud Economics Essentials", "PARTNER", ("#00D084", "#00875A", "rgba(0, 208, 132, 0.6)", "#72F1B8"), icon_econ),
    ("aws-generative-ai", "Generative AI Technical", "PARTNER", ("#A855F7", "#EC4899", "rgba(168, 85, 247, 0.6)", "#F472B6"), icon_genai),
    ("aws-agentic-ai", "Agentic AI Essentials", "PARTNER", ("#06B6D4", "#3B82F6", "rgba(6, 182, 212, 0.6)", "#67E8F9"), icon_agentic),
    ("aws-security-essentials", "Security Essentials", "PARTNER", ("#EF4444", "#F59E0B", "rgba(239, 68, 68, 0.6)", "#FCA5A5"), icon_security),
    ("aws-migration-essentials", "Migration Essentials", "PARTNER", ("#3B82F6", "#1D4ED8", "rgba(59, 130, 246, 0.6)", "#93C5FD"), icon_migration),
    ("aws-devops-essentials", "DevOps Essentials", "PARTNER", ("#F97316", "#EAB308", "rgba(249, 115, 22, 0.6)", "#FDBA74"), icon_devops),
    ("aws-cloud-operations", "Cloud Operations Essentials", "PARTNER", ("#8B5CF6", "#6366F1", "rgba(139, 92, 246, 0.6)", "#C4B5FD"), icon_cloudops),
    ("aws-migration-foundations", "AWS Migration Foundations", "KNOWLEDGE", ("#0284C7", "#0EA5E9", "rgba(2, 132, 199, 0.6)", "#7DD3FC"), icon_foundations),
]

for filename, title, tag, colors, icon in badges:
    create_badge(filename, title, tag, colors, icon)

print("All 9 animated AWS badge icons created successfully!")
