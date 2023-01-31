#!/usr/bin/python3
"""
Progam that print square with # symbol according to input size
"""


def print_square(size):
    """ function that prints a square with the character # """
    s = "size must be an integer"
    if not (isinstance(size, int)):
        raise TypeError(s)
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError(s)
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print('')
