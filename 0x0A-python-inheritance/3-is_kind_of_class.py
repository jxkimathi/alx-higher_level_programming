#!/usr/bin/python3
"""Returns True if object is an instance of or if it is from inherited class"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is instance of class otherwise False"""
    if not isinstance(obj, a_class):
        return False
    else:
        return True
