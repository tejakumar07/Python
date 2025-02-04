email = input()
username,domain = email.split("@")

if username and '.' in domain:
    print("Valid")
else:
    print("Invalid")