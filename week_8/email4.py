# docs.python.org/3/library/re.html
# Official documentation for Regular Expressions
import re

email = input().strip()
#username,domain = email.split()

if re.search("@",email):
    print("Valid")
else:
    print("Invalid")