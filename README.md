# Diabetes Causal Discovery using the PC Algorithm

What the PC Algorithm Does ?
PC (named after Peter Spirtes & Clark Glymour) is a constraint-based causal discovery method.

It assumes:

Causal Markov Condition: Every variable is independent of its non-effects given its direct causes.
Faithfulness: Statistical independencies in the data reflect the causal graph.
No hidden confounders (Causal sufficiency).
Acyclicity: The causal graph has no directed cycles

How it works:

Start with a fully connected undirected graph.
Iteratively remove edges if two variables are found to be conditionally independent (via statistical tests) given some conditioning set 
Orient edges using collider rules and acyclicity (Meek's rules), leading to a partially directed graph (CPDAG) 


Mathematical Foundations
At its core, it uses conditional independence tests (e.g., Fisher’s Z-test for Gaussian data):

Causal Models vs. Pathophysiological Findings

Causal models analyze data to identify potential cause-effect relationships between factors and outcomes, which is great for hypothesis generation and prediction. Pathophysiological findings explain the biological processes behind diseases, providing real-world clinical context.

While pathophysiology offers strong biological plausibility and clinical relevance, causal models excel at uncovering complex or novel causal links from data.

Combining both approaches strengthens a project by linking statistical evidence to meaningful biological mechanisms, ensuring results are both data-driven and clinically valid. This integration forms the most robust and scientifically sound foundation for understanding disease.


Diabetes Causal Model Project:use synthetically generated, it mimics real clinical variables (age, sex, BMI, blood pressure, cholesterol, glucose, etc.)


Results :

What the Graph Shows

1.Glucose as a Central Hub
Connected to Total Cholesterol, HDL, and Cholesterol/HDL Ratio, reflecting how hyperglycemia disrupts lipid metabolism and contributes to dyslipidemia—a hallmark of metabolic syndrome and diabetes

2.Lipid-Lipid Interactions
Edges between log Triglycerides, HDL, and Cholesterol/HDL Ratio align with the well-established inverse TG–HDL relationship, seen in insulin resistance conditions.

3.Demographic & Adiposity Links
Age ↔ BMI represents age-related increases in body weight.
Age ↔ Sex captures differences in metabolic risk trajectories between genders.

Blood Pressure & LDL Connected via Total Cholesterol
Although not directly tied to glucose, BP and LDL link through Total Cholesterol, supporting known cardiovascular risk pathways
