#!/usr/bin/python3
""" Defines a square that inherits from a Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represents a square """

    def __init__(self, size):
        """ size must be private 
            size must be a positive integer """
    self.integer_validator("size", size)
    super().__init__(size, size)
    self.__size = size
