#Solve only the row of a sudoku
import numpy as np

sudoku=np.arange(1,10)
data=np.array([])
print("Enter 9 elements (1-9)\nFor missing value enter 0")
while len(data)<9:
    input_data=np.array(input("Element "+str(len(data+1))+"/9->Enter numbers:")\
    .split(),dtype=np.int32)
    if np.sum(np.isin(data,input_data)) == 0:
        if (np.sum(input_data>9) + np.sum(input_data<0)) == 0:
            data=np.append(data,input_data)
    print("Current Data->",data)
data=data[:10]
print("Given Data\n",data)
print("Processing ...")
missing_value=sudoku[np.array([item not in data for item in sudoku])]
print("missing Value",missing_value)
data=np.where(data==0,missing_value,data)
print("After filling the missing value\n",data)