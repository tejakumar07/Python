"""
In this Program we are Creating our own Even or Odd Function
This code was written in 17th April 2024 @9:35
"""

def main():

    x = int(input("What's X?"))
    if is_even(x):
        print("Even Number")
    else:
        print("Odd Number")
def is_even(n):
    if n%2==0:
        return True
    else:
        return False

main()

"""
We can Make is_even function more easily
by
is_even(n):
   return True if n%2==0 else False
   
we can also use another method 
def is_even(n):
   return n%2==0
here It returns only 2 Boolean Values either True or False

"""