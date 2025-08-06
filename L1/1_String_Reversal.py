def rev(ip_str):
    return ip_str[::-1]

# Get input from the user
user_ip = input("Enter a string to reverse: ")
rev_str = rev(user_ip)

print("Reversed string:", rev_str)
