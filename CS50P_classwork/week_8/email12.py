import re
'''

re.IGNORECASE
re.MULTILINE
re.DOTALL
re.search(pattern,string,flags=0)

'''
email = input("Email: ").strip()

if re.search(r"^\w+@\w+\.edu$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
# This can be Break
# test@harvard.cs50.edu