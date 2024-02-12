#!/usr/bin/python3

"""
JSON to object module
"""


import json


def from_json_string(my_str):
    """ Converts json to obj """
    return json.load(my_str)
