from scipy.stats import norm
import numpy as np

defect_rate = 0.06
total_batteries = 150
defect_count = 12

mean_defects = total_batteries * defect_rate
std_dev_defects = np.sqrt(total_batteries * defect_rate * (1 - defect_rate))

probability_12_or_more = 1 - norm.cdf(defect_count - 0.5, mean_defects, std_dev_defects)

print(f"Probability of 12 or more defectiveones in them is: {probability_12_or_more}")
