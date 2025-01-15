# Description: This program checks if a given year is a leap year or not.

def is_leap(year):
    """
    Determines if a year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is not divisible by 100, unless it is also divisible by 400.

    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:  # Year must be divisible by 4
        if year % 100 == 0:  # If divisible by 100, check divisibility by 400
            return year % 400 == 0
        return True
    return False

def main():
    print("Leap Year Checker")
    print("=" * 20)
    
    try:
        input_year = int(input("Enter a year: "))
        if is_leap(input_year):
            print(f"{input_year} is a leap year.")
        else:
            print(f"{input_year} is not a leap year.")
    except ValueError:
        print("Invalid input! Please enter a valid year.")

if __name__ == "__main__":
    main()
