#Lets fix the bug in the last program
#We use a new concept called 'Slice'
import sys

if len(sys.argv)==1:
    sys.exit("Too few arguments...")

for args in sys.argv[1:]: #This Syntax is called Slice
    print("hello, ",args)
#We can also give sys.argv[1:2] It will print only in between
#We can also give sys.argv[1:-1] it will count form the other direction