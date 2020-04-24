# Python program to generate Pascal Triangle
import numpy as np

num=int(input("Enter the number of lines:"))
pascal=np.zeros((num,num))


for row in np.arange(num):
    for col in np.arange(num):
        if (col==0):
            pascal[row,col]=1
        elif (row==col):
            pascal[row,col]=1
            break
        else:
            pascal[row,col]=pascal[row-1,col-1]+pascal[row-1,col]
print(pascal)
