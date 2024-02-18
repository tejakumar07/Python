"""
This is another ProtoType for house1.py 
"""
name = input("What is your name?").title()

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Slytherin")
    case _:
        print("Who")            