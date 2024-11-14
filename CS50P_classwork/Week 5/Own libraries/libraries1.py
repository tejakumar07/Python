import sys
from libraries import hello

if len(sys.argv)!=2:
    sys.exit()

hello(sys.argv[1])
goodbye(sys.argv[1])