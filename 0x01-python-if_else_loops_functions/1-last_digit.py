#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# my code is here
t = abs(number) % 10
# t for last digits
if number < 10:
    t *= -1
if t > 5 and t != 0:
    print('Last digit of {} is {} and is greater than 5'.format(number,
                                                                t))
elif t < 6 and t != 0:
    print('Last digit of {} is {} and is less than 6 and not 0'
          .format(number, t))
else:
    print('Last digit of {} is {} and is 0'.format(number, t))
