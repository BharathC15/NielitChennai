import numpy as np
trials=10000
sizes=int(input("Enter the no of dices :"))
for j in np.arange(sizes*6+1):
    found=0
    for i in np.arange(trials):
        n=np.sum(np.random.randint(7,size=sizes))
        if(n==j):
            found+=1
    print("Sum Value :",j,"probability",(found/trials)*100,"%")
