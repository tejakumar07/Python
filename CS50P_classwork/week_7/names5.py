"""
In this program we try to read the data from the files
as before we used to write data from the file
"""

with open("files.txt","r") as files:
    lines = files.readlines()

for line in lines:
    print(line)