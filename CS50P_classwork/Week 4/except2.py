try:
    x = int(input("What's X?"))
    print(f"The value of X is {x}")
except ValueError: #If the user Enter anything other than Integer
    print("Oops! Something went wrong.")
    print("X is not an integer")
    print("Try again.")
