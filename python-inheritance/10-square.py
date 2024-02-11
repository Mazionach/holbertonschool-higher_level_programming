#!/usr/bin/python3

""" Square module

defines a square
"""


Rectangle = __import__('9-rectangle.py').Rectangle


def Square(Rectangle):
    """
    Square class
    Based on rectangle
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
