#In this let's try to print in reverse order 
"""
As per the official documentation for sorted technique

sorted(iterable, /, *, keyvalue, reverse=False)

"""
with open("names4.txt") as file:

    for line in sorted(file,reverse=True):
        print(f"hello, {line.rstrip()}")