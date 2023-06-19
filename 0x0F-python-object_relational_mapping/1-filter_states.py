#!/usr/bin/python3
"""
Filter search query
"""
import sys
import MySQLdb

if __name__ == '__main__':
    uname = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host='localhost', user=uname, passwd=password,
                           db=database, port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE BINARY name
                LIKE 'N%' ORDER BY id ASC""")
    query = cur.fetchall()
    for rows in query:
        print(rows)
    cur.close()
    conn.close()
