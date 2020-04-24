#Python program to generate Pell numbers and Silver Ratio
#     Pn = Pn-2 + 2.Pn-1
import numpy as np
n=int(input("Enter the number of terms :"))
pell=np.array([0,1],dtype=np.int64)
while (len(pell)<n):
    pell=np.append(pell,(pell[-2]+2*pell[-1]))
print("Pell Sequence\n",pell,"\nSilver Ratio",pell[-1]/pell[-2])