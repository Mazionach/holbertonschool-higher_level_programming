#!/usr/bin/python3

"""
Square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Init square, based on rectangle """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Write square data """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ Asigns both W and H """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
