import numpy as np
import math

# Assume a coin flipped 300 times and 200 heads appeared
# Is it biased ?
n = 300
heads = 200

# 1 - Set model
# It is binominal

# 2 - Fit params
# P(x) = combination(x, n) * p^x * (1-p)^(1-x)
# n == 300, heads == 200 for heads, p = ?
p = 0.5 # for unbiased coin

# 3 - Formulate null hypothesis
# head means 1, tail means 0
# for unbiased coin we should at least get 150
# P(x >= 200)
def combination(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

p_value = 1 - np.sum([combination(300, i)*np.power(0.5, i)*np.power(0.5, 300-i) for i in range(200)])
print(p_value)

if p_value < 0.05:
    print("Reject.")
elif p_value >= 0.05:
    print("Failed to reject.")
