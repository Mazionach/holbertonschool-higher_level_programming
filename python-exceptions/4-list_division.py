#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n = []
    for i in range(list_length):
        n.append(0)

    for i in range(list_length):
        err = 0
        try:
            d1, d2 = my_list_1[i], my_list_2[i]
        except Exception:
            d1, d2 = 0, 1
            print("out of range")

        try:
            v = d1 / d2
        except TypeError:
            print("wrong type")
            v = 0
        except ZeroDivisionError:
            print("division by 0")
            v = 0
        finally:
            n[i] = v
    return n
