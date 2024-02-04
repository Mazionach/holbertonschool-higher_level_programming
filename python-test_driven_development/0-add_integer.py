#!/usr/bin/python3

""" Module for adding 2 integers
"""


def add_integer(a, b=98):
    """ Adds 2 integers
    checks for types, and casts floats to ints
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
