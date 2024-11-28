#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
from the database `hbtn_0e_0_usa`. Results are sorted in ascending
order by states.id.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    Main entry point of the script:
    - Connects to a MySQL database.
    - Retrieves and displays all states in ascending order by id.
    """
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
