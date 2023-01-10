#!/usr/bin/python3
"""A function that Reads a text file"""


def read_file(filename=""):
    """A function that reads a text file(UTF8) and prints to stdout

    Args:
        filename: File to be read
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
