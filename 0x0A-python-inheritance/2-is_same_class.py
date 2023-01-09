#!/usr/bin/python3
"""Is object an instance"""


def is_same_class(obj, a_class):
    """Returns:
    True: if objects is an instance
    False: Otherwise
    """
    if type(obj) is a_class:
        return True
    return False
