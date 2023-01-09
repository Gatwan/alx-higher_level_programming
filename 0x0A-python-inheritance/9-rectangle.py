#!/usr/bin/python3
""" Define class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents Rectangle """

    def __init__(self, width, height):
        """ width and height must be private
            width and height must be positive integers """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ return area """
        return self.__width * self.__height

    def __str__(self):
        """ Represents string method """
        return "[Rectangle] " + \
            str(self.__width) + "/" + str(self.__height)
