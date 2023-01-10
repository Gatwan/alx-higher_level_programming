#!/usr/bin/python3
""" defines a file """


def read_file(filename=""):
    """ reads a text file """
    with open('tests/my_file_0.txt', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
