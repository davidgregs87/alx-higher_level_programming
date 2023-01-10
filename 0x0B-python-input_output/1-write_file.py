#!/usr/bin/python3
"""A function that Writes a text file"""


def write_file(filename="", text=""):
    """A function that reads a text file(UTF8) and prints to stdout
    Args:
        filename: File to be written.
        text: Lines of Strings to be added.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
