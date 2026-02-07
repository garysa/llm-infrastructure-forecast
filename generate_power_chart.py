#!/usr/bin/env python3
"""
Generate visualization of power bottleneck and China vs US AI race
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('The Power Bottleneck: AI Compute Race 2026-2033', fontsize=16, fontweight='bold')

# LEFT: Power requirements scaling
ax1 = axes[0]
categories = ['Current\nData Center', 'Next-Gen\nTraining', 'GPT-5 Class\nTraining', 'AGI-Scale\nFacility']
power_mw = [75, 750, 150, 7500]  # MW
colors = ['#4CAF50', '#FFC107', '#FF9800', '#F44336']

bars = ax1.bar(categories, power_mw, color=colors, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Power Requirement (MW)', fontsize=12)
ax1.set_title('AI Compute Power Requirements\n(Escalating Dramatically)', fontsize=12, fontweight='bold')
ax1.set_ylim(0, 9000)

# Add reference lines
ax1.axhline(y=1000, color='blue', linestyle='--', linewidth=2, alpha=0.7)
ax1.text(3.5, 1200, '1 Nuclear Reactor (~1 GW)', fontsize=9, color='blue', ha='right')

ax1.axhline(y=5000, color='purple', linestyle='--', linewidth=2, alpha=0.7)
ax1.text(3.5, 5200, 'Entire City (~5 GW)', fontsize=9, color='purple', ha='right')

# Add value labels on bars
for bar, val in zip(bars, power_mw):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 150,
             f'{val:,} MW', ha='center', va='bottom', fontsize=10, fontweight='bold')

# RIGHT: China vs US timeline
ax2 = axes[1]
years = np.array([2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033])

# Compute availability index (arbitrary units representing effective AI compute capacity)
us_compute = [100, 115, 125, 135, 145, 155, 165, 175]  # Efficiency gains but power limited
china_compute = [70, 85, 110, 145, 190, 240, 300, 370]  # Power buildout accelerates

ax2.plot(years, us_compute, 'b-o', linewidth=3, markersize=10, label='US/West (power-constrained)')
ax2.plot(years, china_compute, 'r-s', linewidth=3, markersize=10, label='China (power-expanding)')

# Mark crossover point
crossover_year = 2029
ax2.axvline(x=crossover_year, color='gray', linestyle='--', linewidth=2, alpha=0.7)
ax2.text(crossover_year + 0.1, 50, 'Compute\nParity\n(~2029)', fontsize=9, ha='left', va='bottom')

# Shaded regions
ax2.fill_between(years, us_compute, alpha=0.3, color='blue')
ax2.fill_between(years, china_compute, alpha=0.3, color='red')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Effective AI Compute Capacity (Index)', fontsize=12)
ax2.set_title('Projected AI Compute Race\n(If Power is the Bottleneck)', fontsize=12, fontweight='bold')
ax2.legend(loc='upper left', fontsize=10)
ax2.set_xlim(2025.5, 2033.5)
ax2.set_ylim(0, 400)
ax2.grid(True, alpha=0.3)

# Add annotations
ax2.annotate('China new power\nplants online', xy=(2029, 145), xytext=(2027.5, 200),
            arrowprops=dict(arrowstyle='->', color='red'), fontsize=9, color='red')
ax2.annotate('US grid\nconstraints', xy=(2028, 125), xytext=(2026.5, 160),
            arrowprops=dict(arrowstyle='->', color='blue'), fontsize=9, color='blue')

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/power_bottleneck.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Chart saved: power_bottleneck.png")

# Second figure: Comparison table as visual
fig2, ax3 = plt.subplots(figsize=(12, 6))
ax3.axis('off')

table_data = [
    ['Factor', 'China', 'US/West', 'Advantage'],
    ['Permitting Speed', 'Months', '5-10 years', 'China'],
    ['State Coordination', 'Central planning', 'Fragmented', 'China'],
    ['Grid Buildout', 'Rapid expansion', 'Aging infrastructure', 'China'],
    ['Nuclear Plans', '150+ reactors', 'Regulatory paralysis', 'China'],
    ['Chip Technology', 'Behind (sanctions)', 'Leading edge', 'US'],
    ['AI Talent', 'Growing fast', 'Still concentrated', 'US'],
    ['Private Capital', 'State-directed', 'Abundant VC/tech', 'US'],
    ['Allies', 'Limited', 'Japan/Taiwan/Korea/EU', 'US'],
]

colors_table = [['#1a237e', '#1a237e', '#1a237e', '#1a237e']]  # Header
for row in table_data[1:]:
    if row[3] == 'China':
        colors_table.append(['white', '#ffcdd2', 'white', '#ffcdd2'])
    else:
        colors_table.append(['white', 'white', '#bbdefb', '#bbdefb'])

table = ax3.table(cellText=table_data, cellLoc='center', loc='center',
                  cellColours=colors_table)
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 2)

# Style header
for j in range(4):
    table[(0, j)].set_text_props(color='white', fontweight='bold')
    table[(0, j)].set_facecolor('#1a237e')

ax3.set_title('China vs US: AI Infrastructure Comparison\n', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/china_vs_us_comparison.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Chart saved: china_vs_us_comparison.png")

print("\nBoth power analysis charts generated successfully!")
