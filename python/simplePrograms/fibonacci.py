#Python program to generate Fibonacci numbers
#     Fn = Fn-1 + Fn-2

f1=0
f2=1
fib=0
n=int(input("Enter the number of terms :"))
print(f1)
print(f2)
for i in range(n-2):
    fib=f1+f2
    print(fib)
    f1=f2
    f2=fib