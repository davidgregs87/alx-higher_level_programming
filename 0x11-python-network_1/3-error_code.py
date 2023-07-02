#!/usr/bin/python3
"""A script that print the error code of a url"""
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
