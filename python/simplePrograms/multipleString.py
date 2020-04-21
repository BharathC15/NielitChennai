#Python program to accept Multiple Strings and display them

text=input("Enter multiple string with space delimiter:").split()
i=1
for j in text:
    print("word {} is {}".format(i,j))
    i+=1