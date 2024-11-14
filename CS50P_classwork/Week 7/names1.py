"""
In last program we see that we have taken the names from the user and save the names in the list
In this program we try to save there names programmatically By using the function called open()
the official documentation is available at https://docs.python.org/3/library/functions.html#open
"""

name = input("What is Your Name? ")

file = open("names.txt","w")

file.write(name)

file.close()

#There is a bug in this program that is
"""
When I am running this It succesfully saving my name in name.txt we I try to re run the program
the name i saved previously in names.txt It is replacing with first name
"""

#here the problem occours from "w" everytime i try to run the same program it will recreating the file so let's fix this