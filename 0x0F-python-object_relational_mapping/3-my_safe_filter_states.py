#!/usr/bin/python3
"""AVOID SQL INJECTIONS. script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306, charset="utf8")
    cur = conn.cursor()
    # , to the end of argv[4] because second paramether is a tuple
    cur.execute("SELECT * FROM states WHERE name = %s \
                 ORDER BY id ASC", (argv[4],))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    conn.close()
