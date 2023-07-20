#!/usr/bin/python3


def weight_average(my_list=[]):

    if my_list:
        return sum((k * f for k, f in my_list)) / sum((f for _, f in my_list))
    if my_list == []:
        return 0
    return None
