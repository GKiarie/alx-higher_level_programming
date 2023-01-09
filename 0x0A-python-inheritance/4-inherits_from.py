#!/usr/bin/python3
"""Inherited class checking ftn"""


def inherits_from(obj, a_class):
    """
    Ftn checks if obj is instance of a class
    inheriting from a specified class.
    Returns True if instance, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
