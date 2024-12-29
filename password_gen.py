#random password generator
import random
import string

def password_gen(l):
    password = []
    for _ in range(l):
        password.append(random.choice(string.ascii_letters))
    return ''.join(password)    

print(password_gen(20))