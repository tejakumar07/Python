#here we are using anoter library called JSON
#official URL: docs.python.org/3/library/json.html
#JSON comes with Py non need to install once again.

import json

import requests

import sys

if len(sys.argv)!=2:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])

print(json.dumps(response.json(),indent=2))
