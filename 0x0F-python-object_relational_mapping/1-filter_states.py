#!/usr/bin/env python3
"""Script that lists all entries from
a table in a db where name startswith 'N'"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    [print(state) for state in cur.fetchall()]
