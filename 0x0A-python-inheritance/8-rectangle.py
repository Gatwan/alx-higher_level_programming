#!/usr/bin/python3
""" Defines class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents a rectangle """

    def __init__(self, width, height):
        """ width and height must be private
            width and height must be positive integers """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
