#Python program to perform matrix multiplication
import numpy as np
nrows=3
ncols=3

A=np.array(np.arange(1,10)).reshape(nrows,ncols)
B=np.array(np.arange(9,0,-1)).reshape(nrows,ncols)
C=np.zeros((nrows,ncols))

for row in np.arange(nrows):
    for col in np.arange(ncols):
        C[row,col]=np.sum(A[row]*B[:,col])

print(C)