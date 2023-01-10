#!/usr/bin/python3
""" JSON serialization of an object """
import json

def class_to_json(obj):
    """ returns dictionary description with simple data structure """
    return obj.__dict__
