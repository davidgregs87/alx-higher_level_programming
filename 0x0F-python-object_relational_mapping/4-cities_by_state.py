#!/usr/bin/python3
"""
List all cities in the cities table of the hbtn_0e_4_usa database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    uname = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Setting up a connection
    conn = MySQLdb.connect(host='localhost',
                           user=uname, passwd=password,
                           db=database, charset='utf8', port=3306)
    # Creating cursor object
    cur = conn.cursor()

    # Execute query
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                ORDER BY cities.id ASC""")
    query = cur.fetchall()

    # Iterate through "query"
    for row in query:
        print(row)
    cur.close()
    conn.close()
