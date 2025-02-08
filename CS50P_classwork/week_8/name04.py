import re
name = input('Name: ').strip()

if matches := re.search(r'(.+), *(.+)$',name,re.IGNORECASE):
    name = matches.group(2) + " "+ matches.group(1)
# Volvarous Operator
print(f'Hello, {name}')