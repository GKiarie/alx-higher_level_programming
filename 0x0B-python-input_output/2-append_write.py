#!/usr/bin/python3
"""Appending to a text file"""


def append_write(filename="", text=""):
    """Ftn that appends a string at the and of a text file(UTF-8)
    and returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
