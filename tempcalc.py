#ask user to input temp as integer
temp = float(input("Enter the temperature \n"))

#ask user to input unit of measure as string
unit = input("Celsius(C) or Fahrenheit(F)? \n")

#fahrenheit to celsius
celsius = (temp - 32) * 5/9

#celsius to fahrenheit
fahrenheit = (temp * 1.8) + 32

#convert temp to fahrenheit
F = celsius

#convert temp to celsius
C = fahrenheit

#print temp in C or F based on second user input

#casefold() on variable unit instead of user input
'''if unit.casefold() == "C":
    print(f"{temp}° Celsius is {C}° Fahrenheit")

elif unit.casefold() == "F":
    print(f"{temp}° Fahrenheit is {F}° Celsius")

else:
    print(f"Unsupported Unit of measurement '{unit}'")'''

#casefold() on user input instead of variable unit    
if unit == "C".casefold():
    print(f"{temp}° Celsius is {C}° Fahrenheit")

elif unit == "F".casefold():
    print(f"{temp}° Fahrenheit is {F}° Celsius")

else:
    print(f"Unsupported unit of measurement '{unit}'")

#eventually add support for other units of measurements such as kelvin(?)