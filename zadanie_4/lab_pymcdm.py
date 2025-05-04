import pandas as pd
import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR, WASPAS
from pymcdm.helpers import rankdata
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# === STEP 1: Load data ===

df = pd.read_csv('smartphones.csv')

# Keep only numerical criteria columns (excluding model name)
criteria_columns = ['price_pln', 'battery_mah', 'camera_mp', 'ram_gb', 'rating']
decision_matrix = df[criteria_columns].to_numpy()
alternatives = df['model'].to_list()

# === STEP 2: Define weights and criteria types ===

weights = np.array([0.2, 0.25, 0.2, 0.15, 0.2])   # must sum to 1.0
types = np.array([-1, 1, 1, 1, 1])               # -1 = minimize (price), 1 = maximize

# === STEP 3: Define decision methods ===

bounds = np.array([
    [decision_matrix[:, i].min(), decision_matrix[:, i].max()]
    for i in range(decision_matrix.shape[1])
])

methods = {
    'TOPSIS': TOPSIS(),
    'SPOTIS': SPOTIS(bounds),
    'VIKOR': VIKOR(),
    'WASPAS': WASPAS()
}

results = {}

for name, method in methods.items():
    scores = method(decision_matrix, weights, types)

    reverse = name not in ['SPOTIS', 'VIKOR']  # for SPOTIS and VIKOR: lower score = better
    rankings = rankdata(scores, reverse=reverse)
    results[name] = rankings

# === STEP 4: Ranking table ===

ranking_df = pd.DataFrame(results, index=alternatives)
ranking_df.index.name = 'Smartphone'
ranking_df = ranking_df.sort_values(by='TOPSIS')

print("Smartphone rankings using different MCDM methods:\n")
print(ranking_df.head(15))  # show top 15 ranked smartphones


# === STEP 5: Visualization – Bar chart for TOP 10 ===

# Select top 10 smartphones based on TOPSIS ranking
top10_df = ranking_df.head(10)

# Create grouped bar chart to compare rankings across methods
ax = top10_df.plot(kind='bar', figsize=(14, 8))
plt.title('Comparison of Rankings (TOP 10 Smartphones)', fontsize=14)
plt.ylabel('Ranking (lower is better)', fontsize=12)
plt.xlabel('Smartphone', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Method')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Force y-axis ticks every 1 unit
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

plt.tight_layout()
plt.show()