# Python Program to count the number of vowels in a string
#[Better Way]

t=input("Enter a string:")
vowels=["a","e","i","o","u"]
count=0

for i in t.lower():
    if i in vowels:
        count=count+1
print("Number of vowels in \"{}\" are {}".format(t,count))