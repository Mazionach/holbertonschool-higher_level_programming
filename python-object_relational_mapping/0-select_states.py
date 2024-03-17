#!/usr/bin/python3

"""
Module for handling city database
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')

    states = cur.fetchall()

    for r in states:
        print(r)

    cur.close()
    db.close()
