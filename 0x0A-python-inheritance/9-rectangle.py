#!/usr/bin/python3
""" Base Geometry Class """


class BaseGeometry:
    """ class that improve geometry with integer validator"""
    def area(self):
        """ raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if (type(value) is not int):
            raise TypeError(name + " must be an integer")
        if (value <= 0):
            raise ValueError(name + " must be greater than 0")

""" Program that build a full rectangle """


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Constructor """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """ method that return de area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ string representation """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
