#!/usr/bin/python3

""" Square module

This module defines and handles a square shape

"""


class Square:
    """ Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square

        Args:
            size: the size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """2D position of the square

        Must be a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Print square with "#"

        If size is 0, print empty line
        """
        if self.size == 0:
            print("")
            return

        for y in range(self.position[1]):
            print("")
        for i in range(self.size):
            for x in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print("")
