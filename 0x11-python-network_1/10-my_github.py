#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if __name__ == '__main__':

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    if r.json().get('id'):
        print(r.json().get('id'))
    else:
        print('None')
