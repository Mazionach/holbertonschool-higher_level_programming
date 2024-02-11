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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Implements area of rectangle """
        return self.__height * self.__width

    def __str__(self):
        """ Readable string format of rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.height)
