"""
go to the URL:https://itunes.apple.com/search?entity=song&limit=1&term=weezer
"""
#here limit is 1 that is we are searching 1 song and term means artist we are searching
#When we visit the website, you will observe that it will automatically you will automatically download JSON file
#JSON Stands for Java Script Object Notation

import requests

import sys

if len(sys.argv)!=2:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])

print(response.json())
