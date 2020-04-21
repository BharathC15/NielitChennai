#Python program to print Prime numbers till n
n=int(input("Enter the upper limit :"))
for num in range(2,n+1):
    flag=0
    for i in range(2,int(num/2)):
        if (num%i==0):
            flag=1
    if(flag==0):
        print(num)