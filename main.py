import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df = pd.read_csv('./safety.csv')
print(df.head())