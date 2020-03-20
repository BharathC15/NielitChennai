import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
a=10
b=28
c=8/3
x=y=z=1
dt=0.01
xlist=[]
ylist=[]
zlist=[]
for i in range(1000):
    dx=(a*(y-x))*dt
    dy=(x*(b-z)-y)*dt
    dz=(x*y-c*z)*dt
    x=x+dx
    y=y+dy
    z=z+dz
    xlist.append(x)
    ylist.append(y)
    zlist.append(z)
plt.figure(figsize=(15,7))
sns.scatterplot(xlist,ylist,hue=zlist,size=zlist,alpha=0.4,legend=False)
plt.show()