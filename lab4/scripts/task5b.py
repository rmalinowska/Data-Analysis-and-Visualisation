#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np 

df = pd.read_csv("../data/temperature_clean.csv")
df["MeanTemp"] = df.groupby(["year", "Country", "City"])['AverageTemperatureCelsius'].transform('mean')

countries = df['Country'].unique()   

fig, axes = plt.subplots(3,3,figsize=(14,7))
sns.set_style("darkgrid",{'legend.frameon':True})
g = sns.FacetGrid(df, col='Country', hue="Country", col_wrap=3)
g.map(sns.lineplot, "year", "MeanTemp", units=df["City"], alpha=.7, estimator=None)
g.add_legend()

plt.savefig("../plots/task5b.png")