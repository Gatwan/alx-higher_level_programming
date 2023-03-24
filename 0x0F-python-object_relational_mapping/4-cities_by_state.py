#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


def main():
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3], charset="utf8")
    cur = database.cursor()
    query = "SELECT cities.id, cities.name, states.name {} {} {}".format(
            "FROM cities",
            "LEFT OUTER JOIN states ON cities.state_id=states.id",
            "ORDER BY cities.id ASC")
    cur.execute(query)
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    database.close()


if __name__ == "__main__":
    main()
