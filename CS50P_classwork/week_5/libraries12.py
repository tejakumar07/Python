import sys

if len(sys.argv)==1:
    sys.exit("Too few arguments...")

for args in sys.argv:
    print(args)

#As we see there is a bug in this program i.e suppose we executed this program as 'python libraries12.py teja kumar apple

#The Output is libraries12.py teja kumar apple

#We observe that file name is printting so the output looks like crictic