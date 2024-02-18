"""
This code is Written in 18th feb,2024
on 10:53 PM this is 5th program...
This is about another version of  mario4.py
"""

def main():

    print_square(3)


def print_square(size):

    for _ in range(size):

        print_row(size)

def print_row(width):

    print("#"*width)



main()

