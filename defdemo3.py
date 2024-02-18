"""
This is the updated prototype for 'intdemo2.py'
In this type we will find square of a number, but the catch is 
we are going to use square method which is not avalible in python
by default we are going to create it.
"""
def main():
    x = int(input("What's X? "))
    print("The Square of the 'X' is: ",square(x))
    print("This is the '2nd' type of square: ",square1(x))
    print("This is '3rd' type for square method: ",square2(x))
def square(n):
    return n*n
def square1(n):
    return pow(n,2)
def square2(n):
    return n**2

main()
