#!/usr/bin/python3
"""Defines a square by size, gets the area and prints it"""


class Square:
    """represents the square"""

    def __init__(self, size=0):
        """Initializes the square"""
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Gets the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square"""
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
