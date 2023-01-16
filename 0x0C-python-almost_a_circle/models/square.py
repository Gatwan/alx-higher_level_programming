#!/usr/bin/python3
""" Defines a Square Class
    inherited from class Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overloading method """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh
