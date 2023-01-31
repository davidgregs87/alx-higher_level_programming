#!/usr/bin/python3
"""
Class Rectangle: Defines a Rectangle
"""


class Rectangle:
    """ class that defines a Rectangle with attributes """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the width of rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set passed private attribue of width """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the height of rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set passed private attribute of height """
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
