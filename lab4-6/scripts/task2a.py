#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("../data/temperature_clean.csv")

avg_temp = df["AverageTemperatureCelsius"]

year = df["year"]

fig, ax = plt.subplots(figsize=(13,7))
ax.scatter(year, avg_temp, edgecolors = "black", linewidths=1.5, s=60, facecolor="None")
plt.ylabel("Average Temperature Celsius", fontsize=15)
plt.xlabel("Year", fontsize=15)
plt.savefig("../plots/task2a.png")