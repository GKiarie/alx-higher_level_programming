#!/usr/bin/python3
"""
Module for add all arguments and save them to a file
"""
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
items.extend(argv[1:])
save_to_json_file(items, "add_item.json")
