#We try to handle IndexError

import sys
try:
    print("hello, ",sys.argv[1])

except IndexError:
    print("too few arguments")
