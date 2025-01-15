import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    criteria = {
        "Length (at least 8 characters)": len(password) >= 8,
        "Uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase letter": bool(re.search(r"[a-z]", password)),
        "Digit": bool(re.search(r"\d", password)),
        "Special character": bool(re.search(r"[!@#$%^&*]", password))
    }
    
    # Evaluate strength based on the criteria
    for criterion, meets_criteria in criteria.items():
        if meets_criteria:
            strength += 1
        else:
            print(f"Password is missing: {criterion}")

    return strength

# Test the function
def main():
    password = input("Enter your password: ")
    
    # Check password strength
    strength = check_password_strength(password)
    
    # Examine the strength of the password
    if strength == 5:
        print("Password is very strong!")
    elif strength == 4:
        print("Password is strong!")
    elif strength >= 3:
        print("Password is medium!")
    elif strength >= 2:
        print("Password is weak!")
    else:
        print("Password is very weak!")

if __name__ == "__main__":
    main()
