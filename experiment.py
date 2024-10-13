import numpy as np
from scipy.spatial.distance import jensenshannon
import subprocess
import time

# Number of random numbers to generate
n = 100

# Run C program and collect output
c_output = subprocess.check_output(["./random_generator_c", str(n)]).decode().strip()
c_numbers = [int(x) for x in c_output.split()]

print("C Program Output:", c_numbers)



# # Sleep for 3 seconds
# time.sleep(1)

# Run Rust program and collect output
rust_output = subprocess.check_output(["./random_generator_rust", str(n)]).decode().strip()
# rust_output = subprocess.check_output(["./random_generator_c", str(n)]).decode().strip()
rust_numbers = [int(x) for x in rust_output.split()]
print("Rust Program Output:", rust_numbers)


# Create histograms with identical bins
max_value = max(max(c_numbers), max(rust_numbers)) + 1
c_hist, _ = np.histogram(c_numbers, bins=max_value, range=(0, max_value), density=True)
rust_hist, _ = np.histogram(rust_numbers, bins=max_value, range=(0, max_value), density=True)

# Calculate Jensen-Shannon Divergence
js_divergence = jensenshannon(c_hist, rust_hist)
print(f"Jensen-Shannon Divergence: {js_divergence}")
