#!/usr/bin/env python3
"""
Generate summary visualization for AI 5-year forecast and AGI probability
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# ============================================
# Figure 1: 5-Year AI Trajectory Summary
# ============================================
fig1, ax1 = plt.subplots(figsize=(16, 10))

# Timeline from 2026 to 2031
years = [2026, 2027, 2028, 2029, 2030, 2031]
y_positions = {'capability': 8, 'deployment': 6, 'market': 4, 'agi': 2}

ax1.set_xlim(2025.5, 2031.5)
ax1.set_ylim(0, 10)
ax1.axis('off')

# Title
ax1.text(2028.5, 9.5, 'AI 5-Year Forecast: 2026-2031', fontsize=20, fontweight='bold',
         ha='center', va='center')

# Capability trajectory
ax1.axhline(y=8, color='lightgray', linestyle='-', linewidth=40, alpha=0.3)
ax1.text(2025.7, 8, 'Capability', fontsize=12, fontweight='bold', va='center')

capability_events = [
    (2026, 'Current:\nGPT-4 class', '#4CAF50'),
    (2027, 'Incremental\ngains only', '#8BC34A'),
    (2028, 'Scaling\nwall hit', '#FFC107'),
    (2029, 'Efficiency\nfocus', '#FF9800'),
    (2030, 'New paradigm?\nUncertain', '#FF5722'),
    (2031, 'Plateau or\nbreakthrough', '#9E9E9E'),
]
for year, text, color in capability_events:
    ax1.add_patch(FancyBboxPatch((year-0.35, 7.5), 0.7, 1, boxstyle="round,pad=0.05",
                                  facecolor=color, edgecolor='black', linewidth=1))
    ax1.text(year, 8, text, fontsize=8, ha='center', va='center', fontweight='bold')

# Deployment trajectory
ax1.axhline(y=6, color='lightgray', linestyle='-', linewidth=40, alpha=0.3)
ax1.text(2025.7, 6, 'Deployment', fontsize=12, fontweight='bold', va='center')

deployment_events = [
    (2026, 'Cloud\ndominant', '#2196F3'),
    (2027, 'Local\nrising', '#42A5F5'),
    (2028, 'Hybrid\nstandard', '#7E57C2'),
    (2029, 'Local\nmajority', '#AB47BC'),
    (2030, 'Fragmented\necosystem', '#E91E63'),
    (2031, 'Regional\nAI blocs', '#C2185B'),
]
for year, text, color in deployment_events:
    ax1.add_patch(FancyBboxPatch((year-0.35, 5.5), 0.7, 1, boxstyle="round,pad=0.05",
                                  facecolor=color, edgecolor='black', linewidth=1))
    ax1.text(year, 6, text, fontsize=8, ha='center', va='center', fontweight='bold', color='white')

# Market structure
ax1.axhline(y=4, color='lightgray', linestyle='-', linewidth=40, alpha=0.3)
ax1.text(2025.7, 4, 'Market', fontsize=12, fontweight='bold', va='center')

market_events = [
    (2026, 'Big Tech\nAPIs', '#FDD835'),
    (2027, 'Open source\nrises', '#FFEB3B'),
    (2028, 'Enterprise\non-prem', '#FFC107'),
    (2029, 'Govt\nsovereign AI', '#FF9800'),
    (2030, 'Tiered\nmodel', '#FF5722'),
    (2031, 'Decentralized\necosystem', '#E64A19'),
]
for year, text, color in market_events:
    ax1.add_patch(FancyBboxPatch((year-0.35, 3.5), 0.7, 1, boxstyle="round,pad=0.05",
                                  facecolor=color, edgecolor='black', linewidth=1))
    ax1.text(year, 4, text, fontsize=8, ha='center', va='center', fontweight='bold')

# AGI probability
ax1.axhline(y=2, color='lightgray', linestyle='-', linewidth=40, alpha=0.3)
ax1.text(2025.7, 2, 'AGI?', fontsize=12, fontweight='bold', va='center')

agi_events = [
    (2026, 'No\n(0%)', '#4CAF50'),
    (2027, 'No\n(2%)', '#8BC34A'),
    (2028, 'Unlikely\n(5%)', '#CDDC39'),
    (2029, 'Unlikely\n(8%)', '#FFEB3B'),
    (2030, 'Unlikely\n(12%)', '#FFC107'),
    (2031, 'Unlikely\n(15%)', '#FF9800'),
]
for year, text, color in agi_events:
    ax1.add_patch(FancyBboxPatch((year-0.35, 1.5), 0.7, 1, boxstyle="round,pad=0.05",
                                  facecolor=color, edgecolor='black', linewidth=1))
    ax1.text(year, 2, text, fontsize=8, ha='center', va='center', fontweight='bold')

# Year labels
for year in years:
    ax1.text(year, 0.8, str(year), fontsize=14, ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/five_year_forecast.png', dpi=150,
            bbox_inches='tight', facecolor='white', edgecolor='none')
print("Chart saved: five_year_forecast.png")


# ============================================
# Figure 2: AGI Probability Analysis
# ============================================
fig2, axes = plt.subplots(1, 2, figsize=(16, 8))

# Left: AGI probability by scenario
ax2 = axes[0]
scenarios = ['Optimistic\n(scaling works)', 'Moderate\n(gradual progress)',
             'Pessimistic\n(data wall)', 'Plateau\n(stagnation)']
probabilities = [35, 15, 5, 2]
colors = ['#4CAF50', '#2196F3', '#FF9800', '#F44336']

bars = ax2.barh(scenarios, probabilities, color=colors, edgecolor='black', linewidth=2)
ax2.set_xlabel('Probability of AGI by 2031 (%)', fontsize=12)
ax2.set_title('AGI Probability by Scenario', fontsize=14, fontweight='bold')
ax2.set_xlim(0, 50)

for bar, prob in zip(bars, probabilities):
    ax2.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
             f'{prob}%', va='center', fontsize=12, fontweight='bold')

# Weighted average
ax2.axvline(x=12, color='purple', linestyle='--', linewidth=2)
ax2.text(13, 1.5, 'Weighted avg:\n~12%', fontsize=10, color='purple', fontweight='bold')

# Right: Bottlenecks preventing AGI
ax3 = axes[1]
bottlenecks = ['Training Data\nExhaustion', 'Algorithmic\nCeiling',
               'Power/Energy\nConstraints', 'Economic\nViability', 'Unknown\nUnknowns']
severity = [90, 75, 60, 50, 80]
colors2 = ['#D32F2F', '#E64A19', '#F57C00', '#FBC02D', '#7B1FA2']

bars2 = ax3.barh(bottlenecks, severity, color=colors2, edgecolor='black', linewidth=2)
ax3.set_xlabel('Severity as AGI Blocker (0-100)', fontsize=12)
ax3.set_title('Key Bottlenecks Preventing AGI', fontsize=14, fontweight='bold')
ax3.set_xlim(0, 100)

for bar, sev in zip(bars2, severity):
    ax3.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
             f'{sev}', va='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/agi_probability.png', dpi=150,
            bbox_inches='tight', facecolor='white', edgecolor='none')
print("Chart saved: agi_probability.png")


# ============================================
# Figure 3: Summary Dashboard
# ============================================
fig3, ax4 = plt.subplots(figsize=(16, 12))
ax4.axis('off')

# Title
ax4.text(0.5, 0.95, 'LLM Infrastructure Forecast: Executive Summary',
         fontsize=22, fontweight='bold', ha='center', transform=ax4.transAxes)

# Key findings boxes
findings = [
    ('1. Scaling Era Ending',
     '• Training data exhausted (GPT-4 used 87% of high-quality internet)\n'
     '• Synthetic data causes model collapse\n'
     '• Algorithmic breakthroughs required for further progress',
     '#FFCDD2', 0.02, 0.75),

    ('2. Deployment Fragmenting',
     '• Cloud → Local shift accelerating (65% → 25% by 2029)\n'
     '• Government leading localization (90% local by 2029)\n'
     '• Open source enabling enterprise on-prem',
     '#C8E6C9', 0.35, 0.75),

    ('3. Geopolitical Split',
     '• China vs West: Bifurcated AI ecosystems\n'
     '• Power infrastructure becomes strategic\n'
     '• Neither side achieves AGI monopoly',
     '#BBDEFB', 0.68, 0.75),

    ('4. Hardware Evolution',
     '• ASICs dominate inference (like Bitcoin)\n'
     '• GPUs remain essential for training\n'
     '• Edge devices drive specialized chips',
     '#FFF9C4', 0.02, 0.45),

    ('5. Market Structure',
     '• Tiered model: Public/Enterprise/Govt/Sovereign\n'
     '• No single AGI monopoly possible\n'
     '• Open source catches up to proprietary',
     '#E1BEE7', 0.35, 0.45),

    ('6. AGI Timeline',
     '• By 2031: ~12% probability (weighted average)\n'
     '• Most likely: Continued incremental gains\n'
     '• Data wall is primary blocker, not compute',
     '#FFCCBC', 0.68, 0.45),
]

for title, text, color, x, y in findings:
    rect = FancyBboxPatch((x, y), 0.30, 0.22, transform=ax4.transAxes,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=2)
    ax4.add_patch(rect)
    ax4.text(x + 0.15, y + 0.19, title, fontsize=11, fontweight='bold',
             ha='center', transform=ax4.transAxes)
    ax4.text(x + 0.01, y + 0.15, text, fontsize=9, va='top',
             transform=ax4.transAxes, family='monospace')

# Bottom conclusion
conclusion_box = FancyBboxPatch((0.02, 0.02), 0.96, 0.18, transform=ax4.transAxes,
                                 boxstyle="round,pad=0.02", facecolor='#E8EAF6',
                                 edgecolor='#3F51B5', linewidth=3)
ax4.add_patch(conclusion_box)
ax4.text(0.5, 0.16, 'CONCLUSION: AI in 5 Years', fontsize=14, fontweight='bold',
         ha='center', transform=ax4.transAxes, color='#3F51B5')
ax4.text(0.5, 0.10,
         '• AGI by 2031 is UNLIKELY (~12% probability) — data exhaustion and algorithmic limits are binding constraints\n'
         '• AI will be MORE CAPABLE but incrementally — no transformative leap expected\n'
         '• AI will be MORE FRAGMENTED — regional, sectoral, and organizational silos\n'
         '• The current centralized API model will DECLINE — replaced by distributed, local deployments\n'
         '• Biggest winners: Hardware makers (sell to all sides), Open source (levels playing field)',
         fontsize=10, ha='center', va='top', transform=ax4.transAxes, family='monospace')

plt.savefig('/home/grs/Projects/adhoc/llm_forecast/executive_summary.png', dpi=150,
            bbox_inches='tight', facecolor='white', edgecolor='none')
print("Chart saved: executive_summary.png")

print("\nAll conclusion charts generated successfully!")
