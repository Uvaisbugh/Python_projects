import random
import string

def password_gen(length):
    """
    Generates a random password with the specified length, 
    including uppercase, lowercase, digits, and special characters.
    
    Args:
    length (int): Length of the password.
    
    Returns:
    str: The generated random password.
    """
    # Define the character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lower_case + upper_case + digits + special_characters

    # Ensure the password is not empty and the length is valid
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")

    # Generate a random password by selecting from the combined character set
    password = random.choices(all_characters, k=length)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# Example usage: Generate a random password of length 20
print(password_gen(20))
