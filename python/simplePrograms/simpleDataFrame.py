#Python program to Create a pandas dataframe
import numpy as np
import pandas as pd

data=np.array(input("Enter numbers :").split(),dtype=np.int32)
df=pd.DataFrame({"a":data,"b":data**2,"c":data**3})
print("DataFrame:\n",df)