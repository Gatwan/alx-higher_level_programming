#!/usr/bin/python3
"""Defines student class"""


class Student:
    """Student object"""

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Initializing instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"""
        if isinstance(attrs, list) and\
          all(isinstance(item, str) for item in attrs):
            result = {}
            for i in attrs:
                try:
                    result[i] = self.__dict__[i]
                except Exception:
                    pass
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """"""
        for key, value in json.items():
            self.__dict__[key] = value
