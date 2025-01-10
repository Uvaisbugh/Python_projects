import re

def check_password_strength(password):
    # Check if password is at least 8 characters long
    strength = 0
    if len(password) >= 8:
        strength += 1
    # Check if password contains at least one uppercase letter
    if re.search(r"[A-Z]", password):
        strength += 1
    # Check if password contains at least one lowercase letter
    if re.search(r"[a-z]", password):
        strength += 1
    # Check if password contains at least one digit
    if re.search(r"\d", password):
        strength += 1
    # Check if password contains at least one special character
    if re.search(r"[!@#$%^&*]", password):
        strength += 1
    return strength

# Test the function
password = "Password123!"
print(check_password_strength(password)) 

    