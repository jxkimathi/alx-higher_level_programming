#!/usr/bin/python3
"""Writes a class Student that defines a student"""


class Student:
    """The class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
