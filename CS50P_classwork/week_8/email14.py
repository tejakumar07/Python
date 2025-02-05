import re
email = input('Email: ').strip()

if re.search(r'^\w+@(\w+\.)?\w+\.edu$',email,re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')
# This will work for both the cases 
# test@harvard.edu and test@harvard.cs50.edu
# ? this will allow the 0 or 1 repeatation(here subdomain)
# * we can use this for 0 or more subdomains