#!/usr/bin/python3


""" Rectangle module

rectangle stuff
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class

    Based in BaseGeometry
    """

    def __init__(self, width, height):
        """ Initis rectangle
        validates size
        """
        self.integer_validator(width)
        self.integer_validator(height)
        self.__width = width
        self.__height = height
