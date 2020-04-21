# Increase the precision of float value
'''
It happens because it is the way the underlying c platform handles floating-point numbers and ultimately with the inaccuracy.

Note that this is in the very nature of binary floating-point: this is not a bug either in Python or C, and it is not a bug in your code either. 
You’ll see the same kind of behaviors in all languages that support our hardware’s floating-point arithmetic although some languages may not display the difference by default, or in all output modes). 
We have to consider this behavior when we do care about math problems with needs exact precisions or using it inside conditional statements.

https://docs.python.org/3/tutorial/floatingpoint.html
Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine.
String formatting to produce a limited number of significant digits:
'''
a=2.0
b=1.832
c=a-b
print("{} - {} = {}".format(a,b,c))

#String Formatting
print(format(c, '.3g'))  # give 3 significant digits)
print(format(c, '.2f'))  # give 2 digits after the point
print(repr(c)) #Higher Precise value. Choose the one with 17 significant digits