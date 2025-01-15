def email_slicer():
    print("Welcome to the Email Slicer!")
    print("----------------------------")
    
    # Get email input from the user
    email_input = input("Enter your email address (or type 'exit' to quit): ").strip()
    
    # Allow the user to exit the loop
    if email_input.lower() == 'exit':
        print("Thank you for using the Email Slicer. Goodbye!")
        return False

    try:
        # Split email into username and domain
        username, domain = email_input.split("@")
        # Further split the domain into domain name and extension
        domain_name, extension = domain.split(".")
        
        # Display results
        print("\n--- Email Details ---")
        print(f"Username  : {username}")
        print(f"Domain    : {domain_name}")
        print(f"Extension : {extension}\n")
    except ValueError:
        print("\nInvalid email format. Please enter a valid email address.\n")
    
    return True


def main():
    while True:
        if not email_slicer():
            break


if __name__ == "__main__":
    main()
