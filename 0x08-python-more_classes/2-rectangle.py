#!/usr/bin/python3
"""
Class Rectangle: Defines a Rectangle
"""


class Rectangle:
    """ class that defines a Rectangle with attributes and public methods"""
    def __init__(self, width=0, height=0):
        """ Initializes instances """
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

    def area(self):
        """ Public instance method that returns the rectangle area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))
