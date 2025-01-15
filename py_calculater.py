import math

# Define functions for operations
def add(x, y):
    return x + y

def subtract(x, y): 
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"  
    return x / y

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative numbers"
    return math.factorial(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def log(x):
    return math.log(x)

def ln(x):
    return math.log(x, math.e)

def exp(x):
    return math.exp(x)

def pi():
    return math.pi

def e():
    return math.e

def abs(x):
    return abs(x)

def ceil(x):
    return math.ceil(x)

def floor(x):
    return math.floor(x)

def trunc(x):
    return math.trunc(x)

def round(x):
    return round(x)

def max(x, y):
    return max(x, y)

def min(x, y):
    return min(x, y)

def gcd(x, y):
    return math.gcd(x, y)

def lcm(x, y):
    return math.lcm(x, y)

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Modulus")
    print("8. Factorial")
    print("9. Sin")
    print("10. Cos")
    print("11. Tan")
    print("12. Log")
    print("13. Ln")
    print("14. Exp")
    print("15. Pi")
    print("16. e")
    print("17. Abs")
    print("18. Ceil")
    print("19. Floor")
    print("20. Trunc")
    print("21. Round")
    print("22. Max")
    print("23. Min")
    print("24. GCD")
    print("25. LCM")
    print("26. Exit")

    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'):
        num1 = float(input("Enter first number: "))
        if choice not in ('5', '9', '10', '11', '12', '13', '14', '15', '16'):  # Skip num2 for functions that need only num1
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5': 
            print("Square root of", num1, "=", square_root(num1))

        elif choice == '6':
            print(num1, "^", num2, "=", power(num1, num2))

        elif choice == '7':
            print(num1, "%", num2, "=", modulus(num1, num2))

        elif choice == '8':
            print("Factorial of", num1, "=", factorial(num1))

        elif choice == '9':
            print("Sin of", num1, "=", sin(num1))

        elif choice == '10':
            print("Cos of", num1, "=", cos(num1))

        elif choice == '11':
            print("Tan of", num1, "=", tan(num1))

        elif choice == '12':
            print("Log of", num1, "=", log(num1))

        elif choice == '13':
            print("ln of", num1, "=", ln(num1))

        elif choice == '14':
            print("Exp of", num1, "=", exp(num1))

        elif choice == '15':
            print("Pi =", pi())

        elif choice == '16':
            print("e =", e())

        elif choice == '17':
            print("Abs of", num1, "=", abs(num1))

        elif choice == '18':
            print("Ceil of", num1, "=", ceil(num1))

        elif choice == '19':    
            print("Floor of", num1, "=", floor(num1))   

        elif choice == '20':
            print("Trunc of", num1, "=", trunc(num1))

        elif choice == '21':
            print("Round of", num1, "=", round(num1))

        elif choice == '22':
            print("Max of", num1, "and", num2, "=", max(num1, num2))

        elif choice == '23':
            print("Min of", num1, "and", num2, "=", min(num1, num2))

        elif choice == '24':
            print("GCD of", num1, "and", num2, "=", gcd(num1, num2))

        elif choice == '25':
            print("LCM of", num1, "and", num2, "=", lcm(num1, num2))    

    elif choice == '26':
        break  # Exit the program

    else:
        print("Invalid input! Please select a valid operation.")
