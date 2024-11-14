while True:
    try:
        x = int(input("What's X?"))
    except ValueError:
        print("Please enter a number")
        #we don't need continue keyword
    else:
        break
print(f"You entered {x}")

