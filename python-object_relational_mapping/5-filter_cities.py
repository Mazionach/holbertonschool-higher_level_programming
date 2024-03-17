#!/usr/bin/python3

"""
Script that lists all cities of a given state
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    arg = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (arg,))

    states = cur.fetchall()

    r = ""
    if len(states) > 1:
        for i in range(len(states) - 1):
            r = r + states[i] + ", "
    if len(states) != 0:
        r = r + states[-1]

    print(r)
