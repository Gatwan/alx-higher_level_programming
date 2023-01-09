#!/usr/bin/python3
""" Function to add attribute """


def add_attribute(obj, attr, value):
    """ adds new attribute """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
