import string
import random

alphabet = string.ascii_letters

numbers = [0,1,2,3,4,5,6,7,8,9]

symbols = list(set(string.printable) - set(alphabet) - set(numbers))

print("Welcome to the PyPassword Generator!")
letter_count = int(input("How many letters would you like in your password? \n"))
symbol_count = int(input("How many symbols would you like in your password? \n"))
number_count = int(input("How many numbers would you like in your password? \n"))

password = []

for i in range(0,letter_count):
    password.append(random.choice(alphabet))

for i in range(0,symbol_count):
    password.append(random.choice(symbols))

for i in range(0,number_count):
    password.append(random.choice(numbers))

print(password)
random.shuffle(password)
print(password)

password = ''.join([str(s) for s in password])
print(f"Your password is: {password}")