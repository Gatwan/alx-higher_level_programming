#!/usr/bin/python3
""" function that writes a string to a text file """


def write_file(filename="", text=""):
    """ returns the number of characters written """
    
    with open('tests/my_first_file.txt', 'w+', encoding="utf-8") as f:
        return f.write(text)
