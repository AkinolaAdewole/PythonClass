# Prompt the user to input their weight and convert the input to a floating-point number.
weight = float(input("Input your weight: "))

# Prompt the user to input the unit of their weight (either 'K' for kilograms or 'L' for pounds).
unit = input("Enter unit (K for kilograms, L for pounds): ")

# Check if the entered unit (converted to uppercase) is 'K' (Kilograms).
if unit.upper() == 'K':
    # If the unit is 'K', simply print the weight with 'K' appended (since the user entered the weight in kilograms).
    print(f"Weight in kg: {weight}K")

# Check if the entered unit (converted to uppercase) is 'L' (Pounds).
elif unit.upper() == 'L':
    # If the unit is 'L', convert the weight from pounds to kilograms using the conversion factor (1 pound = 0.453592 kg).
    weight_kg = weight * 0.453592
    # Print the converted weight in kilograms.
    print(f"Weight in kg: {weight_kg}K")

# If the entered unit is neither 'K' nor 'L', handle it by printing an error message.
else:
    print("Invalid command")
