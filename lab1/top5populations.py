#!/usr/bin/env python3

from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import pandas as pd
import numpy as np

def filter_countries(countries_file, population_file):
    countries = pd.read_csv(countries_file)
    populations = pd.read_csv(population_file)
    countries = list(countries["name"].astype(str))
    populations = populations[populations["Country Name"].isin(countries)]
    return populations

def get_most_populated(df, number):
    df = df.sort_values(by=['2021'], ascending = False)
    return df.iloc[0:5,:]

def animation(df):
    names = list(df["Country Name"])
    data = []
    for i in range(df.shape[0]):
        data.append(list(df.iloc[i,4:66]))
    
    data = [np.array(country)/1000000 for country in data]
    max_population = max([max(country) for country in data])
    fig = plt.figure(figsize=(8,6))
    axes = fig.add_subplot(1,1,1)
    axes.set_ylim(0, max_population + max_population*0.1)
    axes.set_yticks([])
    palette = list(reversed(sns.color_palette("bright", 5).as_hex()))
    y1, y2, y3, y4, y5 = [], [], [], [], []
    def animate(i):
        y1=data[0][i]
        y2=data[1][i]
        y3=data[2][i]
        y4=data[3][i]
        y5=data[4][i]
    
        plt.bar(names, sorted([y1, y2, y3, y4, y5]),color=palette) 
    plt.title("Animated Bars", color=("blue"))
    anim = FuncAnimation(fig, animate, frames = len(data[0])-1, interval = 1)
    plt.show()

    return data


filtered_df = filter_countries("countries.csv", "populations.csv")
df_top5 = get_most_populated(filtered_df, 5)
animation(df_top5)

# fig = plt.figure(figsize=(8,6))
# axes = fig.add_subplot(1,1,1)
# axes.set_ylim(0, 150)

# lst1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
# lst2=[0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]

# palette = list(reversed(sns.color_palette("seismic", 2).as_hex()))

# y1, y2, = [], []
# def animate(i):
#     y1=lst1[i]
#     y2=lst2[i]
    
#     plt.bar(["one", "two"], [y1,y2], color=palette)

# plt.title("Some Title, Year: {} ".format(5000), color=("blue"))
# ani = FuncAnimation(fig, animate, interval=100)
# plt.show()
