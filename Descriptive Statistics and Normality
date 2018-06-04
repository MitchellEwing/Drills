import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

#normal distribution
rand1 = np.random.normal(50, 300, 1000)
rand2 = np.random.poisson(1, 1000)
rand1.sort()
rand2.sort()
norm = np.random.normal(0, 1, 1000)
norm.sort()
plt.plot(norm, rand1, "o")
plt.show()
plt.plot(norm, rand2, "o")
plt.show()
plt.hist(rand1, bins=20, color='c')
plt.axvline(rand1.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(rand1.mean() + rand1.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(rand1.mean()-rand1.std(), color='b', linestyle='dashed', linewidth=2) 
plt.show()

#binomial distribution
binomial = np.random.binomial(20, 0.5, 100)
plt.hist(binomial)
plt.show()

#poisson distribution
s = np.random.poisson(5, 100)
plt.hist(s)
plt.show()

#lognormal distribution
lg = np.random.lognormal(0, 1, 100)
plt.hist(lg)
plt.show()

#uniform distribution
uni = np.random.uniform(-1, 0, 100)
plt.hist(uni)
plt.show()

#f distribution
dfnum = 1
dfden = 48
f = np.random.f(dfnum, dfden, 100)
plt.hist(f)
plt.show()

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
