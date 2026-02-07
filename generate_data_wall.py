#!/usr/bin/env python3
"""
Visualize the data exhaustion problem facing LLM scaling
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig = plt.figure(figsize=(16, 12))

# ============================================
# PLOT 1: Data availability vs Model requirements
# ============================================
ax1 = fig.add_subplot(2, 2, 1)

models = ['GPT-2\n(2019)', 'GPT-3\n(2020)', 'GPT-4\n(2023)', 'GPT-5?\n(2025)', 'GPT-6?\n(2027)', 'AGI?\n(2030)']
tokens_required = [10, 300, 13000, 50000, 200000, 1000000]  # Billions of tokens
x_pos = np.arange(len(models))

# Available data
total_internet_text = 15000  # ~15 trillion tokens
annual_new_content = 1500    # ~1.5 trillion/year

bars = ax1.bar(x_pos, tokens_required, color=['green', 'green', 'green', 'orange', 'red', 'darkred'],
               edgecolor='black', linewidth=1.5)

# Horizontal line for available data
ax1.axhline(y=total_internet_text, color='blue', linestyle='--', linewidth=3, label='Total Internet Text (~15T tokens)')
ax1.axhline(y=total_internet_text + 5*annual_new_content, color='lightblue', linestyle=':', linewidth=2,
            label='+ 5 years new content')

ax1.set_xticks(x_pos)
ax1.set_xticklabels(models)
ax1.set_ylabel('Training Tokens Required (Billions)', fontsize=11)
ax1.set_title('The Data Wall: Model Requirements vs Available Data', fontsize=12, fontweight='bold')
ax1.set_yscale('log')
ax1.set_ylim(1, 2000000)
ax1.legend(loc='upper left', fontsize=9)

# Annotations
ax1.annotate('DATA\nEXHAUSTED', xy=(3, 50000), xytext=(3.5, 150000),
            fontsize=12, fontweight='bold', color='red', ha='center')

# ============================================
# PLOT 2: Data sources breakdown
# ============================================
ax2 = fig.add_subplot(2, 2, 2)

sources = ['Common Crawl\n(web)', 'Books\n(scanned)', 'Wikipedia', 'Code\n(GitHub)', 'Scientific\nPapers',
           'Reddit/Forums', 'News\nArchives', 'Other']
tokens = [10000, 2000, 100, 1000, 500, 800, 400, 200]  # Billions
used_pct = [95, 80, 100, 90, 70, 85, 60, 50]  # Percent already used

colors = plt.cm.RdYlGn([1 - u/100 for u in used_pct])

bars = ax2.barh(sources, tokens, color=colors, edgecolor='black', linewidth=1)

# Add percentage labels
for bar, pct in zip(bars, used_pct):
    width = bar.get_width()
    ax2.text(width + 100, bar.get_y() + bar.get_height()/2,
             f'{pct}% used', va='center', fontsize=9, fontweight='bold',
             color='red' if pct > 80 else 'orange' if pct > 60 else 'green')

ax2.set_xlabel('Available Tokens (Billions)', fontsize=11)
ax2.set_title('Training Data Sources: Already Exhausted', fontsize=12, fontweight='bold')
ax2.set_xlim(0, 12000)

# ============================================
# PLOT 3: Synthetic data problem
# ============================================
ax3 = fig.add_subplot(2, 2, 3)

generations = np.arange(0, 11)

# Model quality when training on synthetic data
quality_no_synthetic = np.ones(11) * 100  # Baseline stays flat
quality_10pct_synthetic = 100 * (0.98 ** generations)  # 10% synthetic per generation
quality_50pct_synthetic = 100 * (0.92 ** generations)  # 50% synthetic
quality_90pct_synthetic = 100 * (0.80 ** generations)  # 90% synthetic

ax3.plot(generations, quality_no_synthetic, 'g-', linewidth=3, marker='o', label='0% synthetic (baseline)')
ax3.plot(generations, quality_10pct_synthetic, 'b-', linewidth=3, marker='s', label='10% synthetic/generation')
ax3.plot(generations, quality_50pct_synthetic, 'orange', linewidth=3, marker='^', label='50% synthetic/generation')
ax3.plot(generations, quality_90pct_synthetic, 'r-', linewidth=3, marker='x', label='90% synthetic/generation')

ax3.axhline(y=50, color='red', linestyle='--', linewidth=2, alpha=0.5)
ax3.text(10.2, 50, 'Unusable\nthreshold', fontsize=9, color='red', va='center')

ax3.set_xlabel('Training Generations', fontsize=11)
ax3.set_ylabel('Model Quality (%)', fontsize=11)
ax3.set_title('Model Collapse: Synthetic Data Degrades Quality', fontsize=12, fontweight='bold')
ax3.legend(loc='lower left', fontsize=9)
ax3.set_xlim(0, 10.5)
ax3.set_ylim(0, 110)
ax3.grid(True, alpha=0.3)

# ============================================
# PLOT 4: Alternative strategies comparison
# ============================================
ax4 = fig.add_subplot(2, 2, 4)

strategies = ['More\nCompute', 'Synthetic\nData', 'Licensed\nData', 'Multimodal', 'RLHF\nQuality',
              'Algorithmic\nBreakthrough']
effectiveness = [30, 25, 40, 50, 60, 95]
feasibility = [70, 60, 50, 65, 80, 20]
risk = [20, 80, 40, 30, 25, 10]

x = np.arange(len(strategies))
width = 0.25

bars1 = ax4.bar(x - width, effectiveness, width, label='Effectiveness', color='green', alpha=0.8)
bars2 = ax4.bar(x, feasibility, width, label='Feasibility', color='blue', alpha=0.8)
bars3 = ax4.bar(x + width, risk, width, label='Risk', color='red', alpha=0.8)

ax4.set_xticks(x)
ax4.set_xticklabels(strategies, fontsize=9)
ax4.set_ylabel('Score (0-100)', fontsize=11)
ax4.set_title('Post-Data-Wall Strategies: Effectiveness vs Feasibility vs Risk', fontsize=12, fontweight='bold')
ax4.legend(loc='upper right', fontsize=9)
ax4.set_ylim(0, 110)

# Highlight best option
ax4.annotate('Best path\nif achievable', xy=(5, 95), xytext=(4, 105),
            arrowprops=dict(arrowstyle='->', color='green'), fontsize=9, color='green')

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/data_wall.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Chart saved: data_wall.png")

# ============================================
# Second Figure: Timeline of data exhaustion
# ============================================
fig2, ax5 = plt.subplots(figsize=(14, 7))

years = np.arange(2018, 2036)

# Cumulative data used by AI training
data_consumed = [0.1, 0.5, 2, 4, 6, 9, 13, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5]

# Total available data (grows slowly)
total_available = [12 + (y - 2018) * 1.5 for y in years]

# High quality data (subset)
high_quality = [8 + (y - 2018) * 0.3 for y in years]

ax5.fill_between(years, 0, total_available, alpha=0.3, color='blue', label='Total Internet Text')
ax5.fill_between(years, 0, high_quality, alpha=0.3, color='green', label='High-Quality Subset')
ax5.plot(years, data_consumed, 'r-', linewidth=4, marker='o', markersize=8, label='Cumulative AI Training Consumption')

# Mark key events
events = [
    (2020, 2, 'GPT-3'),
    (2023, 13, 'GPT-4'),
    (2025, 15.5, 'Data wall hit'),
]
for year, val, label in events:
    ax5.annotate(label, xy=(year, val), xytext=(year-0.5, val+3),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=10, fontweight='bold')

# Crossover point
ax5.axvline(x=2025, color='red', linestyle='--', linewidth=2, alpha=0.7)
ax5.text(2025.2, 5, 'HIGH-QUALITY\nDATA EXHAUSTED', fontsize=11, color='red', fontweight='bold')

ax5.set_xlabel('Year', fontsize=12)
ax5.set_ylabel('Tokens (Trillions)', fontsize=12)
ax5.set_title('The Data Exhaustion Timeline: When Does Training Data Run Out?', fontsize=14, fontweight='bold')
ax5.legend(loc='upper left', fontsize=10)
ax5.set_xlim(2018, 2035)
ax5.set_ylim(0, 35)
ax5.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/data_timeline.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Chart saved: data_timeline.png")

print("\nAll data wall charts generated successfully!")
