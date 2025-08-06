def mail(email):
    if "@" not in email:
        return False
    username, domain = email.split("@", 1)
    
    # Check if both parts are non-empty
    if not username or not domain:
        return False
    
    # Domain must have at least one dot and not end/start with a dot
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False
    
    return True

# Get user input
email_input = input("Enter an email address to validate: ")

if mail(email_input):
    print("Valid email address.")
else:
    print("Invalid email address.")
