import re

url = input("URL: ").strip()

username = re.sub(r"^(htpps?://)?(www\.)?x\.com/","",url)
print(f'Username: {username}')