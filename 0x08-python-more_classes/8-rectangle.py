#!/usr/bin/python3
""" This class represents a rectangle """


class Rectangle:
    """ Class that defines a Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Private instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Property setter for width """
        if not isinstance(value, int):
            """ Check if width value is an integer """
            raise TypeError("width must be an integer")
        if value < 0:
            """ Check if width value is greater than 0 """
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Private instance attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Property setter for height """
        if not isinstance(value, int):
            """ Check if height value is an integer """
            raise TypeError("height must be an integer")
        if value < 0:
            """ Check if height value is greater than or equal to zero """
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Finds area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Finds perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            """ checks the value of width and height """
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ converts rectangle to a string """
        if self.width == 0 or self.height == 0:
            """ checks if string is empty """
            return ""
        row = (str(self.print_symbol) * self.width)
        return "\n".join([row] * self.height)

    def __repr__(self):
        """ returns a string representation of the rectangle """
        return 'Rectangle({}, {})'.format(str(self.width), str(self.height))

    def __del__(self):
        """ Prints message when rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
