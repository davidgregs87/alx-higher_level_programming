#!/usr/bin/python3
"""A function that appends a string to a text file"""


def append_write(filename="", text=""):
    """A function that appends a string to a text file(UTF8) \n
        and prints to stdout
    Args:
        filename: File to be written.
        text: Lines of Strings to be added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
