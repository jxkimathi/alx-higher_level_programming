#!/usr/bin/python3
"""Defines a square by size, gets area and compares"""


class Square:
    """Defines the square"""

    def __init__(self, size=0):
        """Initializes the square"""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Gets the area of the square"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Defines the == comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Defines the > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Defines the < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison"""
        return self.area() <= other.area()
