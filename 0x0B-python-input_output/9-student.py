#!/usr/bin/python3
"""Create a Class Student that defines a student"""


class Student:
    """The class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of Student"""
        return self.__dict__
