#!/usr/bin/python3
""" This class represents a rectangle """


class Rectangle:
    """ Class that defines a Rectangle """
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Private instance attribute """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """ Property setter for width """
        if not isinstance(value, int):
            """ Check if width value is an integer """
            raise TypeError("width must be an integer")
        if value < 0:
            """ Check if width value is greater than 0 """
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """ Private instance attribute """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """ Property setter for height """
        if not isinstance(value, int):
            """ Check if height value is an integer """
            raise TypeError("height must be an integer")
        if value < 0:
            """ Check if height value is greater than or equal to zero """
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        """ Finds area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Finds perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            """ checks the value of width and height """
            return 0
        return 2 * (self.width + self.height)
