#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv("../data/temperature.csv")

df = df.dropna().drop("day", axis=1)

AverageTemperatureCelsius = 5/9*(df["AverageTemperatureFahr"]-32)
AverageTemperatureUncertaintyCelsius = 5/9*(df["AverageTemperatureUncertaintyFahr"]-32)

df = df.drop(["AverageTemperatureFahr","AverageTemperatureUncertaintyFahr"], axis=1)

df["AverageTemperatureCelsius"] = AverageTemperatureCelsius
df["AverageTemperatureUncertaintyCelsius"] = AverageTemperatureUncertaintyCelsius

df.to_csv("../data/temperature_clean.csv", sep=",", index=False, header=True)