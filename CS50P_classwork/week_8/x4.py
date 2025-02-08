import re

url = input('URL: ').strip()

matches = re.search(r"^(https?://)?(www\.)?x\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print(f"Username: {matches.group(3)}")
else:
    print("Invalid URL or username not found.")
