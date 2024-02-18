"""
This is another ProtoType for
loopsdemo5.py 
"""
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's the n?"))
        if n <= 0:
            continue
        else:
            break
    return n

def meow(number):
    for _ in range(number):
        print("meow")

main()




