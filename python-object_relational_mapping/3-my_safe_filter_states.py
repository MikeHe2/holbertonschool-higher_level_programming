#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves rows
from the 'states' table that match a given name. The name is
provided as a command-line argument.

Usage: python3 3-my_safe_filter_states.py <username>
<password> <database> <name>
"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE BINARY name=%s
                ORDER BY id ASC """, (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
