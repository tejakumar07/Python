import re

email = input('Email: ').strip().lower()
'''
(A | B)  Either A or B
(...)    a group
(:?...)  non capturing version
'''
if re.search(r'^\w+@\w+\.(edu|com|gov|net)$',email):
    print('Valid')
else:
    print('Invalid')