# Python program to analyze gapminder dataset for India

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")


from gapminder import gapminder
df=gapminder.copy()


features=np.array(["lifeExp","pop","gdpPercap"])

#Group based on country and display the mean of gdpPercap
#print(df.groupby("country")["gdpPercap"].mean())

#Place the index back to the dataframe
#print(df.groupby("country")["gdpPercap"].mean()\
#    .reset_index())

#Sorting based on gdpPercap
#print(df.groupby("country")["gdpPercap"].mean()\
#    .reset_index()\
#    .sort_values("gdpPercap"))

#Sorting based on gdpPercap in descending order
#print(df.groupby("country")["gdpPercap"].mean()\
#    .reset_index()\
#    .sort_values("gdpPercap",ascending=False))

# Extracting only the first 5 values of the sorted data
#print(df.groupby("country")["gdpPercap"].mean()\
#    .reset_index()\
#    .sort_values("gdpPercap",ascending=False)\
#    .head(5))

#Extracting the countries column in the sorted data
#print(df.groupby("country")["gdpPercap"]\
#    .mean()\
#    .reset_index()\
#    .sort_values("gdpPercap",ascending=False)\
#    .head(5)["country"])

# Convert the countries column into numpy array
#print(df.groupby("country")["gdpPercap"]\
#    .mean()\
#    .reset_index()\
#    .sort_values("gdpPercap",ascending=False)\
#    .head(5)["country"].values)

n_countries=int(input("Enter the number of countries to display:"))
sort_type=input("Enter Y to show the top countries based on GDP:")

if (sort_type=="Y"):
    print("\nPerformance of Top",n_countries,"Countries are\n\n")
else:
    print("\nPerformance of Least",n_countries,"Countries are\n\n")

# Function to set the value for ascending
# or descending in the sorting operation
def my_sort(x):
    if x=="Y":       
        return False
    else:
        return True

#Find the Country Name
country_name=df.groupby("country")["gdpPercap"]\
    .mean()\
    .reset_index()\
    .sort_values("gdpPercap",ascending=my_sort(sort_type))\
    .head(n_countries)["country"].values
print("\nList of Country:\n",country_name)

# Function to plot from a dataFrame
def my_growth_plot(conName,df):
    my_color=np.array(["r","b","g"])
    plt.figure(dpi=120)
    plt.suptitle(conName+"'s Performance")
    for j in range(3):
        plt.subplot(3,1,j+1)
        plt.bar(df.index,df[features[j]],color=my_color[j])
        plt.xlabel("Year")
        plt.ylabel(str(features[j]+"_GrowthRate"))
        plt.title(features[j])
    plt.tight_layout()
    plt.show()
    
# Function to find growth rate per country
def my_growth(conName):
    con_df=df[df["country"]==conName]
    con_df.index=con_df["year"].values
    con_df=con_df[features]
    print("\n"+conName+"'s Growth Percentage Information")
    con_df_growth=(con_df - con_df.shift(1))/con_df.shift(1)*100
    print(con_df_growth)
    my_growth_plot(conName,con_df_growth)

# Run the code through each country
for i in country_name:
    my_growth(i)