#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np 

df = pd.read_csv("../data/temperature_clean.csv")

countries = df["country_id"].unique()
data=[]
for c in countries:
    data.append(df[df['country_id']==c]['AverageTemperatureCelsius'])
    
fig, ax = plt.subplots(figsize=(13,7))
sns.set_style("darkgrid")

ax.grid(visible=True, which='major', color='white', linewidth=1, zorder=1)
ax.grid(visible=True, which='minor', color='white', linewidth=2, zorder=1)
ax.set_facecolor('lightgrey')
ax.violinplot(data, showmedians=True)

ax.set_xticks(list(range(1,len(countries)+1)),labels = countries, fontsize=10)
plt.ylabel("Average Temperature Celsius", fontsize=15)
plt.xlabel("Country", fontsize=15)
plt.savefig("../plots/violinplot.png")