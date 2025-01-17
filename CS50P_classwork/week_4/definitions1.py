def main():
    print("The Entered Number is:",get_int())
def get_int():
    while True:
            try:
                return int(input("What's X?"))
            except ValueError:
                print("Please enter a number")


main()