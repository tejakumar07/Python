def main():
    name = get_name()
    house = get_house()
    print(f'{name} form {house}')
def get_name():
    return input("name: ")
def get_house():
    return input("house: ")
if __name__ == "__main__":
    main()