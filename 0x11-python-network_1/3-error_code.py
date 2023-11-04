#!/usr/bin/python3
'''
    comment
'''
import urllib
import urllib.request
import sys

if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as status:
                print(status.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
