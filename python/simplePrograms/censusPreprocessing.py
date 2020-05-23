# Preprocessing Census.csv file

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

df=pd.read_csv("census.csv")

df.replace(["Nan","NaN","NA","inf"],np.nan,inplace=True)
df["Age"]=df["Age"].astype("float")
df["Hours Perweek"]=df["Hours Perweek"].astype("float")

df.boxplot()
plt.show()

# Preprocessing NA values in Hours Perweek
# Replacing Outlier with nan value

df[df["Hours Perweek"]>200]=np.nan
# Replace all the nan values with the mean value
df["Hours Perweek"].fillna(np.nanmean(df["Hours Perweek"]),inplace=True)

# To replace with median use np.nanmedian() function

df.boxplot()
plt.show()