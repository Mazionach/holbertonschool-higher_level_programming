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
        self.size = size

    @property
    def size(self):
        """ Size of the square

        The length of the side of the square,
        must be a positive integer
        """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Print square with "#"

        If size is 0, print empty line
        """
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")
        if self.size == 0:
            print("")
