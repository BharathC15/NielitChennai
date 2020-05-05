# Assignment on Binomial Distribution

import numpy as np
from scipy.stats import binom

'''
1.For a Binomial Distribution parameter n=5 and p=0.3. Find the probabilities of getting
a)At least 3 successes
b)At most 3 successes
c)Exactly 3 failures
'''
print("Assignment 1")
print("At least 3 successes:",1-binom.cdf(k=2,n=5,p=0.3))
print("At most 3 successes:",binom.cdf(k=3,n=5,p=0.3))
print("Excatly 3 failures",binom.pmf(k=5-3,n=5,p=0.3))
print("\n")

'''
2.If on an average one vessel in every ten is wrecked, find the probability that out of five vessels expected to arrive, four at least will arrive safely
'''
print("Assignment 2")

print("Probabilty of atleast 4/5 arrive safely",
        binom.pmf(k=4,n=5,p=9/10)+binom.pmf(k=5,n=5,p=9/10))
print("\n")

'''
3.Five coins are tossed 3,200 times.
a)Find the Frequencies of the distribution of heads and tabulate the results
b)Calculate the mean number of success and standard deviations
'''

print("Assignment 3")
print("Frequency Distribution of Heads")
for k in np.arange(5+1):
    print("Frequency of {} Heads is {}"\
    .format(k,3_200*binom.pmf(k=k,n=5,p=1/2)))
print("Mean of Success",binom.mean(n=5,p=1/2))
print("Standard Deviation of Success",binom.std(n=5,p=1/2))