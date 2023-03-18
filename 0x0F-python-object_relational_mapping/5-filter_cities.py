#!/usr/bin/python3
""" selecting with mysqldb """
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306,
            db=sys.argv[3]
        )
    except MySQLdb.Error:
        print("error connecting")
    cur = connection.cursor()
    try:
        cur.execute("SELECT cities.name FROM cities INNER JOIN states\
 ON cities.state_id = states.id WHERE states.name = %s ORDER\
 BY cities.id", (sys.argv[4],))
        rows = cur.fetchall()
        print(f"{rows[0][0]}, {rows[1][0]}, {rows[2][0]}")
    except MySQLdb.Error:
        print("execution failed")
    cur.close()
    connection.close()
