#!/usr/bin/env python3
"""
Generate visualization of fragmented AGI future landscape
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(16, 10))
fig.suptitle('The Fragmented AGI Future: From Centralized to Tiered Model', fontsize=16, fontweight='bold')

# LEFT SIDE: Current State (2024-2026)
ax1 = axes[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title('Current State (2024-2026)\nCentralized API Model', fontsize=12, fontweight='bold', pad=20)

# Central cloud providers
center_cloud = FancyBboxPatch((3, 4), 4, 2.5, boxstyle="round,pad=0.1",
                               facecolor='#4285F4', edgecolor='black', linewidth=2)
ax1.add_patch(center_cloud)
ax1.text(5, 5.25, 'Centralized AI Providers\n(OpenAI, Anthropic, Google)',
         ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# All sectors connecting to center
sectors_current = [
    (1.5, 8, 'Public/Education', '#34A853'),
    (8.5, 8, 'Enterprise', '#FBBC05'),
    (1.5, 1.5, 'Government', '#EA4335'),
    (8.5, 1.5, 'Healthcare', '#9C27B0'),
    (5, 9, 'Consumers', '#00BCD4'),
]

for x, y, label, color in sectors_current:
    circle = Circle((x, y), 0.8, facecolor=color, edgecolor='black', linewidth=1.5)
    ax1.add_patch(circle)
    ax1.text(x, y, label.split('/')[0], ha='center', va='center', fontsize=8, fontweight='bold', color='white')
    # Arrow to center
    ax1.annotate('', xy=(5, 5.25), xytext=(x, y),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

ax1.text(5, 0.3, '⚠ Data flows to single point\n⚠ Privacy/sovereignty concerns\n⚠ Vendor lock-in',
         ha='center', va='center', fontsize=9, style='italic', color='red')

# RIGHT SIDE: Future State (2028+)
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title('Future State (2028+)\nFragmented Tiered Model', fontsize=12, fontweight='bold', pad=20)

# Tier 1: Public/Open (bottom)
tier1 = FancyBboxPatch((0.5, 0.5), 9, 1.8, boxstyle="round,pad=0.05",
                        facecolor='#34A853', edgecolor='black', linewidth=2, alpha=0.8)
ax2.add_patch(tier1)
ax2.text(5, 1.4, 'TIER 1: Public/Open Models', ha='center', va='center', fontsize=11, fontweight='bold', color='white')
ax2.text(5, 0.9, 'Education • Research • General Public • Open Source (Llama, etc.)',
         ha='center', va='center', fontsize=8, color='white')

# Tier 2: Enterprise (middle-bottom)
tier2 = FancyBboxPatch((0.5, 2.6), 9, 1.8, boxstyle="round,pad=0.05",
                        facecolor='#FBBC05', edgecolor='black', linewidth=2, alpha=0.8)
ax2.add_patch(tier2)
ax2.text(5, 3.5, 'TIER 2: Corporate/Enterprise', ha='center', va='center', fontsize=11, fontweight='bold', color='black')
ax2.text(5, 3.0, 'Private fine-tuned models • On-prem inference • Proprietary data stays internal',
         ha='center', va='center', fontsize=8, color='black')

# Tier 3: Regulated Industries (middle-top)
tier3 = FancyBboxPatch((0.5, 4.7), 9, 1.8, boxstyle="round,pad=0.05",
                        facecolor='#9C27B0', edgecolor='black', linewidth=2, alpha=0.8)
ax2.add_patch(tier3)
ax2.text(5, 5.6, 'TIER 3: Regulated Industries', ha='center', va='center', fontsize=11, fontweight='bold', color='white')
ax2.text(5, 5.1, 'Healthcare • Finance • Legal • Certified & audited models • Compliance-first',
         ha='center', va='center', fontsize=8, color='white')

# Tier 4: Government/Sovereign (top)
tier4 = FancyBboxPatch((0.5, 6.8), 9, 1.8, boxstyle="round,pad=0.05",
                        facecolor='#EA4335', edgecolor='black', linewidth=2, alpha=0.8)
ax2.add_patch(tier4)
ax2.text(5, 7.7, 'TIER 4: Government/Sovereign', ha='center', va='center', fontsize=11, fontweight='bold', color='white')
ax2.text(5, 7.2, 'National security • Air-gapped • Country-specific models • Defense/Intelligence',
         ha='center', va='center', fontsize=8, color='white')

# Arrows showing isolation
ax2.annotate('', xy=(9.7, 1.4), xytext=(9.7, 7.7),
            arrowprops=dict(arrowstyle='<->', color='black', lw=2))
ax2.text(10.3, 4.5, 'Increasing\nData\nSensitivity\n&\nIsolation', ha='left', va='center', fontsize=8, fontweight='bold')

# Key characteristics
ax2.text(5, 9.2, '✓ Data stays in tier\n✓ Regulatory compliance\n✓ Reduced attack surface',
         ha='center', va='center', fontsize=9, style='italic', color='green')

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/agi_future_tiers.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Chart saved: agi_future_tiers.png")

# Also create a market share projection chart
fig2, ax3 = plt.subplots(figsize=(12, 7))

years = ['2024', '2026', '2028', '2030', '2032']
x = np.arange(len(years))

# Projected market share by tier
centralized_api = [85, 60, 35, 20, 10]
public_open = [5, 15, 20, 25, 30]
enterprise_private = [8, 18, 28, 32, 35]
sovereign_govt = [2, 7, 17, 23, 25]

width = 0.6
ax3.bar(x, centralized_api, width, label='Centralized API (current model)', color='#4285F4')
ax3.bar(x, public_open, width, bottom=centralized_api, label='Public/Open Models', color='#34A853')
ax3.bar(x, enterprise_private, width, bottom=np.array(centralized_api)+np.array(public_open),
        label='Enterprise Private', color='#FBBC05')
ax3.bar(x, sovereign_govt, width, bottom=np.array(centralized_api)+np.array(public_open)+np.array(enterprise_private),
        label='Sovereign/Government', color='#EA4335')

ax3.set_ylabel('Market Share (%)', fontsize=12)
ax3.set_xlabel('Year', fontsize=12)
ax3.set_title('Projected AI Compute Market Fragmentation\nFrom Centralized APIs to Tiered Deployment', fontsize=14, fontweight='bold')
ax3.set_xticks(x)
ax3.set_xticklabels(years)
ax3.legend(loc='upper right')
ax3.set_ylim(0, 105)

# Add annotation
ax3.annotate('Centralized model\ndeclines as data\nsovereignty concerns\ngrow',
             xy=(3, 20), xytext=(3.5, 50),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=9, ha='left')

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/agi_market_projection.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Chart saved: agi_market_projection.png")

print("\nBoth charts generated successfully!")
