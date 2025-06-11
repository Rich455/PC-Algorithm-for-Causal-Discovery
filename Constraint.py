
## PC ((named after Peter and Clark) Algorithm Summary (Constraint-Based Causal Discovery)

# It works under two key assumptions:- 
   # Causal Markov Condition: Each variable is conditionally independent of its non-effects given its direct causes.
   # Faithfulness: All conditional independencies in the data reflect the causal graph.


##PC algorithm infers the causal skeleton based on conditional independence tests (e.g., Fisher’s Z-test).
# An edge exists between nodes if the test fails to prove independence at the specified alpha level.



import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from causallearn.search.ConstraintBased.PC import pc

# 1. Load data
df = pd.read_csv('diabetes_causal_data.csv')
features = df.drop(columns=['Outcome'])
data_array = features.values

# 2. Run PC algorithm
cg = pc(data_array, alpha=0.05, indep_test='fisherz')

# 3. Convert to NetworkX graph
G = nx.Graph()
cols = list(features.columns)
n = len(cols)

for i in range(n):
    for j in range(i + 1, n):  # only upper triangle to avoid duplicates
        val_ij = cg.G.graph[i, j]
        val_ji = cg.G.graph[j, i]
        if val_ij != 0 or val_ji != 0:
            G.add_edge(cols[i], cols[j])

# 4. Plot using NetworkX + Matplotlib
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1200, node_color='lightblue', font_size=10)
plt.title("Causal Skeleton Discovered (PC Algorithm)")
plt.savefig('causal_graph_networkx.png', dpi=200)
plt.show()

# 5. Extract edges and save CSV
edges = list(G.edges())
pd.DataFrame(edges, columns=['Source', 'Target']).to_csv('causal_edges_networkx.csv', index=False)
