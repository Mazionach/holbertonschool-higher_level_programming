#!/usr/bin/python3


"""
Arguments to JSON file
"""


import sys


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

try:
    x = load("add_item.json")
except FileNotFoundError:
    x = []

x += sys.argv[1:]
save(x, "add_item.json")
