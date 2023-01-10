#!/usr/bin/python3
"""returns the dictionary with simple data structure"""


def class_to_json(obj):
    """returns the dictionary of obj"""
    return obj.__dict__
