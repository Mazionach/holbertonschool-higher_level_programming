#!/usr/bin/python3

"""
Appending to a simple file
"""


def append_write(filename="", text=""):
    """ Writes to file
    Extends existing file
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(str(text))
