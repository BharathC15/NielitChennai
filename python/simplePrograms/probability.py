# Assignement on Probability

import numpy as np
'''
1.Three coins are tossed. Find the probability of getting
a)At least one head
b)Exactly 2 heads
'''
print("Assignment 1")
ss=2**3 # Sample Space
print("Probability of at least one Head:",7/ss)
print("Probability of excatly two Heads:",3/ss)
print("\n")

'''
2.An integer is chosen at random out of the integers from 1 to 100. What is the probability that it is
a)Multiple of 5
b)Divisible by 7
c)Greater than 70
'''
print("Assignment 2")
numbers=np.arange(1,101)

#multiple of 5
count=0
for i in numbers:
    if i % 5 == 0:
        count+=1
print("Probability of Muliples of 5:",count/len(numbers))

#Divisible by 7
count=0
for i in numbers:
    if i % 7 == 0:
        count+=1
print("Probability of Divisible by 7:",count/len(numbers))

#Greater than 70
count=0
for i in numbers:
    if i > 70:
        count+=1
print("Probability of greater than 70:",count/len(numbers))
print("\n")

'''
3.Generate Prime Numbers till 1000 and find the following among this population
a)Mean
b)Median
c)Range
d)Quartile (1st , 2nd and 3rd )
e)Inter-Quartile Range
f)Variance
g)Standard Deviation
'''

print("Assignment 3")

# Function to generate Numpy array of Prime numbers

def bha_prime_gen(n):
    primeno=np.array([])
    for num in np.arange(2,n+1):
        flag=0
        for i in np.arange(2,int(num/2)):
            if (num%i==0):
                flag=1
        if(flag==0):
            primeno=np.append(primeno,num)
    return primeno

primes=bha_prime_gen(1000)
#print(primes)

print("Mean:",np.mean(primes))
print("Median:",np.median(primes))
print("Range:",np.max(primes)-np.min(primes))
print("Quartiles")
print("1st Quartiles",np.percentile(primes,25))
print("2st Quartiles",np.percentile(primes,50))
print("3st Quartiles",np.percentile(primes,75))
print("InterQuartile Range",
        np.percentile(primes,75)-np.percentile(primes,25))
print("Variance",np.var(primes))
print("Standard Deviations",np.std(primes))