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

def animation(df, outfile):
    names = list(df["Country Name"])
    codes = list(df["Country Code"])
    data = []
    for i in range(df.shape[0]):
        data.append(list(df.iloc[i,4:66]))
    
    data = [np.array(country)/1000000 for country in data]
    max_population = max([max(country) for country in data])
    fig, ax = plt.subplots(figsize=(13,7))    
    palette =['o','*','.', '\\','|']
    def animate(i):    
        y1=data[0][i]
        y2=data[1][i]
        y3=data[2][i]
        y4=data[3][i]
        y5=data[4][i]
        
        ax.clear()
        ax.set_ylim(0, max_population + max_population*0.13)
        ax.set_ylabel("Population size [mln]", fontsize=18, fontweight='bold')
        ax.set_xlabel("Five random countries", fontsize=18, fontweight='bold')
        ax.set_title("Population by year", fontsize=18, fontweight='bold')
        ax.text(-0.55,  max_population + max_population*0.05, 1960+i, fontsize = 25, color="grey") 

        for j, y in enumerate([y1, y2, y3, y4, y5]):
            ax.text(j, y, codes[j]+":"+str(int(y))+"M", color="black", fontsize = 15, horizontalalignment='center', zorder=11)
            ax.bar(j,y, color = 'white', edgecolor='black', hatch=palette[j])

        tickdic = {names[0]:y1, names[1]:y2, names[2]:y3, names[3]:y4, names[4]:y5}
        tcks = [t for t in tickdic]
        plt.xticks(np.arange(5), tcks)
          
    anim = FuncAnimation(fig, animate, frames = len(data[0])-1, interval = 70)
    anim.save(outfile)
    return data

filtered_df = filter_countries("../data/countries.csv", "../data/populations.csv")
df_random = get_random(filtered_df, 5)
animation(df_random, "../plots/bar_random_bw.gif")
