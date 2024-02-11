#!/usr/bin/python3

"""
Reading a simple file
"""


def read_file(filename=""):
    """ Reads file
    prints file to stdout, no line ending
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
