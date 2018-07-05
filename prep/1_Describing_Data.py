# Greg was 14, Marcia was 12, Peter was 11, Jan was 10, Bobby was 8, and 
# Cindy was 6 when they started playing the Brady kids on the Brady Bunch.
# Cousin Oliver was 8 years old when he joined the show. 
# What are the mean, median, and mode of the kids' ages when 
# they first appeared on the show?
# What are the variance, standard deviation, and the standard error?

import numpy as np
import pandas as pd
brady_bunch_array = np.array([14, 12, 11, 10, 8, 6, 8])
df = pd.DataFrame(brady_bunch_array)
df.columns = ['Age']
df.index = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Oliver']
print(df.mean())
print(df.median())
print(df.mode())
print(df.var())
print(df.std())
print(np.std(df ,ddof=1) / np.sqrt(len(df)))

# Mean and Standard Deviation 

# Cindy has a birthday, 
brady_bunch_array[5] = 7
print(df.mean())
print(df.median())
print(df.mode())
print(df.var())
print(df.std())
print(np.std(df ,ddof=1) / np.sqrt(len(df)))

# Nobody likes Cousin Oliver. Maybe the network should have used an 
# even younger actor. 
# Replace Cousin Oliver with 1-year-old Jessica, then recalculate again.
# Does this change your choice of central tendency or variance 
# estimation methods?

df.index = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Jessica']
brady_bunch_array = np.array([14, 12, 11, 10, 8, 6, 1])
print(df.mean())
print(df.median())
print(df.mode())
print(df.var())
print(df.std())
print(np.std(df ,ddof=1) / np.sqrt(len(df)))