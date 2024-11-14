def main():
    print("The Entered Number is:",get_int())
def get_int():
    while True:
            try:
                return int(input("What's X?"))
            except ValueError:
                pass #Here Pass is the keyword It will just pass the Value without saying anything to the user


main()