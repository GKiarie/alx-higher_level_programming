#!/usr/bin/python3
"""Object is  an instance"""


def is_kind_of_class(obj, a_class):
    """Function returns True if obj is an instance
    of a_class, or instance of inherited class, False
    otherwise
    """
    return isinstance(obj, a_class)
