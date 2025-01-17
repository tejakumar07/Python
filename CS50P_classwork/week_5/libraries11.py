"""
sys.exit will exit the program with an error message
"""
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")  #It will automatically exit the program without checking any other condition

if len(sys.argv) > 2:
    sys.exit("Too many arguments")

else:
    print("hello, ",sys.argv[1])
