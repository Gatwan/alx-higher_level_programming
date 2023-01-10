#!/usr/bin/python3
""" JSON serialization of an object """
import json

def class_to_json(obj):
    """ returns dictionary description with simple data structure """
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
        return result
