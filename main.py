# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""
#
# for num in range(nr_letters):
#     password += random.choice(letters)
#
# for num in range(nr_symbols):
#     password += random.choice(symbols)
#
# for num in range(nr_numbers):
#     password += random.choice(numbers)
#


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
new_password = []

for num in range(nr_letters):
    new_password += random.choice(letters)

for num in range(nr_symbols):
    new_password += random.choice(symbols)

for num in range(nr_numbers):
    new_password += random.choice(numbers)

random.shuffle(new_password)
new_password = ''.join(new_password)

print(f"Your password is: {new_password}")
