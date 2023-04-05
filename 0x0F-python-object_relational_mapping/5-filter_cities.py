#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities
   of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    aux_list = []
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306)
    cur = conn.cursor()
    # , to the end of argv[4] because second paramether is a tuple
    cur.execute("SELECT c.name \
                 FROM cities as c \
                 INNER JOIN states as s \
                 ON c.state_id = s.id \
                 WHERE s.name = %s \
                 COLLATE latin1_general_cs \
                 ORDER BY c.id ASC;", (argv[4],))
    query_rows = cur.fetchall()

    for row in query_rows:
        aux_list.append(row[0])
    print(", ".join(aux_list))
    # Close all cursors
    cur.close()
    # Close all databases
    conn.close()
