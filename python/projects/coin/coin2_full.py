import numpy as np
from scipy.stats import binom
n=int(input("Enter the number of Coin Throws :"))
print("\n-------------------------- \n Heads -> Probability\n")
for i in np.arange(0,n+1):
    print(i,"->",binom.pmf(k=i,n=n,p=0.5))
