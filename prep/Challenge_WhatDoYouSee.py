# Daily NAV for DFA Emerging Markets Value Portfolio (DFEVX)
# for the period 4-26-2018 to 5-25-2018.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./assets/DFEVX.csv')
date = df['Date']
close = df['Close']
mean = np.mean(close)
std = np.std(close)
plt.plot(date, close)
# x axis labels
xlabel_beg_end = []
for i in date:
    if i not in ['2018-04-26', '2018-05-25']:
        i = ' '
        xlabel_beg_end.append(i)
    else:
        xlabel_beg_end.append(i)
plt.grid(True)
plt.legend(loc='upper right')
plt.axhline(mean, color='black', linestyle='solid', linewidth=2)
plt.axhline(mean + std, color='red', linestyle='solid', linewidth=2)
plt.axhline(mean - std, color='red', linestyle='solid', linewidth=2)
plt.title('DFEVX (trailing 1-month)')
plt.ylabel('NAV')
plt.xlabel('Date')
plt.xticks(range(0,len(date)),xlabel_beg_end)
plt.show()
