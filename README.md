# An issue encounted when trying to address equivalence checking for random number generation using Jensen-Shannon divergence

## **Objective**

Find a solution to **check equivalence between a C random number generator** and a **Rust random number generator**.



## **Issue**

Preliminary theoretical research suggests that **Jensen-Shannon divergence** can be used to compare the two distributions. However, it has been challenging to achieve a low divergence value in practice.



## **Repository Structure**

- **C Program**: `random_generator.c` – Generates random inputs from 0 to 100.
- **Rust Program**: `random_generator/src/main.rs` – Generates random inputs from 0 to 100.
- **Python Script**: `experiment.py` – Compares the distributions using **SciPy's Jensen-Shannon divergence**.


## **What to Do**

1. **Understand why the current divergence value is around 0.5.**  
   - Investigate differences in the algorithms, seeding, or range logic between the C and Rust implementations.

2. **Attempt to reduce the divergence to 0.**  
   - Ensure consistent random seeding.
   - Verify identical range generation logic between C and Rust.
   - Run larger samples to minimize randomness-induced noise.



# [Jensen–Shannon Divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence)

The **Jensen–Shannon divergence (JSD)** is a method for measuring the similarity between two probability distributions. It is based on the **Kullback–Leibler divergence (KL divergence)** but has key advantages, including being symmetric and always producing a finite value.

## Definition

The Jensen–Shannon divergence between two probability distributions **P** and **Q** is defined as:

```
JS(P || Q) = (1/2) * KL(P || M) + (1/2) * KL(Q || M)
```

where:

```
M = (1/2) * (P + Q)
```

- `KL(P || M)` is the **Kullback–Leibler divergence** between distributions **P** and **M**.
- **M** is the **average distribution** of **P** and **Q**.

The **Jensen–Shannon divergence** is symmetric:

```
JS(P || Q) = JS(Q || P)
```

It satisfies the following properties:

- `0 <= JS(P || Q) <= 1` (if using log base 2).
- A value of **0** indicates that the two distributions are identical.
- A value close to **1** indicates that the distributions are very different.

## Properties

- **Symmetric**: Unlike KL divergence, JSD treats **P** and **Q** equally.
- **Finite**: JSD is always defined, even when the distributions contain zeros.
- **Metric**: The square root of the JSD is a **valid distance metric**.

## Applications

The Jensen–Shannon divergence is widely used in various fields:

- **Natural Language Processing (NLP)**: To measure the difference between language models or text corpora.
- **Bioinformatics**: To compare gene expression profiles.
- **Machine Learning**: To assess the similarity between probability distributions produced by models.
- **Information Theory**: For tasks involving information retrieval or clustering.

## References
- [Jensen–Shannon Divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence)
- [Kullback–Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)
- [Information Theory](https://en.wikipedia.org/wiki/Information_theory)

---

### **Explanation**

- **Math notation**: Used inline `code blocks` (`` ` ``) to ensure math symbols render cleanly.
- **URLs**: Added links for related concepts.
- **Structure**: Clean and GitHub-friendly Markdown layout.

