#!/usr/bin/python3
"""Displayes all values in the table where name matches the value
safe from injections"""


import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = conn.cursor()
    safe = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE LIKE %s".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
