#!/usr/bin/python3
v = 0
while v < 100:
    if v != 99:
        print('{0:02d}'.format(v), end=', ')
    else:
        print(v)
    v += 1
