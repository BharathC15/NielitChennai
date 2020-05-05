# Assignement on Poisson Distribution

import numpy as np
from scipy.stats import poisson

'''
1.Find the probability that atmost 5 defective fuses will be found in a box of 200 fuses if experience shows that 2 per cent of such fuses are defective.
'''
print("Assignment 1")
print("Probability of atmost 5 Defective",poisson.cdf(k=5,mu=200*0.02))
print("\n")

'''
2.The number of accidents in a year attributed to taxi drivers in a city follows a Poisson distribution with mean equal to 3. Out of 1,000 taxi drivers, find approximately the number of drivers with
a)No accidents in a year
b)More than 3 accidents in a year
'''
print("Assignment 2")

print("No of drivers with no accidents in a year",
        poisson.pmf(k=0,mu=3)*1000)
print("No of drivers with more than 3 accidents in a year",
        (1-poisson.cdf(k=3,mu=3))*1000)

print("\n")
'''

3.From the records of 10 Indian Army corps kept over 20 years the following data were obtained showing the number of deaths caused by the horse. Calculate the theoretical Poisson frequencies
No of Deaths:		0	1	2	3	4	Total
Frequency:		109	65	22	3	1	200
'''
print("Assignment 3")
mean_value=(0*109 + 1*65 + 2*22 + 3*3 + 4*1)/200
print("Frequencies of Deaths")
for k in np.arange(4+1):
    print("No of Deaths={}, Frequency={}"\
            .format(k,poisson.pmf(k=k,mu=mean_value)*200))

print("\n")