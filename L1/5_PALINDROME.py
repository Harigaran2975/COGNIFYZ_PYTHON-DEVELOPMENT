def palindrome(s):
    return s == s[::-1]

# Get input from user
text = input("Enter a string to check for palindrome: ")

if palindrome(text):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
