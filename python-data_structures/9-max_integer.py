#!/usr/bin/python3

def max_integer(my_list=[]):

    r = None

    for i in my_list:
        if r is None or r < i:
            r = i
    return r
