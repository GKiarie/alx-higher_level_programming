#!/usr/bin/env python3
"""Script that takes in an argument and displays
all the values in states tb of db where name matches
argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    name = argv[4]
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))
    [print(state) for state in cur.fetchall()]
