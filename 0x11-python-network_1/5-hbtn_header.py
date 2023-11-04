#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if __name__ == "__main__":

    if sys.argv[1]:
        r = requests.get(sys.argv[1])
        print(r.headers.get('X-Request-Id'))
