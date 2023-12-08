import numpy as np
import matplotlib.pyplot as plt

def generate_random_numbers(n):
    return np.random.standard_t(df=10, size=n)

def calculate_mean_std(numbers):
    return np.mean(numbers), np.std(numbers)

def perform_sampling(numbers, sample_size, num_samples):
    sampling_means = []
    for _ in range(num_samples):
        sample = np.random.choice(numbers, size=sample_size, replace=False)
        sampling_means.append(np.mean(sample))
    return sampling_means

def plot_histogram(data):
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=20, density=True, alpha=0.7, color='blue')
    plt.xlabel('Sample Means')
    plt.ylabel('Frequency')
    plt.title('Distribution of Sample Means')
    plt.show()

random_numbers = generate_random_numbers(100)

mean, std_dev = calculate_mean_std(random_numbers)
print(f"Mean of 100 random numbers: {mean}")
print(f"Standard deviation of 100 random numbers: {std_dev}")

sample_size = 30
num_sampling_groups = 15

sampling_means = perform_sampling(random_numbers, sample_size, num_sampling_groups)

sample_mean = np.mean(sampling_means)
sample_std_dev = np.std(sampling_means)
expected_std_dev = std_dev / np.sqrt(sample_size)

print(f"\nMean of sample means: {sample_mean}")
print(f"Standard deviation of sample means: {sample_std_dev}")
print(f"Expected standard deviation based on CLT: {expected_std_dev}")

plot_histogram(sampling_means)
