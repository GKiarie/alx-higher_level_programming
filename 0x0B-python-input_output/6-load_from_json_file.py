#!/usr/bin/python3
"""Java Script Object Notation"""
import json


def load_from_json_file(filename):
    """
    Ftn that creates an object froma JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
