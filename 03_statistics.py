# Part 3: Statistics Fundamentals

import numpy as np
import statistics

data = [10, 20, 20, 30, 40, 50, 50, 60]

print("STATISTICS FUNDAMENTALS")
print("-" * 40)

print("Data:", data)

# Mean
mean = statistics.mean(data)

# Median
median = statistics.median(data)

# Mode
mode = statistics.mode(data)

# Standard deviation
std_dev = statistics.stdev(data)

# Variance
variance = statistics.variance(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std_dev)
print("Variance:", variance)

# NumPy calculations
array = np.array(data)

print("\nUsing NumPy:")
print("Mean:", np.mean(array))
print("Median:", np.median(array))
print("Standard Deviation:", np.std(array))
print("Minimum:", np.min(array))
print("Maximum:", np.max(array))