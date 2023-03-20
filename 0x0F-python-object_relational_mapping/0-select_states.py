#!/usr/bin/python3
"""Module to connect to database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3], charset="utf8")
    curr = database.cursor()
    curr.execute('SELECT * FROM states ORDER BY id ASC')
    data = curr.fetchall()
    for state in data:
        print(state)

    curr.close()
    database.close()
