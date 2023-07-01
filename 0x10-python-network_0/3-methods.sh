#!/bin/bash
# A script that list all method available on a server
curl -sIX OPTIONS "$1" | awk '/Allow/ {print $2, $3, $4}'
