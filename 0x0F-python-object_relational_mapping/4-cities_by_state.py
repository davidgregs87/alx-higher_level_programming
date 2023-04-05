#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                 FROM cities as c \
                 INNER JOIN states as s \
                 ON c.state_id = s.id \
                 ORDER BY c.id ASC;")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    conn.close()
