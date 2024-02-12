#!/usr/bin/python3

""" Pascal triangle module
"""


def pascal_triangle(n):
    """ Returns a pascal triangle of n rows
    in list of lists form
    """
    r = []
    for row in range(n):
        if row == 0:
            r.append([1])
            continue
        t = [1]
        for col in range(row - 1):
            t.append(r[row - 1][col] + r[row - 1][col + 1])
        t.append(1)

        r.append(t)
    return r
