"""
This code is written in 07-04-2024 @16:28
This is my 8th  code 
#"docs.python.org/3/library/functions.html#string-methods"
This is String(str) functions.
"""
name = input("What is your name?")

name=name.strip() #It will remove white spaces before left side and right side

print(f"hello, {name}")

name=name.capitalize()#It will Capitalize the Word by changing the first letter by Capital

print(f"hello {name}")

name = name.title()

print(f"hello {name}")