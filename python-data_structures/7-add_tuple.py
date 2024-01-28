#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    c = []
    a = tuple_a
    b = tuple_b
    if len(a) < 1 and len(b) < 1:
        c += 0
    elif len(a) > 1 and len(b) < 1:
        c += a[0]
    elif len(a) < 1 and len(b) > 1:
        c += b[0]
    else:
        c += a[0] + b[0]
    if len(a) < 2 and len(b) < 2:
        c += 0
    elif len(a) > 2 and len(b) < 2:
        c += a[1]
    elif len(a) < 2 and len(b) > 2:
        c += b[1]
    else:
        c += a[1] + b[1]
    return tuple(c)
