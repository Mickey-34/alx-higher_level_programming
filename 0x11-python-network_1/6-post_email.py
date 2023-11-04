#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if __name__ == "__main__":

    if len(sys.argv[1]) > 1:
        r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
        print(r.text)
