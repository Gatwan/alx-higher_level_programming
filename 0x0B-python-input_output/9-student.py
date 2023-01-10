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

    def to_json(self):
        """"""
        return self.__dict__
