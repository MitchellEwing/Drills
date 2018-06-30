#https://www.kaggle.com/starbucks/starbucks-menu#starbucks_drinkMenu_expanded.csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

starbucks = pd.read_csv('./data/starbucks.csv')
starbucks.head()

classCaff = starbucks.loc[(starbucks['Beverage_category']=='Classic Espresso Drinks'),'Caffeine (mg)']
sigCaff = starbucks.loc[(starbucks['Beverage_category']=='Signature Espresso Drinks'),'Caffeine (mg)']
classCal = starbucks.loc[(starbucks['Beverage_category']=='Classic Espresso Drinks'),'Calories']
sigCal = starbucks.loc[(starbucks['Beverage_category']=='Signature Espresso Drinks'),'Calories']
print(classCal)
classCal.describe()

#plt.hist(sigCaff)
binwidth = 50
#plt.hist(classCaff, bins=range(min(classCaff), max(classCaff) + 50, 50))
plt.hist(classCaff)
#, color='r', alpha=.5, label='Signature Espresso'
#plt.hist(classCaff, color='g', alpha=.5, label='Classical Espresso')
plt.xlabel('x axis label')
plt.legend(loc='upper right')
plt.title('title')
plt.show()
