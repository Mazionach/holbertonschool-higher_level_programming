#!/usr/bin/python3


"""
Arguments to JSON file
"""


import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

x = load("add_item.json")

x += sys.argv

save(x, "add_item.json")
