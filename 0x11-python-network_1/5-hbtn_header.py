#!/usr/bin/python3
"""Retrieve the X-Request-Id of the url passed on the command
line"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    body = requests.get(url)
    body_res = body.headers['X-Request-Id']
    print(body_res)
