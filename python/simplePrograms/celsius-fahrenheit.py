# Python program to convert Celsius to Fahrenheit
# celsius * 1.8 = fahrenheit - 32

celsius=float(input("Enter a celsius value :"))
print("The Fahrenheit value is ",format((celsius*1.8)+32,'.2f'))

fahrenheit=float(input("Enter a fahrenheit value :"))
print("The Celsius value is ",format((fahrenheit-32)/1.8,'.2f'))