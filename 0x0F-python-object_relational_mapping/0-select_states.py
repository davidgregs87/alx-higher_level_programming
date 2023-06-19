#!/usr/bin/python3
"""
Accessing a database(connection) and make a query

"""
import MySQLdb
import sys

# Assign the first, second and third argument to a variable which is to be passed to the connection below
if __name__ == '__main__':
    uname = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

# Replaced connection parameters with command line arguments variables
    conn = MySQLdb.connect(host='localhost', port = 3306 , user = uname , passwd = password , db = database , charset = 'utf8')
    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    query = cur.fetchall()
    for rows in query:
        print(rows)
    cur.close()
    conn.close()
