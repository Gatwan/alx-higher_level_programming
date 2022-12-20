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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
