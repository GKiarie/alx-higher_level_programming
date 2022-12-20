#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Initializing new square class.
    Args:
    size: Integer, size fo new square
    """
    def __init__(self, size=0):
        """Initialization"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of object of square"""
        return (self.__size ** 2)
