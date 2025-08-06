import re

def password_strength_checker(password):
    strength = 0
    sug = []

    if len(password) >= 8:
        strength += 1
    else:
        sug.append("Use at least 8 characters.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        sug.append("Add an uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        sug.append("Add a lowercase letter.")

    if re.search(r'\d', password):
        strength += 1
    else:
        sug.append("Add a number.")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        strength += 1
    else:
        sug.append("Add a special character.")

    if strength == 5:
        print("Strong Password")
    elif strength >= 3:
        print("Moderate Password")
    else:
        print("Weak Password")

    for tip in sug:
        print(" -", tip)

# Run it
user_password = input("Enter a password: ")
password_strength_checker(user_password)
