#!/usr/bin/python3

""" Only subclass

Function to check for subclass
NOT class itself
"""


def inherits_from(obj, a_class):
    """ Check if object inherits
    from a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
