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

Why This Matters Clinically
Mimics real-world diabetes pathophysiology—e.g., impaired glucose regulation → dyslipidemia, contributing to cardiovascular risk.
Highlights key intervention targets: managing glucose to improve lipid profiles or altering BMI/age factors to reduce metabolic burden.
Demonstrates the potential of causal discovery to complement epidemiological research by suggesting plausible causal pathways—even when using synthetic—but structurally realistic data

Clinical vs. Synthetic Data

This graph was built on AI-generated synthetic data, not actual patient records.
While not capturing full real-world variability or confounders, the synthetic model reflects clinically plausible relationships, validating the approach.
In a real EHR dataset, similar methods (PC algorithm) have revealed comparable causal structures between variables like insulin, BP, BMI, glucose, and cholesterol 


Are Results Clinically Significant?

Yes—at least at the level of known metabolic relationships:
Glucose ↔ Lipids
Age ↔ BMI

Lipid network interconnections
Lack of direct edges (e.g., BMI → Glucose) may indicate:

Limitations of the synthetic dataset or the α threshold
Need for real-world data where effect sizes differ
