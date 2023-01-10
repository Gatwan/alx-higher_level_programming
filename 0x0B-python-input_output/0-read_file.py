#!/usr/bin/python3
""" defines a file """


def read_file(filename=""):
    """ reads a text file """
    with open('my_file_0.txt', encoding="utf-8") as f:
        print("{}".format(f.read()))
    f.closed
