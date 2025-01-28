n= 8

for i in range(1,n+1):
    value = 2**(i-1)
    row = []
    for j in range(i):
        row.append(str(value))
        value //= 2
    print(" ".join(row))
    
    
print()
list=["apple","banana","cherry"]
newlist=[name.upper() for name in list]
print(newlist)

print()

def password_check(password):
    if len(password) < 8:
        return False
    if password.isalpha():
        return False
    if password.islower():
        return False
    if password.isdigit():
        return False
    return True

print(password_check("abc123"))

print()

#left triangle pascal pattern
rows = 5  # Number of rows for the pattern

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

print()

#right triangle pascal pattern
rows = 5  # Number of rows for the pattern  
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= rows - i:
            print(' ', end=' ')
        else:
            print(j, end=' ')
    print()
    
    
print()
char = 65
plus=0
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(char+plus),end=' ')
        plus+=1
        
    print()
    
print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(char+j-1),end=' ')
    print()
    
    
print()
noun= "Python_master".upper()
for i in range(8):
    for j in range(i+1):
        print(noun[j],end=' ')
    print()

print()

def pascal(n):
    for i in range(1,n+1):
        value = 2**(i-1)
        row = []
        for j in range(i):
            row.append(str(value))
            value //= 2
        print(" ".join(row))
        
pascal(8)

print()

def string_check(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return {"vowels": vowel_count, "consonants": consonant_count}

result = string_check("Python_master")
print(result)

print()
import random
def mini_number(l):
    return min(l)

print(mini_number([random.randint(1,100) for i in range(10)]))

print()

def upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return {"upper": upper_count, "lower": lower_count}

result = upper_lower("Python_master")
print(result)
print()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

print()

def prime_or_not(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(prime_or_not(13))

print()

def change_case(string):
    return string.swapcase()

print(change_case("Python_master"))

print()

def swap_values(a, b):
    a, b = b, a
    return a, b

print(swap_values(1,2))

print()

