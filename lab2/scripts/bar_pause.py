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

def get_5_nearest_to_afg(df):
    df = df.sort_values(by=['1960'], ascending = False)
    df.reset_index(drop=True, inplace=True)
    index = df.index[df['Country Name'] == "Afghanistan"].item()
    return df.iloc[index-2:index+3,:]

# def get_5(df):
# 	df = df.sort_values(by=['2021'], ascending = False)
# 	df.reset_index(drop=True, inplace=True)
# 	index_afg = df.index[df['Country Name'] == "Afghanistan"].item()
# 	print(df.iloc[index_afg,:]['1960'])
# 	index_pak = df.index[df['Country Name'] == "Pakistan"].item()
# 	print(df.iloc[index_pak,:]['1960'])
# 	index_tur = df.index[df['Country Name'] == "Turkmenistan"].item()
# 	print(df.iloc[index_tur,:]['1960'])

def animation(df, outfile):
    names = list(df["Country Name"])
    codes = list(df["Country Code"])
    data = []
    for i in range(df.shape[0]):
        data.append(list(df.iloc[i,4:66]))
    
    data = [np.array(country)/1000000 for country in data]
    max_population = max([max(country) for country in data])
    fig, ax = plt.subplots(figsize=(13,7))    
    palette = list(reversed(sns.color_palette("bright", 5).as_hex()))
    def animate(i):

        i = i-1960
        y1=data[0][i]
        y2=data[1][i]
        y3=data[2][i]
        y4=data[3][i]
        y5=data[4][i]
        
        ax.clear()
        if i+1960 in [i for i in range(1979,1990)]:
            ax.text(2 , max_population + max_population*0.01, "Soviet–Afghan War 1979-1989", fontsize = 20, color="red", horizontalalignment='center',verticalalignment='center')
        
        ax.set_ylim(0, max_population + max_population*0.13)
        ax.set_ylabel("Population size [mln]", fontsize=18, fontweight='bold')
        ax.set_xlabel("Five countries with closest population size to Afghanistan in 1960", fontsize=18, fontweight='bold')
        ax.set_title("Population by year", fontsize=18, fontweight='bold')
        ax.text(-0.55,  max_population + max_population*0.05, 1960+i, fontsize = 25, color="grey") 
        for j, y in enumerate([y1, y2, y3, y4, y5]):
            ax.text(j, y, codes[j]+":"+str(int(y))+"M", color="black", fontsize = 15, horizontalalignment='center', zorder=11)
            ax.bar(j,y, color=palette[j])
        tickdic = {names[0]:y1, names[1]:y2, names[2]:y3, names[3]:y4, names[4]:y5}
        tcks = [t for t in tickdic]
        plt.xticks(np.arange(5), tcks)
    fr = [str(year) for year in range(1960, 1978)]
    fr.extend(['1979']*16)
    for i in (1980,1981,1982,1983, 1984, 1985, 1986, 1987, 1988, 1989): fr.extend([str(i)]*4)
    fr.extend(str(i) for i in range(1990,2022))  
    fr = [int(f) for f in fr]
    anim = FuncAnimation(fig, animate, frames = fr, interval = 150)
    anim.save(outfile)
    return data

filtered_df = filter_countries("../data/countries.csv", "../data/populations.csv")
df_afg = get_5_nearest_to_afg(filtered_df)
animation(df_afg, "../plots/bar_pause.gif")
