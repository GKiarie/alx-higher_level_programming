#!/usr/bin/python3
"""Rectangle Module."""


class Rectangle:
    """Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize arectangle.
        args:
        width: int, initialized to 0
        height: int, initialized to 0
        exceptions:
        TypeError: height & width must be ints
        ValueError: height & width must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves valus of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrieves value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
