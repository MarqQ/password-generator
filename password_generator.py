"""
This program create a password with random positions until 94 characters
"""

import random
import string

print("Welcome")

password_lenght = int(input("\nEnter the lenght of password: "))

lower_char = string.ascii_lowercase
upper_char = string.ascii_uppercase
number_char = string.digits
symbol_char = string.punctuation

mixing = lower_char + upper_char + number_char + symbol_char

temp = random.sample(mixing, password_lenght)

password = "".join(temp)

print(f"The password is: {password}")
