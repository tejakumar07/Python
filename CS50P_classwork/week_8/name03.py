import re

name = input("Name: ").strip()

matches = re.search(r'^(.+), *(.+)$',name,re.IGNORECASE)

if matches:
    name = matches.group(2)+ " " + matches.group(1)
print(f'hello, {name}')