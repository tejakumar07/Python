"""
When we forgot to close the file it will create problems depending upon the code 
we don't need to close the file there is an another approach to open the file it will
automatically close the file. For this we use a keyword called 'with'
"""

name = input("What is Your name? ")

with open("names4.txt","a") as file:
    file.write(f"{name}\n")