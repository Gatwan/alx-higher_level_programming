#!/usr/bin/python3
""" Describes a class """


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
