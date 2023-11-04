#!/usr/bin/python3
'''
    comment
'''
import requests

r = requests.get('https://intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}\n\t- content: {}'.format(type(r.text), r.text))
