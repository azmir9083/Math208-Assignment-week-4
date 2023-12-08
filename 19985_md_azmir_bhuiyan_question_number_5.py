from scipy.stats import norm

tosses = 12
head_prob = 0.5

mean_val = tosses * head_prob
std_dev = (tosses * head_prob * (1 - head_prob)) ** 0.5

z_lower = (5.5 - mean_val) / std_dev
z_upper = (6.5 - mean_val) / std_dev

exact_prob = norm.cdf(z_upper) - norm.cdf(z_lower)

print("Probability:", exact_prob)
