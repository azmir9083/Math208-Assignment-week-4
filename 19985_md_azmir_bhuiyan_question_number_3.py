import numpy as np

p = 0.05
n = 65
q = 1 - p


theoretical_mean = n * p
theoretical_std = np.sqrt(n * p * q)

binomial_dist = np.random.binomial(n, p, 10000)

empirical_mean = np.mean(binomial_dist)
empirical_std = np.std(binomial_dist)

print(f"Theoretical Mean: {theoretical_mean}, Empirical Mean: {round(empirical_mean, 2)}")
print(f"Theoretical Standard Deviation: {theoretical_std}, Empirical Standard Deviation: {round(empirical_std, 2)}")
