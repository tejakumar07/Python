"""
This code was written in 17th April 2024 @9:40
"""
name = input("What is Your name? ").title()

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")  #This case_: will executed if none of name is matched

print("End of Program")