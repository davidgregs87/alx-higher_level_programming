#!/usr/bin/python3
""" Base Geometry Class inherited"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


""" Program that creates a Rectangle and intance its values """


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Constructor """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
