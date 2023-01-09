#!/usr/bin/python3
"""class Mylist inheriting from list"""


class MyList(list):
    """My list class"""

    def __init__(self):
        """list initiaization"""
        super().__init__

    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
