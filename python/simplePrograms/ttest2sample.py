# Assignemnt on 2 sample T test

import numpy as np

"""
1.Two sets of ten students selected at random from a college were taken:One set was given memory test as they were and the other was given the memory test after two weeks of training and the scores are given below:

Set A	10	8	7	9	8	10	9	6	7	8
Set B	12	8	8	10	8	11	9	8	9	9

Do you think there is a significant effect due to training ?
"""
print("Assignment 1")

sample1=np.array([10,8,7,9,8,10,9,6,7,8])
sample2=np.array([12,8,8,10,8,11,9,8,9,9])
#print(len(sample1),len(sample2))

from scipy.stats import ttest_ind

tstatistics,pvalue=ttest_ind(sample1,sample2)
print("T Statistics:",tstatistics)
print("pvalue:",pvalue)

if pvalue<0.05:
    print("Reject the Null Hypothesis")
    print("Significant Effect due to Training")
else:
    print("Fails to Reject the Null Hypothesis")
    print("No Significant Effect due to Training")
print("\n")

"""
2.A group of 5 patients treated with medicine A weigh 42,39,48,60 and 41 kgs; a second group of 7 patients from the same hospital treated with medicine B weigh 38,42,56,64,68,69 and 62 kgs. Do you agree with the claim that medicine B increases weight significantly.
"""
print("Assignment 2")

sample1=np.array([42,39,48,60,41])
sample2=np.array([8,42,56,64,68,69,62])

tstatistics,pvalue=ttest_ind(sample1,sample2)
print("T Statistics:",tstatistics)
print("pvalue:",pvalue)

if pvalue<0.05:
    print("Reject the Null Hypothesis")
    print("Medicine B increase weight significantly")
else:
    print("Fails to Reject the Null Hypothesis")
    print("Medicine B does not increase weight significantly")
print("\n")

"""
3.Samples of two types of electric bulbs were tested for length of life and the following data were obtained

	Type I	Type II
No of Samples	8	7
Mean of the Samples (in hrs.)	1134	1024
SD of the samples (in hrs.)	35	40

Test at 5 percent level, whether the difference in sample means is significant
"""
print("Assignment 3")
ns1=8
ns2=7
means1=1134
means2=1024
sds1=35
sds2=40

from scipy.stats import ttest_ind_from_stats

tstatistics,pvalue=ttest_ind_from_stats(\
    mean1=means1,std1=sds1,nobs1=ns1,\
    mean2=means2,std2=sds1,nobs2=ns2)
print("T Statistics:",tstatistics)
print("pvalue:",pvalue)

if pvalue<0.05:
    print("Reject the Null Hypothesis")
    print("Two types of bulbs differ significantly with respect to theri mean life")
else:
    print("Fails to Reject the Null Hypothesis")
    print("Two types of bulbs differ significantly with respect to theri mean life")
print("\n")