#!/usr/bin/python3
"""
This class represents a square
"""


class Square:
    """
    This class defines a square by size
    """

    def __init__(self, size=0):
        """
        Initialize size attribute
        """
        self.size = size

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

    def area(self):
        """
        Area of the square
        """
        return self._Square__size ** 2

    def my_print(self):
        """
        prints square with #
        """
        for i in range(self._Square__size):
            for j in range(self._Square__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("")
