import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df = pd.read_csv('safety.csv')
# df.set_index('airline', inplace=True)

# print(df.shape[0]) # row count len(df.index)
# print(df.shape[1]) # column count len(df.column)

column_list = list(df.columns)
column_list.remove('avail_seat_km_per_week')
df['total incidents'] = df[column_list].sum(axis=1)

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
ax1.grid(True)
limit = 10
ax1.bar(df['airline'][:limit], df['total incidents'][:limit])

for label in ax1.xaxis.get_ticklabels():
  label.set_rotation(90)
  label.set_fontsize(10)

for label in ax1.yaxis.get_ticklabels():
  label.set_fontsize(10)

plt.rc('xtick', labelsize=10) 
plt.rc('ytick', labelsize=10) 

plt.xlabel('Airline Company')
plt.ylabel('Total Incidents Per Company')
plt.title('Total Crash Incidents For Airline Companies from 1985-Present');
plt.subplots_adjust(bottom=0.20)
plt.show()