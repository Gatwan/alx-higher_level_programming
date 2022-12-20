#!/usr/bin/python3
import math
"""
This represents a math class
"""


class MagicClass:
    """
    This class defines a circle with a radius
    """
    def __init__(self, radius):
        """
        Initialize the radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
