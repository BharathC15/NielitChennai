import numpy as np
from scipy.stats import t

def bharath_Ttest1s(sMean,sd,pMean,n,alpha=0.05):
    tstatistics=(sMean-pMean)/(sd/np.sqrt(n))
    if tstatistics>0:
        tstatistics=-tstatistics
    print("\nT Statistics:",tstatistics)
    
    tcritical=[t.ppf(q=alpha/2,df=n-1),-t.ppf(q=alpha/2,df=n-1)]
    print("T critical Values are :",tcritical)
    if tstatistics<tcritical[0] or tstatistics>tcritical[1]:
        print("Reject the Null Hypothesis")
    else:
        print("Fail to reject the Null Hypothesis")

    pvalue=2*t.cdf(tstatistics,df=n-1)
    print("\nPvalue value is:",pvalue)
    if pvalue < 0.05:
        print("Reject the Null Hypothesis")
    else:
        print("Fails to reject the Null Hypothesis")

    print("\n")

def bharath_Ttest2s(s1Mean,sd1,n1,s2Mean,sd2,n2,alpha=0.05):
    varianceRatio=np.max([sd1,sd2])/np.min([sd1,sd2])
    if varianceRatio > 2:
        print("\nUnequal Variance:",varianceRatio)
        sdelta=np.sqrt((sd1**2)/n1 + (sd2**2)/n2)
        tstatistics=(s1Mean-s2Mean)/sdelta
        dof=((sd1**2)/n1 + (sd2**2)/n2)**2/ \
            ((s1**2/n1)**2/(n1-1) + (s1**2/n1)**2/(n1-1) )

    else:
        print("\nSimilar Variance:",varianceRatio)
        sp=np.sqrt(((n1-1)*sd1**2+(n2-1)*sd2**2)/(n1+n2-2))
        tstatistics=(s1Mean-s2Mean)/(sp*np.sqrt(1/n1+1/n2))
        dof=n1+n2-2

    if tstatistics>0:
        tstatistics=-tstatistics
    print("\nT Statistics:",tstatistics)
    
    tcritical=[t.ppf(q=alpha/2,df=dof),-t.ppf(q=alpha/2,df=dof)]
    print("T critical Values are :",tcritical)
    
    if tstatistics<tcritical[0] or tstatistics>tcritical[1]:
        print("Reject the Null Hypothesis")
    else:
        print("Fail to reject the Null Hypothesis")

    pvalue=2*t.cdf(tstatistics,df=dof)
    print("\nPvalue value is:",pvalue)
    if pvalue < 0.05:
        print("Reject the Null Hypothesis")
    else:
        print("Fails to reject the Null Hypothesis")

    print("\n")

"""
1.Certain refined edible oil is packed in tins holding 16 kg each. The filling machine can maintain this but with a standard deviation of 0.5 kg. Samples of 25 are taken from the production line. If a sample means is (i)16.35kg (ii)15.8kg, Can we be 95 percent sure that the sample has come from a population of 16kg tins?
"""
print("Assignment 1")
pMean=16
sd=0.5
n=25

print("Sample mean:16.35")
print("H0 : Sample came from the population of 16kg tins")
print("H1 : Sample didn't came from the population of 16kg tins")
bharath_Ttest1s(16.35,sd,pMean,n)


print("Sample mean:15.8")
print("H0 : Sample came from the population of 16kg tins")
print("H1 : Sample didn't came from the population of 16kg tins")
bharath_Ttest1s(15.8,sd,pMean,n)

print("\n")

"""
2.A filling machine is expected to fill 5kg of powder into bags. A sample of 10 bags gave the weighs 4.7, 4.9, 5.0, 5.1, 5.4, 5.2, 4.6,5.1, 4.6 and 4.7. Test whether the machine is working properly.
"""
print("Assignment 2")
sample_array=np.array([4.7, 4.9, 5.0, 5.1, 5.4, 5.2, 4.6,5.1, 4.6, 4.7])

sMean=np.mean(sample_array)
pMean=5
sd=np.std(sample_array,ddof=1)
n=len(sample_array)

print("H0 : Machine Working Properly")
print("H1 : Machine Not working properly")
bharath_Ttest1s(sMean,sd,pMean,n)

"""
3.Two sets of ten students selected at random from a college were taken; One set was given memory test as they were and the other was given the memory test after two weeks of training and the scores are given below
Set A: 10 8 7 9 8 10 9 6 7 8
Set B: 12 8 8 10 8 11 9 8 9 9
Do you think there is a significant effect due to training?
"""
print("Assignement 3")

sample1=np.array([10,8,7,9,8,10,9,6,7,8])
sample2=np.array([12,8,8,10,8,11,9,8,9,9])

print("H0: No Significant Effect due to training")
print("H1: Significant Effect due to training")

s1Mean,s2Mean=np.mean(sample1),np.mean(sample2)
sd1,sd2=np.std(sample1,ddof=1),np.std(sample2,ddof=1)
n1,n2=len(sample1),len(sample2)

bharath_Ttest2s(s1Mean,sd1,n1,s2Mean,sd2,n2,alpha=0.05)
