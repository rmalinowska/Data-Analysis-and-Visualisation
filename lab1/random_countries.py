#!/usr/bin/env python3

from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import pandas as pd
import numpy as np
import random

def filter_countries(countries_file, population_file):
    countries = pd.read_csv(countries_file)
    populations = pd.read_csv(population_file)
    countries = list(countries["name"].astype(str))
    populations = populations[populations["Country Name"].isin(countries)]
    return populations

def get_random(df, number):
    sample = random.sample(range(0, df.shape[0]-1), number)
    df = df.iloc[sample, :]
    return df

def animation(df):
    names = list(df["Country Name"])
    data = []
    for i in range(df.shape[0]):
        data.append(list(df.iloc[i,4:66]))
    
    data = [np.array(country)/1000000 for country in data]
    max_population = max([max(country) for country in data])
    fig = plt.figure(figsize=(8,6))
    axes = fig.add_subplot(1,1,1)
    palette = list(reversed(sns.color_palette("bright", 5).as_hex()))
    def animate(i):
        
        axes.set_ylim(0, max_population + max_population*0.1)
        y1=data[0][i]
        y2=data[1][i]
        y3=data[2][i]
        y4=data[3][i]
        y5=data[4][i]
    
        plt.bar(range(5), [y1, y2, y3, y4, y5],color=palette)
        for t in axes.texts:
            t.set_visible(False)
        axes.text(0, y1, 1960+i, color="grey", fontsize = 16)
        tickdic = {names[0]:y1, names[1]:y2, names[2]:y3, names[3]:y4, names[4]:y5}
        tcks = [i for i in tickdic]
        plt.xticks(np.arange(5), tcks)
        

    plt.title("Population by year")
    plt.ylabel("Population size [mln]")
    plt.xlabel("Five random countries.")
    anim = FuncAnimation(fig, animate, frames = len(data[0])-1, interval = 1)
    plt.show()

    return data

filtered_df = filter_countries("countries.csv", "populations.csv")
df_random = get_random(filtered_df, 5)
animation(df_random)
