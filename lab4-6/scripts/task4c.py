#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np 

df = pd.read_csv("../data/temperature_clean.csv")

df_grouped = df.groupby(['year', 'Country']).mean()

   
fig, ax = plt.subplots(figsize=(14,7))
sns.set_style("darkgrid")

ax.grid(visible=True, which='major', color='white', linewidth=1, zorder=1)
ax.grid(visible=True, which='minor', color='white', linewidth=2, zorder=1)
ax.set_facecolor('lightgrey')
g = sns.lineplot(x='year', y='AverageTemperatureCelsius', data=df_grouped, hue='Country')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.85, box.height])
ax.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1)

plt.ylabel("Average Temperature Celsius", fontsize=15)
plt.xlabel("Country", fontsize=15)
plt.savefig("../plots/task4c.png")