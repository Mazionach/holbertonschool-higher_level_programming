#!/usr/bin/python3

"""
Base class for shapes
"""


import json


class Base():
    """
    Base class for shape objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Shape object init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert list of dictionaries to JSON """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save instances of Base to file """
        if list_objs is None:
            list_objs = []
        n = cls.__name__ + ".json"
        with open(n, "w") as f:
            jl = []
            for elem in list_objs:
                jl.append(elem.to_dictionary())
            f.write(jl)
