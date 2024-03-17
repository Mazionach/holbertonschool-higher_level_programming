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
    cur.execute(f"SELECT * FROM states \
                WHERE name LIKE BINARY '{arg}' \
                ORDER BY states.id ASC")

    states = cursor.fetchall()

    for s in states:
        print(s)
