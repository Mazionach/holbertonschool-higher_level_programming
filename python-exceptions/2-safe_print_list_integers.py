#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    r = 0
    for i in range(x):
        v = my_list[i]
        try:
            print("{:d}".format(v), end="")
        except Exception:
            pass
        else:
            r += 1
    print("")
    return r
