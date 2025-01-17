"""
docs.python.org/3/library/sys.html
sys.argv -->Argument Vector
"""
import sys

print("hello, my name is",sys.argv[1]) #Here i am execting with 'python libraries8.py teja kumar' in terminal

#here sys.argv[1]  will store 'teja' and sys.argv[0] will store the file name i.e libraries8

print("bye, ",sys.argv[2])#It will return Kumar

#We we are not giving any argument vector it will return IndexError