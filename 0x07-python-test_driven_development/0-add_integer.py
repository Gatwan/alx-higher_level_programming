#!/usr/bin/python3
""" Function that adds two integers """


def add_integer(a, b=98):
    """ returns integer addition of a and b.
        a and b must be an integer or float """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
