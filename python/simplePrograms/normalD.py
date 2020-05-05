# Assignment on normal distribution

import numpy as np
from scipy.stats import norm

'''
1.Find the area under the standard normal curve which lie
a)To the right of Z=2.70
b)To the left of Z=1.73
c)To the right of Z=-0.66
d)To the left of Z=-1.88
e)Between Z=-0.90 and Z=-1.85
f)Between Z=-1.45 and Z=1.45
g)Between Z=-0.90 and Z=1.58
'''
print("Assignment 1")

print("Area to the right of z=2.70:",1-norm.cdf(x=2.70))
print("Area to the left of z=1.73:",norm.cdf(x=1.73))
print("Area to the right of z=-0.66:",1-norm.cdf(x=-0.66))
print("Area to the left of z=-1.88:",norm.cdf(x=-1.88))
print("Area Between Z=-0.90 and Z=-1.85:",norm.cdf(x=-0.90)-norm.cdf(x=-1.85))
print("Area Between Z=-1.45 and Z=1.45:",norm.cdf(x=1.45)-norm.cdf(x=-1.45))
print("Area Between Z=-0.90 and Z=1.58:",norm.cdf(x=1.58)-norm.cdf(x=-0.90))

print("\n")

'''
2.The life of a certain kind of electronic device has a mean of 300 hours and a standard deviation of 25 hours. Assuming that the distribution of life times which are measured to the nearest hours can be approximated closely with a normal curve
a)Find the probability that any one of these devices will have a lifetime of more than 350 hours.
b)What percentage will have life time from 220 to 260 hours?
'''
print("Assignment 2")

print("Probability of lifetime More than 350 Hours:",
        1 - norm.cdf(x=350,loc=300,scale=25))
print("Percentage of lifetime from 220 to 260 Hours:",
        (norm.cdf(x=260,loc=300,scale=25)\
        -norm.cdf(x=220,loc=300,scale=25))*100)
print("\n")

'''
3.The customer accounts of a certain departmental store have an average balance of Rs.120 and standard deviation of Rs.40. Assuming that the account balances are normally distributed, find
a)What proportion of accounts is over Rs.150 ?
b)What proportion of accounts is between Rs.100 and Rs.150?
c)What proportion of accounts is between Rs.60 and Rs.90?
'''
print("Assignment 3")

print("Proportion of accounts is over Rs.150:",\
        1 - norm.cdf(x=150,loc=120,scale=40))
print("Proportion of accounts is between Rs.100 and Rs.150:",\
        norm.cdf(x=150,loc=120,scale=40) - norm.cdf(x=100,loc=120,scale=40))
print("Proportion of accounts is between Rs.60 and Rs.90:",\
        norm.cdf(x=90,loc=120,scale=40) - norm.cdf(x=60,loc=120,scale=40))

print("\n")