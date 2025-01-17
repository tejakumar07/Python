def main():
    hello("World")
    goodbye("world")

def hello(name):
    print(f"Hello {name}")
def goodbye(name):
    print(f"Good bye, {name}")

#main()  when we declare this it will call both hello function and goodbye function bcoz lastlt
#there both are in main function
#When we declare in this format it will call only specfic function

if __name__ == "__main__":
    main()