# Python Program to count the number of vowels in a string

t=input("Enter a string:").lower()
vowels=["a","e","i","o","u"]
count=0
for i in t:
    for j in vowels:
        if i==j:
            count=count+1
print("Number of vowel are ",count)