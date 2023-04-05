#!/usr/bin/python3
""" Class inherited from rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle (9-rectangle.py) """
    def __init__(self, size):
        """ Constructor maping size to parent constructor"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Calling parent method area() """
        return (super().area())

    def __str__(self):
        """ Calling parent method str() """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
