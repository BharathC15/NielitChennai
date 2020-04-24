#Python program to find pythogeran triplets till n numbers
# A Pythagorean triplet is a set of three positive integers a, b and c
# such that a2 + b2 = c2

import numpy as np

num = int(input("Enter the Highest number:")) + 1

for a,b,c in [(x,y,z) for x in range(1,num) for y in range(1,num) for z in range(1,num)]:
    if( a**2 + b**2 == c**2):
        print(a,b,c)