import re

class PasswordChecker:
    def check_password_strength(self, password):
        strength = 0
        criteria = {
            "Length (at least 8 characters)": len(password) >= 8,
            "Uppercase letter": bool(re.search(r"[A-Z]", password)),
            "Lowercase letter": bool(re.search(r"[a-z]", password)),
            "Digit": bool(re.search(r"\d", password)),
            "Special character": bool(re.search(r"[!@#$%^&*]", password))
        }
        
        for criterion, meets_criteria in criteria.items():
            if meets_criteria:
                strength += 1
            else:
                print(f"Password is missing: {criterion}")
        
        return strength 
    
    def main(self):
        password = input("Enter your password: ")
        strength = self.check_password_strength(password)
        
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
            
        return strength 

if __name__ == "__main__": 
    checker = PasswordChecker()
    checker.main()