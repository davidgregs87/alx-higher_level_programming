#!/usr/bin/python3
"""Using github api to authenticate with my username
and password to retrieve my github id"""

import requests
import sys
from requests.auth import HTTPBasicAuth
if __name__ == '__main__':
    uname = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'

    req = requests.get(url, auth=HTTPBasicAuth(uname, passwd))
    if req.status_code == 200:
        r = req.json()
        print("{}".format(r.get('id')))
    else:
        print("None")
