#!/usr/bin/python3
"""Defines a rectangle by width and height"""


class Rectangle:
    """Represents the rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the beggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance with width == height == size"""
        return cls(size, size)

    def __str__(self):
        """Prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ()

        rect = []
        for rows in range(0, self.__height):
            [rect.append(str(self.print_symbol))
             for columns in range(0, self.__width)]
            if rows != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return string representation of the string"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Prints a message for the deletion of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
