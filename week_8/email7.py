import re

'''
^    -      matches the start of the string

$    -     matches the end of the string or just 
           the new line at the end of the string
'''

email = input("Email: ").strip()
print(f'the entered email is: {email}')

if re.search(r"^.+@.+\.edu$",email): # .+@.+ ==> ..*@..*
    print('Valid')
else:
    print('Invalid')

