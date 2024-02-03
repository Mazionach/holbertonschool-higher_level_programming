#!/usr/bin/python3

""" Square module

This module defines and handles a square shape

"""


class Square:
    """ Square class
    """

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size: the size of the square
        """
        self.size(size)

    def size(self, size=None):
        """Sets or gets the size of the square

        The size must be a positive int,
        else an error will be raised

        Args:
            size: the size of the square
        """
        if size is not None:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

        return self.__size

    def area(self):
        """Calculate area of square
        """
        return self.__size ** 2
