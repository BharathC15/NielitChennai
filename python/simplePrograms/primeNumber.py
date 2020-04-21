#Python program to print Prime numbers till n
n=int(input("Enter the upper limit :"))
prime=[2]
for num in range(3,n+1):
    flag=0
    for i in prime:
        if(num % i ==0):
            flag=1
    if(flag==0):
        prime.append(num)
print(prime)