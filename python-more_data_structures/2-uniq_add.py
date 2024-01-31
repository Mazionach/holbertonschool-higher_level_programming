#!/usr/bin/python3

def uniq_add(my_list=[]):

    r = 0
    found = []
    for x in my_list:
        if x not in found:
            r += x
            found.append(x)
    return r
