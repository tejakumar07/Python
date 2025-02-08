import re
url = input("URL: ").strip()
# re.sub(pattern, repl, string, count=0, flags=0)
username = re.sub(r'https://x.com/','',url)
print(f'Username: {username}')