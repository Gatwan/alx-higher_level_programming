#!/usr/bin/python3
""" Defines function that appends to a file """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file 
        returns the number of characters added """
    new_line = 0
    with open('tests/file_append.txt', 'a', encoding="utf-8") as f:
        new_line = f.write(text)
    return new_line
