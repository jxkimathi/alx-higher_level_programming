#!/usr/bin/python3
"""Defines MagicClass, gets the area and circumference"""
import math


class MagicClass:
    """Represents the MagicClass"""

    def __init__(self, radius=0):
        """Initializes the MagicClass"""
        self.__radius = radius

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Gets the area of the MagicClass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Gets the circumference of the MagicClass"""
        return 2 * math.pi * self.__radius
