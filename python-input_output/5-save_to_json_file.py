#!/usr/bin/python3

"""
Object to JSON to file module
"""


import json


def save_to_json_file(my_obj, filename):
    """ Converts object to json and saves """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
