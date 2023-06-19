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
    value = sys.argv[4]

    # Setting up a connection
    conn = MySQLdb.connect(host='localhost',
                           user=uname, passwd=password,
                           db=database, charset='utf8', port=3306)
    # Creating cursor object
    cur = conn.cursor()

    # Execute query
    query = ("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s ORDER BY cities.id ASC""")
    cur.execute(query, (value,))
    result = cur.fetchall()
    # Iterate through "query"
    result_strings = [str(row[0]) for row in result]
    print(", ".join(result_strings))
    cur.close()
    conn.close()
