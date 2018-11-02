import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# Import dataframe
df = pd.read_csv('./safety.csv')
df = df[['airline', 'fatalities_85_99', 'fatalities_00_14']]
df.columns = ['airline', 'old_age_deaths', 'new_age_deaths']

bar_limit = 10
old_age_deaths = list(df['old_age_deaths'][:bar_limit])
new_age_deaths = list(df['new_age_deaths'][:bar_limit])
airlines = list(df['airline'][:bar_limit])

groups = len(old_age_deaths)
loc = np.arange(groups) # Locations for the groups
width = 0.3

fig, ax = plt.subplots()

plt.title('Airline Crashes')
plt.xlabel('Airline')
plt.ylabel('Fatalities')

ax.bar(loc, old_age_deaths, width=width, align='edge', label='1985-1999')
ax.bar(loc + width, old_age_deaths, width=width, align='edge', label='2000-2014')
ax.set_xticks(loc)
ax.set_xticklabels(airlines)

for label in ax.xaxis.get_ticklabels():
  label.set_rotation(90)
  label.set_fontsize(10)

for label in ax.yaxis.get_ticklabels():
  label.set_fontsize(10)

plt.subplots_adjust(bottom=0.20)
plt.legend()
plt.show()