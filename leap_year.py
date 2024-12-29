# Description: This program checks if a given year is a leap year or not.
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

input_year = int(input("Enter a year: "))
if is_leap(input_year):
    print(f"{input_year} is a leap year")
else:
    print(f"{input_year} is not a leap year")

