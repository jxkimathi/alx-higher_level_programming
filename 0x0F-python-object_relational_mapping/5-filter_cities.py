#!/usr/bin/python3
"""Lists all cities of that state taken as argument using the database"""


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
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.states_id
                WHERE states.name=%s""", (sys.argv[4],))
    query_rows = cur.fetchall()
    tmp = list(row[0] for row in query_rows)
    print(*tmp, sep=", ")
    cur.close()
    conn.close()
