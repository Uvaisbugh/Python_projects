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
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def days_in_month(year, month):
    """
    Returns the number of days in a given month of a specific year.
    
    Args:
    year (int): The year to check (for leap year determination).
    month (int): The month to check (1 for January, 12 for December).
    
    Returns:
    int: The number of days in the specified month.
    """
    # Days in each month for a non-leap year
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust February days if it's a leap year
    if is_leap(year):
        month_days[1] = 29

    # Return the number of days for the specified month
    return month_days[month - 1]

def main():
    print("Days in Month Checker")
    print("=" * 30)
    
    try:
        year = int(input("Enter a year: "))
        month = int(input("Enter a month (1-12): "))
        
        # Validate month input
        if month < 1 or month > 12:
            print("Invalid month! Please enter a number between 1 and 12.")
        else:
            days = days_in_month(year, month)
            print(f"The number of days in month {month}, year {year} is: {days}")
    except ValueError:
        print("Invalid input! Please enter valid integers for year and month.")

if __name__ == "__main__":
    main()
