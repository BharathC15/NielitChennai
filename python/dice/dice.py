import numpy as np
trials=10_00_000
dice=int(input("Enter the no of dices :"))
for i in np.arange(dice*6 + 1):
    found=0
    for _ in np.arange(trials):
        total=0
        for _ in np.arange(dice):
            total+=np.random.randint(7)
        if(total==i):
            found+=1
    print("Sum Value :",i,"probability",np.round((found/trials)*100,4),"%")
