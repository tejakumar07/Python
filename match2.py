"""
This is another version for match1.py
"""
name = input("What is your name?").title()

match name:
    case "Harry"|"Hermione"|"Ron"|"Teja":        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")       