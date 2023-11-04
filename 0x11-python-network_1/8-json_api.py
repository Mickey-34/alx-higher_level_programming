#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if __name__ == '__main__':

    datal = {'q': ''}
    if len(sys.argv) > 1:
        datal = {'q': sys.argv[1]}

    r = requests.post('http://0.0.0.0:5000/search_user',
                      data=datal)

    try:
        if r.json():
            sumVar = r.json()
            print('[{}] {}'.format(sumVar['id'], sumVar['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
