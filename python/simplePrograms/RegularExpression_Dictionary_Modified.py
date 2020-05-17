corona_people = 'Maharashtra 1100 Delhi 3300 Gujarat 4500 TamilNadu 7500'
c=list(corona_people.split(" "))
corona_db={}
for i in range(0,len(c),2):
    corona_db[c[i]]=c[i+1]
print("Corona Database:",corona_db)

x=input("Enter a State name :")
if corona_db.get(x):
    print("The {} state has {} infected people".format(x,corona_db.get(x)))
else:
    print("The {} state is not in the database".format(x))