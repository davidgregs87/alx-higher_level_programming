#!/usr/bin/python3
"""A script to retrieve the status code if the code
is >= 400"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    body = requests.get(url)
    err_code = body.status_code
    if err_code >= 400:
        print("Error code: {}".format(err_code))
    else:
        print(body.text)
