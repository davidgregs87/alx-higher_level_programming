#!/usr/bin/python3
"""A script to print all commit on a github repo
print only 10 commits"""

import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    paginate = {'per_page': 10}
    req = requests.get(url, params=paginate)
    if req.status_code == 200:
        r = req.json()
        for commits in r:
            print("{}: {}".format(commits["sha"],
                                  commits["commit"]["author"]["name"]))
    else:
        pass
