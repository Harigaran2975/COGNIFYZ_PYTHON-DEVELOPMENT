def cel_to_far(cel):
    return (cel * 9/5) + 32

def far_to_cel(far):
    return (far - 32) * 5/9

# Get temperature input from user
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

if unit == "C":
    converted = cel_to_far(temp)
    print(f"{temp}°C is equal to {converted:.2f}°F")
elif unit == "F":
    converted = far_to_cel(temp)
    print(f"{temp}°F is equal to {converted:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
