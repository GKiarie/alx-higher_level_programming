#!/usr/bin/python3
"""A student Class"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of instance"""
        if attrs is None:
            return self.__dict__
        dict = {}
        for attr in attrs:
            try:
                dict[attr] = self.__dict__[attr]
            except Exception:
                pass
        return dict
