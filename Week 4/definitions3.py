def main():
    x = get_int("What's X?")
    print(f"You Entered Number is {x}")
def get_int(promot):
    while True:
            try:
                return int(input(promot))
            except ValueError:
                pass #Here Pass is the keyword It will just pass the Value without saying anything to the user


main()