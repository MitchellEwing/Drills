# Generate two normally-distribued variables, one with a mean of 5 and
# standard deviation of 0.5, and the other with a mean of 10 and
# standard deviation of  1. Add them together to create a third variable.
# Graph the third variable using a histogram.
# Compute the mean and standard deviation and plot them as vertical lines
# on the histogram.
# Evaluate the descriptive statistics against the data.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
var1 = np.random.normal(5, 0.5, 1000)
var2 = np.random.normal(10, 1, 1000)
var3 = var1 + var2
var1.sort()
var2.sort()
var3.sort()
mean = np.mean(var3)
stdd = np.std(var3)
plt.hist(var3)
plt.axvline(mean, color='black', linestyle='solid', linewidth=2)
plt.axvline(mean + stdd, color='red', linestyle='solid', linewidth=2)
plt.axvline(mean - stdd, color='red', linestyle='solid', linewidth=2)
plt.axvline(mean + stdd + stdd, color='blue', linestyle='solid', linewidth=2)
plt.axvline(mean - stdd - stdd, color='blue', linestyle='solid', linewidth=2)
plt.show()

# 2 std deviations from mean