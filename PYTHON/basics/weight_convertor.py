weight = float(input("Enter your weight: "))
unit = input("Is this weight in (K)g or (L)bs? ").upper()
if unit.upper() == 'K':
    converted = weight / 0.45
    print(f"You are {converted} Lbs")
elif unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} Kgs")
else:
    print("Invalid unit, please enter 'K' for Kilograms or 'L' for Pounds.")