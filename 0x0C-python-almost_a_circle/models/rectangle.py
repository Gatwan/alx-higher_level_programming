#!/usr/bin/python3
""" Defines a Rectangle class 
    inherited from class Base """
from models.base import Base


class Rectangle(Base):
    """ Defines a class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y
