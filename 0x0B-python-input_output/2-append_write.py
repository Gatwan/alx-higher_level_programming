#!/usr/bin/python3
""" Defines function that appends to a file """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file
        returns the number of characters added """

    with open(filename, 'a+', encoding="utf-8") as f:
        return f.write(text)
