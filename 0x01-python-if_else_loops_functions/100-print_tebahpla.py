#!/usr/bin/python3
for p in range(ord('z'), ord('a') - 1, -1):
    if p % 2 == 0:
        x = 0
    else:
        x = 1
    print('{:s}'.format(chr(p - (x * 32))), end='')
