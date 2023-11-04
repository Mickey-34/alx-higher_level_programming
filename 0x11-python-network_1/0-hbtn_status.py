#!/usr/bin/python3
'''
    comment
'''
import urllib.request
import urllib

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    a = type(html)
    b = html
    c = html.decode('utf8')
    print('Body response:')
    print('\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
          .format(a, b, c))
