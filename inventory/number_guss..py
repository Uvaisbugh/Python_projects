import random

try:
    minimum_value = int(input("Specify the minimum : "))
    maximum_value = int(input("maximum value : "))
    number = random.randint(minimum_value, maximum_value)
    attempt = 1

    while True:

        x_try = int(input(f"Guss the number (between {minimum_value} and {maximum_value}): "))
        attempt += 1

        if x_try < number:
            print("Too low ! \nTry again")

        elif x_try > number:
            print("Too high ! \nTry again")

        elif x_try == number:
            print(f"Congratulation! you guessed number in {attempt} attempts.")
        else:
            print("Invalid ")
except ValueError:
    print('Please enter a valid number')
