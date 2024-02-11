#!/usr/bin/python3

""" Base geometry module

For doing geometry
"""


class BaseGeometry():
    """ Class for handling geometry
    """

    def area(self):
        """ Not implemented yet """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a string with a name """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return
