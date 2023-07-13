#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if (a < b):
        f = add(a, b)
        for i in range(4, 6):
            f = add(f, i)
        return (f)
    else:
        return sub(a, b)
