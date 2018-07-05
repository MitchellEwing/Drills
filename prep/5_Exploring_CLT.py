import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
# %matplotlib inline
pop1 = np.random.binomial(10, 0.2, 10000)
pop2 = np.random.binomial(10, 0.5, 10000)

# sample size 1000
sample1 = np.random.choice(pop1, 1000, replace=True)
sample2 = np.random.choice(pop2, 1000, replace=True)
plt.hist(sample1, alpha=0.5, label="sample 1")
plt.hist(sample2, alpha=0.5, label="sample 2")
plt.legend(loc='upper right')
plt.show()
print(sample1.mean())
print(sample2.mean())
print(sample1.std())
print(sample2.std())
diff = sample2.mean() - sample1.mean()
print(diff)

# sample size 20
sample1 = np.random.choice(pop1, 20, replace=True)
sample2 = np.random.choice(pop2, 20, replace=True)
print(sample1.mean())
print(sample2.mean())
print(sample1.std())
print(sample2.std())
diff = sample2.mean() - sample1.mean()
print(diff)

# probability value pop1 change to 0.3, compute t-stat and p-value
pop1 = np.random.binomial(10, 0.3, 10000)
pop2 = np.random.binomial(10, 0.5, 10000)
sample1 = np.random.choice(pop1, 1000, replace=True)
sample2 = np.random.choice(pop2, 1000, replace=True)
from scipy.stats import ttest_ind
print(ttest_ind(sample2, sample1, equal_var=False))

# probability value pop1 change to 0.4, compute t-stat and p-value
pop1 = np.random.binomial(10, 0.4, 10000)
pop2 = np.random.binomial(10, 0.5, 10000)
sample1 = np.random.choice(pop1, 1000, replace=True)
sample2 = np.random.choice(pop2, 1000, replace=True)
from scipy.stats import ttest_ind
print(ttest_ind(sample2, sample1, equal_var=False))