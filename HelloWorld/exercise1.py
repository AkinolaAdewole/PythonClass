weight = float(input("Input your weight: "))
unit = input("Enter unit (K for kilograms, L for pounds): ")

if unit.upper() == 'K':
    print(f"Weight in kg: {weight}K")
elif unit.upper() == 'L':
    weight_kg = weight * 0.453592
    print(f"Weight in kg: {weight_kg}K")
else:
    print("Invalid command")


