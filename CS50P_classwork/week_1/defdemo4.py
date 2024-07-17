#Recall the defdemo2.py
#What is the user is not giving the name
"""
Make sure that the Def is declared first to 
Execute the program sucessfull
"""
def hello(to="world"):
    print("Hello, ",to)

hello()

name = input("What is Your name? ")

hello()
hello(name)