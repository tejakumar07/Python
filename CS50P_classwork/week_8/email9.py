import re

email = input("Email: ").strip().lower()

if re.search(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$',email):
    print("Valid")
else:
    print("Invalid")