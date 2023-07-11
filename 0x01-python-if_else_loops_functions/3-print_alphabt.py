#!/usr/bin/python3
g = 0
while g < 26:
    if g != 4 and g != 16:
        print('{:c}'.format(g + 97), end='')
    g += 1
