#!/usr/bin/python3
"""
Class Rectangle: Defines a Rectangle
"""


class Rectangle:
    """ class that defines a Rectangle with attributes and public methods"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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
        if (self.__width != 0 or self.__height != 0):
            return ((self.__width + self.__height) * 2)
        else:
            return (0)

    def __str__(self):
        """ magic method that print the rectangle with the character # """
        string = ""
        if (self.__width != 0 or self.__height != 0):
            for x in range(self.__height):
                for y in range(self.__width):
                    string += "#"
                string += "\n"
            string = string[:-1]
            return (string)
        else:
            return (string)

    def __repr__(self):
        """ return a string representation of the rectangle to be
        able to recreate a new instance by using eval()
        """
        wid = str(self.__width)
        hei = str(self.__height)
        return "Rectangle(" + wid + ", " + hei + ")"

    def __del__(self):
        """ (destruct) Detect when an instance of Rectangle is deleted
        and print a message """
        print("Bye rectangle...")
