#Python program to generate Fibonacci numbers
#     Fn = Fn-1 + Fn-2
n=int(input("Enter the number of terms :"))
import time
start = time.time()

f1,f2,f=0,1,0
fib=[0,1]
for i in range(n-2):
    f=f1+f2
    fib.append(f)
    f1=f2
    f2=f
print(fib)
print("Time Taken",time.time()-start)