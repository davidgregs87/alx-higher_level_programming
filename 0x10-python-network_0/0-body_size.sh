#!/bin/bash
# A bash script to print the content length of a body of a server response
curl -sI "$1" | awk '/Content-Length/ {print $2}'
