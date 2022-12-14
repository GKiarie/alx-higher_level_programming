#!/usr/bin/python3
"""Reading a text file"""


def read_file(filename=""):
    """Ftn that reads a text file(UTF-8)
    and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
