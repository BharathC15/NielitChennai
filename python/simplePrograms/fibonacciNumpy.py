#Python program to generate Fibonacci numbers
#     Fn = Fn-1 + Fn-2
import numpy as np
n=int(input("Enter the number of terms :"))
fib=np.array([0,1],dtype=np.int64)
while (len(fib)<n):
    fib=np.append(fib,(fib[-1]+fib[-2]))
print(fib)