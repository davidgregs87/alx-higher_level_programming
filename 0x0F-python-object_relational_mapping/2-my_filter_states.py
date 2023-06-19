#!/usr/bin/python3
"""
Retrieve the value in a database with the value on the command line
"""
import sys
import MySQLdb

if __name__ == '__main__':
    uname = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    value = sys.argv[4]

    conn = MySQLdb.connect(host='localhost',
                           user=uname, passwd=password,
                           db=database, port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (value,))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
