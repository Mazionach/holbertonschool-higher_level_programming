#!/usr/bin/python3

"""
Object to JSON module
"""


import json


def to_json_string(my_obj):
    """ Converts object to json """
    return json.dumps(my_obj)
