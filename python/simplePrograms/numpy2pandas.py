# Python program to convert Numpy array to Matrix format
# Convert Numpy Matrix to Pandas DataFrame

import numpy as np
import pandas as pd

data=np.array(np.random.randint(10,size=9))
print("Random 9 element Vector\n",data)

#Convert to Matrix format
data1=data.reshape(3,3)
print("In 3x3 Matrix format\n",data1)

#Convert to DataFrame
data2=pd.DataFrame(data1,index=["x","y","z"],columns=["a","b","c"])
print("In Pandas DataFrame Format\n",data2)