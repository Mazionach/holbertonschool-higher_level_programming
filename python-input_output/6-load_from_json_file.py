#!/usr/bin/python3

"""
JSON from file to object module
"""


import json


def load_from_json_file(filename):
    """ Converts json from file to obj """
    with open(filename, encoding="UTF-8") as f:
        return json.loads(f.read())
