while True:
    try:
        x = int(input("What's X?"))
        break
    except ValueError:
        print("Please enter a number")
        #we don't need continue keyword

print(f"You entered {x}")

