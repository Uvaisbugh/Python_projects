def Converter():
    """
    This function serves as a simple currency converter between USD, INR, and EUR.
    It allows the user to choose a conversion option from a menu and then 
    input an amount to convert. The function provides conversion rates for:
    1. USD to INR
    2. INR to USD
    3. USD to EUR
    4. EUR to USD
    5. INR to EUR
    6. EUR to INR

    The conversion is performed based on fixed rates:
    - 1 USD = 80 INR
    - 1 USD = 0.85 EUR

    After performing the conversion, the result is printed to the console. 
    If an invalid choice is entered, an error message is displayed.
    """

    print("Currency Converter")
    print("1. USD to INR")
    print("2. INR to USD")
    print("3. USD to EUR")
    print("4. EUR to USD")
    print("5. INR to EUR")
    print("6. EUR to INR")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        usd = float(input("Enter the amount in USD: "))
        inr = usd * 80
        print(f"{usd} USD is equal to {inr} INR")
    elif choice == 2:
        inr = float(input("Enter the amount in INR: "))
        usd = inr / 80
        print(f"{inr} INR is equal to {usd} USD")
    elif choice == 3:
        usd = float(input("Enter the amount in USD: "))
        eur = usd * 0.85    
        print(f"{usd} USD is equal to {eur} EUR")
    elif choice == 4:
        eur = float(input("Enter the amount in EUR: "))
        usd = eur / 0.85    
        print(f"{eur} EUR is equal to {usd} USD")
    elif choice == 5:
        inr = float(input("Enter the amount in INR: "))
        eur = inr / 80 * 0.85
        print(f"{inr} INR is equal to {eur} EUR")
    elif choice == 6:
        eur = float(input("Enter the amount in EUR: "))
        inr = eur / 0.85 * 80
        print(f"{eur} EUR is equal to {inr} INR")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.") 
        
        
Converter()