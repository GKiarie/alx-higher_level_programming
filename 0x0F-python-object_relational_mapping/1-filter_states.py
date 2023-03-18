#!/usr/bin/env python3
"""Script that lists all entries from
a table in a db where name startswith 'N'"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
          host='localhost',
          user=argv[1],
          passwd=argv[2],
          db=argv[3])
    except MySQLdb.Error:
        print("Failed to connect")
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("Failed to execute query")
    cur.close()
    db.close()
