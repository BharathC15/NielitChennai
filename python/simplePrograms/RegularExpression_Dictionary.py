
import re

corona_people = 'Maharashtra 1100 Delhi 3300 Gujarat 4500 TamilNadu 7500'
print(corona_people)

number=re.findall(r'\d{3,}',corona_people)
print('the index is ', number[0],number[1],number[2],number[3])
print('Extracting only numbers', number)

state = re.findall(r'[a-zA-Z][a-zA-Z]\w*', corona_people)
print('the states are : ', state)


dict_corona ={}
print('the dict corona is ', dict_corona)

index=0

for eachstate in state:
    print('the value of index is', index)
    print('State value is: ', eachstate)
    dict_corona[eachstate] = number[index]
    index+=1

print('the dictionary for the corona is ',dict_corona)

x=input("Enter a State name :")
if dict_corona.get(x):
    print("The {} state has {} infected people".format(x,dict_corona.get(x)))
else:
    print("The {} state is not in the database".format(x))