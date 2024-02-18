"""
In this, ProtoType  We are going to create 
our own is_even() method it can also furtherly
used in further programs

"""
def main() :
    x = int(input("What's X ?"))
    if is_even(x):
        print("Even")
    else:
        print("odd")
def is_even(n):

    return n % 2 == 0

# What is Happed Here is if the condition is true It will return True (or) False
 


#    return True if n % 2 == 0 else False

    """"
       In this way also we can do

    if n % 2 == 0:
        return True
    else :
        return False
    """
main()  

    