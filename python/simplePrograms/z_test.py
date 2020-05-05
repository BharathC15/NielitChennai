# Z-Test Assignement

"""
A sample of 400 male students is found to have a mean height of 171.38cms. Can it be reasonably regarded as a sample from a large population with mean height 171.17 and standard deviation 3.30cms
"""
print("Assignment 1")
import numpy as np
n=400
sMean=171.38
pMean=171.17
pStd=3.30

zstatistics=(sMean - pMean)/(pStd/np.sqrt(n))
print("Zstatistics :",zstatistics)

from scipy.stats import norm

zcritical_l=norm.ppf(q=0.05/2)
zcritical_u=-zcritical_l
print("Critical Values are :",zcritical_l,zcritical_u)

if zstatistics<zcritical_l or zstatistics>zcritical_u:
    print("Reject the Null Hypothesis")
    print("sample is not from the large population")
else:
    print("Fail to reject the Null Hypothesis")
    print("sample is from the large population")

    print("\n")

"""
2.A sample of 900 items has mean 3.4 and standard deviation 2.61. can the sample be regarded as drawn from a population with mean 3.25 at 1 percent level of significance
"""
print("Assignment 2")
n=900
sMean=3.4
pMean=3.25
pStd=2.61

zstatistics=(sMean - pMean)/(pStd/np.sqrt(n))
print("Zstatistics :",zstatistics)

from scipy.stats import norm

zcritical_l=norm.ppf(q=0.01/2)
zcritical_u=-zcritical_l
print("Critical Values are :",zcritical_l,zcritical_u)

if zstatistics<zcritical_l or zstatistics>zcritical_u:
    print("Reject the Null Hypothesis")
    print("sample is not from the large population")
else:
    print("Fail to reject the Null Hypothesis")
    print("sample is from the large population")