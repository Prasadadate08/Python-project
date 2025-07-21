# This is simple program that generates password based on input by user
# This takes number of times input and number of length input for password

import string
import random

lowercase = string.ascii_lowercase      # 'abcdefghijklmnopqrstuvwxyz'
uppercase = string.ascii_uppercase      # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = string.digits                  # '0123456789'
special_chars = string.punctuation      # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

characters = lowercase + uppercase + digits + special_chars

print("Welcome to password generator \n")

number = input("Enter a number to generate password at that times: ")
number = int(number)

length = input("Enter a number to generate password of that length: ")
length = int(length)
print("\nHere is your passwords")

for i in range(number):
    password = ''
    for c in range(length):
        password += random.choice(characters)
    print("".join(password))
    