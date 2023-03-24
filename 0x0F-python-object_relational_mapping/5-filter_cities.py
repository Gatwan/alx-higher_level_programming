#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


def main():
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3], charset="utf8")
    cur = database.cursor()
    query = "SELECT cities.name FROM cities {} {} '{}' {}".format(
            "JOIN states ON cities.state_id=states.id",
            "WHERE states.name LIKE", argv[4],
            "ORDER BY cities.id ASC")
    cur.execute(query)
    data = cur.fetchall()
    states = ", ".join(row[0] for row in data)
    print(states)
    cur.close()
    database.close()


if __name__ == "__main__":
    main()
