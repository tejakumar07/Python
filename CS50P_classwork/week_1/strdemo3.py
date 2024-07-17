"""
This code is written in 07-04-2024 @16:52
This is my 8th  code 
#"docs.python.org/3/library/functions.html#string-methods"
"""

name = input("What is your name? ")

first ,middle, last = name.split()

print(f"hello, {first}")

print(f"Your Middle name is {middle}")

print(f"Bye, {last}")