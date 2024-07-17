name = input("What is Your name? ").title()

match name:
    case "Harry"| "Hermione" | "Ron"| "Teja":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")  #This case_: will executed if none of name is matched

print("End of Program")