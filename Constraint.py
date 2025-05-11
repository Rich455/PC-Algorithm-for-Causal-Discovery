
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
from causallearn.utils.cit import fisherz

# Step 1: Load dataset
df = pd.read_excel("diabetes_data.xlsx")
data = df.values
column_names = df.columns.tolist()

# Step 2: Run PC Algorithm
cg = pc(data, test_method=fisherz, alpha=0.05, verbose=True)

# Step 3: Extract and show causal edges
print("\nSignificant Causal Edges Discovered:\n")
edges = []
for edge in cg.G.get_graph_edges():
    node_i = edge.node1.get_name()
    node_j = edge.node2.get_name()
    print(f"{node_i} -- {node_j}")
    edges.append((node_i, node_j))

# Step 4: Save edges to CSV
pd.DataFrame(edges, columns=["From", "To"]).to_csv("causal_edges.csv", index=False)

# Step 5: Draw using networkx (undirected)
G = nx.Graph()  # or nx.DiGraph() if you want to customize direction later
G.add_edges_from(edges)

plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, node_color="lightblue", node_size=3000, font_size=10, font_weight="bold")
plt.title("Causal Graph (PC Algorithm)")
plt.axis("off")
plt.savefig("causal_graph.png", dpi=300)
plt.show()


