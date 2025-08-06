# Simple calculator program

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %): ")

if op == "+":
    print("res:", n1 + n2)
elif op == "-":
    print("res:", n1 - n2)
elif op == "*":
    print("res:", n1 * n2)
elif op == "/":
    if n2 != 0:
        print("res:", n1 / n2)
    else:
        print("Error: Cannot divide by zero.")
elif op == "%":
    if n2 != 0:
        print("res:", n1 % n2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator.")
