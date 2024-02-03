#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n = []
    try:
        range(list_length)
    except Exception:
        return n

    for i in range(list_length):
        n.append(0)

    for i in range(list_length):
        try:
            d1, d2 = my_list_1[i], my_list_2[i]
        except Exception:
            print("out of range")
            continue

        try:
            v = d1 / d2
        except TypeError:
            print("wrong type")
            continue
        except ZeroDivisionError:
            print("division by 0")
            continue
        finally:
            n[i] = v
    return n
