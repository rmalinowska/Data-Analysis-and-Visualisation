#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns  

df = pd.read_csv("../data/temperature_clean.csv")

avg_temp = df["AverageTemperatureCelsius"]

year = df["year"]

fig, ax = plt.subplots(figsize=(13,7))
sns.set_style("darkgrid")

ax.grid(visible=True, which='major', color='white', linewidth=1, zorder=1)
ax.grid(visible=True, which='minor', color='white', linewidth=2, zorder=1)
ax.set_facecolor('lightgrey')
ax.scatter(year, avg_temp, edgecolors = "black", linewidths=1, s=20, facecolor="black", zorder=2, alpha=0.15)
plt.ylabel("Average Temperature Celsius", fontsize=15)
plt.xlabel("Year", fontsize=15)
plt.savefig("../plots/avg_temp_vs_year_c.png")