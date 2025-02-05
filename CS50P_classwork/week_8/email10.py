import re
'''
\d  decimal digit
\D  not an decimal Digit
\s  white space characters
\S  not a white space characters
\w  word character ... as well as numbers and underscore
\W  not an word character
'''
email = input('Email: ').strip().lower()

if re.search(r'^\w+@\w+\.edu$',email):   # r'^\w+@\w+\.edu$',email == r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$'
    print('Valid')
else:
    print('Invalid')