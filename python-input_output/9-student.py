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

    def to_json(self):
        """ Return dictionary of student """
        return self.__dict__
