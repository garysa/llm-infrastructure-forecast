#!/usr/bin/env python3
"""
Generate 4 pie charts showing AI sector distribution over 4 years
Sectors: Public, Government, Corporate
Deployment: Cloud vs Local/On-prem
"""
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(16, 14))
fig.suptitle('AI Deployment Evolution by Sector: Cloud vs Local (2026-2029)',
             fontsize=16, fontweight='bold', y=1.02)

# Color scheme
colors_cloud = ['#4285F4', '#5C9EFF', '#89B8FF']  # Blues for cloud
colors_local = ['#EA4335', '#FF7B6B', '#FFAB9E']  # Reds for local
colors_hybrid = ['#FBBC05', '#FFD54F', '#FFE88A']  # Yellows for hybrid

def make_pie(ax, year, data, title):
    """
    data format: [(label, cloud%, local%, size%), ...]
    """
    # Create nested pie chart
    # Outer ring: sectors
    # Inner ring: cloud vs local within each sector

    sectors = [d[0] for d in data]
    sizes = [d[3] for d in data]
    cloud_pcts = [d[1] for d in data]
    local_pcts = [d[2] for d in data]

    # Outer pie - sectors
    outer_colors = ['#34A853', '#4285F4', '#FBBC05']  # Public=Green, Govt=Blue, Corp=Yellow
    wedges1, texts1 = ax.pie(sizes, labels=None, colors=outer_colors,
                              radius=1.0, wedgeprops=dict(width=0.3, edgecolor='white'),
                              startangle=90)

    # Inner pie - cloud vs local breakdown
    inner_sizes = []
    inner_colors = []
    inner_labels = []

    for i, (sector, cloud, local, size) in enumerate(data):
        # Cloud portion
        inner_sizes.append(size * cloud / 100)
        inner_colors.append('#89CFF0')  # Light blue for cloud
        inner_labels.append(f'{sector}\nCloud')

        # Local portion
        inner_sizes.append(size * local / 100)
        inner_colors.append('#FF6B6B')  # Light red for local
        inner_labels.append(f'{sector}\nLocal')

    wedges2, texts2 = ax.pie(inner_sizes, labels=None, colors=inner_colors,
                              radius=0.7, wedgeprops=dict(width=0.35, edgecolor='white'),
                              startangle=90)

    # Add center text
    ax.text(0, 0, f'{year}', ha='center', va='center', fontsize=24, fontweight='bold')

    # Create legend
    ax.set_title(title, fontsize=12, fontweight='bold', pad=20)

    return data

# Year 2026 - Current state (cloud dominant)
ax1 = axes[0, 0]
data_2026 = [
    ('Public', 75, 25, 25),      # Public: 75% cloud, 25% local, 25% of market
    ('Government', 40, 60, 20),  # Govt: 40% cloud, 60% local, 20% of market
    ('Corporate', 65, 35, 55),   # Corp: 65% cloud, 35% local, 55% of market
]

# Donut chart approach
sectors_2026 = ['Public\n(Cloud)', 'Public\n(Local)',
                'Govt\n(Cloud)', 'Govt\n(Local)',
                'Corp\n(Cloud)', 'Corp\n(Local)']
sizes_2026 = [25*0.75, 25*0.25, 20*0.40, 20*0.60, 55*0.65, 55*0.35]
colors_2026 = ['#81C784', '#2E7D32', '#64B5F6', '#1565C0', '#FFD54F', '#F9A825']
explode_2026 = (0.02, 0.02, 0.02, 0.02, 0.02, 0.02)

wedges, texts, autotexts = ax1.pie(sizes_2026, labels=sectors_2026, autopct='%1.0f%%',
                                    colors=colors_2026, explode=explode_2026,
                                    pctdistance=0.75, labeldistance=1.15,
                                    wedgeprops=dict(edgecolor='white', linewidth=2),
                                    textprops={'fontsize': 9})
ax1.set_title('2026 (Current)\nCloud Still Dominant', fontsize=14, fontweight='bold')

# Year 2027 - Transition begins
ax2 = axes[0, 1]
sizes_2027 = [25*0.60, 25*0.40, 20*0.30, 20*0.70, 55*0.50, 55*0.50]
wedges, texts, autotexts = ax2.pie(sizes_2027, labels=sectors_2026, autopct='%1.0f%%',
                                    colors=colors_2026, explode=explode_2026,
                                    pctdistance=0.75, labeldistance=1.15,
                                    wedgeprops=dict(edgecolor='white', linewidth=2),
                                    textprops={'fontsize': 9})
ax2.set_title('2027\nLocal Adoption Accelerates', fontsize=14, fontweight='bold')

# Year 2028 - Major shift
ax3 = axes[1, 0]
sizes_2028 = [25*0.45, 25*0.55, 20*0.15, 20*0.85, 55*0.35, 55*0.65]
wedges, texts, autotexts = ax3.pie(sizes_2028, labels=sectors_2026, autopct='%1.0f%%',
                                    colors=colors_2026, explode=explode_2026,
                                    pctdistance=0.75, labeldistance=1.15,
                                    wedgeprops=dict(edgecolor='white', linewidth=2),
                                    textprops={'fontsize': 9})
ax3.set_title('2028\nLocal Becomes Majority', fontsize=14, fontweight='bold')

# Year 2029 - New equilibrium
ax4 = axes[1, 1]
sizes_2029 = [25*0.35, 25*0.65, 20*0.10, 20*0.90, 55*0.25, 55*0.75]
wedges, texts, autotexts = ax4.pie(sizes_2029, labels=sectors_2026, autopct='%1.0f%%',
                                    colors=colors_2026, explode=explode_2026,
                                    pctdistance=0.75, labeldistance=1.15,
                                    wedgeprops=dict(edgecolor='white', linewidth=2),
                                    textprops={'fontsize': 9})
ax4.set_title('2029\nLocal Dominant Across Sectors', fontsize=14, fontweight='bold')

# Add legend
fig.legend(['Public - Cloud', 'Public - Local',
            'Government - Cloud', 'Government - Local',
            'Corporate - Cloud', 'Corporate - Local'],
           loc='lower center', ncol=3, fontsize=10,
           bbox_to_anchor=(0.5, -0.02))

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/sector_evolution.png', dpi=150,
            bbox_inches='tight', facecolor='white', edgecolor='none')
print("Chart saved: sector_evolution.png")


# ============================================
# Second figure: Summary bar chart
# ============================================
fig2, ax = plt.subplots(figsize=(14, 8))

years = ['2026', '2027', '2028', '2029']
x = np.arange(len(years))
width = 0.12

# Data: Cloud percentages by sector by year
public_cloud = [75, 60, 45, 35]
public_local = [25, 40, 55, 65]
govt_cloud = [40, 30, 15, 10]
govt_local = [60, 70, 85, 90]
corp_cloud = [65, 50, 35, 25]
corp_local = [35, 50, 65, 75]

# Plot grouped bars
bars1 = ax.bar(x - 2.5*width, public_cloud, width, label='Public - Cloud', color='#81C784')
bars2 = ax.bar(x - 1.5*width, public_local, width, label='Public - Local', color='#2E7D32')
bars3 = ax.bar(x - 0.5*width, govt_cloud, width, label='Govt - Cloud', color='#64B5F6')
bars4 = ax.bar(x + 0.5*width, govt_local, width, label='Govt - Local', color='#1565C0')
bars5 = ax.bar(x + 1.5*width, corp_cloud, width, label='Corp - Cloud', color='#FFD54F')
bars6 = ax.bar(x + 2.5*width, corp_local, width, label='Corp - Local', color='#F9A825')

ax.set_ylabel('Percentage of Sector (%)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_title('Cloud vs Local Deployment by Sector (2026-2029)\nData Sovereignty Drives Localization',
             fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(loc='upper right', fontsize=9)
ax.set_ylim(0, 100)
ax.grid(True, axis='y', alpha=0.3)

# Add trend arrows
ax.annotate('', xy=(3, 35), xytext=(0, 75),
            arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=3))
ax.text(1.5, 60, 'Public\nLocalizing', fontsize=10, color='#2E7D32', fontweight='bold')

ax.annotate('', xy=(3, 90), xytext=(0, 60),
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=3))
ax.text(1.5, 80, 'Govt\n→ 90% Local', fontsize=10, color='#1565C0', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/sector_bars.png', dpi=150,
            bbox_inches='tight', facecolor='white', edgecolor='none')
print("Chart saved: sector_bars.png")


# ============================================
# Third figure: Country-level breakdown
# ============================================
fig3, axes3 = plt.subplots(1, 3, figsize=(16, 6))
fig3.suptitle('AI Localization by Country Type (2029 Projection)', fontsize=14, fontweight='bold')

# Developed democracies (US, EU, Japan, Australia)
ax_dev = axes3[0]
labels_dev = ['Cloud APIs\n(US providers)', 'Local/On-prem\n(domestic)', 'Hybrid\n(split)']
sizes_dev = [25, 55, 20]
colors_dev = ['#4285F4', '#EA4335', '#FBBC05']
ax_dev.pie(sizes_dev, labels=labels_dev, autopct='%1.0f%%', colors=colors_dev,
           wedgeprops=dict(edgecolor='white', linewidth=2), textprops={'fontsize': 10})
ax_dev.set_title('Developed Democracies\n(US, EU, Japan, AU)', fontsize=12, fontweight='bold')

# Authoritarian states (China, Russia, Iran)
ax_auth = axes3[1]
labels_auth = ['Cloud APIs\n(foreign)', 'Local/On-prem\n(domestic)', 'State-controlled\ncloud']
sizes_auth = [5, 70, 25]
colors_auth = ['#4285F4', '#EA4335', '#9C27B0']
ax_auth.pie(sizes_auth, labels=labels_auth, autopct='%1.0f%%', colors=colors_auth,
            wedgeprops=dict(edgecolor='white', linewidth=2), textprops={'fontsize': 10})
ax_auth.set_title('Authoritarian States\n(China, Russia, Iran)', fontsize=12, fontweight='bold')

# Developing nations (India, Brazil, Africa)
ax_dev_nations = axes3[2]
labels_dev_nations = ['Cloud APIs\n(US/China)', 'Local/On-prem', 'Mobile-first\ncloud']
sizes_dev_nations = [45, 20, 35]
colors_dev_nations = ['#4285F4', '#EA4335', '#34A853']
ax_dev_nations.pie(sizes_dev_nations, labels=labels_dev_nations, autopct='%1.0f%%',
                   colors=colors_dev_nations,
                   wedgeprops=dict(edgecolor='white', linewidth=2), textprops={'fontsize': 10})
ax_dev_nations.set_title('Developing Nations\n(India, Brazil, Africa)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/country_breakdown.png', dpi=150,
            bbox_inches='tight', facecolor='white', edgecolor='none')
print("Chart saved: country_breakdown.png")

print("\nAll sector pie charts generated successfully!")
