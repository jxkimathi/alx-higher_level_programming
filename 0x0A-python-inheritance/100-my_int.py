#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """The class MyInt"""

    def __eq__(self, value):
        """Overrides == with !="""
        return self.real != value

    def __ne__(self, value):
        """Overrides != with =="""
        return self.real == value
