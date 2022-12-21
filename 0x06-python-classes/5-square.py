#!/usr/bin/python3

""" Write a class Square that defines a square by: (based on 1-square.py)."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (integer): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/Set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""

        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character"""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
