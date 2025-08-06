import random

# Generate a random number between 1 and 100
secret_num = random.randint(1, 100)

print("Welcome to the BRAND Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Loop until the user guesses the number
while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_num:
        print("Too low! Try again.")
    elif guess > secret_num:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_num} correctly.")
        break
