from scipy.stats import norm

mean = 10.3
std_dev = 0.65

prob_less_than_9 = norm.cdf(9, mean, std_dev)
percentage_less_than_9 = prob_less_than_9 * 100

prob_between_9_5_and_10_6 = norm.cdf(10.6, mean, std_dev) - norm.cdf(9.5, mean, std_dev)
percentage_between_9_5_and_10_6 = prob_between_9_5_and_10_6 * 100

top_20_percentile = norm.ppf(0.80, mean, std_dev)

print(f"a. Percentage of lengths less than 9cm: {percentage_less_than_9:.2f}%")
print(f"b. Percentage of lengths between 9.5cm and 10.6cm: {percentage_between_9_5_and_10_6:.2f}%")
print(f"c. Minimum length for the top 20%: {top_20_percentile:.2f}cm")
