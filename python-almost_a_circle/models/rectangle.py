#!/usr/bin/python3

"""
Rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle subclass of Base shape """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectange adds W, H, x and y properties """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ X position of rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Y position of rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate area of rectangle """
        return self.width * self.height

    def __str__(self):
        """ String representation of rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def display(self):
        """ Draw rectangle with text """
        print("\n" * self.y, end="")
        print(((" " * self.x + "#" * self.width + "\n") * self.height)[:-1])

    def update(self, *args, **kwargs):
        """ Update rectangle parameters """
        if not args:
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

    def to_dictionary(self):
        """ Return rectangle in dictionary form """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
