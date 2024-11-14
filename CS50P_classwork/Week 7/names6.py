with open("names4.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ",line)

#Here we got a bug over here i.e.
"""
Suppose the file contain
TEJA
KUMAR
APPLE
then output looks like
hello, TEJA

hello, KUMAR

hello, APPLE
"""
#Here the O/P looks like ugly lets fix this