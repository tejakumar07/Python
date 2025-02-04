# Checking the .edu mail
import re
email = input('Email: ').strip()

if re.search(r".+@.+\.edu",email): #r / will match the particular sequences
    print("Valid")
else:
    print("Invalid")

# My Email is test@harvard.edu.