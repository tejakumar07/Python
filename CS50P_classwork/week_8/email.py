email = input("Email: ").strip()
print(f"Entered Email is: {email}")

if '@' in email:
    print("Valid")
else:
    print("Invalid")