#!/usr/bin/python3

"""
Script to display values with state passed as argument
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    arg = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC".format(arg))

    states = cur.fetchall()

    for s in states:
        print(s)
