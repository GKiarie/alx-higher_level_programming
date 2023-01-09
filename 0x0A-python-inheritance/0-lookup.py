#!/usr/bin/python3
"""python lookup function"""


def lookup(obj):
    """
    Ftn that returns list of available attributes & menthods
    of an object.
    Returns: list
    """
    return dir(obj)
