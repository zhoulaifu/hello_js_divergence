

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

# hello_js_divergence
