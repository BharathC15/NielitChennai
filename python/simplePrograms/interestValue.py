# Python program to find simple interest and compound interest
# Simple Interest = (principle*years*rate)/100
# Compound Interest = principle*(1+rate/100)^years

principle=float(input("Enter the Principal value :"))
years=float(input("Enter the number of years:"))
rate=float(input("Enter the annual rate of Interest:"))
SimpleI=format((principle*years*rate)/100,'.4f')
CompoundI=format(principle*(1+rate/100)**years,'.4f')

print("Simple Interest={},Amount={}".format(SimpleI,principle+SimpleI))
print("Compound Interest={},Amount={}".format(CompoundI,principle+CompoundI))