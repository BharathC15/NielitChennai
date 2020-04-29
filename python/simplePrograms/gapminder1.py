# Python program to analyze gapminder dataset for India

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")


from gapminder import gapminder
df=gapminder.copy()


features=np.array(["lifeExp","pop","gdpPercap"])

India_df=df[df["country"]=="India"]
India_df.index=India_df["year"].values
India_df=India_df[features]
print(India_df)
India_df_growth=(India_df - India_df.shift(1))\
    /India_df.shift(1)*100
print(India_df_growth)

plt.figure(dpi=120)
plt.suptitle("India's Performance")
plt.subplot(3,1,1)
plt.bar(India_df_growth.index,India_df_growth[features[0]],color='r')
plt.xlabel("Year")
plt.ylabel(str(features[0]+"_GrowthRate"))
plt.title(features[0])
plt.subplot(3,1,2)
plt.bar(India_df_growth.index,India_df_growth[features[1]],color='b')
plt.title(features[1])
plt.xlabel("Year")
plt.ylabel(str(features[1]+"_GrowthRate"))
plt.subplot(3,1,3)
plt.bar(India_df_growth.index,India_df_growth[features[2]],color='g')
plt.title(features[2])
plt.xlabel("Year")
plt.ylabel(str(features[2]+"_GrowthRate"))

plt.tight_layout()
plt.show()

