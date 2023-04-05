#!/usr/bin/python3
""" First Rectangle that inherits from Base """
from . base import Base
import json


class Rectangle(Base):
    """ class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retriebe the width of rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set passet private attribute of width """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the height of rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set passed private attribute of height """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieve private instance attribute x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ set private instance attribute x """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieve private instance sttribute y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ set private instance attribute y """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance """
        return (self.__height * self.__width)

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for nline in range(self.y):
            print('')
        for h in range(self.height):
            print(' ' * self.x, end='')
            for w in range(self.width):
                print('#', end='')
            print('')

    def __str__(self):
        """ overriding the __str__ method that returns a custom string """
        mssg = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)
        return (mssg)

    def update(self, *args, **kwargs):
        """ Method that assigns an argument to each attribute
        by Non-keyword and key/value"""
        arlist = ["id", "width", "height", "x", "y"]
        if (args and len(args) != 0):
            for arl in range(len(args)):
                if (arl == 0):
                    super().__init__(args[arl])
                elif (arl < len(arlist)):
                    setattr(self, arlist[arl], args[arl])
        else:
            for key, value in kwargs.items():
                if (key == 'id'):
                    super().__init__(value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        my_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return (my_dict)
