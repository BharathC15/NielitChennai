# Python program to analyze Gapminder dataset

import numpy as np
import pandas as pd

from gapminder import gapminder
df=gapminder.copy()

features=np.array(["lifeExp","pop","gdpPercap"])

print("\nWorld summary")
print(df[features].mean())

print("\nIndia's Summary")
India=df[df["country"]=="India"]
print(India[features].mean())

country_names=np.array(["Brazil","South Africa","India","China","Afghanistan","Bangladesh","Nepal","Pakistan","Sri Lanka","Myanmar","Thailand","Germany","Japan"])

grouping=np.array(["bricks","saarc","bimstec","g4"])

bricks=country_names[[0,2,3,1]]
saarc=country_names[[4,5,2,6,7,8]]
bimstec=country_names[[5,2,9,8,10,6]]
g4=country_names[[2,0,11,12]]

#Storing each groupings in a dataframe
bricks_df=df[df["country"].isin(bricks)]

# To automate for all groupings
for i in grouping:
    vars()[str(i)+"_df"]=df[df["country"].isin(vars()[i])]

# Display the Summary of each grouping
for i in grouping:
    print("\nSummary of",i.upper())
    print(vars()[str(i)+"_df"][features].mean())

# Display the subtraction of Grouping's Summary and India's Summary
print("Grouping - India's Summary")
for i in grouping:
    print("\nSummary difference",i.upper(),"and India")
    print((vars()[str(i)+"_df"][features].mean())-India[features].mean())