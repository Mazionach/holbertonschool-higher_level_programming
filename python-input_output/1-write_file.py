#!/usr/bin/python3

"""
Writing to a simple file
"""


def write_file(filename="", text=""):
    """ Writes to file
    Creates if doesnt exists, overwrites otherwise
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(str(text))
