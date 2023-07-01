#!/bin/bash
# A script that list all method available on a server
curl -sI "$1" | grep Allow | cut -d: -f2 | cut -c 2-
