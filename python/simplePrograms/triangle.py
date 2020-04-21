#Python program to print triangle pattern

n=int(input("Enter the number of lines to print :"))
# Print only the numbers with space
for i in range(1,n+1):
    print((str(i)+str(" "))*i)
print("\n\n")

#Print in a triangle form
for i in range(1,n+1):
    print((str("0")*(n-i))+(str(i)+str("0"))*i)
print("\n\n")
# TO get Diamond Shape
for i in range(1,n+1):
    print((str(" ")*(n-i))+(str(i)+str(" "))*i)
for i in range(n-1,0,-1):
    print((str(" ")*(n-i))+(str(i)+str(" "))*i)