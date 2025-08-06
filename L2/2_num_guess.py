import random

print("Welcome to the Number Guesser Game!")

# Ask user to set the range
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Generate random number within the range
sec_num = random.randint(lower, upper)

print(f"I'm thinking of a number between {lower} and {upper}.")

# Start guessing loop
while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < lower or guess > upper:
            print(f"Please guess a number within the range {lower} to {upper}.")
        elif guess < sec_num:
            print("Too low! Try again.")
        elif guess > sec_num:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {sec_num}.")
            break
    except ValueError:
        print("Please enter a valid integer.")
