#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The class Square"""

    def __init__(self, size):
        """Initializes the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
