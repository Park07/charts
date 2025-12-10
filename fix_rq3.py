import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('full_500m_20251209_212802.csv')
df['algorithm'] = df['algorithm'].replace('VF3', 'VF3PDL')

fig, ax = plt.subplots(figsize=(10, 6))
er_sparse = df[(df['model'] == 'ER') & (df['query'] == 'sparse_8v')].sort_values('edges')
colors = {'CECI': '#2ecc71', 'VF3PDL': '#e74c3c'}

for algo in ['CECI', 'VF3PDL']:
    data = er_sparse[er_sparse['algorithm'] == algo]
    ax.plot(data['edges']/1e6, data['eps'], 'o-', label=algo, linewidth=3, markersize=10, color=colors[algo])

ax.set_xlabel('Edges (Millions)', fontsize=12)
ax.set_ylabel('EPS (log scale)', fontsize=12)
ax.set_title('RQ3: Pruning vs Parallelism on Structureless Graphs', fontsize=14)
ax.set_yscale('log')
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)

# Better positioned annotations
ax.annotate('CECI: ~30M EPS\n(parallel enumeration)', xy=(2, 25000000), fontsize=10, color='#2ecc71')
ax.annotate('VF3PDL: 4K→100 EPS\n(pruning ineffective)', xy=(1.5, 300), fontsize=10, color='#e74c3c')

plt.tight_layout()
plt.savefig('/home/williamp/charts_data/figures/synthetic_rq3_pruning.png', dpi=150, bbox_inches='tight')
print("Fixed RQ3 chart saved")
