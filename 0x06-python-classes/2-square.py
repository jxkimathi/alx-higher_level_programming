#!/usr/bin/python3
"""Defines a square by size validation"""


class Square:
    """Represents the square"""

    def __init__(self, size=0):
        """Initializes the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
