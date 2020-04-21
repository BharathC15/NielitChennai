# Python program to print error if two words are not typed

text=input("Enter two words with a space in between :").split()
if (len(text) == 2):
    print("First word {}\nSecond Word {}".format(text[0],text[1]))
else:
    print("Error! Only two words are accepted")