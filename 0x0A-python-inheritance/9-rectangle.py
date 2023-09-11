#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The inherited class Rectangle"""

    def __init__(self, width, height):
        """Initializes the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Implements the area"""
        return self.__height * self.__width

    def __str__(self):
        """Return the print() and str() representation of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
