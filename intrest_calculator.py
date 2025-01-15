def main():
    print("Welcome to the Monthly Loan Payment Calculator!")
    print("=" * 40)

    # Input: Loan amount, interest rate, and loan duration
    try:
        principal = float(input("Enter the loan amount (principal): "))
        apr = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the loan term (in years): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Calculations: Monthly interest rate, number of months, and monthly payment
    monthly_interest_rate = apr / 1200
    number_of_months = years * 12
    try:
        monthly_payment = principal * monthly_interest_rate / (
            1 - (1 + monthly_interest_rate) ** -number_of_months
        )
    except ZeroDivisionError:
        print("The annual interest rate cannot be zero.")
        return

    # Output: Monthly payment amount
    print("\nCalculation Results:")
    print(f"Loan Amount: ${principal:,.2f}")
    print(f"Annual Interest Rate: {apr:.2f}%")
    print(f"Loan Term: {years} years")
    print(f"Monthly Payment: ${monthly_payment:,.2f}")

    print("=" * 40)


if __name__ == "__main__":
    main()
