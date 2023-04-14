#!/usr/bin/python3
"""Base Class"""


class Base:
    """
    Base class of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = Base.__nb_objects
