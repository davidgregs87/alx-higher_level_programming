#!/usr/bin/python3
"""Search for a letter by using a POST request
then print the result in a formatted way like
this [<id>] <name>"""

import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ''
    res = requests.post(url, data={'q': letter})
    try:
        r = res.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get('id'), r.get('name')))
    except ValueError:
        print("Not a valid JSON")
