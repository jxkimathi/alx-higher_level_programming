#!/usr/bin/python3
"""Inherits a public instance method from list"""


class MyList(list):
    """Representation of the class Mylist"""

    def __init__(self):
        """Initializes the class"""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
