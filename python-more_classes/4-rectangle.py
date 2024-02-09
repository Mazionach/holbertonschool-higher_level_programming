#!/usr/bin/python3

""" Rectangle module

This module defines a rectangle class
"""


class Rectangle:
    """ Rectangle class

    Has a width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width property

        How wide the rectangle is, must be an int greater or equal to 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Height property

        How tall the rectangle is, must be an int greater or equal to 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """ Calculates perimeter of rectangle
        """
        return (self.width * 2 + self.height * 2 if
                self.width != 0 and self.height != 0 else 0)

    def __str__(self):
        """ Rectangle as a string
        """
        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
