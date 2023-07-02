#!/usr/bin/python3
"""A script to post an email to a url
using the requests package"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    body = requests.post(url, data={'email': email})
    print(body.text)
