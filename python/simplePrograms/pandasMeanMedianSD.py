# Python program to create a random numbered DataFrame

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

num=int(input("Enter the number of terms:"))
data=pd.DataFrame({"a":np.random.randint(0,25,num),\
                    "b":np.random.randint(25,50,num),\
                    "c":np.random.randint(50,75,num),\
                    "d":np.random.randint(75,100,num)})

data["mean_abcd"],data["std_abcd"]=data.mean(axis=1),data.std(axis=1)

print(data)

# Plotting only the mean and standard deviation
data.iloc[:,4:].plot(kind="line",subplots=True,fontsize=20)
plt.show()

data.to_json("bhaDF.json")