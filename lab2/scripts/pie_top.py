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

def get_most_populated(df):
    df = df.sort_values(by=['2021'], ascending = False)
    df = df.iloc[0:5,:]
    
    return df

def animation(df, outfile):
    names = list(df["Country Name"])
    codes = list(df["Country Code"])
    areas = [9597.000, 3287.000, 9834.000,  1905.000, 796.095]
    data = []
    for i in range(df.shape[0]):
        data.append(list(df.iloc[i,4:66]))
    
    data = [np.array(country)/1000000 for country in data]
    max_population = max([max(country) for country in data])
    fig, ax = plt.subplots(figsize=(13,7))    
    palette = list(reversed(sns.color_palette("bright", 5).as_hex()))
    

    def animate(i):

        y1=data[0][i]
        y2=data[1][i]
        y3=data[2][i]
        y4=data[3][i]
        y5=data[4][i]
        ax.clear()
        ax.set_xlim(1960,2022)
        ax.set_ylim(0, max_population + max_population*0.13)
        ax.set_title("Population of 5 most populated countries in 2021, year "+str(1960+i), fontsize=18, fontweight='bold')
        ax.text(1989 , max_population + max_population*0.01, 1960+i, fontsize = 25, color="grey")
        labels = []
        for j, y in enumerate([y1, y2, y3, y4, y5]):
            labels.append(names[j]+":"+str(int(y))+"M")
        ax.pie([y1, y2, y3, y4, y5], labels=labels,colors=palette, autopct='%1.1f%%')


    anim = FuncAnimation(fig, animate, frames = len(data[0])-1, interval = 120)
    anim.save(outfile)
    return data

filtered_df = filter_countries("../data/countries.csv", "../data/populations.csv")
df_top= get_most_populated(filtered_df)
animation(df_top, "../plots/pie_top.gif")
