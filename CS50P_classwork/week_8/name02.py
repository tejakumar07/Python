import re

name = input('Name: ').strip()
matches = re.search(r'^(.+), (.+)$',name,re.IGNORECASE)
if matches:
    last, first = matches.groups()
    name = f'{first} {last}'
    # This is similar
    # name = matches.group(2)+ " "+ matches.group(1)
print(f"hello, {name}")