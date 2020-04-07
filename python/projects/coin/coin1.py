import numpy as np
trials=10000
sizes=int(input("Enter the no of flips"))
for j in np.arange(sizes+1):
    found=0
    for i in np.arange(trials):
        n=np.sum(np.random.randint(2,size=sizes))
        if(n==j):
            found+=1
    print("Heads :",j,"probability",found/trials,"\n")
