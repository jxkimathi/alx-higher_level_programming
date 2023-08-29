#!/usr/bin/python3
"""Defines a square by size and gets the area"""


class Square:
    """Represents the square"""

    def __init__(self, size=0):
        """Initializes the square"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area"""
        return self.__size * self.__size
