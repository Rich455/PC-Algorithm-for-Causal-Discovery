# PC-Algorithm-for-Causal-Discovery
This project applies the PC Algorithm, a constraint-based causal discovery method, to a real-world dataset (diabetes_data.xlsx). It identifies statistically significant causal relationships between variables based on conditional independence tests.

Algorithm Theory: PC (Peter and Clark) Algorithm
The PC Algorithm constructs a causal graph (a causal skeleton, optionally directed) using conditional independence testing. It works under two main assumptions:
Causal Markov Condition:
Each variable is independent of its non-effects, given its direct causes.
Faithfulness Condition:
All and only the conditional independencies present in the data correspond to those in the true causal DAG (Directed Acyclic Graph).


 How It Works:
Begins with a fully connected undirected graph.
Iteratively removes edges between variables that are conditionally independent given subsets of other variables (using Fisher’s Z-test).
The remaining edges represent potentially causal relationships.


Technologies Used
Python
causallearn for the PC algorithm
matplotlib & networkx for graph visualization
pandas for data manipulation
Dataset format: .xlsx (converted internally to NumPy array)




