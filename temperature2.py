#input temp in c
temp = float(input("Enter tempertature in Celsius: "))

#use decimal to convert c to f instead of fraction
fahrenheit = (temp * 1.8) + 32

#print conversion
print(f"{temp} in Celsius is equal to {fahrenheit} in Fahrenheit")