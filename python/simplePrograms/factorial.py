#Python program to print factorial of a number

fact=1
n=int(input("Enter an integer:"))
for i in range(1,n+1):
    fact*=i
print("The Factorial of {} is {}".format(n,fact))