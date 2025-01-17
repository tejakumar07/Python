with open("names4.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,",line.rstrip()) #It will fix the bug

#Or we can use

"""
 print("hello,",line,end="")
"""