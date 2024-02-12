#!/usr/bin/python3

"""
Student module
"""


class Student():
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """ Init student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dictionary of student """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {x: elem for x, elem in self.__dict__.items() if x in attrs}
        return self.__dict__
