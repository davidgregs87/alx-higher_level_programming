#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary Representation of a Student Instance"""
        return self.__dict__
