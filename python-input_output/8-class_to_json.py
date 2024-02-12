#!/usr/bin/python3


"""
Convert object attributes to json
"""


def class_to_json(obj):
    """ Returns a dictionary with
    the object's data
    """
    return obj.__dict__
