#!/usr/bin/python3


"""
Arguments to JSON file
"""


import sys
save = __import__('5-save_to_json_file').save_to_json_file


save(sys.argv, "add_item.json")#l)
