#!/usr/bin/python3
# script that takes in an argument and displays all values in the states
# table of hbtn_0e_0_usa where name matches the argument
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{:s}' \
                 COLLATE latin1_general_cs ORDER BY id ASC".format(argv[4]))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    conn.close()
