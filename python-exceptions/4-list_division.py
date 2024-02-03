#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n = []
    for i in range(list_length):
        n.append(0)

    for i in range(list_length):
        err = 0
        try:
            d1 = my_list_1[i]
        except Exception:
            d1 = 0
            err = 1
        try:
            d2 = my_list_2[i]
        except Exception:
            d2 = 0
            err = 1
        if err != 0:
            print("out of range")

        err = 0
        if not ((type(d1) is int) or (type(d1) is float)):
            err = 1
            d1 = 0
        if not ((type(d2) is int) or (type(d2) is float)):
            err = 1
            d2 = 0
        if err != 0:
            print("wrong type")

        try:
            v = d1 / d2
        # except TypeError:
        #    print("wrong type")
        #    v = 0
        except ZeroDivisionError:
            print("division by 0")
            v = 0
        finally:
            n[i] = v
    return n
