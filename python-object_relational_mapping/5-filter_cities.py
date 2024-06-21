#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves data
from two tables: cities and states. It then prints the id,
name of the city, and name of the state for each row in the result set.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
                INNER JOIN states ON states.id = state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC """, (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        cities_name = ', '.join([row[0] for row in query_rows])
    print(cities_name)
    cur.close()
    conn.close()
