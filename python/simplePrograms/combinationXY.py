#Python program to find all combinations of two list

x=[1,2,3,4,5]
y=["a","b","c"]

for i in x:
    for j in y:
        print(i,j)

print([(i,j) for i in x for j in y])