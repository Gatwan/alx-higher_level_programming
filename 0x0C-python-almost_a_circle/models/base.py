#!/usr/bin/python3
""" Describes a class """
import json


class Base:
    """ Defines a class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize instance attribute """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
