#!/usr/bin/python3
"""Returns True if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Returns True if exactly same otherwise False"""
    if type(obj) is not (a_class):
        return False
    else:
        return True
