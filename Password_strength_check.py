import re
# Function to check password strength

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
def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    
    # examine the strength of the password
    if strength == 5:
        print("Password is very strong !")
    elif strength == 4:
        print("Password is strong !")
    elif strength >= 3:
        print("Password is medium !")
    elif strength >= 2:
        print("Password is weak !")
    else:
        print("Password is very weak !")
        
if __name__ == "__main__":
    main()
    

    