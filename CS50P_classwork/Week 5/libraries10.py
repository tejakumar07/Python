#Lets try to add condition to the program

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) == 2:
    print("hello, ", sys.argv[1])
else:
    print("Too many arguments")