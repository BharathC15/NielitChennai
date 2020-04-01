import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
trials=int(input("Enter the no of Trials for this simulation :"))
sum_value,probability=[],[]
dice=int(input("Enter the no of dices :"))
for i in np.arange(1*dice,dice*6 + 1):
    found=0
    for _ in np.arange(trials):
        total=0
        for _ in np.arange(dice):
            total+=np.random.randint(1,7)
        if(total==i):
            found+=1
    sum_value.append(i)
    probability.append(np.round((found/trials)*100,4))
    print("Sum Value :",i,"probability",np.round((found/trials)*100,4),"%")
df=pd.DataFrame({"sum_value":sum_value,"probability":probability})
plt.figure(dpi=120)
title="Total number of Dice thrown = "+str(dice)
sns.color_palette("Set3",n_colors=(dice*6+1))
sns.barplot(x="sum_value",y="probability",data=df)
plt.title(title)
plt.xlabel("Sum of the Dice Value")
plt.ylabel("Probability of Occurance")
plt.show()
