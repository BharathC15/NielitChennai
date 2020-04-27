# Python program to analyze Gapminder dataset

import numpy as np
import pandas as pd

from gapminder import gapminder
df=gapminder.copy()
country_names=np.array(["Brazil","South Africa","India","China","Afghanistan","Bangladesh","Nepal","Pakistan","Sri Lanka","Myanmar","Thailand","Germany","Japan"])

bricks=country_names[[0,2,3,1]]
saarc=country_names[[4,5,2,6,7,8]]
bimstec=country_names[[5,2,9,8,10,6]]
g4=country_names[[2,0,11,12]]

bricks_df=df[df.loc[:,"country"] in bricks]
bricks_df.head()