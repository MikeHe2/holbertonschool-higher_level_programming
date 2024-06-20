"""
This script connects to a MySQL database and retrieves rows from the 'states' table
that match a given name pattern. The script takes command line arguments for the
MySQL username, password, database name, and name pattern to search for.

Usage: python3 2-my_filter_states.py <username> <password> <database> <name_pattern>
"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE\
                '{sys.argv[4]}' ORDER BY id ASC ")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
