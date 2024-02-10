#!/usr/bin/python3

""" list inheritance

Inherits from list
"""


class MyList(list):
    """ My list

    can print itself sorted

    good boy <3
    """

    def print_sorted(self):
        """ Prints the list sorted
        """
        n = self.copy()
        n.sort()
        print(n)
