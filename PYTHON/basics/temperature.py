#temperature conversion
temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in (C)elsius or (F)ahrenheit? ").upper()
if unit == 'C':
    converted = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is {converted}°F")
elif unit == 'F':
    converted = (temp - 32) * 5/9
    print(f"The temperature in Celsius is {converted}°C")
else:
    print("Invalid unit, please enter 'C' for Celsius or 'F' for Fahrenheit.")
    