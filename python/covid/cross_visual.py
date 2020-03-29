# Viusalise with Previous data in x-axis and Current data in y-axis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("covid_India.csv")
#print(df.head())
data=np.array(df["Cases"].values)
#print(data)

#print("Previous day",len(data[:-1]))
#print("Current day",len(data[1:]))

bha=pd.DataFrame({"pDay":data[:-1],"cDay":data[1:]})
#print(bha)

sns.set()
plt.figure(dpi=120)
sns.scatterplot(x="pDay",y="cDay",data=bha)
plt.title("Corono Virus trend in India")
plt.xlabel("Previous Day")
plt.ylabel("Next Day")
plt.show()