#!/usr/bin/python3
w = 0
while w < 8:
    z = w
    while z <= 9:
        if w != z:
            print('{}{}'.format(w, z), end=', ')
        z += 1
    w += 1
print('{}{}'.format(w, z - 1), sep='')
