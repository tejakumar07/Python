import re

email = input('Email: ').strip()

# Most of the Browers will use this it will not fix all atleast some of them
pattern = r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~\-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'

if re.search(pattern, email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')
