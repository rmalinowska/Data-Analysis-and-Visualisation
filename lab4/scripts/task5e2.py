#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np 

df = pd.read_csv("../data/temperature_clean.csv")
df["MeanTemp"] = df.groupby(["year", "Country", "City"])['AverageTemperatureCelsius'].transform('mean')

countries = df['Country'].unique()   

fig, axes = plt.subplots(3,3,figsize=(14,7))
sns.set_style("whitegrid",{'legend.frameon':True})
g = sns.FacetGrid(df, col='Country', hue="City", col_wrap=3)
g.map(sns.lineplot, "year", "MeanTemp", units=df["City"], alpha=.7, estimator=None)
g.add_legend()
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Average Temperature', fontsize=22, font='Times New Roman', fontweight='bold')
g.fig.supxlabel("Year", fontsize=22)
g.fig.supylabel("Average Temperature", fontsize=22)
g.fig.subplots_adjust(bottom=0.1)
g.fig.subplots_adjust(left=0.1)

plt.savefig("../plots/task5e2.png")