#!/usr/bin/python3

"""
Base class for shapes
"""


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
