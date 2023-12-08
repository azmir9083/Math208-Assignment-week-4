mean_A, sd_A = 10, 3
mean_B, sd_B = 15, 8

mean_A_plus_B = mean_A + mean_B
sd_A_plus_B = round((sd_A**2 + sd_B**2)**0.5, 2)

mean_A_minus_B = mean_A - mean_B
sd_A_minus_B = round((sd_A**2 + sd_B**2)**0.5, 2)

mean_3A = 3 * mean_A
sd_3A = round(3 * sd_A, 2)

mean_4A_plus_5B = 4 * mean_A + 5 * mean_B
sd_4A_plus_5B = round(((4**2) * sd_A**2 + (5**2) * sd_B**2)**0.5, 2)

print(f"A + B: Mean = {mean_A_plus_B}, Standard Deviation = {sd_A_plus_B}")
print(f"A - B: Mean = {mean_A_minus_B}, Standard Deviation = {sd_A_minus_B}")
print(f"3A: Mean = {mean_3A}, Standard Deviation = {sd_3A}")
print(f"4A + 5B: Mean = {mean_4A_plus_5B}, Standard Deviation = {sd_4A_plus_5B}")
