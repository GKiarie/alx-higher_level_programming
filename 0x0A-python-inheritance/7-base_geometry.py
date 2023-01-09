#!/usr/bin/python3
"""BaseGeometry Class"""


class BaseGeometry:
    """Represents base geometry"""

    def area(self):
        """area method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate values"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
