#!/usr/bin/python3
"""
This class represents a square
"""


class Square:
    """
    This class defines a square by size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize size attribute
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set square position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints square with #

        prints an empty line if square size is 0
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
