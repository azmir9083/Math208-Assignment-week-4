import numpy as np
import matplotlib.pyplot as plt

n = 100
p = 0.1
q = 1 - p

binomial_data = np.random.binomial(n, p, 10000)

mean = n * p
std = np.sqrt(n * p * q)

normal_data = np.random.normal(mean, std, 10000)

plt.hist(binomial_data, bins=30, alpha=0.5, label='Binomial', color='blue')
plt.hist(normal_data, bins=30, alpha=0.5, label='Normal', color='red')
plt.title('Binomial vs Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()
