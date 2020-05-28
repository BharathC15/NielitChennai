#Chi - Squared Test Assignment

import numpy as np

"""
1.A random sample of employees of a large company was selected and the employees were asked to complete a questionnaire. One question asked was whether the employee was in favour of the introduction of flexible working hours. The following table classifies the employees by their response and their response and by their area of work
	Production	Non-Production
In Favour	129	171
Not in Favour	31	69
Test whether there is evidence of a significant association between the response and the area of work
"""
print("Assignment 1")
data=np.array([129,171,31,69]).reshape(2,2)

from scipy.stats import chi2_contingency
chistatistics,pvalue,dof,expected=chi2_contingency(data)
print("Observed value\n",data)
print("Expected value\n",expected)
print("Chi statistics:",chistatistics)
print("P value:",pvalue)

if pvalue<0.05:
    print("Reject the Null hypothesis")
    print("Significant association between response and area of work")
else:
    print("Fails to reject the null hypothesis")
    print("No Significant association between reponse and area of work")

print("\n")

"""
2.The theory predicts that the proportion of beans in four given groups should be 9:3:3:1 in an examination with 1600 beans, the numbers in the four groups were 882,313,287 and 118. Does the experiment result support the theory?
"""

print("Assignment 2")
ratio_sample=np.array([9,3,3,1])
observed_f=np.array([882,313,287,118])
expected_f=ratio_sample*(1600/np.sum(ratio_sample))

print("Observed Frequency:",observed_f)
print("Expected Frequency:",expected_f)

from scipy.stats import chisquare
chistatistics,pvalue=chisquare(f_obs=observed_f,f_exp=expected_f)

print("Chi statistics:",chistatistics)
print("P value:",pvalue)

if pvalue<0.05:
    print("Reject the Null hypothesis")
    print("Proportion of Beans are not in the given ratio")
else:
    print("Fails to reject the null hypothesis")
    print("Proportion of Beans are in the given ratio")