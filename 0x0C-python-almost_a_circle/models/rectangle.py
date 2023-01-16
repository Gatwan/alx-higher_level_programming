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
