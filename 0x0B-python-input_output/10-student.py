#!/usr/bin/python3
""" Defines a class """


class Student:
    """ Student class """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """ public instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation """


        if isinstance(attrs, list) and\
            all(isinstance(item, str) for item in attrs):
            result ={}

            for i in attrs:
                try:
                    result[i] = self.__dict__[i]
                except Exception:
                    pass
            return result
        return self.__dict__
