#!/usr/bin/python3
"""A script to post an email to a url"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data=encoded_data, method='POST')
    with urllib.request.urlopen(request) as response:
        html = response.read().decode('utf-8')
        print(html)
