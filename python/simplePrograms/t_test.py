# T-Test Assignment

import numpy as np

"""
1.Certain refined edible oil is packed in tins holding 16 kg each. The filling machine can maintain this but with a standard deviation of 0.5 kg. Samples of 25 are taken from the production line. If a sample means is (i)16.35kg (ii)15.8kg, Can we be 95 percent sure that the sample has come from a population of 16kg tins?
"""

print("Assignment 1")

from scipy.stats import t
print("\nTrial 1 with 16.35")
pMean=16
sMean=16.35
n=25
tstatistics=(sMean-pMean)/(0.5/np.sqrt(n))
print("T Statistics:",tstatistics)
tcritical_l=t.ppf(q=0.05/2,df=n-1)
tcritical_u=-tcritical_l

if tstatistics<tcritical_l or tstatistics>tcritical_u:
    print("Reject the Null Hypothesis")
else:
    print("Fail to reject the Null Hypothesis")

print("\nTrial 2 with 15.8")
pMean=16
sMean=15.8
n=25
tstatistics=(sMean-pMean)/(0.5/np.sqrt(n))
print("T Statistics:",tstatistics)
tcritical_l=t.ppf(q=0.05/2,df=n-1)
tcritical_u=-tcritical_l

if tstatistics<tcritical_l or tstatistics>tcritical_u:
    print("Reject the Null Hypothesis")
else:
    print("Fail to reject the Null Hypothesis")

print("\n")

"""
2.A filling machine is expected to fill 5kg of powder into bags. A sample of 10 bags gave the weighs 4.7, 4.9, 5.0, 5.1, 5.4, 5.2, 4.6,5.1, 4.6 and 4.7. Test whether the machine is working properly.
"""
print("Assignment 2")
from scipy.stats import ttest_1samp
sample_array=np.array([4.7, 4.9, 5.0, 5.1, 5.4, 5.2, 4.6,5.1, 4.6, 4.7])
tstats,pvalue=ttest_1samp(sample_array,5)

print("T-statistics:",tstats)
print("P value:",pvalue)

if pvalue < 0.05:
    print("Reject the Null Hypothesis")
    print("The filling machine is working properly")
else:
    print("Fails to reject the Null Hypothesis")
    print("The filling machine is working properly")
print("\n")

"""
3.Two sets of ten students selected at random from a college were taken; One set was given memory test as they were and the other was given the memory test after two weeks of training and the scores are given below
Set A: 10 8 7 9 8 10 9 6 7 8
Set B: 12 8 8 10 8 11 9 8 9 9
Do you think there is a significant effect due to training?
"""
print("Assignement 3")

sample1=np.array([10,8,7,9,8,10,9,6,7,8])
sample2=np.array([12,8,8,10,8,11,9,8,9,9])

from scipy.stats import ttest_ind

tstats,pvalue=ttest_ind(sample1,sample2)

print("T-statistics:",tstats)
print("P value:",pvalue)

if pvalue < 0.05:
    print("Reject the Null Hypothesis")
    print("No significant effect due to Training")
else:
    print("Fails to reject the Null Hypothesis")
    print("Significant effect due to Training")