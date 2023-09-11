#!/usr/bin/python3
"""Returns True if the object is instance of class that inherited from class"""


def inherits_from(obj, a_class):
    """Returns True if object is instance of class otherwise False"""

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
