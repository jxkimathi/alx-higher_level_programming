#!/usr/bin/python3
"""Class Square that inherits from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            "id" : self.id,
            "size" : self.size,
            "x" : self.x,
            "y" : self.y
        }

    def __str__(self):
        """Overrides the __str__ method to return a stdout"""
        string = (f"[Square] ({self.id}) ")
        string += (f"{self.x}/{self.y} - {self.width}")
        return string
