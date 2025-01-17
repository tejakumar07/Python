def main():
    number=get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter a number: "))

        if n > 0:
            return n #here it will return n value and also break form the loop

    #return n  if we use break keyword

def meow(number):
    for i in range(number):
        print("meow")
   

main()