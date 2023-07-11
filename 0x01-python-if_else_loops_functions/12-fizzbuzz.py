#!/usr/bin/python3
def fizzbuzz():
    str1 = 'Fizz'
    str2 = 'Buzz'
    for u in range(1, 101):
        if u % 3 == 0 and u % 5 == 0:
            print('{:s}'.format(str1 + str2), end=' ')
        elif u % 3 == 0 and u % 5 != 0:
            print('{:s}'.format(str1), end=' ')
        elif u % 3 != 0 and u % 5 == 0:
            print('{:s}'.format(str2), end=' ')
        else:
            print('{}'.format(u), end=' ')
        if u == 100:
            print(end='')
