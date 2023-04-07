#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np 

df = pd.read_csv("../data/temperature_clean.csv")

df_grouped = df.groupby(['year', 'Country']).mean()

years = sorted(df['year'].unique())
    

fig, ax = plt.subplots(figsize=(12,7))
sns.set_style("darkgrid")

ax.grid(visible=True, which='major', color='white', linewidth=1, zorder=1)
ax.grid(visible=True, which='minor', color='white', linewidth=2, zorder=1)
ax.set_facecolor('lightgrey')
sns.lineplot(x='year', y='AverageTemperatureCelsius', data=df_grouped, estimator=None, color="black")
    
plt.ylabel("Average Temperature Celsius", fontsize=15)
plt.xlabel("Year", fontsize=15)
plt.savefig("../plots/task4a.png")