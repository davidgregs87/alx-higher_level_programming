#!/usr/bin/python3
"""
To avoid SQL injection we need to parameterize
our query and use placeholders always
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Assigning arguments to a variable
    uname = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    value = sys.argv[4]

    # Create a connection
    conn = MySQLdb.connect(host='localhost',
                           user=uname, passwd=password,
                           db=database, port=3306, charset='utf8')
    # Create a cursor object
    cur = conn.cursor()

    # Execute a query
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (value,))
    result = cur.fetchall()

    # Iterate through "result"
    for row in result:
        print(row)

    # Close cursor object
    cur.close()

    # Close connection
    conn.close()
