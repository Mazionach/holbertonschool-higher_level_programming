#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n = []
    for i in range(list_length):
        n.append(0)

    for i in range(list_length):
        try:
            d1 = my_list_1[i]
        except Exception:
            d1 = 0
            print("out of range")
            try:
                d2 = my_list_2[i]
            except Exception:
                d2 = 0
        else:
            try:
                d2 = my_list_2[i]
            except Exception:
                d2 = 0
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
