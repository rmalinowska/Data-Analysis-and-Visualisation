#!/usr/bin/env python3

import pandas as pd
import datetime
from matplotlib import pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

df = pd.read_csv("../data/gantt_data.csv")

fig, ax = plt.subplots(figsize=(22, 12))
xticks = [0,31,61, 92, 123, 154, 185, 215, 246, 276, 307, 338, 368]
xticklabels = ["Oct 2023", "Nov", "Dec", "Jan 2024", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct"]

category_colors = ["dimgray", "lightgrey", "darkgrey", "gainsboro", "dimgray", "grey", "whitesmoke", "white"]
categories = df["Category"].unique()

ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.xaxis.set_minor_locator(MultipleLocator(1))

ax.set_yticks([4*i+1.5 for i in range(len(categories))],labels=categories)

gantt_plot_rows = []
categories_height = {}

for cat in categories:
    subdf = df[df["Category"]==cat]
    gantt_plot_rows.append(list(zip(subdf["days_to_start"], subdf["task_duration"])))

for i, row in enumerate(gantt_plot_rows):
    ax.broken_barh(xranges=row, yrange=(i*4, 3), label=categories[i], color=category_colors[i], edgecolor="black")
    categories_height[categories[i]] = i*4 + 1.5

for i in range(df.shape[0]):
    category = df.iloc[i,0]
    if category == "term":
        ax.text(df.iloc[i,7].item(),categories_height[category], df.iloc[i, 1], fontsize=16, color="white")
    elif category in ["classes", "linkage"]:
        ax.text(df.iloc[i,7].item(),categories_height[category], df.iloc[i, 1], fontsize=16)
    elif category == "deadline":
        if df.iloc[i,1] == "linkage deletion request":
            ax.text(df.iloc[i,7].item()-10,categories_height[category], df.iloc[i, 1], fontsize=10)
        else:
            ax.text(df.iloc[i,7].item()-30,categories_height[category], df.iloc[i, 1], fontsize=10)
    elif category == "language exams":
        if df.iloc[i, 1] == "language certification exams":
            ax.text(df.iloc[i,7].item()-45,categories_height[category], df.iloc[i, 1], fontsize=10)
        else:
            ax.text(df.iloc[i,7].item(),categories_height[category], df.iloc[i, 1], fontsize=10)
    elif category == "exams":
        if df.iloc[i,1] == "re-take summer exams":
            ax.text(df.iloc[i,7].item()-15,categories_height[category], df.iloc[i, 1], fontsize=10)
        elif df.iloc[i,1] in ["winter exams", "summer exams"]:
            ax.text(df.iloc[i,7].item()-5,categories_height[category], df.iloc[i, 1], fontsize=10)
        else:
            ax.text(df.iloc[i,7].item(),categories_height[category], df.iloc[i, 1], fontsize=10)
    elif category == "decisions":
        if df.iloc[i,1] == "completing whole year decisions":
            ax.text(df.iloc[i,7].item()-50,categories_height[category], df.iloc[i, 1], fontsize=13)
        else:
            ax.text(df.iloc[i,7].item()-30,categories_height[category], df.iloc[i, 1], fontsize=14)
    elif category == "holiday":
        ax.text(df.iloc[i,7].item(),categories_height[category], df.iloc[i, 1], fontsize=11)

plt.savefig("../plots/gantt_bw.png")