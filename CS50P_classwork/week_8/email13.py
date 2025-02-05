import re
email = input('Email: ').strip()
if re.search(r'^\w+@\w+\.\w+\.edu$',email,re.IGNORECASE):
    print('valid')
else:
    print('invalid')
# This will break the test@harvard.edu
# and it will work for test@harvard.cs50.edu