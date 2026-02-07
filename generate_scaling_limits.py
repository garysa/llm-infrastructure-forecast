#!/usr/bin/env python3
"""
Model AGI scaling limits compared to Moore's Law
Extrapolate scenarios where scaling breaks down
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

fig = plt.figure(figsize=(16, 12))

# Create grid for subplots
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 1, 2)

# ============================================
# PLOT 1: Moore's Law Historical + Slowdown
# ============================================
years_moore = np.arange(1970, 2036)

# Ideal Moore's Law (doubling every 2 years)
transistors_ideal = 2000 * (2 ** ((years_moore - 1970) / 2))

# Actual trajectory (slowed after 2010)
transistors_actual = []
for y in years_moore:
    if y <= 2010:
        # Classic Moore's Law
        val = 2000 * (2 ** ((y - 1970) / 2))
    else:
        # Slowdown: doubling every 3 years instead of 2
        base_2010 = 2000 * (2 ** ((2010 - 1970) / 2))
        val = base_2010 * (2 ** ((y - 2010) / 3))
    transistors_actual.append(val)

ax1.semilogy(years_moore, transistors_ideal, 'b--', linewidth=2, label="Ideal Moore's Law (2x/2yr)", alpha=0.6)
ax1.semilogy(years_moore, transistors_actual, 'b-', linewidth=3, label="Actual (slowed post-2010)")
ax1.axvline(x=2010, color='red', linestyle=':', linewidth=2, alpha=0.7)
ax1.text(2011, 1e6, "Dennard\nScaling\nEnds", fontsize=9, color='red')
ax1.axvline(x=2025, color='orange', linestyle=':', linewidth=2, alpha=0.7)
ax1.text(2026, 1e4, "Physical\nLimits", fontsize=9, color='orange')

ax1.set_xlabel('Year', fontsize=11)
ax1.set_ylabel('Transistors per Chip', fontsize=11)
ax1.set_title("Moore's Law: The Template for Scaling Breakdown", fontsize=12, fontweight='bold')
ax1.legend(loc='lower right', fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(1970, 2035)

# ============================================
# PLOT 2: AI Scaling Laws - Historical
# ============================================
# Model capability index (arbitrary, representing benchmark performance)
years_ai = np.arange(2017, 2027)
models = {
    2017: ('Transformer', 10),
    2018: ('BERT', 15),
    2019: ('GPT-2', 25),
    2020: ('GPT-3', 55),
    2021: ('Codex', 70),
    2022: ('ChatGPT', 85),
    2023: ('GPT-4', 100),
    2024: ('Claude 3', 110),
    2025: ('GPT-4.5+', 118),
    2026: ('Current', 124),
}

years_plot = list(models.keys())
capabilities = [models[y][1] for y in years_plot]
names = [models[y][0] for y in years_plot]

ax2.plot(years_plot, capabilities, 'g-o', linewidth=3, markersize=10)
for i, (y, cap, name) in enumerate(zip(years_plot, capabilities, names)):
    offset = 5 if i % 2 == 0 else -10
    ax2.annotate(name, (y, cap), textcoords="offset points", xytext=(0, offset),
                ha='center', fontsize=8)

# Show diminishing returns
ax2.annotate('Diminishing\nreturns?', xy=(2025, 118), xytext=(2023.5, 130),
            arrowprops=dict(arrowstyle='->', color='red'), fontsize=10, color='red')

ax2.set_xlabel('Year', fontsize=11)
ax2.set_ylabel('Model Capability Index', fontsize=11)
ax2.set_title('AI Scaling: Historical Progress (2017-2026)', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(2016, 2027)
ax2.set_ylim(0, 150)

# ============================================
# PLOT 3: Future Scenarios (2026-2036)
# ============================================
years_future = np.arange(2026, 2037)
base_capability = 124  # 2026 starting point

# Scenario 1: Optimistic - Scaling continues (unlikely)
scenario_optimistic = base_capability * (1.25 ** (years_future - 2026))

# Scenario 2: Moderate - Slowdown like Moore's Law
scenario_moderate = []
for y in years_future:
    # Growth rate declines from 25% to 8% over decade
    years_elapsed = y - 2026
    growth_rate = 0.25 - (0.017 * years_elapsed)  # Linear decay
    if years_elapsed == 0:
        scenario_moderate.append(base_capability)
    else:
        scenario_moderate.append(scenario_moderate[-1] * (1 + growth_rate))

# Scenario 3: Pessimistic - Hard ceiling (data/compute wall)
scenario_pessimistic = []
ceiling = 180  # Hard capability ceiling
for y in years_future:
    years_elapsed = y - 2026
    # Asymptotic approach to ceiling
    val = ceiling - (ceiling - base_capability) * np.exp(-0.15 * years_elapsed)
    scenario_pessimistic.append(val)

# Scenario 4: Plateau - Brief gains then stagnation
scenario_plateau = []
for y in years_future:
    years_elapsed = y - 2026
    if years_elapsed <= 2:
        val = base_capability * (1.15 ** years_elapsed)
    else:
        val = base_capability * (1.15 ** 2) * (1.02 ** (years_elapsed - 2))
    scenario_plateau.append(val)

ax3.plot(years_future, scenario_optimistic, 'g-', linewidth=3, label='Optimistic: Scaling Continues', marker='o')
ax3.plot(years_future, scenario_moderate, 'b-', linewidth=3, label='Moderate: Moore\'s Law Pattern', marker='s')
ax3.plot(years_future, scenario_pessimistic, 'orange', linewidth=3, label='Pessimistic: Hard Ceiling', marker='^')
ax3.plot(years_future, scenario_plateau, 'r-', linewidth=3, label='Plateau: Stagnation by 2028', marker='x')

# AGI threshold line
ax3.axhline(y=500, color='purple', linestyle='--', linewidth=2, alpha=0.7)
ax3.text(2036.2, 500, 'Hypothetical\nAGI Threshold', fontsize=10, color='purple', va='center')

# Annotations for key points
ax3.annotate('Data exhaustion?\nInternet-scale training\ndata already used',
             xy=(2028, scenario_pessimistic[2]), xytext=(2029.5, 220),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax3.annotate('Algorithmic\nbreakthrough\nrequired?',
             xy=(2032, scenario_plateau[6]), xytext=(2033, 100),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax3.set_xlabel('Year', fontsize=11)
ax3.set_ylabel('Model Capability Index', fontsize=11)
ax3.set_title('AI Capability Projections 2026-2036: If Scaling Doesn\'t Hold', fontsize=12, fontweight='bold')
ax3.legend(loc='upper left', fontsize=10)
ax3.grid(True, alpha=0.3)
ax3.set_xlim(2025.5, 2037)
ax3.set_ylim(0, 600)

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/scaling_limits.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Chart saved: scaling_limits.png")

# ============================================
# Second Figure: Detailed breakdown of bottlenecks
# ============================================
fig2, ax4 = plt.subplots(figsize=(14, 8))

years_detail = np.arange(2024, 2037)
base = 100

# Stack of limiting factors
compute_limit = np.array([100, 115, 130, 140, 145, 148, 150, 151, 152, 152, 152, 152, 152])
data_limit = np.array([100, 112, 122, 128, 132, 134, 135, 135, 135, 135, 135, 135, 135])
algorithm_limit = np.array([100, 108, 115, 120, 124, 127, 129, 130, 131, 131, 132, 132, 132])
energy_limit = np.array([100, 110, 118, 124, 128, 130, 131, 131, 131, 131, 131, 131, 131])

# The actual capability is the minimum of all limits
actual_capability = np.minimum.reduce([compute_limit, data_limit, algorithm_limit, energy_limit])

ax4.fill_between(years_detail, 0, compute_limit, alpha=0.3, color='blue', label='Compute Scaling Limit')
ax4.fill_between(years_detail, 0, data_limit, alpha=0.3, color='green', label='Training Data Limit')
ax4.fill_between(years_detail, 0, algorithm_limit, alpha=0.3, color='orange', label='Algorithmic Efficiency Limit')
ax4.fill_between(years_detail, 0, energy_limit, alpha=0.3, color='red', label='Energy/Power Limit')
ax4.plot(years_detail, actual_capability, 'k-', linewidth=4, label='Actual Capability (binding constraint)')

# Mark when each becomes binding
ax4.annotate('Compute\nbinding', xy=(2025, 108), xytext=(2024, 85),
            arrowprops=dict(arrowstyle='->', color='blue'), fontsize=9, color='blue')
ax4.annotate('Data\nbecomes\nbinding', xy=(2028, 128), xytext=(2026.5, 145),
            arrowprops=dict(arrowstyle='->', color='green'), fontsize=9, color='green')
ax4.annotate('Energy\ncrisis', xy=(2030, 131), xytext=(2031, 145),
            arrowprops=dict(arrowstyle='->', color='red'), fontsize=9, color='red')

ax4.set_xlabel('Year', fontsize=12)
ax4.set_ylabel('Capability Index (2024 = 100)', fontsize=12)
ax4.set_title('The Binding Constraint Problem: What Limits AGI?\n(Capability = Minimum of All Constraints)',
              fontsize=14, fontweight='bold')
ax4.legend(loc='upper left', fontsize=10)
ax4.grid(True, alpha=0.3)
ax4.set_xlim(2024, 2036)
ax4.set_ylim(0, 170)

plt.tight_layout()
plt.savefig('/home/grs/Projects/adhoc/llm_forecast/binding_constraints.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Chart saved: binding_constraints.png")

print("\nAll scaling limit charts generated successfully!")
