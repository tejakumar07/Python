import re
'''
[] set of characters
[^] complementing the set
'''

email = input("Email: ").strip().lower()

if re.search(r"^[^@]+@[^@]+\.edu$",email):
    print("Valid")
else:
    print("Invalid")