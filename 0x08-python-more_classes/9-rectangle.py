#!/usr/bin/python3
"""
Class Rectangle: Defines a Rectangle
"""


class Rectangle:
    """ class that defines a Rectangle with attributes and public methods"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static method that returns the biggest rectangle
        based on the area """
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ Class method that returns a new Rectangle instance
        with width == height == size """
        return cls(size, size)

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

    def __str__(self):
        """ magic method that print the rectangle with the character # """
        string = ""
        if (self.__width == 0 or self.__height == 0):
            return (string)
        else:
            for x in range(self.__height):
                for y in range(self.__width):
                    string += str(self.print_symbol)
                string += "\n"
            string = string[:-1]
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
        type(self).number_of_instances -= 1
