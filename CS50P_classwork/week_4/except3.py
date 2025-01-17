try:
    x = int(input("What's X?"))
except ValueError: #If the user Enter anything other than Integer
    print("Oops! Something went wrong.")
    print("X is not an integer")
    print("Try again.")
else:  #If the user entered an number then else block will be executed
    print(f"X is {x}")

"""
If we Don't declare else block and directly call the variable 'x'
If the User entered a number then the program looks perfect if the user entered not an Integer 
then It raises another exception called 'NameError'
why this happens is if it is not a Integer It will raise an exception called 'ValueError'
so the value of string is not copied from left to right so it variable x is cleared 
by ValueError
"""
